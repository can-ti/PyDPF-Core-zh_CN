"""
invariants
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class invariants(Operator):
    """Computes the element-wise invariants of a tensor field.

    Parameters
    ----------
    field : Field


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.invariant.invariants()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.invariant.invariants(
    ...     field=my_field,
    ... )

    >>> # Get output data
    >>> result_field_int = op.outputs.field_int()
    >>> result_field_eqv = op.outputs.field_eqv()
    >>> result_field_max_shear = op.outputs.field_max_shear()
    """

    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="invariants_deriv", config=config, server=server)
        self._inputs = InputsInvariants(self)
        self._outputs = OutputsInvariants(self)
        if field is not None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        description = """Computes the element-wise invariants of a tensor field."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field_int",
                    type_names=["field"],
                    optional=False,
                    document="""Stress intensity field""",
                ),
                1: PinSpecification(
                    name="field_eqv",
                    type_names=["field"],
                    optional=False,
                    document="""Stress equivalent intensity""",
                ),
                2: PinSpecification(
                    name="field_max_shear",
                    type_names=["field"],
                    optional=False,
                    document="""Max shear stress field""",
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
            ``None``, attempts to use the the global server.
        """
        return Operator.default_config(name="invariants_deriv", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsInvariants
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsInvariants
        """
        return super().outputs


class InputsInvariants(_Inputs):
    """Intermediate class used to connect user inputs to
    invariants operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.invariant.invariants()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    """

    def __init__(self, op: Operator):
        super().__init__(invariants._spec().inputs, op)
        self._field = Input(invariants._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Parameters
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.invariants()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field


class OutputsInvariants(_Outputs):
    """Intermediate class used to get outputs from
    invariants operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.invariant.invariants()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field_int = op.outputs.field_int()
    >>> result_field_eqv = op.outputs.field_eqv()
    >>> result_field_max_shear = op.outputs.field_max_shear()
    """

    def __init__(self, op: Operator):
        super().__init__(invariants._spec().outputs, op)
        self._field_int = Output(invariants._spec().output_pin(0), 0, op)
        self._outputs.append(self._field_int)
        self._field_eqv = Output(invariants._spec().output_pin(1), 1, op)
        self._outputs.append(self._field_eqv)
        self._field_max_shear = Output(invariants._spec().output_pin(2), 2, op)
        self._outputs.append(self._field_max_shear)

    @property
    def field_int(self):
        """Allows to get field_int output of the operator

        Returns
        ----------
        my_field_int : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.invariants()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_int = op.outputs.field_int()
        """  # noqa: E501
        return self._field_int

    @property
    def field_eqv(self):
        """Allows to get field_eqv output of the operator

        Returns
        ----------
        my_field_eqv : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.invariants()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_eqv = op.outputs.field_eqv()
        """  # noqa: E501
        return self._field_eqv

    @property
    def field_max_shear(self):
        """Allows to get field_max_shear output of the operator

        Returns
        ----------
        my_field_max_shear : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.invariants()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_max_shear = op.outputs.field_max_shear()
        """  # noqa: E501
        return self._field_max_shear
