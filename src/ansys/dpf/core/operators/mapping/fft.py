"""
fft
===
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class fft(Operator):
    """Computes the Fast Fourier Transform on each component of input Field
    or each field of input Fields Container (you can use
    transpose_fields_container to have relevant scoping). Fields are
    assumed with the same scoping, number of components and
    representing equally spaced data, ideally resampled to have a 2^n
    points (prepare_sampling_fft with time_freq_interpolation can help
    creating these fields). If Complex label is present, Complex to
    Complex FFT performed otherwise Real to Complex is performed (only
    half of the coefficient will be returned).

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container.
    scale_forward_transform : float, optional
        Scale for forward transform, default is 1.0.
    inplace : bool, optional
        True if inplace, default is false.
    force_fft_points : int, optional
        Explicitely define number of fft points to
        either rescope or perform zero
        padding.
    cutoff_frequency : float, optional
        Restrict output frequency output up to this
        cutoff frequency


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mapping.fft()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_scale_forward_transform = float()
    >>> op.inputs.scale_forward_transform.connect(my_scale_forward_transform)
    >>> my_inplace = bool()
    >>> op.inputs.inplace.connect(my_inplace)
    >>> my_force_fft_points = int()
    >>> op.inputs.force_fft_points.connect(my_force_fft_points)
    >>> my_cutoff_frequency = float()
    >>> op.inputs.cutoff_frequency.connect(my_cutoff_frequency)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mapping.fft(
    ...     field=my_field,
    ...     scale_forward_transform=my_scale_forward_transform,
    ...     inplace=my_inplace,
    ...     force_fft_points=my_force_fft_points,
    ...     cutoff_frequency=my_cutoff_frequency,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        field=None,
        scale_forward_transform=None,
        inplace=None,
        force_fft_points=None,
        cutoff_frequency=None,
        config=None,
        server=None,
    ):
        super().__init__(name="fft", config=config, server=server)
        self._inputs = InputsFft(self)
        self._outputs = OutputsFft(self)
        if field is not None:
            self.inputs.field.connect(field)
        if scale_forward_transform is not None:
            self.inputs.scale_forward_transform.connect(scale_forward_transform)
        if inplace is not None:
            self.inputs.inplace.connect(inplace)
        if force_fft_points is not None:
            self.inputs.force_fft_points.connect(force_fft_points)
        if cutoff_frequency is not None:
            self.inputs.cutoff_frequency.connect(cutoff_frequency)

    @staticmethod
    def _spec():
        description = """Computes the Fast Fourier Transform on each component of input Field
            or each field of input Fields Container (you can use
            transpose_fields_container to have relevant scoping).
            Fields are assumed with the same scoping, number of
            components and representing equally spaced data, ideally
            resampled to have a 2^n points (prepare_sampling_fft with
            time_freq_interpolation can help creating these fields).
            If Complex label is present, Complex to Complex FFT
            performed otherwise Real to Complex is performed (only
            half of the coefficient will be returned)."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Field or fields container.""",
                ),
                3: PinSpecification(
                    name="scale_forward_transform",
                    type_names=["double"],
                    optional=True,
                    document="""Scale for forward transform, default is 1.0.""",
                ),
                4: PinSpecification(
                    name="inplace",
                    type_names=["bool"],
                    optional=True,
                    document="""True if inplace, default is false.""",
                ),
                5: PinSpecification(
                    name="force_fft_points",
                    type_names=["int32"],
                    optional=True,
                    document="""Explicitely define number of fft points to
        either rescope or perform zero
        padding.""",
                ),
                6: PinSpecification(
                    name="cutoff_frequency",
                    type_names=["double"],
                    optional=True,
                    document="""Restrict output frequency output up to this
        cutoff frequency""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Output complex fields container with labels
        matching input fields container. no
        supports binded, but
        prepare_sampling_fft provides it.""",
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
        return Operator.default_config(name="fft", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFft
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsFft
        """
        return super().outputs


class InputsFft(_Inputs):
    """Intermediate class used to connect user inputs to
    fft operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mapping.fft()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_scale_forward_transform = float()
    >>> op.inputs.scale_forward_transform.connect(my_scale_forward_transform)
    >>> my_inplace = bool()
    >>> op.inputs.inplace.connect(my_inplace)
    >>> my_force_fft_points = int()
    >>> op.inputs.force_fft_points.connect(my_force_fft_points)
    >>> my_cutoff_frequency = float()
    >>> op.inputs.cutoff_frequency.connect(my_cutoff_frequency)
    """

    def __init__(self, op: Operator):
        super().__init__(fft._spec().inputs, op)
        self._field = Input(fft._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._scale_forward_transform = Input(fft._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._scale_forward_transform)
        self._inplace = Input(fft._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._inplace)
        self._force_fft_points = Input(fft._spec().input_pin(5), 5, op, -1)
        self._inputs.append(self._force_fft_points)
        self._cutoff_frequency = Input(fft._spec().input_pin(6), 6, op, -1)
        self._inputs.append(self._cutoff_frequency)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Field or fields container.

        Parameters
        ----------
        my_field : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.fft()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def scale_forward_transform(self):
        """Allows to connect scale_forward_transform input to the operator.

        Scale for forward transform, default is 1.0.

        Parameters
        ----------
        my_scale_forward_transform : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.fft()
        >>> op.inputs.scale_forward_transform.connect(my_scale_forward_transform)
        >>> # or
        >>> op.inputs.scale_forward_transform(my_scale_forward_transform)
        """
        return self._scale_forward_transform

    @property
    def inplace(self):
        """Allows to connect inplace input to the operator.

        True if inplace, default is false.

        Parameters
        ----------
        my_inplace : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.fft()
        >>> op.inputs.inplace.connect(my_inplace)
        >>> # or
        >>> op.inputs.inplace(my_inplace)
        """
        return self._inplace

    @property
    def force_fft_points(self):
        """Allows to connect force_fft_points input to the operator.

        Explicitely define number of fft points to
        either rescope or perform zero
        padding.

        Parameters
        ----------
        my_force_fft_points : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.fft()
        >>> op.inputs.force_fft_points.connect(my_force_fft_points)
        >>> # or
        >>> op.inputs.force_fft_points(my_force_fft_points)
        """
        return self._force_fft_points

    @property
    def cutoff_frequency(self):
        """Allows to connect cutoff_frequency input to the operator.

        Restrict output frequency output up to this
        cutoff frequency

        Parameters
        ----------
        my_cutoff_frequency : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.fft()
        >>> op.inputs.cutoff_frequency.connect(my_cutoff_frequency)
        >>> # or
        >>> op.inputs.cutoff_frequency(my_cutoff_frequency)
        """
        return self._cutoff_frequency


class OutputsFft(_Outputs):
    """Intermediate class used to get outputs from
    fft operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mapping.fft()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(fft._spec().outputs, op)
        self._fields_container = Output(fft._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.mapping.fft()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
