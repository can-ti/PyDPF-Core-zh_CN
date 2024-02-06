"""
add_constant
============
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class add_constant(Operator):
    """Computes the sum of a field (in 0) and a scalar (in 1).

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container with only one field
        is expected
    ponderation : float
        Double or vector of double


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.add_constant()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_ponderation = float()
    >>> op.inputs.ponderation.connect(my_ponderation)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.add_constant(
    ...     field=my_field,
    ...     ponderation=my_ponderation,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, field=None, ponderation=None, config=None, server=None):
        super().__init__(name="add_constant", config=config, server=server)
        self._inputs = InputsAddConstant(self)
        self._outputs = OutputsAddConstant(self)
        if field is not None:
            self.inputs.field.connect(field)
        if ponderation is not None:
            self.inputs.ponderation.connect(ponderation)

    @staticmethod
    def _spec():
        description = """Computes the sum of a field (in 0) and a scalar (in 1)."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
                ),
                1: PinSpecification(
                    name="ponderation",
                    type_names=["double", "vector<double>"],
                    optional=False,
                    document="""Double or vector of double""",
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
        return Operator.default_config(name="add_constant", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAddConstant
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsAddConstant
        """
        return super().outputs


class InputsAddConstant(_Inputs):
    """Intermediate class used to connect user inputs to
    add_constant operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.add_constant()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_ponderation = float()
    >>> op.inputs.ponderation.connect(my_ponderation)
    """

    def __init__(self, op: Operator):
        super().__init__(add_constant._spec().inputs, op)
        self._field = Input(add_constant._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._ponderation = Input(add_constant._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._ponderation)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_field : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.add_constant()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def ponderation(self):
        """Allows to connect ponderation input to the operator.

        Double or vector of double

        Parameters
        ----------
        my_ponderation : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.add_constant()
        >>> op.inputs.ponderation.connect(my_ponderation)
        >>> # or
        >>> op.inputs.ponderation(my_ponderation)
        """
        return self._ponderation


class OutputsAddConstant(_Outputs):
    """Intermediate class used to get outputs from
    add_constant operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.add_constant()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(add_constant._spec().outputs, op)
        self._field = Output(add_constant._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.add_constant()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
