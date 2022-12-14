"""
migrate_to_h5dpf
================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class migrate_to_h5dpf(Operator):
    """Read mesh properties from the results files contained in the streams
    or data sources and make those properties available through a mesh
    selection manager in output.

    Parameters
    ----------
    filename : str
        Filename of the migrated file
    comma_separated_list_of_results : str, optional
        List of result (source operator names) that
        will be stored. if empty, all
        available results will be converted.
    all_time_sets : bool, optional
        Default is true
    streams_container : StreamsContainer, optional
        Streams (result file container) (optional)
    data_sources : DataSources, optional
        If the stream is null then we need to get the
        file path from the data sources


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.migrate_to_h5dpf()

    >>> # Make input connections
    >>> my_filename = str()
    >>> op.inputs.filename.connect(my_filename)
    >>> my_comma_separated_list_of_results = str()
    >>> op.inputs.comma_separated_list_of_results.connect(my_comma_separated_list_of_results)
    >>> my_all_time_sets = bool()
    >>> op.inputs.all_time_sets.connect(my_all_time_sets)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.migrate_to_h5dpf(
    ...     filename=my_filename,
    ...     comma_separated_list_of_results=my_comma_separated_list_of_results,
    ...     all_time_sets=my_all_time_sets,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_migrated_file = op.outputs.migrated_file()
    """

    def __init__(
        self,
        filename=None,
        comma_separated_list_of_results=None,
        all_time_sets=None,
        streams_container=None,
        data_sources=None,
        config=None,
        server=None,
    ):
        super().__init__(name="hdf5::h5dpf::migrate_file", config=config, server=server)
        self._inputs = InputsMigrateToH5Dpf(self)
        self._outputs = OutputsMigrateToH5Dpf(self)
        if filename is not None:
            self.inputs.filename.connect(filename)
        if comma_separated_list_of_results is not None:
            self.inputs.comma_separated_list_of_results.connect(
                comma_separated_list_of_results
            )
        if all_time_sets is not None:
            self.inputs.all_time_sets.connect(all_time_sets)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        description = """Read mesh properties from the results files contained in the streams
            or data sources and make those properties available
            through a mesh selection manager in output."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="filename",
                    type_names=["string"],
                    optional=False,
                    document="""Filename of the migrated file""",
                ),
                1: PinSpecification(
                    name="comma_separated_list_of_results",
                    type_names=["string"],
                    optional=True,
                    document="""List of result (source operator names) that
        will be stored. if empty, all
        available results will be converted.""",
                ),
                2: PinSpecification(
                    name="all_time_sets",
                    type_names=["bool"],
                    optional=True,
                    document="""Default is true""",
                ),
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=True,
                    document="""Streams (result file container) (optional)""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=True,
                    document="""If the stream is null then we need to get the
        file path from the data sources""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="migrated_file",
                    type_names=["data_sources"],
                    optional=False,
                    document="""""",
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
        return Operator.default_config(name="hdf5::h5dpf::migrate_file", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMigrateToH5Dpf
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMigrateToH5Dpf
        """
        return super().outputs


class InputsMigrateToH5Dpf(_Inputs):
    """Intermediate class used to connect user inputs to
    migrate_to_h5dpf operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.migrate_to_h5dpf()
    >>> my_filename = str()
    >>> op.inputs.filename.connect(my_filename)
    >>> my_comma_separated_list_of_results = str()
    >>> op.inputs.comma_separated_list_of_results.connect(my_comma_separated_list_of_results)
    >>> my_all_time_sets = bool()
    >>> op.inputs.all_time_sets.connect(my_all_time_sets)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(migrate_to_h5dpf._spec().inputs, op)
        self._filename = Input(migrate_to_h5dpf._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._filename)
        self._comma_separated_list_of_results = Input(
            migrate_to_h5dpf._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._comma_separated_list_of_results)
        self._all_time_sets = Input(migrate_to_h5dpf._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._all_time_sets)
        self._streams_container = Input(
            migrate_to_h5dpf._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(migrate_to_h5dpf._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)

    @property
    def filename(self):
        """Allows to connect filename input to the operator.

        Filename of the migrated file

        Parameters
        ----------
        my_filename : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.migrate_to_h5dpf()
        >>> op.inputs.filename.connect(my_filename)
        >>> # or
        >>> op.inputs.filename(my_filename)
        """
        return self._filename

    @property
    def comma_separated_list_of_results(self):
        """Allows to connect comma_separated_list_of_results input to the operator.

        List of result (source operator names) that
        will be stored. if empty, all
        available results will be converted.

        Parameters
        ----------
        my_comma_separated_list_of_results : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.migrate_to_h5dpf()
        >>> op.inputs.comma_separated_list_of_results.connect(my_comma_separated_list_of_results)
        >>> # or
        >>> op.inputs.comma_separated_list_of_results(my_comma_separated_list_of_results)
        """
        return self._comma_separated_list_of_results

    @property
    def all_time_sets(self):
        """Allows to connect all_time_sets input to the operator.

        Default is true

        Parameters
        ----------
        my_all_time_sets : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.migrate_to_h5dpf()
        >>> op.inputs.all_time_sets.connect(my_all_time_sets)
        >>> # or
        >>> op.inputs.all_time_sets(my_all_time_sets)
        """
        return self._all_time_sets

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator.

        Streams (result file container) (optional)

        Parameters
        ----------
        my_streams_container : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.migrate_to_h5dpf()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        If the stream is null then we need to get the
        file path from the data sources

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.migrate_to_h5dpf()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsMigrateToH5Dpf(_Outputs):
    """Intermediate class used to get outputs from
    migrate_to_h5dpf operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.migrate_to_h5dpf()
    >>> # Connect inputs : op.inputs. ...
    >>> result_migrated_file = op.outputs.migrated_file()
    """

    def __init__(self, op: Operator):
        super().__init__(migrate_to_h5dpf._spec().outputs, op)
        self._migrated_file = Output(migrate_to_h5dpf._spec().output_pin(0), 0, op)
        self._outputs.append(self._migrated_file)

    @property
    def migrated_file(self):
        """Allows to get migrated_file output of the operator

        Returns
        ----------
        my_migrated_file : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.migrate_to_h5dpf()
        >>> # Connect inputs : op.inputs. ...
        >>> result_migrated_file = op.outputs.migrated_file()
        """  # noqa: E501
        return self._migrated_file