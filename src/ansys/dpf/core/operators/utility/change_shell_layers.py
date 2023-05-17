"""
change_shell_layers
===================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.outputs import _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class change_shell_layers(Operator):
    """Extract the expected shell layers from the input fields, if the fields
    contain only one layer then it returns the input fields

    Parameters
    ----------
    fields_container : FieldsContainer or Field
    e_shell_layer : int
        0:top, 1: bottom, 2: bottomtop, 3:mid,
        4:bottomtopmid
    mesh : MeshedRegion or MeshesContainer, optional
        Mesh support of the input fields_container,
        in case it does not have one defined.
        if the fields_container contains
        mixed shell/solid results, the mesh
        is required (either by connecting
        this pin or in the support).


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.change_shell_layers()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_e_shell_layer = int()
    >>> op.inputs.e_shell_layer.connect(my_e_shell_layer)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.change_shell_layers(
    ...     fields_container=my_fields_container,
    ...     e_shell_layer=my_e_shell_layer,
    ...     mesh=my_mesh,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_container=None,
        e_shell_layer=None,
        mesh=None,
        config=None,
        server=None,
    ):
        super().__init__(name="change_shellLayers", config=config, server=server)
        self._inputs = InputsChangeShellLayers(self)
        self._outputs = OutputsChangeShellLayers(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if e_shell_layer is not None:
            self.inputs.e_shell_layer.connect(e_shell_layer)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        description = """Extract the expected shell layers from the input fields, if the fields
            contain only one layer then it returns the input fields"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container", "field"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="e_shell_layer",
                    type_names=["int32", "enum dataProcessing::EShellLayers"],
                    optional=False,
                    document="""0:top, 1: bottom, 2: bottomtop, 3:mid,
        4:bottomtopmid""",
                ),
                2: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document="""Mesh support of the input fields_container,
        in case it does not have one defined.
        if the fields_container contains
        mixed shell/solid results, the mesh
        is required (either by connecting
        this pin or in the support).""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container", "field"],
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
        return Operator.default_config(name="change_shellLayers", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsChangeShellLayers
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsChangeShellLayers
        """
        return super().outputs


class InputsChangeShellLayers(_Inputs):
    """Intermediate class used to connect user inputs to
    change_shell_layers operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.change_shell_layers()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_e_shell_layer = int()
    >>> op.inputs.e_shell_layer.connect(my_e_shell_layer)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    """

    def __init__(self, op: Operator):
        super().__init__(change_shell_layers._spec().inputs, op)
        self._fields_container = Input(
            change_shell_layers._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._e_shell_layer = Input(change_shell_layers._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._e_shell_layer)
        self._mesh = Input(change_shell_layers._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._mesh)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.change_shell_layers()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def e_shell_layer(self):
        """Allows to connect e_shell_layer input to the operator.

        0:top, 1: bottom, 2: bottomtop, 3:mid,
        4:bottomtopmid

        Parameters
        ----------
        my_e_shell_layer : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.change_shell_layers()
        >>> op.inputs.e_shell_layer.connect(my_e_shell_layer)
        >>> # or
        >>> op.inputs.e_shell_layer(my_e_shell_layer)
        """
        return self._e_shell_layer

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Mesh support of the input fields_container,
        in case it does not have one defined.
        if the fields_container contains
        mixed shell/solid results, the mesh
        is required (either by connecting
        this pin or in the support).

        Parameters
        ----------
        my_mesh : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.change_shell_layers()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh


class OutputsChangeShellLayers(_Outputs):
    """Intermediate class used to get outputs from
    change_shell_layers operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.change_shell_layers()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(change_shell_layers._spec().outputs, op)
        self.fields_container_as_fields_container = Output(
            _modify_output_spec_with_one_type(
                change_shell_layers._spec().output_pin(0), "fields_container"
            ),
            0,
            op,
        )
        self._outputs.append(self.fields_container_as_fields_container)
        self.fields_container_as_field = Output(
            _modify_output_spec_with_one_type(
                change_shell_layers._spec().output_pin(0), "field"
            ),
            0,
            op,
        )
        self._outputs.append(self.fields_container_as_field)
