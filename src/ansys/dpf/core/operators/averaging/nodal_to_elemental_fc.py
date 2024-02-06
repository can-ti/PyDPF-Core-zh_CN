"""
nodal_to_elemental_fc
=====================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class nodal_to_elemental_fc(Operator):
    """Transforms Nodal fields into Elemental fields using an averaging
    process. The result is computed on a given element's scoping. If
    the input fields are mixed shell/solid, and the shell's layers are
    not specified as collapsed, then the fields are split by element
    shape and the output fields container has an elshape label.

    Parameters
    ----------
    fields_container : FieldsContainer
    mesh : MeshedRegion or MeshesContainer, optional
        The mesh region in this pin is used to
        perform the averaging. it is used if
        there is no fields support.
    scoping : Scoping or ScopingsContainer, optional
        Average only on these elements. if it is a
        scoping container, the label must
        correspond to the one of the fields
        containers.
    collapse_shell_layers : bool, optional
        If true, shell layers are averaged as well
        (default is false).
    merge_solid_shell : bool, optional
        For shell/solid mixed field, gather in one
        field all solids and shells (only on
        one layer, false by default).
    shell_layer : int, optional
        If merge_solid_shell pin set to true, user
        have to choose a shell layer. for
        shell/solid mixed field, gather in
        one field all solids and shells (only
        on one layer).


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.averaging.nodal_to_elemental_fc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_collapse_shell_layers = bool()
    >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
    >>> my_merge_solid_shell = bool()
    >>> op.inputs.merge_solid_shell.connect(my_merge_solid_shell)
    >>> my_shell_layer = int()
    >>> op.inputs.shell_layer.connect(my_shell_layer)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.averaging.nodal_to_elemental_fc(
    ...     fields_container=my_fields_container,
    ...     mesh=my_mesh,
    ...     scoping=my_scoping,
    ...     collapse_shell_layers=my_collapse_shell_layers,
    ...     merge_solid_shell=my_merge_solid_shell,
    ...     shell_layer=my_shell_layer,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_container=None,
        mesh=None,
        scoping=None,
        collapse_shell_layers=None,
        merge_solid_shell=None,
        shell_layer=None,
        config=None,
        server=None,
    ):
        super().__init__(name="nodal_to_elemental_fc", config=config, server=server)
        self._inputs = InputsNodalToElementalFc(self)
        self._outputs = OutputsNodalToElementalFc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if scoping is not None:
            self.inputs.scoping.connect(scoping)
        if collapse_shell_layers is not None:
            self.inputs.collapse_shell_layers.connect(collapse_shell_layers)
        if merge_solid_shell is not None:
            self.inputs.merge_solid_shell.connect(merge_solid_shell)
        if shell_layer is not None:
            self.inputs.shell_layer.connect(shell_layer)

    @staticmethod
    def _spec():
        description = """Transforms Nodal fields into Elemental fields using an averaging
            process. The result is computed on a given element's
            scoping. If the input fields are mixed shell/solid, and
            the shell's layers are not specified as collapsed, then
            the fields are split by element shape and the output
            fields container has an elshape label."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document="""The mesh region in this pin is used to
        perform the averaging. it is used if
        there is no fields support.""",
                ),
                3: PinSpecification(
                    name="scoping",
                    type_names=["scoping", "scopings_container"],
                    optional=True,
                    document="""Average only on these elements. if it is a
        scoping container, the label must
        correspond to the one of the fields
        containers.""",
                ),
                10: PinSpecification(
                    name="collapse_shell_layers",
                    type_names=["bool"],
                    optional=True,
                    document="""If true, shell layers are averaged as well
        (default is false).""",
                ),
                26: PinSpecification(
                    name="merge_solid_shell",
                    type_names=["bool"],
                    optional=True,
                    document="""For shell/solid mixed field, gather in one
        field all solids and shells (only on
        one layer, false by default).""",
                ),
                27: PinSpecification(
                    name="shell_layer",
                    type_names=["int32"],
                    optional=True,
                    document="""If merge_solid_shell pin set to true, user
        have to choose a shell layer. for
        shell/solid mixed field, gather in
        one field all solids and shells (only
        on one layer).""",
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
        return Operator.default_config(name="nodal_to_elemental_fc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNodalToElementalFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsNodalToElementalFc
        """
        return super().outputs


class InputsNodalToElementalFc(_Inputs):
    """Intermediate class used to connect user inputs to
    nodal_to_elemental_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_collapse_shell_layers = bool()
    >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
    >>> my_merge_solid_shell = bool()
    >>> op.inputs.merge_solid_shell.connect(my_merge_solid_shell)
    >>> my_shell_layer = int()
    >>> op.inputs.shell_layer.connect(my_shell_layer)
    """

    def __init__(self, op: Operator):
        super().__init__(nodal_to_elemental_fc._spec().inputs, op)
        self._fields_container = Input(
            nodal_to_elemental_fc._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._mesh = Input(nodal_to_elemental_fc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh)
        self._scoping = Input(nodal_to_elemental_fc._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._scoping)
        self._collapse_shell_layers = Input(
            nodal_to_elemental_fc._spec().input_pin(10), 10, op, -1
        )
        self._inputs.append(self._collapse_shell_layers)
        self._merge_solid_shell = Input(
            nodal_to_elemental_fc._spec().input_pin(26), 26, op, -1
        )
        self._inputs.append(self._merge_solid_shell)
        self._shell_layer = Input(
            nodal_to_elemental_fc._spec().input_pin(27), 27, op, -1
        )
        self._inputs.append(self._shell_layer)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        The mesh region in this pin is used to
        perform the averaging. it is used if
        there is no fields support.

        Parameters
        ----------
        my_mesh : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator.

        Average only on these elements. if it is a
        scoping container, the label must
        correspond to the one of the fields
        containers.

        Parameters
        ----------
        my_scoping : Scoping or ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> # or
        >>> op.inputs.scoping(my_scoping)
        """
        return self._scoping

    @property
    def collapse_shell_layers(self):
        """Allows to connect collapse_shell_layers input to the operator.

        If true, shell layers are averaged as well
        (default is false).

        Parameters
        ----------
        my_collapse_shell_layers : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> op.inputs.collapse_shell_layers.connect(my_collapse_shell_layers)
        >>> # or
        >>> op.inputs.collapse_shell_layers(my_collapse_shell_layers)
        """
        return self._collapse_shell_layers

    @property
    def merge_solid_shell(self):
        """Allows to connect merge_solid_shell input to the operator.

        For shell/solid mixed field, gather in one
        field all solids and shells (only on
        one layer, false by default).

        Parameters
        ----------
        my_merge_solid_shell : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> op.inputs.merge_solid_shell.connect(my_merge_solid_shell)
        >>> # or
        >>> op.inputs.merge_solid_shell(my_merge_solid_shell)
        """
        return self._merge_solid_shell

    @property
    def shell_layer(self):
        """Allows to connect shell_layer input to the operator.

        If merge_solid_shell pin set to true, user
        have to choose a shell layer. for
        shell/solid mixed field, gather in
        one field all solids and shells (only
        on one layer).

        Parameters
        ----------
        my_shell_layer : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> op.inputs.shell_layer.connect(my_shell_layer)
        >>> # or
        >>> op.inputs.shell_layer(my_shell_layer)
        """
        return self._shell_layer


class OutputsNodalToElementalFc(_Outputs):
    """Intermediate class used to get outputs from
    nodal_to_elemental_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(nodal_to_elemental_fc._spec().outputs, op)
        self._fields_container = Output(
            nodal_to_elemental_fc._spec().output_pin(0), 0, op
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
        >>> op = dpf.operators.averaging.nodal_to_elemental_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
