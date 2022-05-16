"""
euler_load_buckling
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class euler_load_buckling(Operator):
    """Computing Euler's Critical Load. Formula: Ncr = n*E*I*pi*pi /(L*L)

    Parameters
    ----------
    field_beam_end_condition : DataSources or Field
         this pin contains file csv or field of
        beam's end condition added by the
        user. if there's no file added, it
        would take value of all beam's end
        condition as 1.
    field_beam_moment_inertia : Field
        Field of beam's moment inertia
    field_beam_young_modulus : Field
        Field of beam's young modulus
    field_beam_length : Field
        Field of beam's length


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.euler_load_buckling()

    >>> # Make input connections
    >>> my_field_beam_end_condition = dpf.DataSources()
    >>> op.inputs.field_beam_end_condition.connect(my_field_beam_end_condition)
    >>> my_field_beam_moment_inertia = dpf.Field()
    >>> op.inputs.field_beam_moment_inertia.connect(my_field_beam_moment_inertia)
    >>> my_field_beam_young_modulus = dpf.Field()
    >>> op.inputs.field_beam_young_modulus.connect(my_field_beam_young_modulus)
    >>> my_field_beam_length = dpf.Field()
    >>> op.inputs.field_beam_length.connect(my_field_beam_length)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.euler_load_buckling(
    ...     field_beam_end_condition=my_field_beam_end_condition,
    ...     field_beam_moment_inertia=my_field_beam_moment_inertia,
    ...     field_beam_young_modulus=my_field_beam_young_modulus,
    ...     field_beam_length=my_field_beam_length,
    ... )

    >>> # Get output data
    >>> result_field_euler_critical_load = op.outputs.field_euler_critical_load()
    >>> result_field_euler_critical_load_yy = op.outputs.field_euler_critical_load_yy()
    >>> result_field_euler_critical_load_zz = op.outputs.field_euler_critical_load_zz()
    """

    def __init__(
        self,
        field_beam_end_condition=None,
        field_beam_moment_inertia=None,
        field_beam_young_modulus=None,
        field_beam_length=None,
        config=None,
        server=None,
    ):
        super().__init__(name="euler_load_buckling", config=config, server=server)
        self._inputs = InputsEulerLoadBuckling(self)
        self._outputs = OutputsEulerLoadBuckling(self)
        if field_beam_end_condition is not None:
            self.inputs.field_beam_end_condition.connect(field_beam_end_condition)
        if field_beam_moment_inertia is not None:
            self.inputs.field_beam_moment_inertia.connect(field_beam_moment_inertia)
        if field_beam_young_modulus is not None:
            self.inputs.field_beam_young_modulus.connect(field_beam_young_modulus)
        if field_beam_length is not None:
            self.inputs.field_beam_length.connect(field_beam_length)

    @staticmethod
    def _spec():
        description = (
            """Computing Euler's Critical Load. Formula: Ncr = n*E*I*pi*pi /(L*L)"""
        )
        spec = Specification(
            description=description,
            map_input_pin_spec={
                5: PinSpecification(
                    name="field_beam_end_condition",
                    type_names=["data_sources", "field"],
                    optional=False,
                    document=""" this pin contains file csv or field of
        beam's end condition added by the
        user. if there's no file added, it
        would take value of all beam's end
        condition as 1.""",
                ),
                6: PinSpecification(
                    name="field_beam_moment_inertia",
                    type_names=["field"],
                    optional=False,
                    document="""Field of beam's moment inertia""",
                ),
                7: PinSpecification(
                    name="field_beam_young_modulus",
                    type_names=["field"],
                    optional=False,
                    document="""Field of beam's young modulus""",
                ),
                8: PinSpecification(
                    name="field_beam_length",
                    type_names=["field"],
                    optional=False,
                    document="""Field of beam's length""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field_euler_critical_load",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains euler's critical load
        about the principle axis of the cross
        section having the least moment of
        inertia.""",
                ),
                1: PinSpecification(
                    name="field_euler_critical_load_yy",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains euler's critical load on
        axis y.""",
                ),
                2: PinSpecification(
                    name="field_euler_critical_load_zz",
                    type_names=["field"],
                    optional=False,
                    document="""This field contains euler's critical load on
        axis z.""",
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
        return Operator.default_config(name="euler_load_buckling", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsEulerLoadBuckling
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsEulerLoadBuckling
        """
        return super().outputs


class InputsEulerLoadBuckling(_Inputs):
    """Intermediate class used to connect user inputs to
    euler_load_buckling operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.euler_load_buckling()
    >>> my_field_beam_end_condition = dpf.DataSources()
    >>> op.inputs.field_beam_end_condition.connect(my_field_beam_end_condition)
    >>> my_field_beam_moment_inertia = dpf.Field()
    >>> op.inputs.field_beam_moment_inertia.connect(my_field_beam_moment_inertia)
    >>> my_field_beam_young_modulus = dpf.Field()
    >>> op.inputs.field_beam_young_modulus.connect(my_field_beam_young_modulus)
    >>> my_field_beam_length = dpf.Field()
    >>> op.inputs.field_beam_length.connect(my_field_beam_length)
    """

    def __init__(self, op: Operator):
        super().__init__(euler_load_buckling._spec().inputs, op)
        self._field_beam_end_condition = Input(
            euler_load_buckling._spec().input_pin(5), 5, op, -1
        )
        self._inputs.append(self._field_beam_end_condition)
        self._field_beam_moment_inertia = Input(
            euler_load_buckling._spec().input_pin(6), 6, op, -1
        )
        self._inputs.append(self._field_beam_moment_inertia)
        self._field_beam_young_modulus = Input(
            euler_load_buckling._spec().input_pin(7), 7, op, -1
        )
        self._inputs.append(self._field_beam_young_modulus)
        self._field_beam_length = Input(
            euler_load_buckling._spec().input_pin(8), 8, op, -1
        )
        self._inputs.append(self._field_beam_length)

    @property
    def field_beam_end_condition(self):
        """Allows to connect field_beam_end_condition input to the operator.

         this pin contains file csv or field of
        beam's end condition added by the
        user. if there's no file added, it
        would take value of all beam's end
        condition as 1.

        Parameters
        ----------
        my_field_beam_end_condition : DataSources or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_load_buckling()
        >>> op.inputs.field_beam_end_condition.connect(my_field_beam_end_condition)
        >>> # or
        >>> op.inputs.field_beam_end_condition(my_field_beam_end_condition)
        """
        return self._field_beam_end_condition

    @property
    def field_beam_moment_inertia(self):
        """Allows to connect field_beam_moment_inertia input to the operator.

        Field of beam's moment inertia

        Parameters
        ----------
        my_field_beam_moment_inertia : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_load_buckling()
        >>> op.inputs.field_beam_moment_inertia.connect(my_field_beam_moment_inertia)
        >>> # or
        >>> op.inputs.field_beam_moment_inertia(my_field_beam_moment_inertia)
        """
        return self._field_beam_moment_inertia

    @property
    def field_beam_young_modulus(self):
        """Allows to connect field_beam_young_modulus input to the operator.

        Field of beam's young modulus

        Parameters
        ----------
        my_field_beam_young_modulus : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_load_buckling()
        >>> op.inputs.field_beam_young_modulus.connect(my_field_beam_young_modulus)
        >>> # or
        >>> op.inputs.field_beam_young_modulus(my_field_beam_young_modulus)
        """
        return self._field_beam_young_modulus

    @property
    def field_beam_length(self):
        """Allows to connect field_beam_length input to the operator.

        Field of beam's length

        Parameters
        ----------
        my_field_beam_length : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_load_buckling()
        >>> op.inputs.field_beam_length.connect(my_field_beam_length)
        >>> # or
        >>> op.inputs.field_beam_length(my_field_beam_length)
        """
        return self._field_beam_length


class OutputsEulerLoadBuckling(_Outputs):
    """Intermediate class used to get outputs from
    euler_load_buckling operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.euler_load_buckling()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field_euler_critical_load = op.outputs.field_euler_critical_load()
    >>> result_field_euler_critical_load_yy = op.outputs.field_euler_critical_load_yy()
    >>> result_field_euler_critical_load_zz = op.outputs.field_euler_critical_load_zz()
    """

    def __init__(self, op: Operator):
        super().__init__(euler_load_buckling._spec().outputs, op)
        self._field_euler_critical_load = Output(
            euler_load_buckling._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._field_euler_critical_load)
        self._field_euler_critical_load_yy = Output(
            euler_load_buckling._spec().output_pin(1), 1, op
        )
        self._outputs.append(self._field_euler_critical_load_yy)
        self._field_euler_critical_load_zz = Output(
            euler_load_buckling._spec().output_pin(2), 2, op
        )
        self._outputs.append(self._field_euler_critical_load_zz)

    @property
    def field_euler_critical_load(self):
        """Allows to get field_euler_critical_load output of the operator

        Returns
        ----------
        my_field_euler_critical_load : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_load_buckling()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_euler_critical_load = op.outputs.field_euler_critical_load()
        """  # noqa: E501
        return self._field_euler_critical_load

    @property
    def field_euler_critical_load_yy(self):
        """Allows to get field_euler_critical_load_yy output of the operator

        Returns
        ----------
        my_field_euler_critical_load_yy : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_load_buckling()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_euler_critical_load_yy = op.outputs.field_euler_critical_load_yy()
        """  # noqa: E501
        return self._field_euler_critical_load_yy

    @property
    def field_euler_critical_load_zz(self):
        """Allows to get field_euler_critical_load_zz output of the operator

        Returns
        ----------
        my_field_euler_critical_load_zz : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_load_buckling()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_euler_critical_load_zz = op.outputs.field_euler_critical_load_zz()
        """  # noqa: E501
        return self._field_euler_critical_load_zz
