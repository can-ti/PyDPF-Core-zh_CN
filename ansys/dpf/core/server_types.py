"""
Server types
============
Contains the different kinds of
servers available for the factory.
"""
import abc
import io
import os
import socket
import subprocess
import time
from abc import ABC
from threading import Thread

import psutil

import ansys.dpf.core as core
from ansys.dpf.core import errors, session
from ansys.dpf.core._version import server_to_ansys_grpc_dpf_version, server_to_ansys_version
# from ansys.dpf.core.server import LOG, RUNNING_DOCKER, LOCALHOST, DPF_DEFAULT_PORT

import logging
LOG = logging.getLogger(__name__)
LOG.setLevel("DEBUG")
DPF_DEFAULT_PORT = int(os.environ.get("DPF_PORT", 50054))
LOCALHOST = os.environ.get("DPF_IP", "127.0.0.1")
RUNNING_DOCKER = {"use_docker": "DPF_DOCKER" in os.environ.keys()}
if RUNNING_DOCKER["use_docker"]:
    RUNNING_DOCKER["docker_name"] = os.environ.get("DPF_DOCKER")
RUNNING_DOCKER['args'] = ""
MAX_PORT = 65535


def _get_dll_path(name, ansys_path=""):
    """Helper function to get the right dll path for Linux or Windows"""
    from ansys.dpf.gate import _version
    ISPOSIX = os.name == "posix"
    if ansys_path == "":
        ANSYS_INSTALL = os.environ.get("AWP_ROOT" + str(_version.__ansys_version__), None)
    else:
        ANSYS_INSTALL = ansys_path
    SUB_FOLDERS = os.path.join(ANSYS_INSTALL, "aisol", "dll" if ISPOSIX else "bin",
                               "linx64" if ISPOSIX else "winx64")
    if ISPOSIX:
        name = "lib" + name
    return os.path.join(SUB_FOLDERS, name)


def check_valid_ip(ip):
    """Check if a valid IP address is entered.

    This method raises an error when an invalid IP address is entered.
    """
    try:
        socket.inet_aton(ip)
    except OSError:
        raise ValueError(f'Invalid IP address "{ip}"')


def _run_launch_server_process(ansys_path, ip, port, docker_name):
    if docker_name:
        docker_server_port = int(os.environ.get("DOCKER_SERVER_PORT", port))
        dpf_run_dir = os.getcwd()
        from ansys.dpf.core import LOCAL_DOWNLOADED_EXAMPLES_PATH
        if os.name == "nt":
            run_cmd = f"docker run -d -p {port}:{docker_server_port} " \
                      f"{RUNNING_DOCKER['args']} " \
                      f'-v "{LOCAL_DOWNLOADED_EXAMPLES_PATH}:/tmp/downloaded_examples" ' \
                      f"-e DOCKER_SERVER_PORT={docker_server_port} " \
                      f"--expose={docker_server_port} " \
                      f"{docker_name}"
        else:
            run_cmd = ["docker run",
                       "-d",
                       f"-p"+f"{port}:{docker_server_port}",
                       RUNNING_DOCKER['args'],
                       f'-v "{LOCAL_DOWNLOADED_EXAMPLES_PATH}:/tmp/downloaded_examples"'
                       f"-e DOCKER_SERVER_PORT={docker_server_port}",
                       f"--expose={docker_server_port}",
                       docker_name]
    else:
        if os.name == "nt":
            run_cmd = f"Ans.Dpf.Grpc.bat --address {ip} --port {port}"
            path_in_install = "aisol/bin/winx64"
        else:
            run_cmd = ["./Ans.Dpf.Grpc.sh", f"--address {ip}", f"--port {port}"]
            path_in_install = "aisol/bin/linx64"

        # verify ansys path is valid
        if os.path.isdir(f"{ansys_path}/{path_in_install}"):
            dpf_run_dir = f"{ansys_path}/{path_in_install}"
        else:
            dpf_run_dir = f"{ansys_path}"
        if not os.path.isdir(dpf_run_dir):
            raise NotADirectoryError(
                f'Invalid ansys path at "{ansys_path}".  '
                "Unable to locate the directory containing DPF at "
                f'"{dpf_run_dir}"'
            )

    old_dir = os.getcwd()
    os.chdir(dpf_run_dir)
    process = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.chdir(old_dir)
    return process


def launch_dpf(ansys_path, ip=LOCALHOST, port=DPF_DEFAULT_PORT, timeout=10, docker_name=None):
    """Launch Ansys DPF.

    Parameters
    ----------
    ansys_path : str, optional
        Root path for the Ansys installation directory. For example, ``"/ansys_inc/v212/"``.
        The default is the latest Ansys installation.
    ip : str, optional
        IP address of the remote or local instance to connect to. The
        default is ``"LOCALHOST"``.
    port : int
        Port to connect to the remote instance on. The default is
        ``"DPF_DEFAULT_PORT"``, which is 50054.
    timeout : float, optional
        Maximum number of seconds for the initialization attempt.
        The default is ``10``. Once the specified number of seconds
        passes, the connection fails.
    docker_name : str, optional
        To start DPF server as a docker, specify the docker name here.

    Returns
    -------
    process : subprocess.Popen
        DPF Process.
    """
    process = _run_launch_server_process(ansys_path, ip, port, docker_name)

    # check to see if the service started
    lines = []
    docker_id = []

    def read_stdout():
        for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
            LOG.debug(line)
            lines.append(line)
        if docker_name:
            docker_id.append(lines[0].replace("\n", ""))
            docker_process = subprocess.Popen(f"docker logs {docker_id[0]}",
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
            for line in io.TextIOWrapper(docker_process.stdout, encoding="utf-8"):
                LOG.debug(line)
                lines.append(line)

    current_errors = []

    def read_stderr():
        for line in io.TextIOWrapper(process.stderr, encoding="utf-8"):
            LOG.error(line)
            current_errors.append(line)

    # must be in the background since the process reader is blocking
    Thread(target=read_stdout, daemon=True).start()
    Thread(target=read_stderr, daemon=True).start()

    t_timeout = time.time() + timeout
    started = False
    timedout = False
    while not started:
        started = any("server started" in line for line in lines)

        if time.time() > t_timeout:
            if timedout:
                raise TimeoutError(f"Server did not start in {timeout+timeout} seconds")
            timedout = True
            t_timeout += timeout

    # verify there were no errors
    time.sleep(0.1)
    if current_errors:
        try:
            process.kill()
        except PermissionError:
            pass
        errstr = "\n".join(current_errors)
        if "Only one usage of each socket address" in errstr:
            raise errors.InvalidPortError(f"Port {port} in use")
        raise RuntimeError(errstr)

    if len(docker_id) > 0:
        return docker_id[0]


def check_ansys_grpc_dpf_version(server, timeout):
    import ansys.grpc
    import grpc
    state = grpc.channel_ready_future(server.channel)
    # verify connection has matured
    tstart = time.time()
    while ((time.time() - tstart) < timeout) and not state._matured:
        time.sleep(0.001)

    if not state._matured:
        raise TimeoutError(
            f"Failed to connect to {server._input_ip}:{server._input_port} in {timeout} seconds"
        )

    LOG.debug("Established connection to DPF gRPC")
    grpc_module_version = ansys.grpc.dpf.__version__
    server_version = server.version
    right_grpc_module_version = server_to_ansys_grpc_dpf_version.get(server_version, None)
    ansys_version_to_use = server_to_ansys_version.get(server_version, 'Unknown')
    #    raise ImportWarning(f"{ansys_version_to_use} Ansys unified install is available. "
    #                         f"{server_to_ansys_version.get(server_version, 'Unknown')}"
    #                        f"{ansys_version_to_use}"
    #                         f"install version {right_grpc_module_version} of ansys-grpc-dpf"
    #                         f" with the command: \n"
    #                         f"     pip install ansys-grpc-dpf=={right_grpc_module_version}"
    #                         )


class BaseServer(abc.ABC):
    """Abstract class for servers"""
    @abc.abstractmethod
    def __init__(self, as_global = True):
        """Base class for all types of servers: grpc, in process...

        Parameters
        ----------
        as_global : bool, optional
            Global variable that stores the IP address and port for the DPF
            module. All DPF objects created in this Python session will
            use this IP and port. The default is ``True``.
        """
        # TODO: Use _server_id to compare servers for equality?
        self._server_id = None
        self._session_instance = None
        self._base_service_instance = None

        # assign to global channel when requested
        if as_global:
            core.SERVER = self


    def has_client(self):
        return not (self.client is None)

    @property
    @abc.abstractmethod
    def client(self):
        pass

    @property
    @abc.abstractmethod
    def version(self):
        pass

    @property
    @abc.abstractmethod
    def available_api_types(self):
        pass

    @abc.abstractmethod
    def get_api_for_type(self, c_api, grpc_api):
        pass

    @property
    @abc.abstractmethod
    def _base_service(self):
        pass

    @property
    @abc.abstractmethod
    def info(self):
        pass

    @property
    def _session(self):
        if not self._session_instance:
            self._session_instance = session.Session(self)
        return self._session_instance

    @property
    def _base_service(self):
        if not self._base_service_instance:
            from ansys.dpf.core.core import BaseService

            self._base_service_instance = BaseService(self, timeout=1)
        return self._base_service_instance

    @property
    @abc.abstractmethod
    def os(self):
        """Get the operating system of the server

        Returns
        -------
        os : str
            "nt" or "posix"
        """
        pass

    @property
    def on_docker(self):
        return hasattr(self, "_server_id") and self._server_id is not None

    @abc.abstractmethod
    def shutdown(self):
        pass

    def check_version(self, required_version, msg=None):
        """Check if the server version matches with a required version.

        Parameters
        ----------
        required_version : str
            Required version to compare with the server version.
        msg : str, optional
            Message for the raised exception if version requirements do not match.

        Raises
        ------
        dpf_errors : errors
            errors.DpfVersionNotSupported is raised if failure.

        Returns
        -------
        bool
            ``True`` if the server version meets the requirement.
        """
        from ansys.dpf.core.check_version import server_meet_version_and_raise

        return server_meet_version_and_raise(required_version, self, msg)

    def meet_version(self, required_version):
        """Check if the server version matches with a required version.

        Parameters
        ----------
        required_version : str
            Required version to compare with the server version.

        Returns
        -------
        bool
            ``True`` if the server version meets the requirement.
        """
        from ansys.dpf.core.check_version import server_meet_version

        return server_meet_version(required_version, self)

    def __str__(self):
        return f"DPF Server: {self.info}"

    @abc.abstractmethod
    def __eq__(self, other_server):
        pass

    def __ne__(self, other_server):
        """Return true, if the servers are not equal"""
        return not self.__eq__(other_server)

    @abc.abstractmethod
    def __del__(self):
        try:
            if id(core.SERVER) == id(self):
                core.SERVER = None
        except:
            pass

        try:
            for i, server in enumerate(core._server_instances):
                if server() == self:
                    core._server_instances.remove(server)
        except:
            pass


class CServer(BaseServer, ABC):
    """Abstract class for servers going through the DPFClientAPI"""
    def __init__(self,
                 ansys_path="",
                 as_global=True,
                 load_operators=True):

        super().__init__(as_global=as_global)
        from ansys.dpf.gate import capi
        ISPOSIX = os.name == "posix"
        name = "DPFClientAPI"
        if ISPOSIX:
            name = "DPFClientAPI.so"
        path = _get_dll_path(name, ansys_path)
        capi.load_api(path)
        self._own_process = False

    @property
    def available_api_types(self):
        return "c_api"

    def get_api_for_type(self, capi, grpcapi):
        return capi

    def __del__(self):
        try:
            if self._own_process:
                self.shutdown()
            super().__del__()
        except:
            pass


class GrpcClient:
    def __init__(self, ip, port):
        from ansys.dpf.gate import client_capi
        self._internal_obj = client_capi.ClientCAPI.client_new(str(ip), str(port))


class GrpcServer(CServer):
    """Server using the gRPC communication protocol"""
    def __init__(self,
        ansys_path="",
        ip=LOCALHOST,
        port=DPF_DEFAULT_PORT,
        timeout=10,
        as_global=True,
        load_operators=True,
        launch_server=True,
        docker_name=None):
        # Load DPFClientAPI
        super().__init__(ansys_path=ansys_path, as_global=as_global, load_operators=load_operators)
        # Load Ans.Dpf.GrpcClient
        from ansys.dpf.gate.utils import data_processing_core_load_api

        name = "Ans.Dpf.GrpcClient"
        path = _get_dll_path(name, ansys_path)
        data_processing_core_load_api(path, "remote")

        if launch_server:
            self._server_id = launch_dpf(ansys_path, ip, port,
                                         docker_name=docker_name, timeout=timeout)

        self._client = GrpcClient(ip, port)


        # store port and ip for later reference
        self._input_ip = ip
        self._input_port = port
        self.live = True
        self.ansys_path = ansys_path
        self._own_process = launch_server

    @property
    def version(self):
        from ansys.dpf.gate import data_processing_capi, integral_types
        api = data_processing_capi.DataProcessingCAPI
        major = integral_types.MutableInt32()
        minor = integral_types.MutableInt32()
        api.data_processing_get_server_version_on_client(self.client, major, minor)
        out =  str(int(major)) + "." + str(int(minor))
        return out

    @property
    def _base_service(self):
        raise NotImplementedError

    @property
    def info(self):
        """Server information.

        Returns
        -------
        info : dictionary
            Dictionary with server information, including ``"server_ip"``,
            ``"server_port"``, ``"server_process_id"``, and
            ``"server_version"`` keys.
        """
        return self._base_service.server_info

    @property
    def os(self):
        from ansys.dpf.gate import data_processing_capi
        api = data_processing_capi.DataProcessingCAPI
        return api.data_processing_get_os_on_client(self.client)

    def shutdown(self):
        from ansys.dpf.gate import data_processing_capi
        api = data_processing_capi.DataProcessingCAPI
        api.data_processing_release_server(self.client)

    def __eq__(self, other_server):
        """Return true, if ***** are equals"""
        if isinstance(other_server, GrpcServer):
            raise NotImplementedError
        return False

    @property
    def client(self, ip=LOCALHOST, port=DPF_DEFAULT_PORT):
        return self._client

    @property
    def ip(self):
        """IP address of the server.

        Returns
        -------
        ip : str
        """
        return self._input_ip

    @property
    def port(self):
        """Port of the server.

        Returns
        -------
        port : int
        """
        return self._input_port


class InProcessServer(CServer):
    """Server using the InProcess communication protocol"""
    def __init__(self,
        ansys_path="",
        as_global=True,
        load_operators=True,
        docker_name=None,
        timeout=None):

        # Load DPFClientAPI
        super().__init__(ansys_path=ansys_path, as_global=as_global, load_operators=load_operators)
        # Load DataProcessingCore
        from ansys.dpf.gate.utils import data_processing_core_load_api
        from ansys.dpf.gate import data_processing_capi
        name = "DataProcessingCore"
        path = _get_dll_path(name, ansys_path)
        data_processing_core_load_api(path, "common")
        data_processing_capi.DataProcessingCAPI.data_processing_initialize_with_context(1, None)

    @property
    def version(self):
        from ansys.dpf.gate import data_processing_capi, integral_types
        api = data_processing_capi.DataProcessingCAPI
        major = integral_types.MutableInt32()
        minor = integral_types.MutableInt32()
        api.data_processing_get_server_version(major, minor)
        out =  str(int(major)) + "." + str(int(minor))
        return out

    @property
    def _base_service(self):
        raise NotImplementedError

    @property
    def info(self):
        raise NotImplementedError

    @property
    def os(self):
        # Since it is InProcess, one could return the current os
        return os.name

    def shutdown(self):
        pass

    def __eq__(self, other_server):
        """Return true, if ***** are equals"""
        if isinstance(other_server, InProcessServer):
            raise NotImplementedError
        return False

    @property
    def client(self):
        return None

class LegacyGrpcServer(BaseServer):
    """Provides an instance of the DPF server using InProcess gRPC.
    Kept for backward-compatibility with dpf servers <0.5.0.

    Parameters
    -----------
    ansys_path : str
        Path for the DPF executable.
    ip : str
        IP address of the remote or local instance to connect to. The
        default is ``"LOCALHOST"``.
    port : int
        Port to connect to the remote instance on. The default is
        ``"DPF_DEFAULT_PORT"``, which is 50054.
    timeout : float, optional
        Maximum number of seconds for the initialization attempt.
        The default is ``10``. Once the specified number of seconds
        passes, the connection fails.
    as_global : bool, optional
        Global variable that stores the IP address and port for the DPF
        module. All DPF objects created in this Python session will
        use this IP and port. The default is ``True``.
    load_operators : bool, optional
        Whether to automatically load the math operators. The default
        is ``True``.
    launch_server : bool, optional
        Whether to launch the server on Windows.
    docker_name : str, optional
        To start DPF server as a docker, specify the docker name here.
    """
    def __init__(
        self,
        ansys_path="",
        ip=LOCALHOST,
        port=DPF_DEFAULT_PORT,
        timeout=10,
        as_global=True,
        load_operators=True,
        launch_server=True,
        docker_name=None,
    ):
        """Start the DPF server."""
        # Use ansys.grpc.dpf

        super().__init__(as_global=as_global)

        # Load Ans.Dpf.Grpc?
        import grpc

        # check valid ip and port
        check_valid_ip(ip)
        if not isinstance(port, int):
            raise ValueError("Port must be an integer")
        import platform
        if os.name == "posix" and "ubuntu" in platform.platform().lower():
            raise OSError("DPF does not support Ubuntu")
        elif launch_server:
            self._server_id = launch_dpf(ansys_path, ip, port,
                                         docker_name=docker_name, timeout=timeout)

        self.channel = grpc.insecure_channel("%s:%d" % (ip, port))

        # TODO: add to PIDs ...

        # store port and ip for later reference
        self._input_ip = ip
        self._input_port = port
        self.live = True
        self.ansys_path = ansys_path
        self._own_process = launch_server
        self._stubs = {}

        check_ansys_grpc_dpf_version(self, timeout)

    @property
    def client(self):
        return self

    @property
    def available_api_types(self):
        return list(self._stubs.values())

    def get_api_for_type(self, capi, grpcapi):
        return grpcapi

    def create_stub_if_necessary(self, stub_name, stub_type):
        if not (stub_name in self._stubs.keys()):
            self._stubs[stub_name] = stub_type(self.channel)

    def get_stub(self, stub_name):
        if not (stub_name in self._stubs.keys()):
            return None
        else:
            return self._stubs[stub_name]

    @property
    def info(self):
        """Server information.

        Returns
        -------
        info : dictionary
            Dictionary with server information, including ``"server_ip"``,
            ``"server_port"``, ``"server_process_id"``, and
            ``"server_version"`` keys.
        """
        return self._base_service.server_info

    @property
    def ip(self):
        """IP address of the server.

        Returns
        -------
        ip : str
        """
        try:
            return self._base_service.server_info["server_ip"]
        except:
            return ""

    @property
    def port(self):
        """Port of the server.

        Returns
        -------
        port : int
        """
        try:
            return self._base_service.server_info["server_port"]
        except:
            return 0

    @property
    def version(self):
        """Version of the server.

        Returns
        -------
        version : str
        """
        return self._base_service.server_info["server_version"]

    @property
    def os(self):
        """Get the operating system of the server

        Returns
        -------
        os : str
            "nt" or "posix"
        """
        return self._base_service.server_info["os"]

    def shutdown(self):
        if self._own_process and self.live and self._base_service:
            self._base_service._prepare_shutdown()
            if self.on_docker:
                run_cmd = f"docker stop {self._server_id}"
                process = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                run_cmd = f"docker rm {self._server_id}"
                for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
                    pass
                process = subprocess.Popen(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                try:
                    self._base_service._release_server()
                except:
                    try:
                        p = psutil.Process(self._base_service.server_info["server_process_id"])
                        p.kill()
                        time.sleep(0.01)
                    except:
                        pass

            self.live = False

    def __eq__(self, other_server):
        """Return true, if the ip and the port are equals"""
        if isinstance(other_server, LegacyGrpcServer):
            return self.ip == other_server.ip and self.port == other_server.port
        return False

    def __del__(self):
        try:
            if self._own_process:
                self.shutdown()
            super().__del__()
        except:
            pass

# Python 3.10
# from typing import TypeAlias
# DpfServer: TypeAlias = LegacyGrpcServer
# Python <3.10
DpfServer = LegacyGrpcServer
