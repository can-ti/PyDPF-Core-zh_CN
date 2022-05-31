"""
mesh_plan_clip
--------------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class mesh_plan_clip(Operator):
    """Clip a volume mesh along a plane, and keep one side.

    Parameters
    ----------
    mesh_or_field : MeshedRegion or Field
    normal : Field
        An overall 3d vector that gives normal
        direction of the plane.
    origin : Field
        An overall 3d vector that gives a point of
        the plane.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.mesh_plan_clip()

    >>> # Make input connections
    >>> my_mesh_or_field = dpf.MeshedRegion()
    >>> op.inputs.mesh_or_field.connect(my_mesh_or_field)
    >>> my_normal = dpf.Field()
    >>> op.inputs.normal.connect(my_normal)
    >>> my_origin = dpf.Field()
    >>> op.inputs.origin.connect(my_origin)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.mesh_plan_clip(
    ...     mesh_or_field=my_mesh_or_field,
    ...     normal=my_normal,
    ...     origin=my_origin,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    >>> result_mesh = op.outputs.mesh()
    """

    def __init__(
        self, mesh_or_field=None, normal=None, origin=None, config=None, server=None
    ):
        super().__init__(name="mesh_plan_clip", config=config, server=server)
        self._inputs = InputsMeshPlanClip(self)
        self._outputs = OutputsMeshPlanClip(self)
        if mesh_or_field is not None:
            self.inputs.mesh_or_field.connect(mesh_or_field)
        if normal is not None:
            self.inputs.normal.connect(normal)
        if origin is not None:
            self.inputs.origin.connect(origin)

    @staticmethod
    def _spec():
        description = """Clip a volume mesh along a plane, and keep one side."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="mesh_or_field",
                    type_names=["abstract_meshed_region", "field"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="normal",
                    type_names=["field"],
                    optional=False,
                    document="""An overall 3d vector that gives normal
        direction of the plane.""",
                ),
                2: PinSpecification(
                    name="origin",
                    type_names=["field"],
                    optional=False,
                    document="""An overall 3d vector that gives a point of
        the plane.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
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
        return Operator.default_config(name="mesh_plan_clip", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMeshPlanClip
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMeshPlanClip
        """
        return super().outputs


class InputsMeshPlanClip(_Inputs):
    """Intermediate class used to connect user inputs to
    mesh_plan_clip operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.mesh_plan_clip()
    >>> my_mesh_or_field = dpf.MeshedRegion()
    >>> op.inputs.mesh_or_field.connect(my_mesh_or_field)
    >>> my_normal = dpf.Field()
    >>> op.inputs.normal.connect(my_normal)
    >>> my_origin = dpf.Field()
    >>> op.inputs.origin.connect(my_origin)
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_plan_clip._spec().inputs, op)
        self._mesh_or_field = Input(mesh_plan_clip._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._mesh_or_field)
        self._normal = Input(mesh_plan_clip._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._normal)
        self._origin = Input(mesh_plan_clip._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._origin)

    @property
    def mesh_or_field(self):
        """Allows to connect mesh_or_field input to the operator.

        Parameters
        ----------
        my_mesh_or_field : MeshedRegion or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_plan_clip()
        >>> op.inputs.mesh_or_field.connect(my_mesh_or_field)
        >>> # or
        >>> op.inputs.mesh_or_field(my_mesh_or_field)
        """
        return self._mesh_or_field

    @property
    def normal(self):
        """Allows to connect normal input to the operator.

        An overall 3d vector that gives normal
        direction of the plane.

        Parameters
        ----------
        my_normal : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_plan_clip()
        >>> op.inputs.normal.connect(my_normal)
        >>> # or
        >>> op.inputs.normal(my_normal)
        """
        return self._normal

    @property
    def origin(self):
        """Allows to connect origin input to the operator.

        An overall 3d vector that gives a point of
        the plane.

        Parameters
        ----------
        my_origin : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_plan_clip()
        >>> op.inputs.origin.connect(my_origin)
        >>> # or
        >>> op.inputs.origin(my_origin)
        """
        return self._origin


class OutputsMeshPlanClip(_Outputs):
    """Intermediate class used to get outputs from
    mesh_plan_clip operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.mesh_plan_clip()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    >>> result_mesh = op.outputs.mesh()
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_plan_clip._spec().outputs, op)
        self._field = Output(mesh_plan_clip._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)
        self._mesh = Output(mesh_plan_clip._spec().output_pin(2), 2, op)
        self._outputs.append(self._mesh)

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_plan_clip()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field

    @property
    def mesh(self):
        """Allows to get mesh output of the operator

        Returns
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_plan_clip()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh()
        """  # noqa: E501
        return self._mesh
