"""
to_nodal
========
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class to_nodal(Operator):
    """Transforms a field into a Nodal field using an averaging process. The
    result is computed on a given node's scoping.

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container with only one field
        is expected
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
    >>> op = dpf.operators.averaging.to_nodal()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_merge_solid_shell = bool()
    >>> op.inputs.merge_solid_shell.connect(my_merge_solid_shell)
    >>> my_shell_layer = int()
    >>> op.inputs.shell_layer.connect(my_shell_layer)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.averaging.to_nodal(
    ...     field=my_field,
    ...     mesh_scoping=my_mesh_scoping,
    ...     merge_solid_shell=my_merge_solid_shell,
    ...     shell_layer=my_shell_layer,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        field=None,
        mesh_scoping=None,
        merge_solid_shell=None,
        shell_layer=None,
        config=None,
        server=None,
    ):
        super().__init__(name="to_nodal", config=config, server=server)
        self._inputs = InputsToNodal(self)
        self._outputs = OutputsToNodal(self)
        if field is not None:
            self.inputs.field.connect(field)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if merge_solid_shell is not None:
            self.inputs.merge_solid_shell.connect(merge_solid_shell)
        if shell_layer is not None:
            self.inputs.shell_layer.connect(shell_layer)

    @staticmethod
    def _spec():
        description = """Transforms a field into a Nodal field using an averaging process. The
            result is computed on a given node's scoping."""
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
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="to_nodal", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsToNodal
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsToNodal
        """
        return super().outputs


class InputsToNodal(_Inputs):
    """Intermediate class used to connect user inputs to
    to_nodal operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.averaging.to_nodal()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_merge_solid_shell = bool()
    >>> op.inputs.merge_solid_shell.connect(my_merge_solid_shell)
    >>> my_shell_layer = int()
    >>> op.inputs.shell_layer.connect(my_shell_layer)
    """

    def __init__(self, op: Operator):
        super().__init__(to_nodal._spec().inputs, op)
        self._field = Input(to_nodal._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._mesh_scoping = Input(to_nodal._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._merge_solid_shell = Input(to_nodal._spec().input_pin(26), 26, op, -1)
        self._inputs.append(self._merge_solid_shell)
        self._shell_layer = Input(to_nodal._spec().input_pin(27), 27, op, -1)
        self._inputs.append(self._shell_layer)

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
        >>> op = dpf.operators.averaging.to_nodal()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Parameters
        ----------
        my_mesh_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.to_nodal()
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
        >>> op = dpf.operators.averaging.to_nodal()
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
        >>> op = dpf.operators.averaging.to_nodal()
        >>> op.inputs.shell_layer.connect(my_shell_layer)
        >>> # or
        >>> op.inputs.shell_layer(my_shell_layer)
        """
        return self._shell_layer


class OutputsToNodal(_Outputs):
    """Intermediate class used to get outputs from
    to_nodal operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.averaging.to_nodal()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(to_nodal._spec().outputs, op)
        self._field = Output(to_nodal._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.averaging.to_nodal()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
