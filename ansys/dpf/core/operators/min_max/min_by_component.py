"""
min_by_component
================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class min_by_component(Operator):
    """Give the minimum for each element rank by comparing several fields.

    Parameters
    ----------
    use_absolute_value : bool
        Use_absolute_value
    field1 : Field or FieldsContainer
        Field or fields container with only one field
        is expected
    field2 : Field or FieldsContainer
        Field or fields container with only one field
        is expected


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.min_max.min_by_component()

    >>> # Make input connections
    >>> my_use_absolute_value = bool()
    >>> op.inputs.use_absolute_value.connect(my_use_absolute_value)
    >>> my_field1 = dpf.Field()
    >>> op.inputs.field1.connect(my_field1)
    >>> my_field2 = dpf.Field()
    >>> op.inputs.field2.connect(my_field2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.min_max.min_by_component(
    ...     use_absolute_value=my_use_absolute_value,
    ...     field1=my_field1,
    ...     field2=my_field2,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        use_absolute_value=None,
        field1=None,
        field2=None,
        config=None,
        server=None,
    ):
        super().__init__(name="min_by_component", config=config, server=server)
        self._inputs = InputsMinByComponent(self)
        self._outputs = OutputsMinByComponent(self)
        if use_absolute_value is not None:
            self.inputs.use_absolute_value.connect(use_absolute_value)
        if field1 is not None:
            self.inputs.field1.connect(field1)
        if field2 is not None:
            self.inputs.field2.connect(field2)

    @staticmethod
    def _spec():
        description = (
            """Give the minimum for each element rank by comparing several fields."""
        )
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="use_absolute_value",
                    type_names=["bool"],
                    optional=False,
                    document="""Use_absolute_value""",
                ),
                1: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
                ),
                2: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
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
        return Operator.default_config(name="min_by_component", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMinByComponent
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMinByComponent
        """
        return super().outputs


class InputsMinByComponent(_Inputs):
    """Intermediate class used to connect user inputs to
    min_by_component operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.min_max.min_by_component()
    >>> my_use_absolute_value = bool()
    >>> op.inputs.use_absolute_value.connect(my_use_absolute_value)
    >>> my_field1 = dpf.Field()
    >>> op.inputs.field1.connect(my_field1)
    >>> my_field2 = dpf.Field()
    >>> op.inputs.field2.connect(my_field2)
    """

    def __init__(self, op: Operator):
        super().__init__(min_by_component._spec().inputs, op)
        self._use_absolute_value = Input(
            min_by_component._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._use_absolute_value)
        self._field1 = Input(min_by_component._spec().input_pin(1), 1, op, 0)
        self._inputs.append(self._field1)
        self._field2 = Input(min_by_component._spec().input_pin(2), 2, op, 1)
        self._inputs.append(self._field2)

    @property
    def use_absolute_value(self):
        """Allows to connect use_absolute_value input to the operator.

        Use_absolute_value

        Parameters
        ----------
        my_use_absolute_value : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_by_component()
        >>> op.inputs.use_absolute_value.connect(my_use_absolute_value)
        >>> # or
        >>> op.inputs.use_absolute_value(my_use_absolute_value)
        """
        return self._use_absolute_value

    @property
    def field1(self):
        """Allows to connect field1 input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_field1 : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_by_component()
        >>> op.inputs.field1.connect(my_field1)
        >>> # or
        >>> op.inputs.field1(my_field1)
        """
        return self._field1

    @property
    def field2(self):
        """Allows to connect field2 input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_field2 : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_by_component()
        >>> op.inputs.field2.connect(my_field2)
        >>> # or
        >>> op.inputs.field2(my_field2)
        """
        return self._field2


class OutputsMinByComponent(_Outputs):
    """Intermediate class used to get outputs from
    min_by_component operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.min_max.min_by_component()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(min_by_component._spec().outputs, op)
        self._field = Output(min_by_component._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_by_component()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
