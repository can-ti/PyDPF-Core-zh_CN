"""
grpc_start_server
-----------------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class grpc_start_server(Operator):
    """Starts a dpf's grpc server (if local) or connect to one and keep it
    waiting for requests in a streams.

    Parameters
    ----------
    ip : str, optional
        If no ip address is put the local ip address
        is taken
    port : str or int, optional
        If no port is put port 50052 is taken
    starting_option : int, optional
        Default is 1 that starts server in new
        thread. with 0, this thread will be
        waiting for grpc calls and will not
        be usable for anything else. with 2,
        it the server will be started in a
        new process.
    should_start_server : bool, optional
        If true, the server is assumed to be local
        and is started. if false, only a
        client (able to send grpc calls) will
        be started
    data_sources : DataSources, optional
        A data sources with result key 'grpc' and
        file path port:ip can be used instead
        of the input port and ip.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.server.grpc_start_server()

    >>> # Make input connections
    >>> my_ip = str()
    >>> op.inputs.ip.connect(my_ip)
    >>> my_port = str()
    >>> op.inputs.port.connect(my_port)
    >>> my_starting_option = int()
    >>> op.inputs.starting_option.connect(my_starting_option)
    >>> my_should_start_server = bool()
    >>> op.inputs.should_start_server.connect(my_should_start_server)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.server.grpc_start_server(
    ...     ip=my_ip,
    ...     port=my_port,
    ...     starting_option=my_starting_option,
    ...     should_start_server=my_should_start_server,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_grpc_streams = op.outputs.grpc_streams()
    """

    def __init__(
        self,
        ip=None,
        port=None,
        starting_option=None,
        should_start_server=None,
        data_sources=None,
        config=None,
        server=None,
    ):
        super().__init__(name="grpc::stream_provider", config=config, server=server)
        self._inputs = InputsGrpcStartServer(self)
        self._outputs = OutputsGrpcStartServer(self)
        if ip is not None:
            self.inputs.ip.connect(ip)
        if port is not None:
            self.inputs.port.connect(port)
        if starting_option is not None:
            self.inputs.starting_option.connect(starting_option)
        if should_start_server is not None:
            self.inputs.should_start_server.connect(should_start_server)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        description = """Starts a dpf's grpc server (if local) or connect to one and keep it
            waiting for requests in a streams."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="ip",
                    type_names=["string"],
                    optional=True,
                    document="""If no ip address is put the local ip address
        is taken""",
                ),
                1: PinSpecification(
                    name="port",
                    type_names=["string", "int32"],
                    optional=True,
                    document="""If no port is put port 50052 is taken""",
                ),
                2: PinSpecification(
                    name="starting_option",
                    type_names=["int32"],
                    optional=True,
                    document="""Default is 1 that starts server in new
        thread. with 0, this thread will be
        waiting for grpc calls and will not
        be usable for anything else. with 2,
        it the server will be started in a
        new process.""",
                ),
                3: PinSpecification(
                    name="should_start_server",
                    type_names=["bool"],
                    optional=True,
                    document="""If true, the server is assumed to be local
        and is started. if false, only a
        client (able to send grpc calls) will
        be started""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=True,
                    document="""A data sources with result key 'grpc' and
        file path port:ip can be used instead
        of the input port and ip.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="grpc_streams",
                    type_names=["streams_container"],
                    optional=True,
                    document="""Dpf streams handling the server, if the
        server is started in this thread than
        nothing is added in output""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server=None):
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server : server.DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="grpc::stream_provider", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsGrpcStartServer
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsGrpcStartServer
        """
        return super().outputs


class InputsGrpcStartServer(_Inputs):
    """Intermediate class used to connect user inputs to
    grpc_start_server operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.server.grpc_start_server()
    >>> my_ip = str()
    >>> op.inputs.ip.connect(my_ip)
    >>> my_port = str()
    >>> op.inputs.port.connect(my_port)
    >>> my_starting_option = int()
    >>> op.inputs.starting_option.connect(my_starting_option)
    >>> my_should_start_server = bool()
    >>> op.inputs.should_start_server.connect(my_should_start_server)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(grpc_start_server._spec().inputs, op)
        self._ip = Input(grpc_start_server._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._ip)
        self._port = Input(grpc_start_server._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._port)
        self._starting_option = Input(grpc_start_server._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._starting_option)
        self._should_start_server = Input(
            grpc_start_server._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._should_start_server)
        self._data_sources = Input(grpc_start_server._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)

    @property
    def ip(self):
        """Allows to connect ip input to the operator.

        If no ip address is put the local ip address
        is taken

        Parameters
        ----------
        my_ip : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.server.grpc_start_server()
        >>> op.inputs.ip.connect(my_ip)
        >>> # or
        >>> op.inputs.ip(my_ip)
        """
        return self._ip

    @property
    def port(self):
        """Allows to connect port input to the operator.

        If no port is put port 50052 is taken

        Parameters
        ----------
        my_port : str or int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.server.grpc_start_server()
        >>> op.inputs.port.connect(my_port)
        >>> # or
        >>> op.inputs.port(my_port)
        """
        return self._port

    @property
    def starting_option(self):
        """Allows to connect starting_option input to the operator.

        Default is 1 that starts server in new
        thread. with 0, this thread will be
        waiting for grpc calls and will not
        be usable for anything else. with 2,
        it the server will be started in a
        new process.

        Parameters
        ----------
        my_starting_option : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.server.grpc_start_server()
        >>> op.inputs.starting_option.connect(my_starting_option)
        >>> # or
        >>> op.inputs.starting_option(my_starting_option)
        """
        return self._starting_option

    @property
    def should_start_server(self):
        """Allows to connect should_start_server input to the operator.

        If true, the server is assumed to be local
        and is started. if false, only a
        client (able to send grpc calls) will
        be started

        Parameters
        ----------
        my_should_start_server : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.server.grpc_start_server()
        >>> op.inputs.should_start_server.connect(my_should_start_server)
        >>> # or
        >>> op.inputs.should_start_server(my_should_start_server)
        """
        return self._should_start_server

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        A data sources with result key 'grpc' and
        file path port:ip can be used instead
        of the input port and ip.

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.server.grpc_start_server()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsGrpcStartServer(_Outputs):
    """Intermediate class used to get outputs from
    grpc_start_server operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.server.grpc_start_server()
    >>> # Connect inputs : op.inputs. ...
    >>> result_grpc_streams = op.outputs.grpc_streams()
    """

    def __init__(self, op: Operator):
        super().__init__(grpc_start_server._spec().outputs, op)
        self._grpc_streams = Output(grpc_start_server._spec().output_pin(0), 0, op)
        self._outputs.append(self._grpc_streams)

    @property
    def grpc_streams(self):
        """Allows to get grpc_streams output of the operator

        Returns
        ----------
        my_grpc_streams : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.server.grpc_start_server()
        >>> # Connect inputs : op.inputs. ...
        >>> result_grpc_streams = op.outputs.grpc_streams()
        """  # noqa: E501
        return self._grpc_streams
