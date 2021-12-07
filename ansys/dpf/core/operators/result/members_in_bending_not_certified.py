"""Autogenerated DPF operator classes.

Created on 12/06/2021, 14:29:14.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class members_in_bending_not_certified(Operator):
    """This operator is a non-certified example of buckling resistance
    verification for the bending members. It is only provided as an
    example if you want to develop your own compute norm operator. The
    results computed by this beta operator have not been certified by
    ANSYS. ANSYS declines all responsibility for the use of this
    operator. HATS Beam and irregular beams (unequal I-Beam, not-
    square Channel-Beam, not-square Angle L-beam, unequal hollow
    rectanglar beam) not supported.

    Parameters
    ----------
    time_scoping : Scoping or int, optional
    field_yield_strength : Field
        This pin contains field of beam's yield
        strength defined by the user.
    class_cross_section : bool
        Selection for a cross-section. true: class 1
        or 2 cross-sections. false: class 3
        cross section. if the user defines
        the cross section as class 1 or 2,
        the section modulus would be plastic
        section modulus. if it's class 3-
        cross section,the section modulus
        would be elastic section modulus
    streams : StreamsContainer, optional
         result file container allowed to be kept
        open to cache data.
    data_sources : DataSources, optional
        Result file path container, used if no
        streams are set.
    partial_factor : float
        Partial safety factor for resistance of
        members to instability assessed by
        member checks. default value: 1.
    mesh : MeshedRegion
         mesh containing beam's properties defined by
        user
    bending_moment_y : FieldsContainer
        Fields container of bending moment on axis y
        defined by user
    bending_moment_z : FieldsContainer
        Fields container of bending moment on axis z
        defined by user


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.members_in_bending_not_certified()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_field_yield_strength = dpf.Field()
    >>> op.inputs.field_yield_strength.connect(my_field_yield_strength)
    >>> my_class_cross_section = bool()
    >>> op.inputs.class_cross_section.connect(my_class_cross_section)
    >>> my_streams = dpf.StreamsContainer()
    >>> op.inputs.streams.connect(my_streams)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_partial_factor = float()
    >>> op.inputs.partial_factor.connect(my_partial_factor)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_bending_moment_y = dpf.FieldsContainer()
    >>> op.inputs.bending_moment_y.connect(my_bending_moment_y)
    >>> my_bending_moment_z = dpf.FieldsContainer()
    >>> op.inputs.bending_moment_z.connect(my_bending_moment_z)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.members_in_bending_not_certified(
    ...     time_scoping=my_time_scoping,
    ...     field_yield_strength=my_field_yield_strength,
    ...     class_cross_section=my_class_cross_section,
    ...     streams=my_streams,
    ...     data_sources=my_data_sources,
    ...     partial_factor=my_partial_factor,
    ...     mesh=my_mesh,
    ...     bending_moment_y=my_bending_moment_y,
    ...     bending_moment_z=my_bending_moment_z,
    ... )

    >>> # Get output data
    >>> result_buckling_resistance_bending_yy = op.outputs.buckling_resistance_bending_yy()
    >>> result_buckling_resistance_bending_zz = op.outputs.buckling_resistance_bending_zz()
    """

    def __init__(
        self,
        time_scoping=None,
        field_yield_strength=None,
        class_cross_section=None,
        streams=None,
        data_sources=None,
        partial_factor=None,
        mesh=None,
        bending_moment_y=None,
        bending_moment_z=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="members_in_bending_not_certified", config=config, server=server
        )
        self._inputs = InputsMembersInBendingNotCertified(self)
        self._outputs = OutputsMembersInBendingNotCertified(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if field_yield_strength is not None:
            self.inputs.field_yield_strength.connect(field_yield_strength)
        if class_cross_section is not None:
            self.inputs.class_cross_section.connect(class_cross_section)
        if streams is not None:
            self.inputs.streams.connect(streams)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if partial_factor is not None:
            self.inputs.partial_factor.connect(partial_factor)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if bending_moment_y is not None:
            self.inputs.bending_moment_y.connect(bending_moment_y)
        if bending_moment_z is not None:
            self.inputs.bending_moment_z.connect(bending_moment_z)

    @staticmethod
    def _spec():
        description = """This operator is a non-certified example of buckling resistance
            verification for the bending members. It is only provided
            as an example if you want to develop your own compute norm
            operator. The results computed by this beta operator have
            not been certified by ANSYS. ANSYS declines all
            responsibility for the use of this operator. HATS Beam and
            irregular beams (unequal I-Beam, not-square Channel-Beam,
            not-square Angle L-beam, unequal hollow rectanglar beam)
            not supported."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_scoping",
                    type_names=["scoping", "vector<int32>", "int32"],
                    optional=True,
                    document="""""",
                ),
                1: PinSpecification(
                    name="field_yield_strength",
                    type_names=["field"],
                    optional=False,
                    document="""This pin contains field of beam's yield
        strength defined by the user.""",
                ),
                2: PinSpecification(
                    name="class_cross_section",
                    type_names=["bool"],
                    optional=False,
                    document="""Selection for a cross-section. true: class 1
        or 2 cross-sections. false: class 3
        cross section. if the user defines
        the cross section as class 1 or 2,
        the section modulus would be plastic
        section modulus. if it's class 3-
        cross section,the section modulus
        would be elastic section modulus""",
                ),
                3: PinSpecification(
                    name="streams",
                    type_names=["streams_container"],
                    optional=True,
                    document=""" result file container allowed to be kept
        open to cache data.""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=True,
                    document="""Result file path container, used if no
        streams are set.""",
                ),
                6: PinSpecification(
                    name="partial_factor",
                    type_names=["double"],
                    optional=False,
                    document="""Partial safety factor for resistance of
        members to instability assessed by
        member checks. default value: 1.""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document=""" mesh containing beam's properties defined by
        user""",
                ),
                8: PinSpecification(
                    name="bending_moment_y",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fields container of bending moment on axis y
        defined by user""",
                ),
                9: PinSpecification(
                    name="bending_moment_z",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fields container of bending moment on axis z
        defined by user""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="buckling_resistance_bending_yy",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fields container of buckling resistance
        factor on axis y-y in case of
        bending(m). these factors should be
        less than 1 and positive.""",
                ),
                1: PinSpecification(
                    name="buckling_resistance_bending_zz",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fields container of buckling resistance
        factor on axis z-z in case of
        bending(m). these factors should be
        less than 1 and positive.""",
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
            ``None``, attempts to use the the global server.
        """
        return Operator.default_config(
            name="members_in_bending_not_certified", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMembersInBendingNotCertified
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMembersInBendingNotCertified
        """
        return super().outputs


class InputsMembersInBendingNotCertified(_Inputs):
    """Intermediate class used to connect user inputs to
    members_in_bending_not_certified operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.members_in_bending_not_certified()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_field_yield_strength = dpf.Field()
    >>> op.inputs.field_yield_strength.connect(my_field_yield_strength)
    >>> my_class_cross_section = bool()
    >>> op.inputs.class_cross_section.connect(my_class_cross_section)
    >>> my_streams = dpf.StreamsContainer()
    >>> op.inputs.streams.connect(my_streams)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_partial_factor = float()
    >>> op.inputs.partial_factor.connect(my_partial_factor)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_bending_moment_y = dpf.FieldsContainer()
    >>> op.inputs.bending_moment_y.connect(my_bending_moment_y)
    >>> my_bending_moment_z = dpf.FieldsContainer()
    >>> op.inputs.bending_moment_z.connect(my_bending_moment_z)
    """

    def __init__(self, op: Operator):
        super().__init__(members_in_bending_not_certified._spec().inputs, op)
        self._time_scoping = Input(
            members_in_bending_not_certified._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._time_scoping)
        self._field_yield_strength = Input(
            members_in_bending_not_certified._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._field_yield_strength)
        self._class_cross_section = Input(
            members_in_bending_not_certified._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._class_cross_section)
        self._streams = Input(
            members_in_bending_not_certified._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams)
        self._data_sources = Input(
            members_in_bending_not_certified._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)
        self._partial_factor = Input(
            members_in_bending_not_certified._spec().input_pin(6), 6, op, -1
        )
        self._inputs.append(self._partial_factor)
        self._mesh = Input(
            members_in_bending_not_certified._spec().input_pin(7), 7, op, -1
        )
        self._inputs.append(self._mesh)
        self._bending_moment_y = Input(
            members_in_bending_not_certified._spec().input_pin(8), 8, op, -1
        )
        self._inputs.append(self._bending_moment_y)
        self._bending_moment_z = Input(
            members_in_bending_not_certified._spec().input_pin(9), 9, op, -1
        )
        self._inputs.append(self._bending_moment_z)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        Parameters
        ----------
        my_time_scoping : Scoping or int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.members_in_bending_not_certified()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def field_yield_strength(self):
        """Allows to connect field_yield_strength input to the operator.

        This pin contains field of beam's yield
        strength defined by the user.

        Parameters
        ----------
        my_field_yield_strength : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.members_in_bending_not_certified()
        >>> op.inputs.field_yield_strength.connect(my_field_yield_strength)
        >>> # or
        >>> op.inputs.field_yield_strength(my_field_yield_strength)
        """
        return self._field_yield_strength

    @property
    def class_cross_section(self):
        """Allows to connect class_cross_section input to the operator.

        Selection for a cross-section. true: class 1
        or 2 cross-sections. false: class 3
        cross section. if the user defines
        the cross section as class 1 or 2,
        the section modulus would be plastic
        section modulus. if it's class 3-
        cross section,the section modulus
        would be elastic section modulus

        Parameters
        ----------
        my_class_cross_section : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.members_in_bending_not_certified()
        >>> op.inputs.class_cross_section.connect(my_class_cross_section)
        >>> # or
        >>> op.inputs.class_cross_section(my_class_cross_section)
        """
        return self._class_cross_section

    @property
    def streams(self):
        """Allows to connect streams input to the operator.

         result file container allowed to be kept
        open to cache data.

        Parameters
        ----------
        my_streams : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.members_in_bending_not_certified()
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
        >>> op = dpf.operators.result.members_in_bending_not_certified()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def partial_factor(self):
        """Allows to connect partial_factor input to the operator.

        Partial safety factor for resistance of
        members to instability assessed by
        member checks. default value: 1.

        Parameters
        ----------
        my_partial_factor : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.members_in_bending_not_certified()
        >>> op.inputs.partial_factor.connect(my_partial_factor)
        >>> # or
        >>> op.inputs.partial_factor(my_partial_factor)
        """
        return self._partial_factor

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

         mesh containing beam's properties defined by
        user

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.members_in_bending_not_certified()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def bending_moment_y(self):
        """Allows to connect bending_moment_y input to the operator.

        Fields container of bending moment on axis y
        defined by user

        Parameters
        ----------
        my_bending_moment_y : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.members_in_bending_not_certified()
        >>> op.inputs.bending_moment_y.connect(my_bending_moment_y)
        >>> # or
        >>> op.inputs.bending_moment_y(my_bending_moment_y)
        """
        return self._bending_moment_y

    @property
    def bending_moment_z(self):
        """Allows to connect bending_moment_z input to the operator.

        Fields container of bending moment on axis z
        defined by user

        Parameters
        ----------
        my_bending_moment_z : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.members_in_bending_not_certified()
        >>> op.inputs.bending_moment_z.connect(my_bending_moment_z)
        >>> # or
        >>> op.inputs.bending_moment_z(my_bending_moment_z)
        """
        return self._bending_moment_z


class OutputsMembersInBendingNotCertified(_Outputs):
    """Intermediate class used to get outputs from
    members_in_bending_not_certified operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.members_in_bending_not_certified()
    >>> # Connect inputs : op.inputs. ...
    >>> result_buckling_resistance_bending_yy = op.outputs.buckling_resistance_bending_yy()
    >>> result_buckling_resistance_bending_zz = op.outputs.buckling_resistance_bending_zz()
    """

    def __init__(self, op: Operator):
        super().__init__(members_in_bending_not_certified._spec().outputs, op)
        self._buckling_resistance_bending_yy = Output(
            members_in_bending_not_certified._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._buckling_resistance_bending_yy)
        self._buckling_resistance_bending_zz = Output(
            members_in_bending_not_certified._spec().output_pin(1), 1, op
        )
        self._outputs.append(self._buckling_resistance_bending_zz)

    @property
    def buckling_resistance_bending_yy(self):
        """Allows to get buckling_resistance_bending_yy output of the operator

        Returns
        ----------
        my_buckling_resistance_bending_yy : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.members_in_bending_not_certified()
        >>> # Connect inputs : op.inputs. ...
        >>> result_buckling_resistance_bending_yy = op.outputs.buckling_resistance_bending_yy()
        """  # noqa: E501
        return self._buckling_resistance_bending_yy

    @property
    def buckling_resistance_bending_zz(self):
        """Allows to get buckling_resistance_bending_zz output of the operator

        Returns
        ----------
        my_buckling_resistance_bending_zz : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.members_in_bending_not_certified()
        >>> # Connect inputs : op.inputs. ...
        >>> result_buckling_resistance_bending_zz = op.outputs.buckling_resistance_bending_zz()
        """  # noqa: E501
        return self._buckling_resistance_bending_zz
