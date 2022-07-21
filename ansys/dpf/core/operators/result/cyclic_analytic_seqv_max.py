"""
cyclic_analytic_seqv_max
========================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class cyclic_analytic_seqv_max(Operator):
    """Compute the maximum of the Von Mises equivalent stress that can be
    expected on 360 degrees

    Parameters
    ----------
    time_scoping : Scoping, optional
    mesh_scoping : ScopingsContainer or Scoping, optional
    fields_container : FieldsContainer
        Field container with the base and duplicate
        sectors
    bool_rotate_to_global : bool, optional
        Default is true
    cyclic_support : CyclicSupport


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.cyclic_analytic_seqv_max()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_bool_rotate_to_global = bool()
    >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
    >>> my_cyclic_support = dpf.CyclicSupport()
    >>> op.inputs.cyclic_support.connect(my_cyclic_support)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.cyclic_analytic_seqv_max(
    ...     time_scoping=my_time_scoping,
    ...     mesh_scoping=my_mesh_scoping,
    ...     fields_container=my_fields_container,
    ...     bool_rotate_to_global=my_bool_rotate_to_global,
    ...     cyclic_support=my_cyclic_support,
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
        cyclic_support=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="cyclic_analytic_stress_eqv_max", config=config, server=server
        )
        self._inputs = InputsCyclicAnalyticSeqvMax(self)
        self._outputs = OutputsCyclicAnalyticSeqvMax(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if bool_rotate_to_global is not None:
            self.inputs.bool_rotate_to_global.connect(bool_rotate_to_global)
        if cyclic_support is not None:
            self.inputs.cyclic_support.connect(cyclic_support)

    @staticmethod
    def _spec():
        description = """Compute the maximum of the Von Mises equivalent stress that can be
            expected on 360 degrees"""
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
                16: PinSpecification(
                    name="cyclic_support",
                    type_names=["cyclic_support"],
                    optional=False,
                    document="""""",
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
        return Operator.default_config(
            name="cyclic_analytic_stress_eqv_max", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCyclicAnalyticSeqvMax
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCyclicAnalyticSeqvMax
        """
        return super().outputs


class InputsCyclicAnalyticSeqvMax(_Inputs):
    """Intermediate class used to connect user inputs to
    cyclic_analytic_seqv_max operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.cyclic_analytic_seqv_max()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.ScopingsContainer()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_bool_rotate_to_global = bool()
    >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
    >>> my_cyclic_support = dpf.CyclicSupport()
    >>> op.inputs.cyclic_support.connect(my_cyclic_support)
    """

    def __init__(self, op: Operator):
        super().__init__(cyclic_analytic_seqv_max._spec().inputs, op)
        self._time_scoping = Input(
            cyclic_analytic_seqv_max._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(
            cyclic_analytic_seqv_max._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._mesh_scoping)
        self._fields_container = Input(
            cyclic_analytic_seqv_max._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._fields_container)
        self._bool_rotate_to_global = Input(
            cyclic_analytic_seqv_max._spec().input_pin(5), 5, op, -1
        )
        self._inputs.append(self._bool_rotate_to_global)
        self._cyclic_support = Input(
            cyclic_analytic_seqv_max._spec().input_pin(16), 16, op, -1
        )
        self._inputs.append(self._cyclic_support)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        Parameters
        ----------
        my_time_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_analytic_seqv_max()
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
        >>> op = dpf.operators.result.cyclic_analytic_seqv_max()
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
        >>> op = dpf.operators.result.cyclic_analytic_seqv_max()
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
        >>> op = dpf.operators.result.cyclic_analytic_seqv_max()
        >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
        >>> # or
        >>> op.inputs.bool_rotate_to_global(my_bool_rotate_to_global)
        """
        return self._bool_rotate_to_global

    @property
    def cyclic_support(self):
        """Allows to connect cyclic_support input to the operator.

        Parameters
        ----------
        my_cyclic_support : CyclicSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cyclic_analytic_seqv_max()
        >>> op.inputs.cyclic_support.connect(my_cyclic_support)
        >>> # or
        >>> op.inputs.cyclic_support(my_cyclic_support)
        """
        return self._cyclic_support


class OutputsCyclicAnalyticSeqvMax(_Outputs):
    """Intermediate class used to get outputs from
    cyclic_analytic_seqv_max operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.cyclic_analytic_seqv_max()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(cyclic_analytic_seqv_max._spec().outputs, op)
        self._fields_container = Output(
            cyclic_analytic_seqv_max._spec().output_pin(0), 0, op
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
        >>> op = dpf.operators.result.cyclic_analytic_seqv_max()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
