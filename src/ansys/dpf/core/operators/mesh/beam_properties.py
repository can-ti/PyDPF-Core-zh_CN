"""
beam_properties
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class beam_properties(Operator):
    """Reads the beam's properties from the result files contained in the
    streams or data sources.

    Parameters
    ----------
    streams : StreamsContainer, optional
        Result file container allowed to be kept open
        to cache data.
    data_sources : DataSources
        Result file path container, used if no
        streams are set.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.beam_properties()

    >>> # Make input connections
    >>> my_streams = dpf.StreamsContainer()
    >>> op.inputs.streams.connect(my_streams)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.beam_properties(
    ...     streams=my_streams,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_mesh_out = op.outputs.mesh_out()
    >>> result_field_type_section_id = op.outputs.field_type_section_id()
    >>> result_field_area = op.outputs.field_area()
    >>> result_field_moment_inertia = op.outputs.field_moment_inertia()
    >>> result_field_geometry = op.outputs.field_geometry()
    >>> result_field_young_modulus = op.outputs.field_young_modulus()
    >>> result_field_poisson_ratio = op.outputs.field_poisson_ratio()
    >>> result_field_shear_modulus = op.outputs.field_shear_modulus()
    >>> result_field_beam_length = op.outputs.field_beam_length()
    >>> result_field_torsion_constant = op.outputs.field_torsion_constant()
    >>> result_field_warping_constant = op.outputs.field_warping_constant()
    >>> result_field_offset_type = op.outputs.field_offset_type()
    >>> result_field_offset_y = op.outputs.field_offset_y()
    >>> result_field_offset_z = op.outputs.field_offset_z()
    """

    def __init__(self, streams=None, data_sources=None, config=None, server=None):
        super().__init__(name="beam_properties", config=config, server=server)
        self._inputs = InputsBeamProperties(self)
        self._outputs = OutputsBeamProperties(self)
        if streams is not None:
            self.inputs.streams.connect(streams)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        description = """Reads the beam's properties from the result files contained in the
            streams or data sources."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                3: PinSpecification(
                    name="streams",
                    type_names=["streams_container"],
                    optional=True,
                    document="""Result file container allowed to be kept open
        to cache data.""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""Result file path container, used if no
        streams are set.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="mesh_out",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""This mesh updates a new map containing a
        field of the beam's properties if
        there is at least one beam in mesh.""",
                ),
                1: PinSpecification(
                    name="field_type_section_id",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains the section id of beams.
        1:rec; 3:csolid, 4:ctube, 5:chan,
        6:z, 7:l, 8:i, 9:t, 11:hats, 12:hrec.""",
                ),
                2: PinSpecification(
                    name="field_area",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains the area of beams.""",
                ),
                3: PinSpecification(
                    name="field_moment_inertia",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains the inertia moment of
        beams. iyy, iyz, izz.""",
                ),
                4: PinSpecification(
                    name="field_geometry",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains the geometry of beams.
        rec:b,h. csolid:ri. ctube:ri, re.
        chan:w1,w2,w3,t1,t2,t3.
        z:w1,w2,w3,t1,t2,t3. l:w1,w2,t1,t2.
        i:w1,w2,w3,t1,t2,t3. t:w1,w2,t1,t2.
        hats: w1,w2,w3,w4,t1,t2,t3,t4.
        hrec:w1,w2,t1,t2,t3,t4.""",
                ),
                5: PinSpecification(
                    name="field_young_modulus",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains the young's modulus of
        beams.""",
                ),
                6: PinSpecification(
                    name="field_poisson_ratio",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains the poisson's ratio of
        beams.""",
                ),
                7: PinSpecification(
                    name="field_shear_modulus",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains the shear modulus of
        beams.""",
                ),
                8: PinSpecification(
                    name="field_beam_length",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains the length of beams.""",
                ),
                9: PinSpecification(
                    name="field_torsion_constant",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains the torsion constant of
        beams.""",
                ),
                10: PinSpecification(
                    name="field_warping_constant",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains the warping constant of
        beams.""",
                ),
                11: PinSpecification(
                    name="field_offset_type",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains offset type of beams.""",
                ),
                12: PinSpecification(
                    name="field_offset_y",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains offset y of beams.""",
                ),
                13: PinSpecification(
                    name="field_offset_z",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains offset z of beams.""",
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
        return Operator.default_config(name="beam_properties", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsBeamProperties
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsBeamProperties
        """
        return super().outputs


class InputsBeamProperties(_Inputs):
    """Intermediate class used to connect user inputs to
    beam_properties operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.beam_properties()
    >>> my_streams = dpf.StreamsContainer()
    >>> op.inputs.streams.connect(my_streams)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(beam_properties._spec().inputs, op)
        self._streams = Input(beam_properties._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._streams)
        self._data_sources = Input(beam_properties._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)

    @property
    def streams(self):
        """Allows to connect streams input to the operator.

        Result file container allowed to be kept open
        to cache data.

        Parameters
        ----------
        my_streams : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> op.inputs.streams.connect(my_streams)
        >>> # or
        >>> op.inputs.streams(my_streams)
        """
        return self._streams

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Result file path container, used if no
        streams are set.

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsBeamProperties(_Outputs):
    """Intermediate class used to get outputs from
    beam_properties operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.beam_properties()
    >>> # Connect inputs : op.inputs. ...
    >>> result_mesh_out = op.outputs.mesh_out()
    >>> result_field_type_section_id = op.outputs.field_type_section_id()
    >>> result_field_area = op.outputs.field_area()
    >>> result_field_moment_inertia = op.outputs.field_moment_inertia()
    >>> result_field_geometry = op.outputs.field_geometry()
    >>> result_field_young_modulus = op.outputs.field_young_modulus()
    >>> result_field_poisson_ratio = op.outputs.field_poisson_ratio()
    >>> result_field_shear_modulus = op.outputs.field_shear_modulus()
    >>> result_field_beam_length = op.outputs.field_beam_length()
    >>> result_field_torsion_constant = op.outputs.field_torsion_constant()
    >>> result_field_warping_constant = op.outputs.field_warping_constant()
    >>> result_field_offset_type = op.outputs.field_offset_type()
    >>> result_field_offset_y = op.outputs.field_offset_y()
    >>> result_field_offset_z = op.outputs.field_offset_z()
    """

    def __init__(self, op: Operator):
        super().__init__(beam_properties._spec().outputs, op)
        self._mesh_out = Output(beam_properties._spec().output_pin(0), 0, op)
        self._outputs.append(self._mesh_out)
        self._field_type_section_id = Output(
            beam_properties._spec().output_pin(1), 1, op
        )
        self._outputs.append(self._field_type_section_id)
        self._field_area = Output(beam_properties._spec().output_pin(2), 2, op)
        self._outputs.append(self._field_area)
        self._field_moment_inertia = Output(
            beam_properties._spec().output_pin(3), 3, op
        )
        self._outputs.append(self._field_moment_inertia)
        self._field_geometry = Output(beam_properties._spec().output_pin(4), 4, op)
        self._outputs.append(self._field_geometry)
        self._field_young_modulus = Output(beam_properties._spec().output_pin(5), 5, op)
        self._outputs.append(self._field_young_modulus)
        self._field_poisson_ratio = Output(beam_properties._spec().output_pin(6), 6, op)
        self._outputs.append(self._field_poisson_ratio)
        self._field_shear_modulus = Output(beam_properties._spec().output_pin(7), 7, op)
        self._outputs.append(self._field_shear_modulus)
        self._field_beam_length = Output(beam_properties._spec().output_pin(8), 8, op)
        self._outputs.append(self._field_beam_length)
        self._field_torsion_constant = Output(
            beam_properties._spec().output_pin(9), 9, op
        )
        self._outputs.append(self._field_torsion_constant)
        self._field_warping_constant = Output(
            beam_properties._spec().output_pin(10), 10, op
        )
        self._outputs.append(self._field_warping_constant)
        self._field_offset_type = Output(beam_properties._spec().output_pin(11), 11, op)
        self._outputs.append(self._field_offset_type)
        self._field_offset_y = Output(beam_properties._spec().output_pin(12), 12, op)
        self._outputs.append(self._field_offset_y)
        self._field_offset_z = Output(beam_properties._spec().output_pin(13), 13, op)
        self._outputs.append(self._field_offset_z)

    @property
    def mesh_out(self):
        """Allows to get mesh_out output of the operator

        Returns
        ----------
        my_mesh_out : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh_out = op.outputs.mesh_out()
        """  # noqa: E501
        return self._mesh_out

    @property
    def field_type_section_id(self):
        """Allows to get field_type_section_id output of the operator

        Returns
        ----------
        my_field_type_section_id : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_type_section_id = op.outputs.field_type_section_id()
        """  # noqa: E501
        return self._field_type_section_id

    @property
    def field_area(self):
        """Allows to get field_area output of the operator

        Returns
        ----------
        my_field_area : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_area = op.outputs.field_area()
        """  # noqa: E501
        return self._field_area

    @property
    def field_moment_inertia(self):
        """Allows to get field_moment_inertia output of the operator

        Returns
        ----------
        my_field_moment_inertia : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_moment_inertia = op.outputs.field_moment_inertia()
        """  # noqa: E501
        return self._field_moment_inertia

    @property
    def field_geometry(self):
        """Allows to get field_geometry output of the operator

        Returns
        ----------
        my_field_geometry : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_geometry = op.outputs.field_geometry()
        """  # noqa: E501
        return self._field_geometry

    @property
    def field_young_modulus(self):
        """Allows to get field_young_modulus output of the operator

        Returns
        ----------
        my_field_young_modulus : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_young_modulus = op.outputs.field_young_modulus()
        """  # noqa: E501
        return self._field_young_modulus

    @property
    def field_poisson_ratio(self):
        """Allows to get field_poisson_ratio output of the operator

        Returns
        ----------
        my_field_poisson_ratio : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_poisson_ratio = op.outputs.field_poisson_ratio()
        """  # noqa: E501
        return self._field_poisson_ratio

    @property
    def field_shear_modulus(self):
        """Allows to get field_shear_modulus output of the operator

        Returns
        ----------
        my_field_shear_modulus : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_shear_modulus = op.outputs.field_shear_modulus()
        """  # noqa: E501
        return self._field_shear_modulus

    @property
    def field_beam_length(self):
        """Allows to get field_beam_length output of the operator

        Returns
        ----------
        my_field_beam_length : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_beam_length = op.outputs.field_beam_length()
        """  # noqa: E501
        return self._field_beam_length

    @property
    def field_torsion_constant(self):
        """Allows to get field_torsion_constant output of the operator

        Returns
        ----------
        my_field_torsion_constant : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_torsion_constant = op.outputs.field_torsion_constant()
        """  # noqa: E501
        return self._field_torsion_constant

    @property
    def field_warping_constant(self):
        """Allows to get field_warping_constant output of the operator

        Returns
        ----------
        my_field_warping_constant : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_warping_constant = op.outputs.field_warping_constant()
        """  # noqa: E501
        return self._field_warping_constant

    @property
    def field_offset_type(self):
        """Allows to get field_offset_type output of the operator

        Returns
        ----------
        my_field_offset_type : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_offset_type = op.outputs.field_offset_type()
        """  # noqa: E501
        return self._field_offset_type

    @property
    def field_offset_y(self):
        """Allows to get field_offset_y output of the operator

        Returns
        ----------
        my_field_offset_y : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_offset_y = op.outputs.field_offset_y()
        """  # noqa: E501
        return self._field_offset_y

    @property
    def field_offset_z(self):
        """Allows to get field_offset_z output of the operator

        Returns
        ----------
        my_field_offset_z : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_offset_z = op.outputs.field_offset_z()
        """  # noqa: E501
        return self._field_offset_z
