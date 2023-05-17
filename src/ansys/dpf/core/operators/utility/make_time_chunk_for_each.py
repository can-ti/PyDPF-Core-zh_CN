"""
make_time_chunk_for_each
========================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class make_time_chunk_for_each(Operator):
    """Splits a list of time/freq values into chunks depending on evaluated
    result properties,mesh size and max number of bytes accepted and
    calls 'make_for_each_range' to generate a range that can be
    consumed by the for_each operator

    Parameters
    ----------
    target_time_freq_values : float
        List of time/freq values to potentially split
        in chunks.
    operator_to_iterate : Operator
        Operator that must be reconnected with the
        range values.
    pin_index : int
    abstract_meshed_region : MeshedRegion
        The number of nodes (for "nodal" results) or
        number of elements (for "elemental"
        results) is used to compute the
        chunk.
    chunk_config : DataTree
        A data tree with an int attribute
        "max_num_bytes", an int attribute
        "dimensionality" (average result size
        by entity), a string attribute
        "location" ("nodal" or"elemental") is
        expected.
    producer_op11 : Operator
    producer_op12 : Operator
    output_pin_of_producer_op11 : int
    output_pin_of_producer_op12 : int
    input_pin_of_consumer_op11 : int
    input_pin_of_consumer_op12 : int
    consumer_op11 : Operator
    consumer_op12 : Operator


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.make_time_chunk_for_each()

    >>> # Make input connections
    >>> my_target_time_freq_values = float()
    >>> op.inputs.target_time_freq_values.connect(my_target_time_freq_values)
    >>> my_operator_to_iterate = dpf.Operator()
    >>> op.inputs.operator_to_iterate.connect(my_operator_to_iterate)
    >>> my_pin_index = int()
    >>> op.inputs.pin_index.connect(my_pin_index)
    >>> my_abstract_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
    >>> my_chunk_config = dpf.DataTree()
    >>> op.inputs.chunk_config.connect(my_chunk_config)
    >>> my_producer_op11 = dpf.Operator()
    >>> op.inputs.producer_op11.connect(my_producer_op11)
    >>> my_producer_op12 = dpf.Operator()
    >>> op.inputs.producer_op12.connect(my_producer_op12)
    >>> my_output_pin_of_producer_op11 = int()
    >>> op.inputs.output_pin_of_producer_op11.connect(my_output_pin_of_producer_op11)
    >>> my_output_pin_of_producer_op12 = int()
    >>> op.inputs.output_pin_of_producer_op12.connect(my_output_pin_of_producer_op12)
    >>> my_input_pin_of_consumer_op11 = int()
    >>> op.inputs.input_pin_of_consumer_op11.connect(my_input_pin_of_consumer_op11)
    >>> my_input_pin_of_consumer_op12 = int()
    >>> op.inputs.input_pin_of_consumer_op12.connect(my_input_pin_of_consumer_op12)
    >>> my_consumer_op11 = dpf.Operator()
    >>> op.inputs.consumer_op11.connect(my_consumer_op11)
    >>> my_consumer_op12 = dpf.Operator()
    >>> op.inputs.consumer_op12.connect(my_consumer_op12)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.make_time_chunk_for_each(
    ...     target_time_freq_values=my_target_time_freq_values,
    ...     operator_to_iterate=my_operator_to_iterate,
    ...     pin_index=my_pin_index,
    ...     abstract_meshed_region=my_abstract_meshed_region,
    ...     chunk_config=my_chunk_config,
    ...     producer_op11=my_producer_op11,
    ...     producer_op12=my_producer_op12,
    ...     output_pin_of_producer_op11=my_output_pin_of_producer_op11,
    ...     output_pin_of_producer_op12=my_output_pin_of_producer_op12,
    ...     input_pin_of_consumer_op11=my_input_pin_of_consumer_op11,
    ...     input_pin_of_consumer_op12=my_input_pin_of_consumer_op12,
    ...     consumer_op11=my_consumer_op11,
    ...     consumer_op12=my_consumer_op12,
    ... )

    >>> # Get output data
    >>> result_chunks = op.outputs.chunks()
    """

    def __init__(
        self,
        target_time_freq_values=None,
        operator_to_iterate=None,
        pin_index=None,
        abstract_meshed_region=None,
        chunk_config=None,
        producer_op11=None,
        producer_op12=None,
        output_pin_of_producer_op11=None,
        output_pin_of_producer_op12=None,
        input_pin_of_consumer_op11=None,
        input_pin_of_consumer_op12=None,
        consumer_op11=None,
        consumer_op12=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="mechanical::make_time_chunk_for_each", config=config, server=server
        )
        self._inputs = InputsMakeTimeChunkForEach(self)
        self._outputs = OutputsMakeTimeChunkForEach(self)
        if target_time_freq_values is not None:
            self.inputs.target_time_freq_values.connect(target_time_freq_values)
        if operator_to_iterate is not None:
            self.inputs.operator_to_iterate.connect(operator_to_iterate)
        if pin_index is not None:
            self.inputs.pin_index.connect(pin_index)
        if abstract_meshed_region is not None:
            self.inputs.abstract_meshed_region.connect(abstract_meshed_region)
        if chunk_config is not None:
            self.inputs.chunk_config.connect(chunk_config)
        if producer_op11 is not None:
            self.inputs.producer_op11.connect(producer_op11)
        if producer_op12 is not None:
            self.inputs.producer_op12.connect(producer_op12)
        if output_pin_of_producer_op11 is not None:
            self.inputs.output_pin_of_producer_op11.connect(output_pin_of_producer_op11)
        if output_pin_of_producer_op12 is not None:
            self.inputs.output_pin_of_producer_op12.connect(output_pin_of_producer_op12)
        if input_pin_of_consumer_op11 is not None:
            self.inputs.input_pin_of_consumer_op11.connect(input_pin_of_consumer_op11)
        if input_pin_of_consumer_op12 is not None:
            self.inputs.input_pin_of_consumer_op12.connect(input_pin_of_consumer_op12)
        if consumer_op11 is not None:
            self.inputs.consumer_op11.connect(consumer_op11)
        if consumer_op12 is not None:
            self.inputs.consumer_op12.connect(consumer_op12)

    @staticmethod
    def _spec():
        description = """Splits a list of time/freq values into chunks depending on evaluated
            result properties,mesh size and max number of bytes
            accepted and calls &quot;make_for_each_range&quot; to generate a
            range that can be consumed by the for_each operator"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="target_time_freq_values",
                    type_names=["vector<double>", "double"],
                    optional=False,
                    document="""List of time/freq values to potentially split
        in chunks.""",
                ),
                1: PinSpecification(
                    name="operator_to_iterate",
                    type_names=["operator"],
                    optional=False,
                    document="""Operator that must be reconnected with the
        range values.""",
                ),
                2: PinSpecification(
                    name="pin_index",
                    type_names=["int32"],
                    optional=False,
                    document="""""",
                ),
                7: PinSpecification(
                    name="abstract_meshed_region",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""The number of nodes (for "nodal" results) or
        number of elements (for "elemental"
        results) is used to compute the
        chunk.""",
                ),
                200: PinSpecification(
                    name="chunk_config",
                    type_names=["abstract_data_tree"],
                    optional=False,
                    document="""A data tree with an int attribute
        "max_num_bytes", an int attribute
        "dimensionality" (average result size
        by entity), a string attribute
        "location" ("nodal" or"elemental") is
        expected.""",
                ),
                1000: PinSpecification(
                    name="producer_op1",
                    type_names=["operator"],
                    optional=False,
                    document="""""",
                ),
                1001: PinSpecification(
                    name="producer_op1",
                    type_names=["operator"],
                    optional=False,
                    document="""""",
                ),
                1001: PinSpecification(
                    name="output_pin_of_producer_op1",
                    type_names=["int32"],
                    optional=False,
                    document="""""",
                ),
                1002: PinSpecification(
                    name="output_pin_of_producer_op1",
                    type_names=["int32"],
                    optional=False,
                    document="""""",
                ),
                1002: PinSpecification(
                    name="input_pin_of_consumer_op1",
                    type_names=["int32"],
                    optional=False,
                    document="""""",
                ),
                1003: PinSpecification(
                    name="input_pin_of_consumer_op1",
                    type_names=["int32"],
                    optional=False,
                    document="""""",
                ),
                1003: PinSpecification(
                    name="consumer_op1",
                    type_names=["operator"],
                    optional=False,
                    document="""""",
                ),
                1004: PinSpecification(
                    name="consumer_op1",
                    type_names=["operator"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="chunks",
                    optional=False,
                    document="""To connect to "producer_consumer_for_each"
        operator on pin 0""",
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
        return Operator.default_config(
            name="mechanical::make_time_chunk_for_each", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMakeTimeChunkForEach
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMakeTimeChunkForEach
        """
        return super().outputs


class InputsMakeTimeChunkForEach(_Inputs):
    """Intermediate class used to connect user inputs to
    make_time_chunk_for_each operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.make_time_chunk_for_each()
    >>> my_target_time_freq_values = float()
    >>> op.inputs.target_time_freq_values.connect(my_target_time_freq_values)
    >>> my_operator_to_iterate = dpf.Operator()
    >>> op.inputs.operator_to_iterate.connect(my_operator_to_iterate)
    >>> my_pin_index = int()
    >>> op.inputs.pin_index.connect(my_pin_index)
    >>> my_abstract_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
    >>> my_chunk_config = dpf.DataTree()
    >>> op.inputs.chunk_config.connect(my_chunk_config)
    >>> my_producer_op11 = dpf.Operator()
    >>> op.inputs.producer_op11.connect(my_producer_op11)
    >>> my_producer_op12 = dpf.Operator()
    >>> op.inputs.producer_op12.connect(my_producer_op12)
    >>> my_output_pin_of_producer_op11 = int()
    >>> op.inputs.output_pin_of_producer_op11.connect(my_output_pin_of_producer_op11)
    >>> my_output_pin_of_producer_op12 = int()
    >>> op.inputs.output_pin_of_producer_op12.connect(my_output_pin_of_producer_op12)
    >>> my_input_pin_of_consumer_op11 = int()
    >>> op.inputs.input_pin_of_consumer_op11.connect(my_input_pin_of_consumer_op11)
    >>> my_input_pin_of_consumer_op12 = int()
    >>> op.inputs.input_pin_of_consumer_op12.connect(my_input_pin_of_consumer_op12)
    >>> my_consumer_op11 = dpf.Operator()
    >>> op.inputs.consumer_op11.connect(my_consumer_op11)
    >>> my_consumer_op12 = dpf.Operator()
    >>> op.inputs.consumer_op12.connect(my_consumer_op12)
    """

    def __init__(self, op: Operator):
        super().__init__(make_time_chunk_for_each._spec().inputs, op)
        self._target_time_freq_values = Input(
            make_time_chunk_for_each._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._target_time_freq_values)
        self._operator_to_iterate = Input(
            make_time_chunk_for_each._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._operator_to_iterate)
        self._pin_index = Input(
            make_time_chunk_for_each._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._pin_index)
        self._abstract_meshed_region = Input(
            make_time_chunk_for_each._spec().input_pin(7), 7, op, -1
        )
        self._inputs.append(self._abstract_meshed_region)
        self._chunk_config = Input(
            make_time_chunk_for_each._spec().input_pin(200), 200, op, -1
        )
        self._inputs.append(self._chunk_config)
        self._producer_op11 = Input(
            make_time_chunk_for_each._spec().input_pin(1000), 1000, op, 0
        )
        self._inputs.append(self._producer_op11)
        self._producer_op12 = Input(
            make_time_chunk_for_each._spec().input_pin(1001), 1001, op, 1
        )
        self._inputs.append(self._producer_op12)
        self._output_pin_of_producer_op11 = Input(
            make_time_chunk_for_each._spec().input_pin(1001), 1001, op, 0
        )
        self._inputs.append(self._output_pin_of_producer_op11)
        self._output_pin_of_producer_op12 = Input(
            make_time_chunk_for_each._spec().input_pin(1002), 1002, op, 1
        )
        self._inputs.append(self._output_pin_of_producer_op12)
        self._input_pin_of_consumer_op11 = Input(
            make_time_chunk_for_each._spec().input_pin(1002), 1002, op, 0
        )
        self._inputs.append(self._input_pin_of_consumer_op11)
        self._input_pin_of_consumer_op12 = Input(
            make_time_chunk_for_each._spec().input_pin(1003), 1003, op, 1
        )
        self._inputs.append(self._input_pin_of_consumer_op12)
        self._consumer_op11 = Input(
            make_time_chunk_for_each._spec().input_pin(1003), 1003, op, 0
        )
        self._inputs.append(self._consumer_op11)
        self._consumer_op12 = Input(
            make_time_chunk_for_each._spec().input_pin(1004), 1004, op, 1
        )
        self._inputs.append(self._consumer_op12)

    @property
    def target_time_freq_values(self):
        """Allows to connect target_time_freq_values input to the operator.

        List of time/freq values to potentially split
        in chunks.

        Parameters
        ----------
        my_target_time_freq_values : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.target_time_freq_values.connect(my_target_time_freq_values)
        >>> # or
        >>> op.inputs.target_time_freq_values(my_target_time_freq_values)
        """
        return self._target_time_freq_values

    @property
    def operator_to_iterate(self):
        """Allows to connect operator_to_iterate input to the operator.

        Operator that must be reconnected with the
        range values.

        Parameters
        ----------
        my_operator_to_iterate : Operator

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.operator_to_iterate.connect(my_operator_to_iterate)
        >>> # or
        >>> op.inputs.operator_to_iterate(my_operator_to_iterate)
        """
        return self._operator_to_iterate

    @property
    def pin_index(self):
        """Allows to connect pin_index input to the operator.

        Parameters
        ----------
        my_pin_index : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.pin_index.connect(my_pin_index)
        >>> # or
        >>> op.inputs.pin_index(my_pin_index)
        """
        return self._pin_index

    @property
    def abstract_meshed_region(self):
        """Allows to connect abstract_meshed_region input to the operator.

        The number of nodes (for "nodal" results) or
        number of elements (for "elemental"
        results) is used to compute the
        chunk.

        Parameters
        ----------
        my_abstract_meshed_region : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
        >>> # or
        >>> op.inputs.abstract_meshed_region(my_abstract_meshed_region)
        """
        return self._abstract_meshed_region

    @property
    def chunk_config(self):
        """Allows to connect chunk_config input to the operator.

        A data tree with an int attribute
        "max_num_bytes", an int attribute
        "dimensionality" (average result size
        by entity), a string attribute
        "location" ("nodal" or"elemental") is
        expected.

        Parameters
        ----------
        my_chunk_config : DataTree

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.chunk_config.connect(my_chunk_config)
        >>> # or
        >>> op.inputs.chunk_config(my_chunk_config)
        """
        return self._chunk_config

    @property
    def producer_op11(self):
        """Allows to connect producer_op11 input to the operator.

        Parameters
        ----------
        my_producer_op11 : Operator

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.producer_op11.connect(my_producer_op11)
        >>> # or
        >>> op.inputs.producer_op11(my_producer_op11)
        """
        return self._producer_op11

    @property
    def producer_op12(self):
        """Allows to connect producer_op12 input to the operator.

        Parameters
        ----------
        my_producer_op12 : Operator

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.producer_op12.connect(my_producer_op12)
        >>> # or
        >>> op.inputs.producer_op12(my_producer_op12)
        """
        return self._producer_op12

    @property
    def output_pin_of_producer_op11(self):
        """Allows to connect output_pin_of_producer_op11 input to the operator.

        Parameters
        ----------
        my_output_pin_of_producer_op11 : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.output_pin_of_producer_op11.connect(my_output_pin_of_producer_op11)
        >>> # or
        >>> op.inputs.output_pin_of_producer_op11(my_output_pin_of_producer_op11)
        """
        return self._output_pin_of_producer_op11

    @property
    def output_pin_of_producer_op12(self):
        """Allows to connect output_pin_of_producer_op12 input to the operator.

        Parameters
        ----------
        my_output_pin_of_producer_op12 : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.output_pin_of_producer_op12.connect(my_output_pin_of_producer_op12)
        >>> # or
        >>> op.inputs.output_pin_of_producer_op12(my_output_pin_of_producer_op12)
        """
        return self._output_pin_of_producer_op12

    @property
    def input_pin_of_consumer_op11(self):
        """Allows to connect input_pin_of_consumer_op11 input to the operator.

        Parameters
        ----------
        my_input_pin_of_consumer_op11 : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.input_pin_of_consumer_op11.connect(my_input_pin_of_consumer_op11)
        >>> # or
        >>> op.inputs.input_pin_of_consumer_op11(my_input_pin_of_consumer_op11)
        """
        return self._input_pin_of_consumer_op11

    @property
    def input_pin_of_consumer_op12(self):
        """Allows to connect input_pin_of_consumer_op12 input to the operator.

        Parameters
        ----------
        my_input_pin_of_consumer_op12 : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.input_pin_of_consumer_op12.connect(my_input_pin_of_consumer_op12)
        >>> # or
        >>> op.inputs.input_pin_of_consumer_op12(my_input_pin_of_consumer_op12)
        """
        return self._input_pin_of_consumer_op12

    @property
    def consumer_op11(self):
        """Allows to connect consumer_op11 input to the operator.

        Parameters
        ----------
        my_consumer_op11 : Operator

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.consumer_op11.connect(my_consumer_op11)
        >>> # or
        >>> op.inputs.consumer_op11(my_consumer_op11)
        """
        return self._consumer_op11

    @property
    def consumer_op12(self):
        """Allows to connect consumer_op12 input to the operator.

        Parameters
        ----------
        my_consumer_op12 : Operator

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> op.inputs.consumer_op12.connect(my_consumer_op12)
        >>> # or
        >>> op.inputs.consumer_op12(my_consumer_op12)
        """
        return self._consumer_op12


class OutputsMakeTimeChunkForEach(_Outputs):
    """Intermediate class used to get outputs from
    make_time_chunk_for_each operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.make_time_chunk_for_each()
    >>> # Connect inputs : op.inputs. ...
    >>> result_chunks = op.outputs.chunks()
    """

    def __init__(self, op: Operator):
        super().__init__(make_time_chunk_for_each._spec().outputs, op)
        self._chunks = Output(make_time_chunk_for_each._spec().output_pin(0), 0, op)
        self._outputs.append(self._chunks)

    @property
    def chunks(self):
        """Allows to get chunks output of the operator

        Returns
        ----------
        my_chunks :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_time_chunk_for_each()
        >>> # Connect inputs : op.inputs. ...
        >>> result_chunks = op.outputs.chunks()
        """  # noqa: E501
        return self._chunks
