"""
result_info_provider
====================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class result_info_provider(Operator):
    """Read the result info with information sucha as available results or
    unit system from the results files contained in the streams or
    data sources.

    Parameters
    ----------
    streams_container : StreamsContainer, optional
        Streams (result file container) (optional)
    data_sources : DataSources
        If the stream is null then we need to get the
        file path from the data sources


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.metadata.result_info_provider()

    >>> # Make input connections
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.metadata.result_info_provider(
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_result_info = op.outputs.result_info()
    """

    def __init__(
        self, streams_container=None, data_sources=None, config=None, server=None
    ):
        super().__init__(name="result_info_provider", config=config, server=server)
        self._inputs = InputsResultInfoProvider(self)
        self._outputs = OutputsResultInfoProvider(self)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        description = """Read the result info with information sucha as available results or
            unit system from the results files contained in the
            streams or data sources."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=True,
                    document="""Streams (result file container) (optional)""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""If the stream is null then we need to get the
        file path from the data sources""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="result_info",
                    type_names=["result_info"],
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
        return Operator.default_config(name="result_info_provider", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsResultInfoProvider
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsResultInfoProvider
        """
        return super().outputs


class InputsResultInfoProvider(_Inputs):
    """Intermediate class used to connect user inputs to
    result_info_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.metadata.result_info_provider()
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(result_info_provider._spec().inputs, op)
        self._streams_container = Input(
            result_info_provider._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(result_info_provider._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)

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
        >>> op = dpf.operators.metadata.result_info_provider()
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
        >>> op = dpf.operators.metadata.result_info_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsResultInfoProvider(_Outputs):
    """Intermediate class used to get outputs from
    result_info_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.metadata.result_info_provider()
    >>> # Connect inputs : op.inputs. ...
    >>> result_result_info = op.outputs.result_info()
    """

    def __init__(self, op: Operator):
        super().__init__(result_info_provider._spec().outputs, op)
        self._result_info = Output(result_info_provider._spec().output_pin(0), 0, op)
        self._outputs.append(self._result_info)

    @property
    def result_info(self):
        """Allows to get result_info output of the operator

        Returns
        ----------
        my_result_info : ResultInfo

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.metadata.result_info_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_result_info = op.outputs.result_info()
        """  # noqa: E501
        return self._result_info