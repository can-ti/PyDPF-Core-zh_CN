"""
cyclic_expanded_el_strain
-------------------------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class cyclic_expanded_el_strain(Operator):
    """Read mapdl::rst::EPEL from an rst file and expand it with cyclic
    symmetry.

    Parameters
    ----------
    time_scoping : Scoping, optional
    mesh_scoping : ScopingsContainer or Scoping, optional
    fields_container : FieldsContainer, optional
        Fieldscontainer already allocated modified
        inplace
    streams_container : StreamsContainer or Stream, optional
        Streams containing the result file.
    data_sources : DataSources
        Data sources containing the result file.
    bool_rotate_to_global : bool, optional
        Default is true
    sector_mesh : MeshedRegion or MeshesContainer, optional
        Mesh of the base sector (can be a skin).
    requested_location : str, optional
        Location needed in output
    read_cyclic : int, optional
        If 0 cyclic symmetry is ignored, if 1 cyclic
        sector is read, if 2 cyclic expansion
        is done, if 3 cyclic expansion is
        done and stages are merged (default
        is 1)
    expanded_meshed_region : MeshedRegion or MeshesContainer, optional
        Mesh expanded.
    cyclic_support : CyclicSupport, optional
    sectors_to_expand : Scoping or ScopingsContainer, optional
        Sectors to expand (start at 0), for
        multistage: use scopings container
        with 'stage' label.
    phi : float, optional
        Phi angle (default value 0.0)


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.cyclic_expanded_el_strain()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_bool_rotate_to_global = bool()
    >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
    >>> my_sector_mesh = dpf.MeshedRegion()
    >>> op.inputs.sector_mesh.connect(my_sector_mesh)
    >>> my_requested_location = str()
    >>> op.inputs.requested_location.connect(my_requested_location)
    >>> my_read_cyclic = int()
    >>> op.inputs.read_cyclic.connect(my_read_cyclic)
    >>> my_expanded_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.expanded_meshed_region.connect(my_expanded_meshed_region)
    >>> my_cyclic_support = dpf.CyclicSupport()
    >>> op.inputs.cyclic_support.connect(my_cyclic_support)
    >>> my_sectors_to_expand = dpf.Scoping()
    >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
    >>> my_phi = float()
    >>> op.inputs.phi.connect(my_phi)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.cyclic_expanded_el_strain(
    ...     time_scoping=my_time_scoping,
    ...     mesh_scoping=my_mesh_scoping,
    ...     fields_container=my_fields_container,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     bool_rotate_to_global=my_bool_rotate_to_global,
    ...     sector_mesh=my_sector_mesh,
    ...     requested_location=my_requested_location,
    ...     read_cyclic=my_read_cyclic,
    ...     expanded_meshed_region=my_expanded_meshed_region,
    ...     cyclic_support=my_cyclic_support,
    ...     sectors_to_expand=my_sectors_to_expand,
    ...     phi=my_phi,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    >>> result_expanded_meshes = op.outputs.expanded_meshes()
    """

    def __init__(
        self,
        time_scoping=None,
        mesh_scoping=None,
        fields_container=None,
        streams_container=None,
        data_sources=None,
        bool_rotate_to_global=None,
        sector_mesh=None,
        requested_location=None,
        read_cyclic=None,
        expanded_meshed_region=None,
        cyclic_support=None,
        sectors_to_expand=None,
        phi=None,
        config=None,
        server=None,
    ):
        super().__init__(name="mapdl::rst::EPEL_cyclic", config=config, server=server)
        self._inputs = InputsCyclicExpandedElStrain(self)
        self._outputs = OutputsCyclicExpandedElStrain(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if bool_rotate_to_global is not None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if sector_mesh is not None:
            self.inputs.sector_mesh.connect(sector_mesh)
        if requested_location is not None:
            self.inputs.requested_location.connect(requested_location)
        if read_cyclic is not None:
            self.inputs.read_cyclic.connect(read_cyclic)
        if expanded_meshed_region is not None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if cyclic_support is not None:
            self.inputs.cyclic_support.connect(cyclic_support)
        if sectors_to_expand is not None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)
        if phi is not None:
            self.inputs.phi.connect(phi)

    @staticmethod
    def _spec():
        description = """Read mapdl::rst::EPEL from an rst file and expand it with cyclic
            symmetry."""
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
                    optional=True,
                    document="""Fieldscontainer already allocated modified
        inplace""",
                ),
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container", "stream"],
                    optional=True,
                    document="""Streams containing the result file.""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""Data sources containing the result file.""",
                ),
                5: PinSpecification(
                    name="bool_rotate_to_global",
                    type_names=["bool"],
                    optional=True,
                    document="""Default is true""",
                ),
                7: PinSpecification(
                    name="sector_mesh",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document="""Mesh of the base sector (can be a skin).""",
                ),
                9: PinSpecification(
                    name="requested_location",
                    type_names=["string"],
                    optional=True,
                    document="""Location needed in output""",
                ),
                14: PinSpecification(
                    name="read_cyclic",
                    type_names=["enum dataProcessing::ECyclicReading", "int32"],
                    optional=True,
                    document="""If 0 cyclic symmetry is ignored, if 1 cyclic
        sector is read, if 2 cyclic expansion
        is done, if 3 cyclic expansion is
        done and stages are merged (default
        is 1)""",
                ),
                15: PinSpecification(
                    name="expanded_meshed_region",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document="""Mesh expanded.""",
                ),
                16: PinSpecification(
                    name="cyclic_support",
                    type_names=["cyclic_support"],
                    optional=True,
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
                    document="""Phi angle (default value 0.0)""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fieldscontainer filled in""",
                ),
                1: PinSpecification(
                    name="expanded_meshes",
                    type_names=["meshes_container"],
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
        return Operator.default_config(name="mapdl::rst::EPEL_cyclic", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCyclicExpandedElStrain
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCyclicExpandedElStrain
        """
        return super().outputs


class InputsCyclicExpandedElStrain(_Inputs):
    """Intermediate class used to connect user inputs to
    cyclic_expanded_el_strain operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.cyclic_expanded_el_strain()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_bool_rotate_to_global = bool()
    >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
    >>> my_sector_mesh = dpf.MeshedRegion()
    >>> op.inputs.sector_mesh.connect(my_sector_mesh)
    >>> my_requested_location = str()
    >>> op.inputs.requested_location.connect(my_requested_location)
    >>> my_read_cyclic = int()
    >>> op.inputs.read_cyclic.connect(my_read_cyclic)
    >>> my_expanded_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.expanded_meshed_region.connect(my_expanded_meshed_region)
    >>> my_cyclic_support = dpf.CyclicSupport()
    >>> op.inputs.cyclic_support.connect(my_cyclic_support)
    >>> my_sectors_to_expand = dpf.Scoping()
    >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
    >>> my_phi = float()
    >>> op.inputs.phi.connect(my_phi)
    """

    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_el_strain._spec().inputs, op)
        self._time_scoping = Input(
            cyclic_expanded_el_strain._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(
            cyclic_expanded_el_strain._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._mesh_scoping)
        self._fields_container = Input(
            cyclic_expanded_el_strain._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._fields_container)
        self._streams_container = Input(
            cyclic_expanded_el_strain._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(
            cyclic_expanded_el_strain._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)
        self._bool_rotate_to_global = Input(
            cyclic_expanded_el_strain._spec().input_pin(5), 5, op, -1
        )
        self._inputs.append(self._bool_rotate_to_global)
        self._sector_mesh = Input(
            cyclic_expanded_el_strain._spec().input_pin(7), 7, op, -1
        )
        self._inputs.append(self._sector_mesh)
        self._requested_location = Input(
            cyclic_expanded_el_strain._spec().input_pin(9), 9, op, -1
        )
        self._inputs.append(self._requested_location)
        self._read_cyclic = Input(
            cyclic_expanded_el_strain._spec().input_pin(14), 14, op, -1
        )
        self._inputs.append(self._read_cyclic)
        self._expanded_meshed_region = Input(
            cyclic_expanded_el_strain._spec().input_pin(15), 15, op, -1
        )
        self._inputs.append(self._expanded_meshed_region)
        self._cyclic_support = Input(
            cyclic_expanded_el_strain._spec().input_pin(16), 16, op, -1
        )
        self._inputs.append(self._cyclic_support)
        self._sectors_to_expand = Input(
            cyclic_expanded_el_strain._spec().input_pin(18), 18, op, -1
        )
        self._inputs.append(self._sectors_to_expand)
        self._phi = Input(cyclic_expanded_el_strain._spec().input_pin(19), 19, op, -1)
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
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
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
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Fieldscontainer already allocated modified
        inplace

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator.

        Streams containing the result file.

        Parameters
        ----------
        my_streams_container : StreamsContainer or Stream

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Data sources containing the result file.

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

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
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
        >>> # or
        >>> op.inputs.bool_rotate_to_global(my_bool_rotate_to_global)
        """
        return self._bool_rotate_to_global

    @property
    def sector_mesh(self):
        """Allows to connect sector_mesh input to the operator.

        Mesh of the base sector (can be a skin).

        Parameters
        ----------
        my_sector_mesh : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.sector_mesh.connect(my_sector_mesh)
        >>> # or
        >>> op.inputs.sector_mesh(my_sector_mesh)
        """
        return self._sector_mesh

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator.

        Location needed in output

        Parameters
        ----------
        my_requested_location : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> # or
        >>> op.inputs.requested_location(my_requested_location)
        """
        return self._requested_location

    @property
    def read_cyclic(self):
        """Allows to connect read_cyclic input to the operator.

        If 0 cyclic symmetry is ignored, if 1 cyclic
        sector is read, if 2 cyclic expansion
        is done, if 3 cyclic expansion is
        done and stages are merged (default
        is 1)

        Parameters
        ----------
        my_read_cyclic : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.read_cyclic.connect(my_read_cyclic)
        >>> # or
        >>> op.inputs.read_cyclic(my_read_cyclic)
        """
        return self._read_cyclic

    @property
    def expanded_meshed_region(self):
        """Allows to connect expanded_meshed_region input to the operator.

        Mesh expanded.

        Parameters
        ----------
        my_expanded_meshed_region : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.expanded_meshed_region.connect(my_expanded_meshed_region)
        >>> # or
        >>> op.inputs.expanded_meshed_region(my_expanded_meshed_region)
        """
        return self._expanded_meshed_region

    @property
    def cyclic_support(self):
        """Allows to connect cyclic_support input to the operator.

        Parameters
        ----------
        my_cyclic_support : CyclicSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
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
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
        >>> # or
        >>> op.inputs.sectors_to_expand(my_sectors_to_expand)
        """
        return self._sectors_to_expand

    @property
    def phi(self):
        """Allows to connect phi input to the operator.

        Phi angle (default value 0.0)

        Parameters
        ----------
        my_phi : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> op.inputs.phi.connect(my_phi)
        >>> # or
        >>> op.inputs.phi(my_phi)
        """
        return self._phi


class OutputsCyclicExpandedElStrain(_Outputs):
    """Intermediate class used to get outputs from
    cyclic_expanded_el_strain operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.cyclic_expanded_el_strain()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    >>> result_expanded_meshes = op.outputs.expanded_meshes()
    """

    def __init__(self, op: Operator):
        super().__init__(cyclic_expanded_el_strain._spec().outputs, op)
        self._fields_container = Output(
            cyclic_expanded_el_strain._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._fields_container)
        self._expanded_meshes = Output(
            cyclic_expanded_el_strain._spec().output_pin(1), 1, op
        )
        self._outputs.append(self._expanded_meshes)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator

        Returns
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container

    @property
    def expanded_meshes(self):
        """Allows to get expanded_meshes output of the operator

        Returns
        ----------
        my_expanded_meshes : MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_expanded_el_strain()
        >>> # Connect inputs : op.inputs. ...
        >>> result_expanded_meshes = op.outputs.expanded_meshes()
        """  # noqa: E501
        return self._expanded_meshes
