"""
migrate_to_vtu
==============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class migrate_to_vtu(Operator):
    """Extract all results from a datasources and exports them into vtu
    format. All the connected inputs are forwarded to the result
    providers operators.

    Parameters
    ----------
    time_scoping : Scoping, optional
        Time sets to export, default is all
    streams_container : StreamsContainer, optional
        Result file container allowed to be kept open
        to cache data
    data_sources : DataSources
        Result file path container, used if no
        streams are set
    directory : str
        Directory path
    base_name : str, optional
        Vtu base file name, (default is file)
    result1 : str, optional
        If operator's names are connected to this
        pin, only these results are exported
        (else all available results are
        exported)
    result2 : str, optional
        If operator's names are connected to this
        pin, only these results are exported
        (else all available results are
        exported)
    write_mode : str, optional
        Available are rawbinarycompressed, rawbinary,
        base64appended, base64inline, ascii,
        default is (rawbinarycompressed)


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.migrate_to_vtu()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_directory = str()
    >>> op.inputs.directory.connect(my_directory)
    >>> my_base_name = str()
    >>> op.inputs.base_name.connect(my_base_name)
    >>> my_result1 = str()
    >>> op.inputs.result1.connect(my_result1)
    >>> my_result2 = str()
    >>> op.inputs.result2.connect(my_result2)
    >>> my_write_mode = str()
    >>> op.inputs.write_mode.connect(my_write_mode)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.migrate_to_vtu(
    ...     time_scoping=my_time_scoping,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     directory=my_directory,
    ...     base_name=my_base_name,
    ...     result1=my_result1,
    ...     result2=my_result2,
    ...     write_mode=my_write_mode,
    ... )

    >>> # Get output data
    >>> result_path = op.outputs.path()
    """

    def __init__(
        self,
        time_scoping=None,
        streams_container=None,
        data_sources=None,
        directory=None,
        base_name=None,
        result1=None,
        result2=None,
        write_mode=None,
        config=None,
        server=None,
    ):
        super().__init__(name="migrate_to_vtu", config=config, server=server)
        self._inputs = InputsMigrateToVtu(self)
        self._outputs = OutputsMigrateToVtu(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if directory is not None:
            self.inputs.directory.connect(directory)
        if base_name is not None:
            self.inputs.base_name.connect(base_name)
        if result1 is not None:
            self.inputs.result1.connect(result1)
        if result2 is not None:
            self.inputs.result2.connect(result2)
        if write_mode is not None:
            self.inputs.write_mode.connect(write_mode)

    @staticmethod
    def _spec():
        description = """Extract all results from a datasources and exports them into vtu
            format. All the connected inputs are forwarded to the
            result providers operators."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_scoping",
                    type_names=["scoping", "vector<int32>"],
                    optional=True,
                    document="""Time sets to export, default is all""",
                ),
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=True,
                    document="""Result file container allowed to be kept open
        to cache data""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""Result file path container, used if no
        streams are set""",
                ),
                20: PinSpecification(
                    name="directory",
                    type_names=["string"],
                    optional=False,
                    document="""Directory path""",
                ),
                21: PinSpecification(
                    name="base_name",
                    type_names=["string"],
                    optional=True,
                    document="""Vtu base file name, (default is file)""",
                ),
                30: PinSpecification(
                    name="result",
                    type_names=["string"],
                    optional=True,
                    document="""If operator's names are connected to this
        pin, only these results are exported
        (else all available results are
        exported)""",
                ),
                31: PinSpecification(
                    name="result",
                    type_names=["string"],
                    optional=True,
                    document="""If operator's names are connected to this
        pin, only these results are exported
        (else all available results are
        exported)""",
                ),
                100: PinSpecification(
                    name="write_mode",
                    type_names=["string"],
                    optional=True,
                    document="""Available are rawbinarycompressed, rawbinary,
        base64appended, base64inline, ascii,
        default is (rawbinarycompressed)""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="path",
                    type_names=["data_sources"],
                    optional=False,
                    document="""List of output vtu file path""",
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
        return Operator.default_config(name="migrate_to_vtu", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMigrateToVtu
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMigrateToVtu
        """
        return super().outputs


class InputsMigrateToVtu(_Inputs):
    """Intermediate class used to connect user inputs to
    migrate_to_vtu operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.migrate_to_vtu()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_directory = str()
    >>> op.inputs.directory.connect(my_directory)
    >>> my_base_name = str()
    >>> op.inputs.base_name.connect(my_base_name)
    >>> my_result1 = str()
    >>> op.inputs.result1.connect(my_result1)
    >>> my_result2 = str()
    >>> op.inputs.result2.connect(my_result2)
    >>> my_write_mode = str()
    >>> op.inputs.write_mode.connect(my_write_mode)
    """

    def __init__(self, op: Operator):
        super().__init__(migrate_to_vtu._spec().inputs, op)
        self._time_scoping = Input(migrate_to_vtu._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._time_scoping)
        self._streams_container = Input(migrate_to_vtu._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._streams_container)
        self._data_sources = Input(migrate_to_vtu._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)
        self._directory = Input(migrate_to_vtu._spec().input_pin(20), 20, op, -1)
        self._inputs.append(self._directory)
        self._base_name = Input(migrate_to_vtu._spec().input_pin(21), 21, op, -1)
        self._inputs.append(self._base_name)
        self._result1 = Input(migrate_to_vtu._spec().input_pin(30), 30, op, 0)
        self._inputs.append(self._result1)
        self._result2 = Input(migrate_to_vtu._spec().input_pin(31), 31, op, 1)
        self._inputs.append(self._result2)
        self._write_mode = Input(migrate_to_vtu._spec().input_pin(100), 100, op, -1)
        self._inputs.append(self._write_mode)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        Time sets to export, default is all

        Parameters
        ----------
        my_time_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.migrate_to_vtu()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator.

        Result file container allowed to be kept open
        to cache data

        Parameters
        ----------
        my_streams_container : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.migrate_to_vtu()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Result file path container, used if no
        streams are set

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.migrate_to_vtu()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def directory(self):
        """Allows to connect directory input to the operator.

        Directory path

        Parameters
        ----------
        my_directory : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.migrate_to_vtu()
        >>> op.inputs.directory.connect(my_directory)
        >>> # or
        >>> op.inputs.directory(my_directory)
        """
        return self._directory

    @property
    def base_name(self):
        """Allows to connect base_name input to the operator.

        Vtu base file name, (default is file)

        Parameters
        ----------
        my_base_name : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.migrate_to_vtu()
        >>> op.inputs.base_name.connect(my_base_name)
        >>> # or
        >>> op.inputs.base_name(my_base_name)
        """
        return self._base_name

    @property
    def result1(self):
        """Allows to connect result1 input to the operator.

        If operator's names are connected to this
        pin, only these results are exported
        (else all available results are
        exported)

        Parameters
        ----------
        my_result1 : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.migrate_to_vtu()
        >>> op.inputs.result1.connect(my_result1)
        >>> # or
        >>> op.inputs.result1(my_result1)
        """
        return self._result1

    @property
    def result2(self):
        """Allows to connect result2 input to the operator.

        If operator's names are connected to this
        pin, only these results are exported
        (else all available results are
        exported)

        Parameters
        ----------
        my_result2 : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.migrate_to_vtu()
        >>> op.inputs.result2.connect(my_result2)
        >>> # or
        >>> op.inputs.result2(my_result2)
        """
        return self._result2

    @property
    def write_mode(self):
        """Allows to connect write_mode input to the operator.

        Available are rawbinarycompressed, rawbinary,
        base64appended, base64inline, ascii,
        default is (rawbinarycompressed)

        Parameters
        ----------
        my_write_mode : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.migrate_to_vtu()
        >>> op.inputs.write_mode.connect(my_write_mode)
        >>> # or
        >>> op.inputs.write_mode(my_write_mode)
        """
        return self._write_mode


class OutputsMigrateToVtu(_Outputs):
    """Intermediate class used to get outputs from
    migrate_to_vtu operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.migrate_to_vtu()
    >>> # Connect inputs : op.inputs. ...
    >>> result_path = op.outputs.path()
    """

    def __init__(self, op: Operator):
        super().__init__(migrate_to_vtu._spec().outputs, op)
        self._path = Output(migrate_to_vtu._spec().output_pin(0), 0, op)
        self._outputs.append(self._path)

    @property
    def path(self):
        """Allows to get path output of the operator

        Returns
        ----------
        my_path : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.migrate_to_vtu()
        >>> # Connect inputs : op.inputs. ...
        >>> result_path = op.outputs.path()
        """  # noqa: E501
        return self._path
