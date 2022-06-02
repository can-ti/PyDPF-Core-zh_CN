import pytest
from ansys import dpf
from ansys.dpf.core import path_utilities, errors, server_types
from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols
from ansys.dpf.core.server import set_server_configuration, _global_server
from ansys.dpf.core.server import start_local_server, connect_to_server
from ansys.dpf.core.server import shutdown_all_session_servers, has_local_server
from ansys.dpf.core.server import get_or_create_server
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0


server_configs = [None,
                  ServerConfig(),
                  ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
                  ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
                  ServerConfig(protocol=CommunicationProtocols.InProcess, legacy=False),
                  ServerConfig(protocol=None, legacy=False),
                  ] \
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0 else \
    [None,
     ServerConfig(),
     ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
     ]


@pytest.mark.parametrize("server_config", server_configs, scope="class")
class TestServerConfigs:
    @pytest.fixture(scope="class", autouse=True)
    def cleanup(self, request):
        """Cleanup a testing directory once we are finished."""
        def reset_server_config():
            set_server_configuration(ServerConfig())
        request.addfinalizer(reset_server_config)

    def test__global_server(self, server_config):
        set_server_configuration(server_config)
        print(dpf.core.SERVER_CONFIGURATION)
        shutdown_all_session_servers()
        _global_server()
        assert has_local_server()

    def test_set_server_configuration(self, server_config):
        set_server_configuration(server_config)
        assert dpf.core.SERVER_CONFIGURATION == server_config

    def test_start_local_server(self, server_config):
        set_server_configuration(server_config)
        print(dpf.core.SERVER_CONFIGURATION)
        server = start_local_server(timeout=1)
        assert has_local_server()
        server = None
        shutdown_all_session_servers()

    def test_start_local_server_with_config(self, server_config):
        set_server_configuration(None)
        shutdown_all_session_servers()
        start_local_server(config=server_config)
        assert has_local_server()
        shutdown_all_session_servers()

    def test_connect_to_server(self, server_config):
        set_server_configuration(server_config)
        print(dpf.core.SERVER_CONFIGURATION)
        shutdown_all_session_servers()
        start_local_server(timeout=10.)
        print("has_local_server", has_local_server())
        if hasattr(dpf.core.SERVER, "ip"):
            connect_to_server(ip=dpf.core.SERVER.ip, port=dpf.core.SERVER.port, timeout=10., as_global=False)
        else:
            connect_to_server(timeout=10., as_global=False)
        assert has_local_server()

    def test_shutdown_all_session_servers(self, server_config):
        set_server_configuration(server_config)
        print(dpf.core.SERVER_CONFIGURATION)
        start_local_server(timeout=1)
        shutdown_all_session_servers()
        assert not has_local_server()


@pytest.mark.parametrize("server_config", server_configs)
class TestServer:
    @pytest.fixture(scope="class", autouse=True)
    def cleanup(self, request):
        """Cleanup a testing directory once we are finished."""

        def reset_server_config():
            set_server_configuration(ServerConfig())

        request.addfinalizer(reset_server_config)

    def test_available_api_types(self, server_config):
        set_server_configuration(server_config)
        server = get_or_create_server(None)
        assert has_local_server()
        types = server.available_api_types

    def test_client(self, server_config):
        set_server_configuration(server_config)
        server = get_or_create_server(None)
        assert has_local_server()
        client = server.client


def test_busy_port():
    if not dpf.core.SERVER:
        start_local_server()
    busy_port = dpf.core.SERVER.port
    with pytest.raises(errors.InvalidPortError):
        server_types.launch_dpf(ansys_path = dpf.core.misc.find_ansys(), port=busy_port)
    server = start_local_server(as_global=False, port=busy_port)
    assert server.port != busy_port
