"""
elemental_heat_generation
=========================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class elemental_heat_generation(Operator):
    """Read/compute Elemental Heat Generation by calling the readers defined
    by the datasources.

    Parameters
    ----------
    time_scoping : Scoping or int or float or Field, optional
        Time/freq values (use doubles or field),
        time/freq set ids (use ints or
        scoping) or time/freq step ids (use
        scoping with timefreq_steps location)
        required in output.to specify
        time/freq values at specific load
        steps, put a field (and not a list)
        in input with a scoping located on
        "timefreq_steps".linear time freq
        intrapolation is performed if the
        values are not in the result files
        and the data at the max time or freq
        is taken when time/freqs are higher
        than available time/freqs in result
        files.
    mesh_scoping : ScopingsContainer or Scoping, optional
        Nodes or elements scoping required in output.
        the output fields will be scoped on
        these node or element ids. to figure
        out the ordering of the fields data,
        look at their scoping ids as they
        might not be ordered as the input
        scoping was. the scoping's location
        indicates whether nodes or elements
        are asked for. using scopings
        container allows you to split the
        result fields container into domains
    fields_container : FieldsContainer, optional
        Fields container already allocated modified
        inplace
    streams_container : StreamsContainer, optional
        Result file container allowed to be kept open
        to cache data
    data_sources : DataSources
        Result file path container, used if no
        streams are set
    bool_rotate_to_global : bool, optional
        If true the field is rotated to global
        coordinate system (default true)
    mesh : MeshedRegion or MeshesContainer, optional
        Prevents from reading the mesh in the result
        files
    read_cyclic : int, optional
        If 0 cyclic symmetry is ignored, if 1 cyclic
        sector is read, if 2 cyclic expansion
        is done, if 3 cyclic expansion is
        done and stages are merged (default
        is 1)


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.elemental_heat_generation()

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
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_read_cyclic = int()
    >>> op.inputs.read_cyclic.connect(my_read_cyclic)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.elemental_heat_generation(
    ...     time_scoping=my_time_scoping,
    ...     mesh_scoping=my_mesh_scoping,
    ...     fields_container=my_fields_container,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     bool_rotate_to_global=my_bool_rotate_to_global,
    ...     mesh=my_mesh,
    ...     read_cyclic=my_read_cyclic,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        time_scoping=None,
        mesh_scoping=None,
        fields_container=None,
        streams_container=None,
        data_sources=None,
        bool_rotate_to_global=None,
        mesh=None,
        read_cyclic=None,
        config=None,
        server=None,
    ):
        super().__init__(name="EHC", config=config, server=server)
        self._inputs = InputsElementalHeatGeneration(self)
        self._outputs = OutputsElementalHeatGeneration(self)
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
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if read_cyclic is not None:
            self.inputs.read_cyclic.connect(read_cyclic)

    @staticmethod
    def _spec():
        description = """Read/compute Elemental Heat Generation by calling the readers defined
            by the datasources."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_scoping",
                    type_names=[
                        "scoping",
                        "int32",
                        "vector<int32>",
                        "double",
                        "field",
                        "vector<double>",
                    ],
                    optional=True,
                    document="""Time/freq values (use doubles or field),
        time/freq set ids (use ints or
        scoping) or time/freq step ids (use
        scoping with timefreq_steps location)
        required in output.to specify
        time/freq values at specific load
        steps, put a field (and not a list)
        in input with a scoping located on
        "timefreq_steps".linear time freq
        intrapolation is performed if the
        values are not in the result files
        and the data at the max time or freq
        is taken when time/freqs are higher
        than available time/freqs in result
        files.""",
                ),
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scopings_container", "scoping"],
                    optional=True,
                    document="""Nodes or elements scoping required in output.
        the output fields will be scoped on
        these node or element ids. to figure
        out the ordering of the fields data,
        look at their scoping ids as they
        might not be ordered as the input
        scoping was. the scoping's location
        indicates whether nodes or elements
        are asked for. using scopings
        container allows you to split the
        result fields container into domains""",
                ),
                2: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=True,
                    document="""Fields container already allocated modified
        inplace""",
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
                5: PinSpecification(
                    name="bool_rotate_to_global",
                    type_names=["bool"],
                    optional=True,
                    document="""If true the field is rotated to global
        coordinate system (default true)""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document="""Prevents from reading the mesh in the result
        files""",
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
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
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
        return Operator.default_config(name="EHC", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementalHeatGeneration
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsElementalHeatGeneration
        """
        return super().outputs


class InputsElementalHeatGeneration(_Inputs):
    """Intermediate class used to connect user inputs to
    elemental_heat_generation operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.elemental_heat_generation()
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
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_read_cyclic = int()
    >>> op.inputs.read_cyclic.connect(my_read_cyclic)
    """

    def __init__(self, op: Operator):
        super().__init__(elemental_heat_generation._spec().inputs, op)
        self._time_scoping = Input(
            elemental_heat_generation._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(
            elemental_heat_generation._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._mesh_scoping)
        self._fields_container = Input(
            elemental_heat_generation._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._fields_container)
        self._streams_container = Input(
            elemental_heat_generation._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(
            elemental_heat_generation._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)
        self._bool_rotate_to_global = Input(
            elemental_heat_generation._spec().input_pin(5), 5, op, -1
        )
        self._inputs.append(self._bool_rotate_to_global)
        self._mesh = Input(elemental_heat_generation._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)
        self._read_cyclic = Input(
            elemental_heat_generation._spec().input_pin(14), 14, op, -1
        )
        self._inputs.append(self._read_cyclic)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        Time/freq values (use doubles or field),
        time/freq set ids (use ints or
        scoping) or time/freq step ids (use
        scoping with timefreq_steps location)
        required in output.to specify
        time/freq values at specific load
        steps, put a field (and not a list)
        in input with a scoping located on
        "timefreq_steps".linear time freq
        intrapolation is performed if the
        values are not in the result files
        and the data at the max time or freq
        is taken when time/freqs are higher
        than available time/freqs in result
        files.

        Parameters
        ----------
        my_time_scoping : Scoping or int or float or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.elemental_heat_generation()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Nodes or elements scoping required in output.
        the output fields will be scoped on
        these node or element ids. to figure
        out the ordering of the fields data,
        look at their scoping ids as they
        might not be ordered as the input
        scoping was. the scoping's location
        indicates whether nodes or elements
        are asked for. using scopings
        container allows you to split the
        result fields container into domains

        Parameters
        ----------
        my_mesh_scoping : ScopingsContainer or Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.elemental_heat_generation()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Fields container already allocated modified
        inplace

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.elemental_heat_generation()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

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
        >>> op = dpf.operators.result.elemental_heat_generation()
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
        >>> op = dpf.operators.result.elemental_heat_generation()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def bool_rotate_to_global(self):
        """Allows to connect bool_rotate_to_global input to the operator.

        If true the field is rotated to global
        coordinate system (default true)

        Parameters
        ----------
        my_bool_rotate_to_global : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.elemental_heat_generation()
        >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
        >>> # or
        >>> op.inputs.bool_rotate_to_global(my_bool_rotate_to_global)
        """
        return self._bool_rotate_to_global

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Prevents from reading the mesh in the result
        files

        Parameters
        ----------
        my_mesh : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.elemental_heat_generation()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

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
        >>> op = dpf.operators.result.elemental_heat_generation()
        >>> op.inputs.read_cyclic.connect(my_read_cyclic)
        >>> # or
        >>> op.inputs.read_cyclic(my_read_cyclic)
        """
        return self._read_cyclic


class OutputsElementalHeatGeneration(_Outputs):
    """Intermediate class used to get outputs from
    elemental_heat_generation operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.elemental_heat_generation()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(elemental_heat_generation._spec().outputs, op)
        self._fields_container = Output(
            elemental_heat_generation._spec().output_pin(0), 0, op
        )
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
        >>> op = dpf.operators.result.elemental_heat_generation()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
