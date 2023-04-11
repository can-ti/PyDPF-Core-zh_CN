"""
cyclic_expansion
================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class cyclic_expansion(Operator):
    """Expand cyclic results from a fieldsContainer for given sets, sectors
    and scoping (optionals).

    Parameters
    ----------
    time_scoping : Scoping, optional
    mesh_scoping : ScopingsContainer or Scoping, optional
    fields_container : FieldsContainer
        Field container with the base and duplicate
        sectors
    bool_rotate_to_global : bool, optional
        Default is true
    map_size_scoping_out : optional
        Map provider by scoping adapter
    merge_stages : bool, optional
    cyclic_support : CyclicSupport
    sectors_to_expand : Scoping or ScopingsContainer, optional
        Sectors to expand (start at 0), for
        multistage: use scopings container
        with 'stage' label.
    phi : float, optional
        Angle phi in degrees (default value 0.0)


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.cyclic_expansion()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_bool_rotate_to_global = bool()
    >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
    >>> my_map_size_scoping_out = dpf.()
    >>> op.inputs.map_size_scoping_out.connect(my_map_size_scoping_out)
    >>> my_merge_stages = bool()
    >>> op.inputs.merge_stages.connect(my_merge_stages)
    >>> my_cyclic_support = dpf.CyclicSupport()
    >>> op.inputs.cyclic_support.connect(my_cyclic_support)
    >>> my_sectors_to_expand = dpf.Scoping()
    >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
    >>> my_phi = float()
    >>> op.inputs.phi.connect(my_phi)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.cyclic_expansion(
    ...     time_scoping=my_time_scoping,
    ...     mesh_scoping=my_mesh_scoping,
    ...     fields_container=my_fields_container,
    ...     bool_rotate_to_global=my_bool_rotate_to_global,
    ...     map_size_scoping_out=my_map_size_scoping_out,
    ...     merge_stages=my_merge_stages,
    ...     cyclic_support=my_cyclic_support,
    ...     sectors_to_expand=my_sectors_to_expand,
    ...     phi=my_phi,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        time_scoping=None,
        mesh_scoping=None,
        fields_container=None,
        bool_rotate_to_global=None,
        map_size_scoping_out=None,
        merge_stages=None,
        cyclic_support=None,
        sectors_to_expand=None,
        phi=None,
        config=None,
        server=None,
    ):
        super().__init__(name="cyclic_expansion", config=config, server=server)
        self._inputs = InputsCyclicExpansion(self)
        self._outputs = OutputsCyclicExpansion(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if bool_rotate_to_global is not None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if map_size_scoping_out is not None:
            self.inputs.map_size_scoping_out.connect(map_size_scoping_out)
        if merge_stages is not None:
            self.inputs.merge_stages.connect(merge_stages)
        if cyclic_support is not None:
            self.inputs.cyclic_support.connect(cyclic_support)
        if sectors_to_expand is not None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)
        if phi is not None:
            self.inputs.phi.connect(phi)

    @staticmethod
    def _spec():
        description = """Expand cyclic results from a fieldsContainer for given sets, sectors
            and scoping (optionals)."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_scoping",
                    type_names=["scoping", "vector<int32>"],
                    optional=True,
                    document="""""",
                ),
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scopings_container", "scoping", "vector<int32>"],
                    optional=True,
                    document="""""",
                ),
                2: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Field container with the base and duplicate
        sectors""",
                ),
                5: PinSpecification(
                    name="bool_rotate_to_global",
                    type_names=["bool"],
                    optional=True,
                    document="""Default is true""",
                ),
                6: PinSpecification(
                    name="map_size_scoping_out",
                    type_names=["umap<int32,int32>"],
                    optional=True,
                    document="""Map provider by scoping adapter""",
                ),
                14: PinSpecification(
                    name="merge_stages",
                    type_names=["bool"],
                    optional=True,
                    document="""""",
                ),
                16: PinSpecification(
                    name="cyclic_support",
                    type_names=["cyclic_support"],
                    optional=False,
                    document="""""",
                ),
                18: PinSpecification(
                    name="sectors_to_expand",
                    type_names=["vector<int32>", "scoping", "scopings_container"],
                    optional=True,
                    document="""Sectors to expand (start at 0), for
        multistage: use scopings container
        with 'stage' label.""",
                ),
                19: PinSpecification(
                    name="phi",
                    type_names=["double"],
                    optional=True,
                    document="""Angle phi in degrees (default value 0.0)""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fieldscontainer filled in""",
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
        return Operator.default_config(name="cyclic_expansion", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCyclicExpansion
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCyclicExpansion
        """
        return super().outputs


class InputsCyclicExpansion(_Inputs):
    """Intermediate class used to connect user inputs to
    cyclic_expansion operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.cyclic_expansion()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_bool_rotate_to_global = bool()
    >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
    >>> my_map_size_scoping_out = dpf.()
    >>> op.inputs.map_size_scoping_out.connect(my_map_size_scoping_out)
    >>> my_merge_stages = bool()
    >>> op.inputs.merge_stages.connect(my_merge_stages)
    >>> my_cyclic_support = dpf.CyclicSupport()
    >>> op.inputs.cyclic_support.connect(my_cyclic_support)
    >>> my_sectors_to_expand = dpf.Scoping()
    >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
    >>> my_phi = float()
    >>> op.inputs.phi.connect(my_phi)
    """

    def __init__(self, op: Operator):
        super().__init__(cyclic_expansion._spec().inputs, op)
        self._time_scoping = Input(cyclic_expansion._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(cyclic_expansion._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._fields_container = Input(cyclic_expansion._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._fields_container)
        self._bool_rotate_to_global = Input(
            cyclic_expansion._spec().input_pin(5), 5, op, -1
        )
        self._inputs.append(self._bool_rotate_to_global)
        self._map_size_scoping_out = Input(
            cyclic_expansion._spec().input_pin(6), 6, op, -1
        )
        self._inputs.append(self._map_size_scoping_out)
        self._merge_stages = Input(cyclic_expansion._spec().input_pin(14), 14, op, -1)
        self._inputs.append(self._merge_stages)
        self._cyclic_support = Input(cyclic_expansion._spec().input_pin(16), 16, op, -1)
        self._inputs.append(self._cyclic_support)
        self._sectors_to_expand = Input(
            cyclic_expansion._spec().input_pin(18), 18, op, -1
        )
        self._inputs.append(self._sectors_to_expand)
        self._phi = Input(cyclic_expansion._spec().input_pin(19), 19, op, -1)
        self._inputs.append(self._phi)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        Parameters
        ----------
        my_time_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expansion()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Parameters
        ----------
        my_mesh_scoping : ScopingsContainer or Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expansion()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Field container with the base and duplicate
        sectors

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expansion()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def bool_rotate_to_global(self):
        """Allows to connect bool_rotate_to_global input to the operator.

        Default is true

        Parameters
        ----------
        my_bool_rotate_to_global : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expansion()
        >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
        >>> # or
        >>> op.inputs.bool_rotate_to_global(my_bool_rotate_to_global)
        """
        return self._bool_rotate_to_global

    @property
    def map_size_scoping_out(self):
        """Allows to connect map_size_scoping_out input to the operator.

        Map provider by scoping adapter

        Parameters
        ----------
        my_map_size_scoping_out :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expansion()
        >>> op.inputs.map_size_scoping_out.connect(my_map_size_scoping_out)
        >>> # or
        >>> op.inputs.map_size_scoping_out(my_map_size_scoping_out)
        """
        return self._map_size_scoping_out

    @property
    def merge_stages(self):
        """Allows to connect merge_stages input to the operator.

        Parameters
        ----------
        my_merge_stages : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expansion()
        >>> op.inputs.merge_stages.connect(my_merge_stages)
        >>> # or
        >>> op.inputs.merge_stages(my_merge_stages)
        """
        return self._merge_stages

    @property
    def cyclic_support(self):
        """Allows to connect cyclic_support input to the operator.

        Parameters
        ----------
        my_cyclic_support : CyclicSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expansion()
        >>> op.inputs.cyclic_support.connect(my_cyclic_support)
        >>> # or
        >>> op.inputs.cyclic_support(my_cyclic_support)
        """
        return self._cyclic_support

    @property
    def sectors_to_expand(self):
        """Allows to connect sectors_to_expand input to the operator.

        Sectors to expand (start at 0), for
        multistage: use scopings container
        with 'stage' label.

        Parameters
        ----------
        my_sectors_to_expand : Scoping or ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expansion()
        >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
        >>> # or
        >>> op.inputs.sectors_to_expand(my_sectors_to_expand)
        """
        return self._sectors_to_expand

    @property
    def phi(self):
        """Allows to connect phi input to the operator.

        Angle phi in degrees (default value 0.0)

        Parameters
        ----------
        my_phi : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expansion()
        >>> op.inputs.phi.connect(my_phi)
        >>> # or
        >>> op.inputs.phi(my_phi)
        """
        return self._phi


class OutputsCyclicExpansion(_Outputs):
    """Intermediate class used to get outputs from
    cyclic_expansion operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.cyclic_expansion()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(cyclic_expansion._spec().outputs, op)
        self._fields_container = Output(cyclic_expansion._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.result.cyclic_expansion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
