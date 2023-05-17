"""
outer_product
=============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class outer_product(Operator):
    """Computes the outer product of two vector fields.

    Parameters
    ----------
    fieldA : Field or FieldsContainer or float
        Field or fields container with only one field
        is expected
    fieldB : Field or FieldsContainer or float
        Field or fields container with only one field
        is expected


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.outer_product()

    >>> # Make input connections
    >>> my_fieldA = dpf.Field()
    >>> op.inputs.fieldA.connect(my_fieldA)
    >>> my_fieldB = dpf.Field()
    >>> op.inputs.fieldB.connect(my_fieldB)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.outer_product(
    ...     fieldA=my_fieldA,
    ...     fieldB=my_fieldB,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="outer_product", config=config, server=server)
        self._inputs = InputsOuterProduct(self)
        self._outputs = OutputsOuterProduct(self)
        if fieldA is not None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB is not None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        description = """Computes the outer product of two vector fields."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fieldA",
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
                    name="fieldB",
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
        return Operator.default_config(name="outer_product", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsOuterProduct
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsOuterProduct
        """
        return super().outputs


class InputsOuterProduct(_Inputs):
    """Intermediate class used to connect user inputs to
    outer_product operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.outer_product()
    >>> my_fieldA = dpf.Field()
    >>> op.inputs.fieldA.connect(my_fieldA)
    >>> my_fieldB = dpf.Field()
    >>> op.inputs.fieldB.connect(my_fieldB)
    """

    def __init__(self, op: Operator):
        super().__init__(outer_product._spec().inputs, op)
        self._fieldA = Input(outer_product._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fieldA)
        self._fieldB = Input(outer_product._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._fieldB)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_fieldA : Field or FieldsContainer or float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.outer_product()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> # or
        >>> op.inputs.fieldA(my_fieldA)
        """
        return self._fieldA

    @property
    def fieldB(self):
        """Allows to connect fieldB input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_fieldB : Field or FieldsContainer or float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.outer_product()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> # or
        >>> op.inputs.fieldB(my_fieldB)
        """
        return self._fieldB


class OutputsOuterProduct(_Outputs):
    """Intermediate class used to get outputs from
    outer_product operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.outer_product()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(outer_product._spec().outputs, op)
        self._field = Output(outer_product._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.outer_product()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
