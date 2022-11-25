"""
fft_approx
==========
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class fft_approx(Operator):
    """Computes the fitting curve using FFT filtering and cubic fitting in
    space (node i: x=time, y=data), with possibility to compute the
    first and the second derivatives of the curve.

    Parameters
    ----------
    time_scoping : Scoping, optional
        A time scoping to rescope / split an iunput
        fields container
    mesh_scoping : Scoping or ScopingsContainer, optional
        A space (mesh entities) scopings (or
        container) to rescope / split an
        input fields container
    entity_to_fit : FieldsContainer
        Data changing in time to be fitted
    component_number : int
        Component number as an int, ex '0' for
        x-displacement, '1' for
        y-displacement,...
    first_derivative : bool
        Calculate the first derivative? (bool):
        default is false
    second_derivative : bool
        Calculate the second derivative? (bool):
        default is false
    fit_data : bool
        Calculate the fitted values? (bool): default
        is false


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.fft_approx()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_entity_to_fit = dpf.FieldsContainer()
    >>> op.inputs.entity_to_fit.connect(my_entity_to_fit)
    >>> my_component_number = int()
    >>> op.inputs.component_number.connect(my_component_number)
    >>> my_first_derivative = bool()
    >>> op.inputs.first_derivative.connect(my_first_derivative)
    >>> my_second_derivative = bool()
    >>> op.inputs.second_derivative.connect(my_second_derivative)
    >>> my_fit_data = bool()
    >>> op.inputs.fit_data.connect(my_fit_data)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.fft_approx(
    ...     time_scoping=my_time_scoping,
    ...     mesh_scoping=my_mesh_scoping,
    ...     entity_to_fit=my_entity_to_fit,
    ...     component_number=my_component_number,
    ...     first_derivative=my_first_derivative,
    ...     second_derivative=my_second_derivative,
    ...     fit_data=my_fit_data,
    ... )

    >>> # Get output data
    >>> result_fitted_entity_y = op.outputs.fitted_entity_y()
    >>> result_first_der_dy = op.outputs.first_der_dy()
    >>> result_second_der_d2y = op.outputs.second_der_d2y()
    """

    def __init__(
        self,
        time_scoping=None,
        mesh_scoping=None,
        entity_to_fit=None,
        component_number=None,
        first_derivative=None,
        second_derivative=None,
        fit_data=None,
        config=None,
        server=None,
    ):
        super().__init__(name="fft_approx", config=config, server=server)
        self._inputs = InputsFftApprox(self)
        self._outputs = OutputsFftApprox(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if entity_to_fit is not None:
            self.inputs.entity_to_fit.connect(entity_to_fit)
        if component_number is not None:
            self.inputs.component_number.connect(component_number)
        if first_derivative is not None:
            self.inputs.first_derivative.connect(first_derivative)
        if second_derivative is not None:
            self.inputs.second_derivative.connect(second_derivative)
        if fit_data is not None:
            self.inputs.fit_data.connect(fit_data)

    @staticmethod
    def _spec():
        description = """Computes the fitting curve using FFT filtering and cubic fitting in
            space (node i: x=time, y=data), with possibility to
            compute the first and the second derivatives of the curve."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_scoping",
                    type_names=["vector<int32>", "scoping"],
                    optional=True,
                    document="""A time scoping to rescope / split an iunput
        fields container""",
                ),
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["umap<int32,int32>", "scoping", "scopings_container"],
                    optional=True,
                    document="""A space (mesh entities) scopings (or
        container) to rescope / split an
        input fields container""",
                ),
                2: PinSpecification(
                    name="entity_to_fit",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Data changing in time to be fitted""",
                ),
                3: PinSpecification(
                    name="component_number",
                    type_names=["int32"],
                    optional=False,
                    document="""Component number as an int, ex '0' for
        x-displacement, '1' for
        y-displacement,...""",
                ),
                4: PinSpecification(
                    name="first_derivative",
                    type_names=["bool"],
                    optional=False,
                    document="""Calculate the first derivative? (bool):
        default is false""",
                ),
                5: PinSpecification(
                    name="second_derivative",
                    type_names=["bool"],
                    optional=False,
                    document="""Calculate the second derivative? (bool):
        default is false""",
                ),
                6: PinSpecification(
                    name="fit_data",
                    type_names=["bool"],
                    optional=False,
                    document="""Calculate the fitted values? (bool): default
        is false""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fitted_entity_y",
                    type_names=["fields_container"],
                    optional=False,
                    document="""The fitted entity is fitted using fft along
        the space scoping (node i: x=time,
        y=data): fitted y is expected to be
        close to the input data""",
                ),
                1: PinSpecification(
                    name="first_der_dy",
                    type_names=["fields_container"],
                    optional=False,
                    document="""The first derivative (dy) from the fitted y""",
                ),
                2: PinSpecification(
                    name="second_der_d2y",
                    type_names=["fields_container"],
                    optional=False,
                    document="""The second derivative (d2y) from the fitted y""",
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
        return Operator.default_config(name="fft_approx", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFftApprox
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFftApprox
        """
        return super().outputs


class InputsFftApprox(_Inputs):
    """Intermediate class used to connect user inputs to
    fft_approx operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.fft_approx()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_entity_to_fit = dpf.FieldsContainer()
    >>> op.inputs.entity_to_fit.connect(my_entity_to_fit)
    >>> my_component_number = int()
    >>> op.inputs.component_number.connect(my_component_number)
    >>> my_first_derivative = bool()
    >>> op.inputs.first_derivative.connect(my_first_derivative)
    >>> my_second_derivative = bool()
    >>> op.inputs.second_derivative.connect(my_second_derivative)
    >>> my_fit_data = bool()
    >>> op.inputs.fit_data.connect(my_fit_data)
    """

    def __init__(self, op: Operator):
        super().__init__(fft_approx._spec().inputs, op)
        self._time_scoping = Input(fft_approx._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(fft_approx._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._entity_to_fit = Input(fft_approx._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._entity_to_fit)
        self._component_number = Input(fft_approx._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._component_number)
        self._first_derivative = Input(fft_approx._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._first_derivative)
        self._second_derivative = Input(fft_approx._spec().input_pin(5), 5, op, -1)
        self._inputs.append(self._second_derivative)
        self._fit_data = Input(fft_approx._spec().input_pin(6), 6, op, -1)
        self._inputs.append(self._fit_data)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        A time scoping to rescope / split an iunput
        fields container

        Parameters
        ----------
        my_time_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        A space (mesh entities) scopings (or
        container) to rescope / split an
        input fields container

        Parameters
        ----------
        my_mesh_scoping : Scoping or ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def entity_to_fit(self):
        """Allows to connect entity_to_fit input to the operator.

        Data changing in time to be fitted

        Parameters
        ----------
        my_entity_to_fit : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.entity_to_fit.connect(my_entity_to_fit)
        >>> # or
        >>> op.inputs.entity_to_fit(my_entity_to_fit)
        """
        return self._entity_to_fit

    @property
    def component_number(self):
        """Allows to connect component_number input to the operator.

        Component number as an int, ex '0' for
        x-displacement, '1' for
        y-displacement,...

        Parameters
        ----------
        my_component_number : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.component_number.connect(my_component_number)
        >>> # or
        >>> op.inputs.component_number(my_component_number)
        """
        return self._component_number

    @property
    def first_derivative(self):
        """Allows to connect first_derivative input to the operator.

        Calculate the first derivative? (bool):
        default is false

        Parameters
        ----------
        my_first_derivative : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.first_derivative.connect(my_first_derivative)
        >>> # or
        >>> op.inputs.first_derivative(my_first_derivative)
        """
        return self._first_derivative

    @property
    def second_derivative(self):
        """Allows to connect second_derivative input to the operator.

        Calculate the second derivative? (bool):
        default is false

        Parameters
        ----------
        my_second_derivative : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.second_derivative.connect(my_second_derivative)
        >>> # or
        >>> op.inputs.second_derivative(my_second_derivative)
        """
        return self._second_derivative

    @property
    def fit_data(self):
        """Allows to connect fit_data input to the operator.

        Calculate the fitted values? (bool): default
        is false

        Parameters
        ----------
        my_fit_data : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_approx()
        >>> op.inputs.fit_data.connect(my_fit_data)
        >>> # or
        >>> op.inputs.fit_data(my_fit_data)
        """
        return self._fit_data


class OutputsFftApprox(_Outputs):
    """Intermediate class used to get outputs from
    fft_approx operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.fft_approx()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fitted_entity_y = op.outputs.fitted_entity_y()
    >>> result_first_der_dy = op.outputs.first_der_dy()
    >>> result_second_der_d2y = op.outputs.second_der_d2y()
    """

    def __init__(self, op: Operator):
        super().__init__(fft_approx._spec().outputs, op)
        self._fitted_entity_y = Output(fft_approx._spec().output_pin(0), 0, op)
        self._outputs.append(self._fitted_entity_y)
        self._first_der_dy = Output(fft_approx._spec().output_pin(1), 1, op)
        self._outputs.append(self._first_der_dy)
        self._second_der_d2y = Output(fft_approx._spec().output_pin(2), 2, op)
        self._outputs.append(self._second_der_d2y)

    @property
    def fitted_entity_y(self):
        """Allows to get fitted_entity_y output of the operator

        Returns
        ----------
        my_fitted_entity_y : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_approx()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fitted_entity_y = op.outputs.fitted_entity_y()
        """  # noqa: E501
        return self._fitted_entity_y

    @property
    def first_der_dy(self):
        """Allows to get first_der_dy output of the operator

        Returns
        ----------
        my_first_der_dy : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_approx()
        >>> # Connect inputs : op.inputs. ...
        >>> result_first_der_dy = op.outputs.first_der_dy()
        """  # noqa: E501
        return self._first_der_dy

    @property
    def second_der_d2y(self):
        """Allows to get second_der_d2y output of the operator

        Returns
        ----------
        my_second_der_d2y : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_approx()
        >>> # Connect inputs : op.inputs. ...
        >>> result_second_der_d2y = op.outputs.second_der_d2y()
        """  # noqa: E501
        return self._second_der_d2y
