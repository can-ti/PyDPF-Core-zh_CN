"""
split_fields
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class split_fields(Operator):
    """Split the input field or fields container based on the input mesh
    regions

    Parameters
    ----------
    field_or_fields_container : Field or FieldsContainer
    mesh_controller : MeshesContainer
        Body meshes in the mesh controller cannot be
        mixed shell/solid


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.split_fields()

    >>> # Make input connections
    >>> my_field_or_fields_container = dpf.Field()
    >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
    >>> my_mesh_controller = dpf.MeshesContainer()
    >>> op.inputs.mesh_controller.connect(my_mesh_controller)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.split_fields(
    ...     field_or_fields_container=my_field_or_fields_container,
    ...     mesh_controller=my_mesh_controller,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        field_or_fields_container=None,
        mesh_controller=None,
        config=None,
        server=None,
    ):
        super().__init__(name="split_fields", config=config, server=server)
        self._inputs = InputsSplitFields(self)
        self._outputs = OutputsSplitFields(self)
        if field_or_fields_container is not None:
            self.inputs.field_or_fields_container.connect(field_or_fields_container)
        if mesh_controller is not None:
            self.inputs.mesh_controller.connect(mesh_controller)

    @staticmethod
    def _spec():
        description = """Split the input field or fields container based on the input mesh
            regions"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field_or_fields_container",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="mesh_controller",
                    type_names=["meshes_container"],
                    optional=False,
                    document="""Body meshes in the mesh controller cannot be
        mixed shell/solid""",
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
            ``None``, attempts to use the the global server.
        """
        return Operator.default_config(name="split_fields", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSplitFields
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSplitFields
        """
        return super().outputs


class InputsSplitFields(_Inputs):
    """Intermediate class used to connect user inputs to
    split_fields operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.split_fields()
    >>> my_field_or_fields_container = dpf.Field()
    >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
    >>> my_mesh_controller = dpf.MeshesContainer()
    >>> op.inputs.mesh_controller.connect(my_mesh_controller)
    """

    def __init__(self, op: Operator):
        super().__init__(split_fields._spec().inputs, op)
        self._field_or_fields_container = Input(
            split_fields._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._field_or_fields_container)
        self._mesh_controller = Input(split_fields._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_controller)

    @property
    def field_or_fields_container(self):
        """Allows to connect field_or_fields_container input to the operator.

        Parameters
        ----------
        my_field_or_fields_container : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.split_fields()
        >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
        >>> # or
        >>> op.inputs.field_or_fields_container(my_field_or_fields_container)
        """
        return self._field_or_fields_container

    @property
    def mesh_controller(self):
        """Allows to connect mesh_controller input to the operator.

        Body meshes in the mesh controller cannot be
        mixed shell/solid

        Parameters
        ----------
        my_mesh_controller : MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.split_fields()
        >>> op.inputs.mesh_controller.connect(my_mesh_controller)
        >>> # or
        >>> op.inputs.mesh_controller(my_mesh_controller)
        """
        return self._mesh_controller


class OutputsSplitFields(_Outputs):
    """Intermediate class used to get outputs from
    split_fields operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.split_fields()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(split_fields._spec().outputs, op)
        self._fields_container = Output(split_fields._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.mesh.split_fields()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
