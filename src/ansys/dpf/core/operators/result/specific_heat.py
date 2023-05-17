"""
specific_heat
=============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class specific_heat(Operator):
    """Read Specific Heat by calling the readers defined by the datasources.

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
    streams_container : StreamsContainer, optional
        Result file container allowed to be kept open
        to cache data
    data_sources : DataSources
        Result file path container, used if no
        streams are set
    mesh : MeshedRegion or MeshesContainer, optional
        Prevents from reading the mesh in the result
        files
    zone_scoping : Scoping or int, optional
        (for fluid results only) zone id (integer) or
        vector of zone ids (vector) or zone
        scoping (scoping)
    qualifiers1 : LabelSpace, optional
        (for fluid results only) labelspace with
        combination of zone, phases or
        species ids
    qualifiers2 : LabelSpace, optional
        (for fluid results only) labelspace with
        combination of zone, phases or
        species ids


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.specific_heat()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_zone_scoping = dpf.Scoping()
    >>> op.inputs.zone_scoping.connect(my_zone_scoping)
    >>> my_qualifiers1 = dpf.LabelSpace()
    >>> op.inputs.qualifiers1.connect(my_qualifiers1)
    >>> my_qualifiers2 = dpf.LabelSpace()
    >>> op.inputs.qualifiers2.connect(my_qualifiers2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.specific_heat(
    ...     time_scoping=my_time_scoping,
    ...     mesh_scoping=my_mesh_scoping,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     mesh=my_mesh,
    ...     zone_scoping=my_zone_scoping,
    ...     qualifiers1=my_qualifiers1,
    ...     qualifiers2=my_qualifiers2,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        time_scoping=None,
        mesh_scoping=None,
        streams_container=None,
        data_sources=None,
        mesh=None,
        zone_scoping=None,
        qualifiers1=None,
        qualifiers2=None,
        config=None,
        server=None,
    ):
        super().__init__(name="CP", config=config, server=server)
        self._inputs = InputsSpecificHeat(self)
        self._outputs = OutputsSpecificHeat(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if zone_scoping is not None:
            self.inputs.zone_scoping.connect(zone_scoping)
        if qualifiers1 is not None:
            self.inputs.qualifiers1.connect(qualifiers1)
        if qualifiers2 is not None:
            self.inputs.qualifiers2.connect(qualifiers2)

    @staticmethod
    def _spec():
        description = (
            """Read Specific Heat by calling the readers defined by the datasources."""
        )
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
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document="""Prevents from reading the mesh in the result
        files""",
                ),
                25: PinSpecification(
                    name="zone_scoping",
                    type_names=["scoping", "int32", "vector<int32>"],
                    optional=True,
                    document="""(for fluid results only) zone id (integer) or
        vector of zone ids (vector) or zone
        scoping (scoping)""",
                ),
                1000: PinSpecification(
                    name="qualifiers",
                    type_names=["label_space"],
                    optional=True,
                    document="""(for fluid results only) labelspace with
        combination of zone, phases or
        species ids""",
                ),
                1001: PinSpecification(
                    name="qualifiers",
                    type_names=["label_space"],
                    optional=True,
                    document="""(for fluid results only) labelspace with
        combination of zone, phases or
        species ids""",
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
        return Operator.default_config(name="CP", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSpecificHeat
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsSpecificHeat
        """
        return super().outputs


class InputsSpecificHeat(_Inputs):
    """Intermediate class used to connect user inputs to
    specific_heat operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.specific_heat()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_zone_scoping = dpf.Scoping()
    >>> op.inputs.zone_scoping.connect(my_zone_scoping)
    >>> my_qualifiers1 = dpf.LabelSpace()
    >>> op.inputs.qualifiers1.connect(my_qualifiers1)
    >>> my_qualifiers2 = dpf.LabelSpace()
    >>> op.inputs.qualifiers2.connect(my_qualifiers2)
    """

    def __init__(self, op: Operator):
        super().__init__(specific_heat._spec().inputs, op)
        self._time_scoping = Input(specific_heat._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(specific_heat._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._streams_container = Input(specific_heat._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._streams_container)
        self._data_sources = Input(specific_heat._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)
        self._mesh = Input(specific_heat._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)
        self._zone_scoping = Input(specific_heat._spec().input_pin(25), 25, op, -1)
        self._inputs.append(self._zone_scoping)
        self._qualifiers1 = Input(specific_heat._spec().input_pin(1000), 1000, op, 0)
        self._inputs.append(self._qualifiers1)
        self._qualifiers2 = Input(specific_heat._spec().input_pin(1001), 1001, op, 1)
        self._inputs.append(self._qualifiers2)

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
        >>> op = dpf.operators.result.specific_heat()
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
        >>> op = dpf.operators.result.specific_heat()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

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
        >>> op = dpf.operators.result.specific_heat()
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
        >>> op = dpf.operators.result.specific_heat()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

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
        >>> op = dpf.operators.result.specific_heat()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def zone_scoping(self):
        """Allows to connect zone_scoping input to the operator.

        (for fluid results only) zone id (integer) or
        vector of zone ids (vector) or zone
        scoping (scoping)

        Parameters
        ----------
        my_zone_scoping : Scoping or int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.specific_heat()
        >>> op.inputs.zone_scoping.connect(my_zone_scoping)
        >>> # or
        >>> op.inputs.zone_scoping(my_zone_scoping)
        """
        return self._zone_scoping

    @property
    def qualifiers1(self):
        """Allows to connect qualifiers1 input to the operator.

        (for fluid results only) labelspace with
        combination of zone, phases or
        species ids

        Parameters
        ----------
        my_qualifiers1 : LabelSpace

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.specific_heat()
        >>> op.inputs.qualifiers1.connect(my_qualifiers1)
        >>> # or
        >>> op.inputs.qualifiers1(my_qualifiers1)
        """
        return self._qualifiers1

    @property
    def qualifiers2(self):
        """Allows to connect qualifiers2 input to the operator.

        (for fluid results only) labelspace with
        combination of zone, phases or
        species ids

        Parameters
        ----------
        my_qualifiers2 : LabelSpace

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.specific_heat()
        >>> op.inputs.qualifiers2.connect(my_qualifiers2)
        >>> # or
        >>> op.inputs.qualifiers2(my_qualifiers2)
        """
        return self._qualifiers2


class OutputsSpecificHeat(_Outputs):
    """Intermediate class used to get outputs from
    specific_heat operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.specific_heat()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(specific_heat._spec().outputs, op)
        self._fields_container = Output(specific_heat._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.result.specific_heat()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
