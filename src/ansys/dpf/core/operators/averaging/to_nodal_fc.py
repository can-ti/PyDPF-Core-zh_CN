"""
to_nodal_fc
===========
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class to_nodal_fc(Operator):
    """Transforms fields into Nodal fields using an averaging process. The
    result is computed on a given node's scoping.

    Parameters
    ----------
    fields_container : FieldsContainer
    mesh : MeshedRegion, optional
    mesh_scoping : Scoping, optional
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
    >>> op = dpf.operators.averaging.to_nodal_fc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_merge_solid_shell = bool()
    >>> op.inputs.merge_solid_shell.connect(my_merge_solid_shell)
    >>> my_shell_layer = int()
    >>> op.inputs.shell_layer.connect(my_shell_layer)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.averaging.to_nodal_fc(
    ...     fields_container=my_fields_container,
    ...     mesh=my_mesh,
    ...     mesh_scoping=my_mesh_scoping,
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
        mesh_scoping=None,
        merge_solid_shell=None,
        shell_layer=None,
        config=None,
        server=None,
    ):
        super().__init__(name="to_nodal_fc", config=config, server=server)
        self._inputs = InputsToNodalFc(self)
        self._outputs = OutputsToNodalFc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if merge_solid_shell is not None:
            self.inputs.merge_solid_shell.connect(merge_solid_shell)
        if shell_layer is not None:
            self.inputs.shell_layer.connect(shell_layer)

    @staticmethod
    def _spec():
        description = """Transforms fields into Nodal fields using an averaging process. The
            result is computed on a given node's scoping."""
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
                    type_names=["abstract_meshed_region"],
                    optional=True,
                    document="""""",
                ),
                3: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""""",
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
        return Operator.default_config(name="to_nodal_fc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsToNodalFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsToNodalFc
        """
        return super().outputs


class InputsToNodalFc(_Inputs):
    """Intermediate class used to connect user inputs to
    to_nodal_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.averaging.to_nodal_fc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_merge_solid_shell = bool()
    >>> op.inputs.merge_solid_shell.connect(my_merge_solid_shell)
    >>> my_shell_layer = int()
    >>> op.inputs.shell_layer.connect(my_shell_layer)
    """

    def __init__(self, op: Operator):
        super().__init__(to_nodal_fc._spec().inputs, op)
        self._fields_container = Input(to_nodal_fc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fields_container)
        self._mesh = Input(to_nodal_fc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh)
        self._mesh_scoping = Input(to_nodal_fc._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._merge_solid_shell = Input(to_nodal_fc._spec().input_pin(26), 26, op, -1)
        self._inputs.append(self._merge_solid_shell)
        self._shell_layer = Input(to_nodal_fc._spec().input_pin(27), 27, op, -1)
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
        >>> op = dpf.operators.averaging.to_nodal_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.to_nodal_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Parameters
        ----------
        my_mesh_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.to_nodal_fc()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

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
        >>> op = dpf.operators.averaging.to_nodal_fc()
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
        >>> op = dpf.operators.averaging.to_nodal_fc()
        >>> op.inputs.shell_layer.connect(my_shell_layer)
        >>> # or
        >>> op.inputs.shell_layer(my_shell_layer)
        """
        return self._shell_layer


class OutputsToNodalFc(_Outputs):
    """Intermediate class used to get outputs from
    to_nodal_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.averaging.to_nodal_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(to_nodal_fc._spec().outputs, op)
        self._fields_container = Output(to_nodal_fc._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.averaging.to_nodal_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
