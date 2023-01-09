"""
beam_tr_shear_stress
====================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class beam_tr_shear_stress(Operator):
    """Read Beam TR Shear Stress (LSDyna) by calling the readers defined by
    the datasources.

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
        Elements scoping required in output.
    streams_container : StreamsContainer, optional
        Result file container allowed to be kept open
        to cache data
    data_sources : DataSources
        Result file path container, used if no
        streams are set
    integration_point : int, optional
        Integration point where the result will be
        read from. default value: 0 (first
        integration point).
    unit_system : int or str, optional
        Unit system id (int) or semicolon-separated
        list of base unit strings


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.beam_tr_shear_stress()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_integration_point = int()
    >>> op.inputs.integration_point.connect(my_integration_point)
    >>> my_unit_system = int()
    >>> op.inputs.unit_system.connect(my_unit_system)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.beam_tr_shear_stress(
    ...     time_scoping=my_time_scoping,
    ...     mesh_scoping=my_mesh_scoping,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     integration_point=my_integration_point,
    ...     unit_system=my_unit_system,
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
        integration_point=None,
        unit_system=None,
        config=None,
        server=None,
    ):
        super().__init__(name="B_ST2", config=config, server=server)
        self._inputs = InputsBeamTrShearStress(self)
        self._outputs = OutputsBeamTrShearStress(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if integration_point is not None:
            self.inputs.integration_point.connect(integration_point)
        if unit_system is not None:
            self.inputs.unit_system.connect(unit_system)

    @staticmethod
    def _spec():
        description = """Read Beam TR Shear Stress (LSDyna) by calling the readers defined by
            the datasources."""
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
                    document="""Elements scoping required in output.""",
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
                6: PinSpecification(
                    name="integration_point",
                    type_names=["int32"],
                    optional=True,
                    document="""Integration point where the result will be
        read from. default value: 0 (first
        integration point).""",
                ),
                50: PinSpecification(
                    name="unit_system",
                    type_names=["int32", "string"],
                    optional=True,
                    document="""Unit system id (int) or semicolon-separated
        list of base unit strings""",
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
        return Operator.default_config(name="B_ST2", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsBeamTrShearStress
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsBeamTrShearStress
        """
        return super().outputs


class InputsBeamTrShearStress(_Inputs):
    """Intermediate class used to connect user inputs to
    beam_tr_shear_stress operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.beam_tr_shear_stress()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_integration_point = int()
    >>> op.inputs.integration_point.connect(my_integration_point)
    >>> my_unit_system = int()
    >>> op.inputs.unit_system.connect(my_unit_system)
    """

    def __init__(self, op: Operator):
        super().__init__(beam_tr_shear_stress._spec().inputs, op)
        self._time_scoping = Input(beam_tr_shear_stress._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(beam_tr_shear_stress._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._streams_container = Input(
            beam_tr_shear_stress._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(beam_tr_shear_stress._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)
        self._integration_point = Input(
            beam_tr_shear_stress._spec().input_pin(6), 6, op, -1
        )
        self._inputs.append(self._integration_point)
        self._unit_system = Input(
            beam_tr_shear_stress._spec().input_pin(50), 50, op, -1
        )
        self._inputs.append(self._unit_system)

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
        >>> op = dpf.operators.result.beam_tr_shear_stress()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Elements scoping required in output.

        Parameters
        ----------
        my_mesh_scoping : ScopingsContainer or Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.beam_tr_shear_stress()
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
        >>> op = dpf.operators.result.beam_tr_shear_stress()
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
        >>> op = dpf.operators.result.beam_tr_shear_stress()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def integration_point(self):
        """Allows to connect integration_point input to the operator.

        Integration point where the result will be
        read from. default value: 0 (first
        integration point).

        Parameters
        ----------
        my_integration_point : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.beam_tr_shear_stress()
        >>> op.inputs.integration_point.connect(my_integration_point)
        >>> # or
        >>> op.inputs.integration_point(my_integration_point)
        """
        return self._integration_point

    @property
    def unit_system(self):
        """Allows to connect unit_system input to the operator.

        Unit system id (int) or semicolon-separated
        list of base unit strings

        Parameters
        ----------
        my_unit_system : int or str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.beam_tr_shear_stress()
        >>> op.inputs.unit_system.connect(my_unit_system)
        >>> # or
        >>> op.inputs.unit_system(my_unit_system)
        """
        return self._unit_system


class OutputsBeamTrShearStress(_Outputs):
    """Intermediate class used to get outputs from
    beam_tr_shear_stress operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.beam_tr_shear_stress()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(beam_tr_shear_stress._spec().outputs, op)
        self._fields_container = Output(
            beam_tr_shear_stress._spec().output_pin(0), 0, op
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
        >>> op = dpf.operators.result.beam_tr_shear_stress()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
