"""
von_mises_eqv
=============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class von_mises_eqv(Operator):
    """Computes the element-wise Von-Mises criteria on a tensor field.

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container with only one field
        is expected
    poisson_ratio : float or int
        Poisson ratio to be used in equivalent strain
        calculation.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.invariant.von_mises_eqv()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_poisson_ratio = float()
    >>> op.inputs.poisson_ratio.connect(my_poisson_ratio)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.invariant.von_mises_eqv(
    ...     field=my_field,
    ...     poisson_ratio=my_poisson_ratio,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, field=None, poisson_ratio=None, config=None, server=None):
        super().__init__(name="eqv", config=config, server=server)
        self._inputs = InputsVonMisesEqv(self)
        self._outputs = OutputsVonMisesEqv(self)
        if field is not None:
            self.inputs.field.connect(field)
        if poisson_ratio is not None:
            self.inputs.poisson_ratio.connect(poisson_ratio)

    @staticmethod
    def _spec():
        description = (
            """Computes the element-wise Von-Mises criteria on a tensor field."""
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
                13: PinSpecification(
                    name="poisson_ratio",
                    type_names=["double", "int32"],
                    optional=False,
                    document="""Poisson ratio to be used in equivalent strain
        calculation.""",
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
        return Operator.default_config(name="eqv", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsVonMisesEqv
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsVonMisesEqv
        """
        return super().outputs


class InputsVonMisesEqv(_Inputs):
    """Intermediate class used to connect user inputs to
    von_mises_eqv operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.invariant.von_mises_eqv()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_poisson_ratio = float()
    >>> op.inputs.poisson_ratio.connect(my_poisson_ratio)
    """

    def __init__(self, op: Operator):
        super().__init__(von_mises_eqv._spec().inputs, op)
        self._field = Input(von_mises_eqv._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._poisson_ratio = Input(von_mises_eqv._spec().input_pin(13), 13, op, -1)
        self._inputs.append(self._poisson_ratio)

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
        >>> op = dpf.operators.invariant.von_mises_eqv()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def poisson_ratio(self):
        """Allows to connect poisson_ratio input to the operator.

        Poisson ratio to be used in equivalent strain
        calculation.

        Parameters
        ----------
        my_poisson_ratio : float or int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.von_mises_eqv()
        >>> op.inputs.poisson_ratio.connect(my_poisson_ratio)
        >>> # or
        >>> op.inputs.poisson_ratio(my_poisson_ratio)
        """
        return self._poisson_ratio


class OutputsVonMisesEqv(_Outputs):
    """Intermediate class used to get outputs from
    von_mises_eqv operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.invariant.von_mises_eqv()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(von_mises_eqv._spec().outputs, op)
        self._field = Output(von_mises_eqv._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.invariant.von_mises_eqv()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field