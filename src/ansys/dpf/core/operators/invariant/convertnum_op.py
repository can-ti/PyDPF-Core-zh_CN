"""
convertnum_op
=============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class convertnum_op(Operator):
    """Converts a fields container from one mapdl ordering to another mapdl
    ordering. Supported mapdl ordering are BCS=0, FUL=1, NOD=2.

    Parameters
    ----------
    input_ordering : int
        Input ordering number
    output_ordering : int
        Output ordering number
    fields_container : FieldsContainer
        Expect fields container
    data_sources : DataSources
        Data_sources (must contain the full file).


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.invariant.convertnum_op()

    >>> # Make input connections
    >>> my_input_ordering = int()
    >>> op.inputs.input_ordering.connect(my_input_ordering)
    >>> my_output_ordering = int()
    >>> op.inputs.output_ordering.connect(my_output_ordering)
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.invariant.convertnum_op(
    ...     input_ordering=my_input_ordering,
    ...     output_ordering=my_output_ordering,
    ...     fields_container=my_fields_container,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        input_ordering=None,
        output_ordering=None,
        fields_container=None,
        data_sources=None,
        config=None,
        server=None,
    ):
        super().__init__(name="convertnum_op", config=config, server=server)
        self._inputs = InputsConvertnumOp(self)
        self._outputs = OutputsConvertnumOp(self)
        if input_ordering is not None:
            self.inputs.input_ordering.connect(input_ordering)
        if output_ordering is not None:
            self.inputs.output_ordering.connect(output_ordering)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        description = """Converts a fields container from one mapdl ordering to another mapdl
            ordering. Supported mapdl ordering are BCS=0, FUL=1,
            NOD=2."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="input_ordering",
                    type_names=["int32"],
                    optional=False,
                    document="""Input ordering number""",
                ),
                1: PinSpecification(
                    name="output_ordering",
                    type_names=["int32"],
                    optional=False,
                    document="""Output ordering number""",
                ),
                2: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Expect fields container""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""Data_sources (must contain the full file).""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
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
        return Operator.default_config(name="convertnum_op", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsConvertnumOp
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsConvertnumOp
        """
        return super().outputs


class InputsConvertnumOp(_Inputs):
    """Intermediate class used to connect user inputs to
    convertnum_op operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.invariant.convertnum_op()
    >>> my_input_ordering = int()
    >>> op.inputs.input_ordering.connect(my_input_ordering)
    >>> my_output_ordering = int()
    >>> op.inputs.output_ordering.connect(my_output_ordering)
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(convertnum_op._spec().inputs, op)
        self._input_ordering = Input(convertnum_op._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._input_ordering)
        self._output_ordering = Input(convertnum_op._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._output_ordering)
        self._fields_container = Input(convertnum_op._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._fields_container)
        self._data_sources = Input(convertnum_op._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)

    @property
    def input_ordering(self):
        """Allows to connect input_ordering input to the operator.

        Input ordering number

        Parameters
        ----------
        my_input_ordering : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.convertnum_op()
        >>> op.inputs.input_ordering.connect(my_input_ordering)
        >>> # or
        >>> op.inputs.input_ordering(my_input_ordering)
        """
        return self._input_ordering

    @property
    def output_ordering(self):
        """Allows to connect output_ordering input to the operator.

        Output ordering number

        Parameters
        ----------
        my_output_ordering : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.convertnum_op()
        >>> op.inputs.output_ordering.connect(my_output_ordering)
        >>> # or
        >>> op.inputs.output_ordering(my_output_ordering)
        """
        return self._output_ordering

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Expect fields container

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.convertnum_op()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Data_sources (must contain the full file).

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.convertnum_op()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsConvertnumOp(_Outputs):
    """Intermediate class used to get outputs from
    convertnum_op operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.invariant.convertnum_op()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(convertnum_op._spec().outputs, op)
        self._fields_container = Output(convertnum_op._spec().output_pin(0), 0, op)
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator

        Returns
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.convertnum_op()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
