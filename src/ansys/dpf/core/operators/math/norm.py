"""
norm
====
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class norm(Operator):
    """Computes the element-wise L2 norm of the field elementary data.

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container with only one field
        is expected


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.norm()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.norm(
    ...     field=my_field,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="norm", config=config, server=server)
        self._inputs = InputsNorm(self)
        self._outputs = OutputsNorm(self)
        if field is not None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        description = (
            """Computes the element-wise L2 norm of the field elementary data."""
        )
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
        return Operator.default_config(name="norm", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNorm
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsNorm
        """
        return super().outputs


class InputsNorm(_Inputs):
    """Intermediate class used to connect user inputs to
    norm operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.norm()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    """

    def __init__(self, op: Operator):
        super().__init__(norm._spec().inputs, op)
        self._field = Input(norm._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)

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
        >>> op = dpf.operators.math.norm()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field


class OutputsNorm(_Outputs):
    """Intermediate class used to get outputs from
    norm operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.norm()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(norm._spec().outputs, op)
        self._field = Output(norm._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.norm()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
