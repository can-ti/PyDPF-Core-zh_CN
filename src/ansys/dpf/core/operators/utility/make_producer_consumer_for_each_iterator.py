"""
make_producer_consumer_for_each_iterator
========================================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class make_producer_consumer_for_each_iterator(Operator):
    """Generates an iterator that can be consumed by the for_each
    operator.The chain of Operators are split into a first part : the
    producers and a second part : the consumers.Asynchronous buffers
    are indeed to connect the producers and the consumers.

    Parameters
    ----------
    try_generate_iterable : bool, optional
        If true, already iterable values connected in
        pin 3 like vectors, scoping,
        timefreqsupport, containers and
        datasources are split to iterate on
        it (default is true)
    iterable : optional
        Iterable object, generated by
        make_for_each_range oeprator, that
        can be combined with the one
        currently generated.
    operator_to_iterate : Operator
        Operator that must be reconnected with the
        range values.
    pin_index : int
    valueA :
    valueB :
    valueC1 :
    valueC2 :
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
    >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()

    >>> # Make input connections
    >>> my_try_generate_iterable = bool()
    >>> op.inputs.try_generate_iterable.connect(my_try_generate_iterable)
    >>> my_iterable = dpf.()
    >>> op.inputs.iterable.connect(my_iterable)
    >>> my_operator_to_iterate = dpf.Operator()
    >>> op.inputs.operator_to_iterate.connect(my_operator_to_iterate)
    >>> my_pin_index = int()
    >>> op.inputs.pin_index.connect(my_pin_index)
    >>> my_valueA = dpf.()
    >>> op.inputs.valueA.connect(my_valueA)
    >>> my_valueB = dpf.()
    >>> op.inputs.valueB.connect(my_valueB)
    >>> my_valueC1 = dpf.()
    >>> op.inputs.valueC1.connect(my_valueC1)
    >>> my_valueC2 = dpf.()
    >>> op.inputs.valueC2.connect(my_valueC2)
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
    >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator(
    ...     try_generate_iterable=my_try_generate_iterable,
    ...     iterable=my_iterable,
    ...     operator_to_iterate=my_operator_to_iterate,
    ...     pin_index=my_pin_index,
    ...     valueA=my_valueA,
    ...     valueB=my_valueB,
    ...     valueC1=my_valueC1,
    ...     valueC2=my_valueC2,
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
    >>> result_iterator = op.outputs.iterator()
    """

    def __init__(
        self,
        try_generate_iterable=None,
        iterable=None,
        operator_to_iterate=None,
        pin_index=None,
        valueA=None,
        valueB=None,
        valueC1=None,
        valueC2=None,
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
            name="make_producer_consumer_for_each_iterator",
            config=config,
            server=server,
        )
        self._inputs = InputsMakeProducerConsumerForEachIterator(self)
        self._outputs = OutputsMakeProducerConsumerForEachIterator(self)
        if try_generate_iterable is not None:
            self.inputs.try_generate_iterable.connect(try_generate_iterable)
        if iterable is not None:
            self.inputs.iterable.connect(iterable)
        if operator_to_iterate is not None:
            self.inputs.operator_to_iterate.connect(operator_to_iterate)
        if pin_index is not None:
            self.inputs.pin_index.connect(pin_index)
        if valueA is not None:
            self.inputs.valueA.connect(valueA)
        if valueB is not None:
            self.inputs.valueB.connect(valueB)
        if valueC1 is not None:
            self.inputs.valueC1.connect(valueC1)
        if valueC2 is not None:
            self.inputs.valueC2.connect(valueC2)
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
        description = """Generates an iterator that can be consumed by the for_each
            operator.The chain of Operators are split into a first
            part : the producers and a second part : the
            consumers.Asynchronous buffers are indeed to connect the
            producers and the consumers."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                -1: PinSpecification(
                    name="try_generate_iterable",
                    type_names=["bool"],
                    optional=True,
                    document="""If true, already iterable values connected in
        pin 3 like vectors, scoping,
        timefreqsupport, containers and
        datasources are split to iterate on
        it (default is true)""",
                ),
                0: PinSpecification(
                    name="iterable",
                    type_names=["any"],
                    optional=True,
                    document="""Iterable object, generated by
        make_for_each_range oeprator, that
        can be combined with the one
        currently generated.""",
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
                3: PinSpecification(
                    name="valueA",
                    type_names=["any"],
                    optional=False,
                    document="""""",
                ),
                4: PinSpecification(
                    name="valueB",
                    type_names=["any"],
                    optional=False,
                    document="""""",
                ),
                5: PinSpecification(
                    name="valueC",
                    type_names=["any"],
                    optional=False,
                    document="""""",
                ),
                6: PinSpecification(
                    name="valueC",
                    type_names=["any"],
                    optional=False,
                    document="""""",
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
                    name="iterator",
                    optional=False,
                    document="""To connect to producer_consumer_for_each""",
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
            name="make_producer_consumer_for_each_iterator", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMakeProducerConsumerForEachIterator
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMakeProducerConsumerForEachIterator
        """
        return super().outputs


class InputsMakeProducerConsumerForEachIterator(_Inputs):
    """Intermediate class used to connect user inputs to
    make_producer_consumer_for_each_iterator operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
    >>> my_try_generate_iterable = bool()
    >>> op.inputs.try_generate_iterable.connect(my_try_generate_iterable)
    >>> my_iterable = dpf.()
    >>> op.inputs.iterable.connect(my_iterable)
    >>> my_operator_to_iterate = dpf.Operator()
    >>> op.inputs.operator_to_iterate.connect(my_operator_to_iterate)
    >>> my_pin_index = int()
    >>> op.inputs.pin_index.connect(my_pin_index)
    >>> my_valueA = dpf.()
    >>> op.inputs.valueA.connect(my_valueA)
    >>> my_valueB = dpf.()
    >>> op.inputs.valueB.connect(my_valueB)
    >>> my_valueC1 = dpf.()
    >>> op.inputs.valueC1.connect(my_valueC1)
    >>> my_valueC2 = dpf.()
    >>> op.inputs.valueC2.connect(my_valueC2)
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
        super().__init__(make_producer_consumer_for_each_iterator._spec().inputs, op)
        self._try_generate_iterable = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(-1), -1, op, -1
        )
        self._inputs.append(self._try_generate_iterable)
        self._iterable = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._iterable)
        self._operator_to_iterate = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._operator_to_iterate)
        self._pin_index = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._pin_index)
        self._valueA = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._valueA)
        self._valueB = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._valueB)
        self._valueC1 = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(5), 5, op, 0
        )
        self._inputs.append(self._valueC1)
        self._valueC2 = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(6), 6, op, 1
        )
        self._inputs.append(self._valueC2)
        self._producer_op11 = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(1000),
            1000,
            op,
            0,
        )
        self._inputs.append(self._producer_op11)
        self._producer_op12 = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(1001),
            1001,
            op,
            1,
        )
        self._inputs.append(self._producer_op12)
        self._output_pin_of_producer_op11 = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(1001),
            1001,
            op,
            0,
        )
        self._inputs.append(self._output_pin_of_producer_op11)
        self._output_pin_of_producer_op12 = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(1002),
            1002,
            op,
            1,
        )
        self._inputs.append(self._output_pin_of_producer_op12)
        self._input_pin_of_consumer_op11 = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(1002),
            1002,
            op,
            0,
        )
        self._inputs.append(self._input_pin_of_consumer_op11)
        self._input_pin_of_consumer_op12 = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(1003),
            1003,
            op,
            1,
        )
        self._inputs.append(self._input_pin_of_consumer_op12)
        self._consumer_op11 = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(1003),
            1003,
            op,
            0,
        )
        self._inputs.append(self._consumer_op11)
        self._consumer_op12 = Input(
            make_producer_consumer_for_each_iterator._spec().input_pin(1004),
            1004,
            op,
            1,
        )
        self._inputs.append(self._consumer_op12)

    @property
    def try_generate_iterable(self):
        """Allows to connect try_generate_iterable input to the operator.

        If true, already iterable values connected in
        pin 3 like vectors, scoping,
        timefreqsupport, containers and
        datasources are split to iterate on
        it (default is true)

        Parameters
        ----------
        my_try_generate_iterable : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
        >>> op.inputs.try_generate_iterable.connect(my_try_generate_iterable)
        >>> # or
        >>> op.inputs.try_generate_iterable(my_try_generate_iterable)
        """
        return self._try_generate_iterable

    @property
    def iterable(self):
        """Allows to connect iterable input to the operator.

        Iterable object, generated by
        make_for_each_range oeprator, that
        can be combined with the one
        currently generated.

        Parameters
        ----------
        my_iterable :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
        >>> op.inputs.iterable.connect(my_iterable)
        >>> # or
        >>> op.inputs.iterable(my_iterable)
        """
        return self._iterable

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
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
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
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
        >>> op.inputs.pin_index.connect(my_pin_index)
        >>> # or
        >>> op.inputs.pin_index(my_pin_index)
        """
        return self._pin_index

    @property
    def valueA(self):
        """Allows to connect valueA input to the operator.

        Parameters
        ----------
        my_valueA :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
        >>> op.inputs.valueA.connect(my_valueA)
        >>> # or
        >>> op.inputs.valueA(my_valueA)
        """
        return self._valueA

    @property
    def valueB(self):
        """Allows to connect valueB input to the operator.

        Parameters
        ----------
        my_valueB :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
        >>> op.inputs.valueB.connect(my_valueB)
        >>> # or
        >>> op.inputs.valueB(my_valueB)
        """
        return self._valueB

    @property
    def valueC1(self):
        """Allows to connect valueC1 input to the operator.

        Parameters
        ----------
        my_valueC1 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
        >>> op.inputs.valueC1.connect(my_valueC1)
        >>> # or
        >>> op.inputs.valueC1(my_valueC1)
        """
        return self._valueC1

    @property
    def valueC2(self):
        """Allows to connect valueC2 input to the operator.

        Parameters
        ----------
        my_valueC2 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
        >>> op.inputs.valueC2.connect(my_valueC2)
        >>> # or
        >>> op.inputs.valueC2(my_valueC2)
        """
        return self._valueC2

    @property
    def producer_op11(self):
        """Allows to connect producer_op11 input to the operator.

        Parameters
        ----------
        my_producer_op11 : Operator

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
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
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
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
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
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
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
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
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
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
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
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
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
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
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
        >>> op.inputs.consumer_op12.connect(my_consumer_op12)
        >>> # or
        >>> op.inputs.consumer_op12(my_consumer_op12)
        """
        return self._consumer_op12


class OutputsMakeProducerConsumerForEachIterator(_Outputs):
    """Intermediate class used to get outputs from
    make_producer_consumer_for_each_iterator operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
    >>> # Connect inputs : op.inputs. ...
    >>> result_iterator = op.outputs.iterator()
    """

    def __init__(self, op: Operator):
        super().__init__(make_producer_consumer_for_each_iterator._spec().outputs, op)
        self._iterator = Output(
            make_producer_consumer_for_each_iterator._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._iterator)

    @property
    def iterator(self):
        """Allows to get iterator output of the operator

        Returns
        ----------
        my_iterator :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_producer_consumer_for_each_iterator()
        >>> # Connect inputs : op.inputs. ...
        >>> result_iterator = op.outputs.iterator()
        """  # noqa: E501
        return self._iterator