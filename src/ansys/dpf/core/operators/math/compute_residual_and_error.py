"""
compute_residual_and_error
==========================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.outputs import _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class compute_residual_and_error(Operator):
    """Computes the norm of a field or a field container.
    When a second entry is provided, the residual (the difference
    between the first and second entry) is calculated along with the
    error.
    When a second input is not provided, the calculation is only
    completed for the first entry.
    The type of calculation performed is based on the specifications
    provided for pins 1 and pin 2 defines the type of error norm (L1
    vs L2).
    Note that if the input is a field container that only contains one
    field, the operator's outputs are of type field

    Parameters
    ----------
    field_or_fields_container1 : Field or FieldsContainer
        Field or fields container - compulsory
    normalization_type : int, optional
        Type of normalization applied to the
        residuals and norm  calculation
        (optional, defaut: absolute):
        0 for absolute,
        1 for relative to the first entry at
        a given time step,
        2 for normalized by the max of the
        first entry at a given time step,
        3 for normalized by the max of the
        first entry over all time steps
    norm_calculation_type : int, optional
        Type for norm calculation (optional, default:
        l2) - it is normalized depending on
        pin2 selection
        1 for l1, ie sum(abs(xi)),
        2 for l2, ie sqrt(sum((xi^2))
    field_reference : int, optional
        Field reference for the normalization step,
        default: 0 for entry 1, 1 for
        residuals - optional
    field_or_fields_container2 : Field or FieldsContainer, optional
        Field or fields container of same
        dimensionality as entry 1 - optional


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.compute_residual_and_error()

    >>> # Make input connections
    >>> my_field_or_fields_container1 = dpf.Field()
    >>> op.inputs.field_or_fields_container1.connect(my_field_or_fields_container1)
    >>> my_normalization_type = int()
    >>> op.inputs.normalization_type.connect(my_normalization_type)
    >>> my_norm_calculation_type = int()
    >>> op.inputs.norm_calculation_type.connect(my_norm_calculation_type)
    >>> my_field_reference = int()
    >>> op.inputs.field_reference.connect(my_field_reference)
    >>> my_field_or_fields_container2 = dpf.Field()
    >>> op.inputs.field_or_fields_container2.connect(my_field_or_fields_container2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.compute_residual_and_error(
    ...     field_or_fields_container1=my_field_or_fields_container1,
    ...     normalization_type=my_normalization_type,
    ...     norm_calculation_type=my_norm_calculation_type,
    ...     field_reference=my_field_reference,
    ...     field_or_fields_container2=my_field_or_fields_container2,
    ... )

    >>> # Get output data
    >>> result_residuals = op.outputs.residuals()
    >>> result_error = op.outputs.error()
    >>> result_residuals_normalization_factor = op.outputs.residuals_normalization_factor()
    >>> result_error_normalization_factor = op.outputs.error_normalization_factor()
    """

    def __init__(
        self,
        field_or_fields_container1=None,
        normalization_type=None,
        norm_calculation_type=None,
        field_reference=None,
        field_or_fields_container2=None,
        config=None,
        server=None,
    ):
        super().__init__(name="error_norm_calc", config=config, server=server)
        self._inputs = InputsComputeResidualAndError(self)
        self._outputs = OutputsComputeResidualAndError(self)
        if field_or_fields_container1 is not None:
            self.inputs.field_or_fields_container1.connect(field_or_fields_container1)
        if normalization_type is not None:
            self.inputs.normalization_type.connect(normalization_type)
        if norm_calculation_type is not None:
            self.inputs.norm_calculation_type.connect(norm_calculation_type)
        if field_reference is not None:
            self.inputs.field_reference.connect(field_reference)
        if field_or_fields_container2 is not None:
            self.inputs.field_or_fields_container2.connect(field_or_fields_container2)

    @staticmethod
    def _spec():
        description = """Computes the norm of a field or a field container.
            When a second entry is provided, the residual (the
            difference between the first and second entry) is
            calculated along with the error.
            When a second input is not provided, the calculation is
            only completed for the first entry.
            The type of calculation performed is based on the
            specifications provided for pins 1 and pin 2 defines the
            type of error norm (L1 vs L2).
            Note that if the input is a field container that only
            contains one field, the operator's outputs are of type
            field"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field_or_fields_container1",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Field or fields container - compulsory""",
                ),
                1: PinSpecification(
                    name="normalization_type",
                    type_names=["int32"],
                    optional=True,
                    document="""Type of normalization applied to the
        residuals and norm  calculation
        (optional, defaut: absolute):
        0 for absolute,
        1 for relative to the first entry at
        a given time step,
        2 for normalized by the max of the
        first entry at a given time step,
        3 for normalized by the max of the
        first entry over all time steps""",
                ),
                2: PinSpecification(
                    name="norm_calculation_type",
                    type_names=["int32"],
                    optional=True,
                    document="""Type for norm calculation (optional, default:
        l2) - it is normalized depending on
        pin2 selection
        1 for l1, ie sum(abs(xi)),
        2 for l2, ie sqrt(sum((xi^2))""",
                ),
                3: PinSpecification(
                    name="field_reference",
                    type_names=["int32"],
                    optional=True,
                    document="""Field reference for the normalization step,
        default: 0 for entry 1, 1 for
        residuals - optional""",
                ),
                4: PinSpecification(
                    name="field_or_fields_container2",
                    type_names=["field", "fields_container"],
                    optional=True,
                    document="""Field or fields container of same
        dimensionality as entry 1 - optional""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="residuals",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""0: normalized residuals (aka field 1 - field
        2) as a field or field container,
        normalized depending on the
        normalization type""",
                ),
                1: PinSpecification(
                    name="error",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""1: error as a field or a field container
        depending on the entry's type.""",
                ),
                2: PinSpecification(
                    name="residuals_normalization_factor",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""2: factor used for residual normalization""",
                ),
                3: PinSpecification(
                    name="error_normalization_factor",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""3: factor used for error norm normalization""",
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
        return Operator.default_config(name="error_norm_calc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsComputeResidualAndError
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsComputeResidualAndError
        """
        return super().outputs


class InputsComputeResidualAndError(_Inputs):
    """Intermediate class used to connect user inputs to
    compute_residual_and_error operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.compute_residual_and_error()
    >>> my_field_or_fields_container1 = dpf.Field()
    >>> op.inputs.field_or_fields_container1.connect(my_field_or_fields_container1)
    >>> my_normalization_type = int()
    >>> op.inputs.normalization_type.connect(my_normalization_type)
    >>> my_norm_calculation_type = int()
    >>> op.inputs.norm_calculation_type.connect(my_norm_calculation_type)
    >>> my_field_reference = int()
    >>> op.inputs.field_reference.connect(my_field_reference)
    >>> my_field_or_fields_container2 = dpf.Field()
    >>> op.inputs.field_or_fields_container2.connect(my_field_or_fields_container2)
    """

    def __init__(self, op: Operator):
        super().__init__(compute_residual_and_error._spec().inputs, op)
        self._field_or_fields_container1 = Input(
            compute_residual_and_error._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._field_or_fields_container1)
        self._normalization_type = Input(
            compute_residual_and_error._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._normalization_type)
        self._norm_calculation_type = Input(
            compute_residual_and_error._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._norm_calculation_type)
        self._field_reference = Input(
            compute_residual_and_error._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._field_reference)
        self._field_or_fields_container2 = Input(
            compute_residual_and_error._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._field_or_fields_container2)

    @property
    def field_or_fields_container1(self):
        """Allows to connect field_or_fields_container1 input to the operator.

        Field or fields container - compulsory

        Parameters
        ----------
        my_field_or_fields_container1 : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.compute_residual_and_error()
        >>> op.inputs.field_or_fields_container1.connect(my_field_or_fields_container1)
        >>> # or
        >>> op.inputs.field_or_fields_container1(my_field_or_fields_container1)
        """
        return self._field_or_fields_container1

    @property
    def normalization_type(self):
        """Allows to connect normalization_type input to the operator.

        Type of normalization applied to the
        residuals and norm  calculation
        (optional, defaut: absolute):
        0 for absolute,
        1 for relative to the first entry at
        a given time step,
        2 for normalized by the max of the
        first entry at a given time step,
        3 for normalized by the max of the
        first entry over all time steps

        Parameters
        ----------
        my_normalization_type : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.compute_residual_and_error()
        >>> op.inputs.normalization_type.connect(my_normalization_type)
        >>> # or
        >>> op.inputs.normalization_type(my_normalization_type)
        """
        return self._normalization_type

    @property
    def norm_calculation_type(self):
        """Allows to connect norm_calculation_type input to the operator.

        Type for norm calculation (optional, default:
        l2) - it is normalized depending on
        pin2 selection
        1 for l1, ie sum(abs(xi)),
        2 for l2, ie sqrt(sum((xi^2))

        Parameters
        ----------
        my_norm_calculation_type : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.compute_residual_and_error()
        >>> op.inputs.norm_calculation_type.connect(my_norm_calculation_type)
        >>> # or
        >>> op.inputs.norm_calculation_type(my_norm_calculation_type)
        """
        return self._norm_calculation_type

    @property
    def field_reference(self):
        """Allows to connect field_reference input to the operator.

        Field reference for the normalization step,
        default: 0 for entry 1, 1 for
        residuals - optional

        Parameters
        ----------
        my_field_reference : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.compute_residual_and_error()
        >>> op.inputs.field_reference.connect(my_field_reference)
        >>> # or
        >>> op.inputs.field_reference(my_field_reference)
        """
        return self._field_reference

    @property
    def field_or_fields_container2(self):
        """Allows to connect field_or_fields_container2 input to the operator.

        Field or fields container of same
        dimensionality as entry 1 - optional

        Parameters
        ----------
        my_field_or_fields_container2 : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.compute_residual_and_error()
        >>> op.inputs.field_or_fields_container2.connect(my_field_or_fields_container2)
        >>> # or
        >>> op.inputs.field_or_fields_container2(my_field_or_fields_container2)
        """
        return self._field_or_fields_container2


class OutputsComputeResidualAndError(_Outputs):
    """Intermediate class used to get outputs from
    compute_residual_and_error operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.compute_residual_and_error()
    >>> # Connect inputs : op.inputs. ...
    >>> result_residuals = op.outputs.residuals()
    >>> result_error = op.outputs.error()
    >>> result_residuals_normalization_factor = op.outputs.residuals_normalization_factor()
    >>> result_error_normalization_factor = op.outputs.error_normalization_factor()
    """

    def __init__(self, op: Operator):
        super().__init__(compute_residual_and_error._spec().outputs, op)
        self.residuals_as_field = Output(
            _modify_output_spec_with_one_type(
                compute_residual_and_error._spec().output_pin(0), "field"
            ),
            0,
            op,
        )
        self._outputs.append(self.residuals_as_field)
        self.residuals_as_fields_container = Output(
            _modify_output_spec_with_one_type(
                compute_residual_and_error._spec().output_pin(0), "fields_container"
            ),
            0,
            op,
        )
        self._outputs.append(self.residuals_as_fields_container)
        self.error_as_field = Output(
            _modify_output_spec_with_one_type(
                compute_residual_and_error._spec().output_pin(1), "field"
            ),
            1,
            op,
        )
        self._outputs.append(self.error_as_field)
        self.error_as_fields_container = Output(
            _modify_output_spec_with_one_type(
                compute_residual_and_error._spec().output_pin(1), "fields_container"
            ),
            1,
            op,
        )
        self._outputs.append(self.error_as_fields_container)
        self.residuals_normalization_factor_as_field = Output(
            _modify_output_spec_with_one_type(
                compute_residual_and_error._spec().output_pin(2), "field"
            ),
            2,
            op,
        )
        self._outputs.append(self.residuals_normalization_factor_as_field)
        self.residuals_normalization_factor_as_fields_container = Output(
            _modify_output_spec_with_one_type(
                compute_residual_and_error._spec().output_pin(2), "fields_container"
            ),
            2,
            op,
        )
        self._outputs.append(self.residuals_normalization_factor_as_fields_container)
        self.error_normalization_factor_as_field = Output(
            _modify_output_spec_with_one_type(
                compute_residual_and_error._spec().output_pin(3), "field"
            ),
            3,
            op,
        )
        self._outputs.append(self.error_normalization_factor_as_field)
        self.error_normalization_factor_as_fields_container = Output(
            _modify_output_spec_with_one_type(
                compute_residual_and_error._spec().output_pin(3), "fields_container"
            ),
            3,
            op,
        )
        self._outputs.append(self.error_normalization_factor_as_fields_container)
