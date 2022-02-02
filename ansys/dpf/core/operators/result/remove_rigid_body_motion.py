"""
remove_rigid_body_motion
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class remove_rigid_body_motion(Operator):
    """Removes rigid body mode from a total displacement field by
    minimization. Use a reference point in order to substract its
    displacement to the result displacement field.

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container with only one field
        is expected
    reference_node_id : int, optional
        Id of the reference entity (node).
    mesh : MeshedRegion, optional
        Default is the mesh in the support


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.remove_rigid_body_motion()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_reference_node_id = int()
    >>> op.inputs.reference_node_id.connect(my_reference_node_id)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.remove_rigid_body_motion(
    ...     field=my_field,
    ...     reference_node_id=my_reference_node_id,
    ...     mesh=my_mesh,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self, field=None, reference_node_id=None, mesh=None, config=None, server=None
    ):
        super().__init__(name="ExtractRigidBodyMotion", config=config, server=server)
        self._inputs = InputsRemoveRigidBodyMotion(self)
        self._outputs = OutputsRemoveRigidBodyMotion(self)
        if field is not None:
            self.inputs.field.connect(field)
        if reference_node_id is not None:
            self.inputs.reference_node_id.connect(reference_node_id)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        description = """Removes rigid body mode from a total displacement field by
            minimization. Use a reference point in order to substract
            its displacement to the result displacement field."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
                ),
                1: PinSpecification(
                    name="reference_node_id",
                    type_names=["int32"],
                    optional=True,
                    document="""Id of the reference entity (node).""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=True,
                    document="""Default is the mesh in the support""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
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
            ``None``, attempts to use the the global server.
        """
        return Operator.default_config(name="ExtractRigidBodyMotion", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRemoveRigidBodyMotion
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRemoveRigidBodyMotion
        """
        return super().outputs


class InputsRemoveRigidBodyMotion(_Inputs):
    """Intermediate class used to connect user inputs to
    remove_rigid_body_motion operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.remove_rigid_body_motion()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_reference_node_id = int()
    >>> op.inputs.reference_node_id.connect(my_reference_node_id)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    """

    def __init__(self, op: Operator):
        super().__init__(remove_rigid_body_motion._spec().inputs, op)
        self._field = Input(remove_rigid_body_motion._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._reference_node_id = Input(
            remove_rigid_body_motion._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._reference_node_id)
        self._mesh = Input(remove_rigid_body_motion._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_field : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.remove_rigid_body_motion()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def reference_node_id(self):
        """Allows to connect reference_node_id input to the operator.

        Id of the reference entity (node).

        Parameters
        ----------
        my_reference_node_id : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.remove_rigid_body_motion()
        >>> op.inputs.reference_node_id.connect(my_reference_node_id)
        >>> # or
        >>> op.inputs.reference_node_id(my_reference_node_id)
        """
        return self._reference_node_id

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Default is the mesh in the support

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.remove_rigid_body_motion()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh


class OutputsRemoveRigidBodyMotion(_Outputs):
    """Intermediate class used to get outputs from
    remove_rigid_body_motion operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.remove_rigid_body_motion()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(remove_rigid_body_motion._spec().outputs, op)
        self._field = Output(remove_rigid_body_motion._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.remove_rigid_body_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
