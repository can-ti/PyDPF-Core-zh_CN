"""
pow
===
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class pow(Operator):
    """Computes element-wise field[i]^p.

    Parameters
    ----------
    field : Field
    factor : float


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.pow()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_factor = float()
    >>> op.inputs.factor.connect(my_factor)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.pow(
    ...     field=my_field,
    ...     factor=my_factor,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, field=None, factor=None, config=None, server=None):
        super().__init__(name="Pow", config=config, server=server)
        self._inputs = InputsPow(self)
        self._outputs = OutputsPow(self)
        if field is not None:
            self.inputs.field.connect(field)
        if factor is not None:
            self.inputs.factor.connect(factor)

    @staticmethod
    def _spec():
        description = """Computes element-wise field[i]^p."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="factor",
                    type_names=["double"],
                    optional=False,
                    document="""""",
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
        return Operator.default_config(name="Pow", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPow
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsPow
        """
        return super().outputs


class InputsPow(_Inputs):
    """Intermediate class used to connect user inputs to
    pow operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.pow()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_factor = float()
    >>> op.inputs.factor.connect(my_factor)
    """

    def __init__(self, op: Operator):
        super().__init__(pow._spec().inputs, op)
        self._field = Input(pow._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._factor = Input(pow._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._factor)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Parameters
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.pow()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def factor(self):
        """Allows to connect factor input to the operator.

        Parameters
        ----------
        my_factor : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.pow()
        >>> op.inputs.factor.connect(my_factor)
        >>> # or
        >>> op.inputs.factor(my_factor)
        """
        return self._factor


class OutputsPow(_Outputs):
    """Intermediate class used to get outputs from
    pow operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.pow()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(pow._spec().outputs, op)
        self._field = Output(pow._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.pow()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
