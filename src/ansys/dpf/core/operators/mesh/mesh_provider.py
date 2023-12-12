"""
mesh_provider
=============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class mesh_provider(Operator):
    """Reads a mesh from result files.

    Parameters
    ----------
    time_scoping : int, optional
        Optional time/frequency set id of the mesh,
        supported for adaptative meshes.
    streams_container : StreamsContainer, optional
        Result file container allowed to be kept open
        to cache data
    data_sources : DataSources
        Result file path container, used if no
        streams are set
    read_cyclic : int, optional
        If 1, cyclic symmetry is ignored. if 2,
        cyclic expansion is done (default is
        1).
    region_scoping : Scoping or int, optional
        Region id (integer) or vector of region ids
        with one entity (vector) or region
        scoping with one id (scoping) (region
        corresponds to zone for fluid results
        or part for lsdyna results).
    laziness : DataTree, optional
        Configurate whether lazy evaluation can be
        performed and to what extent.
        supported attributes are:  -
        "num_named_selections"->num named
        selection to read (-1 is all, int32,
        default si -1), careful: the other
        named selections will not be
        available, use mesh_property_provider
        operator to read them. - all mesh
        property fields "mat",
        "named_selection",
        "apdl_element_type", "section"-> if
        set to 1 these properties will not be
        read and a workflow will be bounded
        to the properties to be evaluated on
        demand, with 0 they are read (default
        is 0).


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.mesh_provider()

    >>> # Make input connections
    >>> my_time_scoping = int()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_read_cyclic = int()
    >>> op.inputs.read_cyclic.connect(my_read_cyclic)
    >>> my_region_scoping = dpf.Scoping()
    >>> op.inputs.region_scoping.connect(my_region_scoping)
    >>> my_laziness = dpf.DataTree()
    >>> op.inputs.laziness.connect(my_laziness)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.mesh_provider(
    ...     time_scoping=my_time_scoping,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     read_cyclic=my_read_cyclic,
    ...     region_scoping=my_region_scoping,
    ...     laziness=my_laziness,
    ... )

    >>> # Get output data
    >>> result_mesh = op.outputs.mesh()
    """

    def __init__(
        self,
        time_scoping=None,
        streams_container=None,
        data_sources=None,
        read_cyclic=None,
        region_scoping=None,
        laziness=None,
        config=None,
        server=None,
    ):
        super().__init__(name="mesh_provider", config=config, server=server)
        self._inputs = InputsMeshProvider(self)
        self._outputs = OutputsMeshProvider(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if read_cyclic is not None:
            self.inputs.read_cyclic.connect(read_cyclic)
        if region_scoping is not None:
            self.inputs.region_scoping.connect(region_scoping)
        if laziness is not None:
            self.inputs.laziness.connect(laziness)

    @staticmethod
    def _spec():
        description = """Reads a mesh from result files."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_scoping",
                    type_names=["int32"],
                    optional=True,
                    document="""Optional time/frequency set id of the mesh,
        supported for adaptative meshes.""",
                ),
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=True,
                    document="""Result file container allowed to be kept open
        to cache data""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""Result file path container, used if no
        streams are set""",
                ),
                14: PinSpecification(
                    name="read_cyclic",
                    type_names=["enum dataProcessing::ECyclicReading", "int32"],
                    optional=True,
                    document="""If 1, cyclic symmetry is ignored. if 2,
        cyclic expansion is done (default is
        1).""",
                ),
                25: PinSpecification(
                    name="region_scoping",
                    type_names=["scoping", "int32", "vector<int32>"],
                    optional=True,
                    document="""Region id (integer) or vector of region ids
        with one entity (vector) or region
        scoping with one id (scoping) (region
        corresponds to zone for fluid results
        or part for lsdyna results).""",
                ),
                200: PinSpecification(
                    name="laziness",
                    type_names=["abstract_data_tree"],
                    optional=True,
                    document="""Configurate whether lazy evaluation can be
        performed and to what extent.
        supported attributes are:  -
        "num_named_selections"->num named
        selection to read (-1 is all, int32,
        default si -1), careful: the other
        named selections will not be
        available, use mesh_property_provider
        operator to read them. - all mesh
        property fields "mat",
        "named_selection",
        "apdl_element_type", "section"-> if
        set to 1 these properties will not be
        read and a workflow will be bounded
        to the properties to be evaluated on
        demand, with 0 they are read (default
        is 0).""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
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
        return Operator.default_config(name="mesh_provider", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMeshProvider
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMeshProvider
        """
        return super().outputs


class InputsMeshProvider(_Inputs):
    """Intermediate class used to connect user inputs to
    mesh_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.mesh_provider()
    >>> my_time_scoping = int()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_read_cyclic = int()
    >>> op.inputs.read_cyclic.connect(my_read_cyclic)
    >>> my_region_scoping = dpf.Scoping()
    >>> op.inputs.region_scoping.connect(my_region_scoping)
    >>> my_laziness = dpf.DataTree()
    >>> op.inputs.laziness.connect(my_laziness)
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_provider._spec().inputs, op)
        self._time_scoping = Input(mesh_provider._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._time_scoping)
        self._streams_container = Input(mesh_provider._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._streams_container)
        self._data_sources = Input(mesh_provider._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)
        self._read_cyclic = Input(mesh_provider._spec().input_pin(14), 14, op, -1)
        self._inputs.append(self._read_cyclic)
        self._region_scoping = Input(mesh_provider._spec().input_pin(25), 25, op, -1)
        self._inputs.append(self._region_scoping)
        self._laziness = Input(mesh_provider._spec().input_pin(200), 200, op, -1)
        self._inputs.append(self._laziness)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        Optional time/frequency set id of the mesh,
        supported for adaptative meshes.

        Parameters
        ----------
        my_time_scoping : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_provider()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator.

        Result file container allowed to be kept open
        to cache data

        Parameters
        ----------
        my_streams_container : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_provider()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Result file path container, used if no
        streams are set

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def read_cyclic(self):
        """Allows to connect read_cyclic input to the operator.

        If 1, cyclic symmetry is ignored. if 2,
        cyclic expansion is done (default is
        1).

        Parameters
        ----------
        my_read_cyclic : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_provider()
        >>> op.inputs.read_cyclic.connect(my_read_cyclic)
        >>> # or
        >>> op.inputs.read_cyclic(my_read_cyclic)
        """
        return self._read_cyclic

    @property
    def region_scoping(self):
        """Allows to connect region_scoping input to the operator.

        Region id (integer) or vector of region ids
        with one entity (vector) or region
        scoping with one id (scoping) (region
        corresponds to zone for fluid results
        or part for lsdyna results).

        Parameters
        ----------
        my_region_scoping : Scoping or int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_provider()
        >>> op.inputs.region_scoping.connect(my_region_scoping)
        >>> # or
        >>> op.inputs.region_scoping(my_region_scoping)
        """
        return self._region_scoping

    @property
    def laziness(self):
        """Allows to connect laziness input to the operator.

        Configurate whether lazy evaluation can be
        performed and to what extent.
        supported attributes are:  -
        "num_named_selections"->num named
        selection to read (-1 is all, int32,
        default si -1), careful: the other
        named selections will not be
        available, use mesh_property_provider
        operator to read them. - all mesh
        property fields "mat",
        "named_selection",
        "apdl_element_type", "section"-> if
        set to 1 these properties will not be
        read and a workflow will be bounded
        to the properties to be evaluated on
        demand, with 0 they are read (default
        is 0).

        Parameters
        ----------
        my_laziness : DataTree

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_provider()
        >>> op.inputs.laziness.connect(my_laziness)
        >>> # or
        >>> op.inputs.laziness(my_laziness)
        """
        return self._laziness


class OutputsMeshProvider(_Outputs):
    """Intermediate class used to get outputs from
    mesh_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.mesh_provider()
    >>> # Connect inputs : op.inputs. ...
    >>> result_mesh = op.outputs.mesh()
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_provider._spec().outputs, op)
        self._mesh = Output(mesh_provider._spec().output_pin(0), 0, op)
        self._outputs.append(self._mesh)

    @property
    def mesh(self):
        """Allows to get mesh output of the operator

        Returns
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh()
        """  # noqa: E501
        return self._mesh
