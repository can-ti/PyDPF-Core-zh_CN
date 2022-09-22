"""
erp_accumulate_results
======================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class erp_accumulate_results(Operator):
    """Compute the Equivalent Radiated Power (ERP) by panels and sum over the
    panels

    Parameters
    ----------
    fields_container : FieldsContainer
    mesh : MeshedRegion or MeshesContainer
        The meshes region in this pin has to be
        boundary or skin mesh
    time_scoping : int or Scoping
        Load step number (if it's specified, the erp
        is computed only on the substeps of
        this step) or time scoping
    mass_density : float
        Mass density (if it's not specified, default
        value of the air is applied).
    speed_of_sound : float
        Speed of sound (if it's not specified,
        default value of the speed of sound
        in the air is applied).
    erp_type : int
        If this pin is set to 0, the classical erp is
        computed, 1 the corrected erp is
        computed (a mesh of one face has to
        be given in the pin 1) and 2 the
        enhanced erp is computed. default is
        0.
    boolean : bool
        If this pin is set to true, the erp level in
        db is computed
    factor : float
        Erp reference value. default is 1e-12


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.erp_accumulate_results()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_time_scoping = int()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mass_density = float()
    >>> op.inputs.mass_density.connect(my_mass_density)
    >>> my_speed_of_sound = float()
    >>> op.inputs.speed_of_sound.connect(my_speed_of_sound)
    >>> my_erp_type = int()
    >>> op.inputs.erp_type.connect(my_erp_type)
    >>> my_boolean = bool()
    >>> op.inputs.boolean.connect(my_boolean)
    >>> my_factor = float()
    >>> op.inputs.factor.connect(my_factor)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.erp_accumulate_results(
    ...     fields_container=my_fields_container,
    ...     mesh=my_mesh,
    ...     time_scoping=my_time_scoping,
    ...     mass_density=my_mass_density,
    ...     speed_of_sound=my_speed_of_sound,
    ...     erp_type=my_erp_type,
    ...     boolean=my_boolean,
    ...     factor=my_factor,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        fields_container=None,
        mesh=None,
        time_scoping=None,
        mass_density=None,
        speed_of_sound=None,
        erp_type=None,
        boolean=None,
        factor=None,
        config=None,
        server=None,
    ):
        super().__init__(name="erp_accumulate_results", config=config, server=server)
        self._inputs = InputsErpAccumulateResults(self)
        self._outputs = OutputsErpAccumulateResults(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if mass_density is not None:
            self.inputs.mass_density.connect(mass_density)
        if speed_of_sound is not None:
            self.inputs.speed_of_sound.connect(speed_of_sound)
        if erp_type is not None:
            self.inputs.erp_type.connect(erp_type)
        if boolean is not None:
            self.inputs.boolean.connect(boolean)
        if factor is not None:
            self.inputs.factor.connect(factor)

    @staticmethod
    def _spec():
        description = """Compute the Equivalent Radiated Power (ERP) by panels and sum over the
            panels"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=False,
                    document="""The meshes region in this pin has to be
        boundary or skin mesh""",
                ),
                2: PinSpecification(
                    name="time_scoping",
                    type_names=["int32", "vector<int32>", "scoping"],
                    optional=False,
                    document="""Load step number (if it's specified, the erp
        is computed only on the substeps of
        this step) or time scoping""",
                ),
                3: PinSpecification(
                    name="mass_density",
                    type_names=["double"],
                    optional=False,
                    document="""Mass density (if it's not specified, default
        value of the air is applied).""",
                ),
                4: PinSpecification(
                    name="speed_of_sound",
                    type_names=["double"],
                    optional=False,
                    document="""Speed of sound (if it's not specified,
        default value of the speed of sound
        in the air is applied).""",
                ),
                5: PinSpecification(
                    name="erp_type",
                    type_names=["int32"],
                    optional=False,
                    document="""If this pin is set to 0, the classical erp is
        computed, 1 the corrected erp is
        computed (a mesh of one face has to
        be given in the pin 1) and 2 the
        enhanced erp is computed. default is
        0.""",
                ),
                6: PinSpecification(
                    name="boolean",
                    type_names=["bool"],
                    optional=False,
                    document="""If this pin is set to true, the erp level in
        db is computed""",
                ),
                7: PinSpecification(
                    name="factor",
                    type_names=["double"],
                    optional=False,
                    document="""Erp reference value. default is 1e-12""",
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
        return Operator.default_config(name="erp_accumulate_results", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsErpAccumulateResults
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsErpAccumulateResults
        """
        return super().outputs


class InputsErpAccumulateResults(_Inputs):
    """Intermediate class used to connect user inputs to
    erp_accumulate_results operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.erp_accumulate_results()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_time_scoping = int()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mass_density = float()
    >>> op.inputs.mass_density.connect(my_mass_density)
    >>> my_speed_of_sound = float()
    >>> op.inputs.speed_of_sound.connect(my_speed_of_sound)
    >>> my_erp_type = int()
    >>> op.inputs.erp_type.connect(my_erp_type)
    >>> my_boolean = bool()
    >>> op.inputs.boolean.connect(my_boolean)
    >>> my_factor = float()
    >>> op.inputs.factor.connect(my_factor)
    """

    def __init__(self, op: Operator):
        super().__init__(erp_accumulate_results._spec().inputs, op)
        self._fields_container = Input(
            erp_accumulate_results._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._mesh = Input(erp_accumulate_results._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh)
        self._time_scoping = Input(
            erp_accumulate_results._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._time_scoping)
        self._mass_density = Input(
            erp_accumulate_results._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._mass_density)
        self._speed_of_sound = Input(
            erp_accumulate_results._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._speed_of_sound)
        self._erp_type = Input(erp_accumulate_results._spec().input_pin(5), 5, op, -1)
        self._inputs.append(self._erp_type)
        self._boolean = Input(erp_accumulate_results._spec().input_pin(6), 6, op, -1)
        self._inputs.append(self._boolean)
        self._factor = Input(erp_accumulate_results._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._factor)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.erp_accumulate_results()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        The meshes region in this pin has to be
        boundary or skin mesh

        Parameters
        ----------
        my_mesh : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.erp_accumulate_results()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        Load step number (if it's specified, the erp
        is computed only on the substeps of
        this step) or time scoping

        Parameters
        ----------
        my_time_scoping : int or Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.erp_accumulate_results()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def mass_density(self):
        """Allows to connect mass_density input to the operator.

        Mass density (if it's not specified, default
        value of the air is applied).

        Parameters
        ----------
        my_mass_density : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.erp_accumulate_results()
        >>> op.inputs.mass_density.connect(my_mass_density)
        >>> # or
        >>> op.inputs.mass_density(my_mass_density)
        """
        return self._mass_density

    @property
    def speed_of_sound(self):
        """Allows to connect speed_of_sound input to the operator.

        Speed of sound (if it's not specified,
        default value of the speed of sound
        in the air is applied).

        Parameters
        ----------
        my_speed_of_sound : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.erp_accumulate_results()
        >>> op.inputs.speed_of_sound.connect(my_speed_of_sound)
        >>> # or
        >>> op.inputs.speed_of_sound(my_speed_of_sound)
        """
        return self._speed_of_sound

    @property
    def erp_type(self):
        """Allows to connect erp_type input to the operator.

        If this pin is set to 0, the classical erp is
        computed, 1 the corrected erp is
        computed (a mesh of one face has to
        be given in the pin 1) and 2 the
        enhanced erp is computed. default is
        0.

        Parameters
        ----------
        my_erp_type : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.erp_accumulate_results()
        >>> op.inputs.erp_type.connect(my_erp_type)
        >>> # or
        >>> op.inputs.erp_type(my_erp_type)
        """
        return self._erp_type

    @property
    def boolean(self):
        """Allows to connect boolean input to the operator.

        If this pin is set to true, the erp level in
        db is computed

        Parameters
        ----------
        my_boolean : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.erp_accumulate_results()
        >>> op.inputs.boolean.connect(my_boolean)
        >>> # or
        >>> op.inputs.boolean(my_boolean)
        """
        return self._boolean

    @property
    def factor(self):
        """Allows to connect factor input to the operator.

        Erp reference value. default is 1e-12

        Parameters
        ----------
        my_factor : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.erp_accumulate_results()
        >>> op.inputs.factor.connect(my_factor)
        >>> # or
        >>> op.inputs.factor(my_factor)
        """
        return self._factor


class OutputsErpAccumulateResults(_Outputs):
    """Intermediate class used to get outputs from
    erp_accumulate_results operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.erp_accumulate_results()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(erp_accumulate_results._spec().outputs, op)
        self._field = Output(erp_accumulate_results._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.result.erp_accumulate_results()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field