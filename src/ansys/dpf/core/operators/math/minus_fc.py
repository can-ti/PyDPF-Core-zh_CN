"""
minus_fc
========
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class minus_fc(Operator):
    """Computes the difference of two fields. If one field's scoping has an
    'overall' location, then this field's values are applied on the
    other field entirely. When using a constant or 'work_by_index',
    you can use 'inplace' to reuse one of the fields.

    Parameters
    ----------
    field_or_fields_container_A : Field or FieldsContainer or float
        Field or fields container with only one field
        is expected
    field_or_fields_container_B : Field or FieldsContainer or float
        Field or fields container with only one field
        is expected


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.minus_fc()

    >>> # Make input connections
    >>> my_field_or_fields_container_A = dpf.Field()
    >>> op.inputs.field_or_fields_container_A.connect(my_field_or_fields_container_A)
    >>> my_field_or_fields_container_B = dpf.Field()
    >>> op.inputs.field_or_fields_container_B.connect(my_field_or_fields_container_B)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.minus_fc(
    ...     field_or_fields_container_A=my_field_or_fields_container_A,
    ...     field_or_fields_container_B=my_field_or_fields_container_B,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        field_or_fields_container_A=None,
        field_or_fields_container_B=None,
        config=None,
        server=None,
    ):
        super().__init__(name="minus_fc", config=config, server=server)
        self._inputs = InputsMinusFc(self)
        self._outputs = OutputsMinusFc(self)
        if field_or_fields_container_A is not None:
            self.inputs.field_or_fields_container_A.connect(field_or_fields_container_A)
        if field_or_fields_container_B is not None:
            self.inputs.field_or_fields_container_B.connect(field_or_fields_container_B)

    @staticmethod
    def _spec():
        description = """Computes the difference of two fields. If one field's scoping has an
            'overall' location, then this field's values are applied
            on the other field entirely. When using a constant or
            'work_by_index', you can use 'inplace' to reuse one of the
            fields."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field_or_fields_container_A",
                    type_names=[
                        "field",
                        "fields_container",
                        "double",
                        "vector<double>",
                    ],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
                ),
                1: PinSpecification(
                    name="field_or_fields_container_B",
                    type_names=[
                        "field",
                        "fields_container",
                        "double",
                        "vector<double>",
                    ],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
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
        return Operator.default_config(name="minus_fc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMinusFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMinusFc
        """
        return super().outputs


class InputsMinusFc(_Inputs):
    """Intermediate class used to connect user inputs to
    minus_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.minus_fc()
    >>> my_field_or_fields_container_A = dpf.Field()
    >>> op.inputs.field_or_fields_container_A.connect(my_field_or_fields_container_A)
    >>> my_field_or_fields_container_B = dpf.Field()
    >>> op.inputs.field_or_fields_container_B.connect(my_field_or_fields_container_B)
    """

    def __init__(self, op: Operator):
        super().__init__(minus_fc._spec().inputs, op)
        self._field_or_fields_container_A = Input(
            minus_fc._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._field_or_fields_container_A)
        self._field_or_fields_container_B = Input(
            minus_fc._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._field_or_fields_container_B)

    @property
    def field_or_fields_container_A(self):
        """Allows to connect field_or_fields_container_A input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_field_or_fields_container_A : Field or FieldsContainer or float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.minus_fc()
        >>> op.inputs.field_or_fields_container_A.connect(my_field_or_fields_container_A)
        >>> # or
        >>> op.inputs.field_or_fields_container_A(my_field_or_fields_container_A)
        """
        return self._field_or_fields_container_A

    @property
    def field_or_fields_container_B(self):
        """Allows to connect field_or_fields_container_B input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_field_or_fields_container_B : Field or FieldsContainer or float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.minus_fc()
        >>> op.inputs.field_or_fields_container_B.connect(my_field_or_fields_container_B)
        >>> # or
        >>> op.inputs.field_or_fields_container_B(my_field_or_fields_container_B)
        """
        return self._field_or_fields_container_B


class OutputsMinusFc(_Outputs):
    """Intermediate class used to get outputs from
    minus_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.minus_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(minus_fc._spec().outputs, op)
        self._fields_container = Output(minus_fc._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.minus_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
