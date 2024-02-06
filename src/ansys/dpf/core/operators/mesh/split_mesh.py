"""
split_mesh
==========
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class split_mesh(Operator):
    """Split the input mesh into several meshes based on a given property
    (material property be default)

    Parameters
    ----------
    mesh_scoping : Scoping, optional
        Scoping
    mesh : MeshedRegion
    property : str


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.split_mesh()

    >>> # Make input connections
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_property = str()
    >>> op.inputs.property.connect(my_property)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.split_mesh(
    ...     mesh_scoping=my_mesh_scoping,
    ...     mesh=my_mesh,
    ...     property=my_property,
    ... )

    >>> # Get output data
    >>> result_meshes = op.outputs.meshes()
    """

    def __init__(
        self, mesh_scoping=None, mesh=None, property=None, config=None, server=None
    ):
        super().__init__(name="split_mesh", config=config, server=server)
        self._inputs = InputsSplitMesh(self)
        self._outputs = OutputsSplitMesh(self)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if property is not None:
            self.inputs.property.connect(property)

    @staticmethod
    def _spec():
        description = """Split the input mesh into several meshes based on a given property
            (material property be default)"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""Scoping""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""""",
                ),
                13: PinSpecification(
                    name="property",
                    type_names=["string"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="meshes",
                    type_names=["meshes_container"],
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
        return Operator.default_config(name="split_mesh", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSplitMesh
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsSplitMesh
        """
        return super().outputs


class InputsSplitMesh(_Inputs):
    """Intermediate class used to connect user inputs to
    split_mesh operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.split_mesh()
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_property = str()
    >>> op.inputs.property.connect(my_property)
    """

    def __init__(self, op: Operator):
        super().__init__(split_mesh._spec().inputs, op)
        self._mesh_scoping = Input(split_mesh._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._mesh = Input(split_mesh._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)
        self._property = Input(split_mesh._spec().input_pin(13), 13, op, -1)
        self._inputs.append(self._property)

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Scoping

        Parameters
        ----------
        my_mesh_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.split_mesh()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.split_mesh()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def property(self):
        """Allows to connect property input to the operator.

        Parameters
        ----------
        my_property : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.split_mesh()
        >>> op.inputs.property.connect(my_property)
        >>> # or
        >>> op.inputs.property(my_property)
        """
        return self._property


class OutputsSplitMesh(_Outputs):
    """Intermediate class used to get outputs from
    split_mesh operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.split_mesh()
    >>> # Connect inputs : op.inputs. ...
    >>> result_meshes = op.outputs.meshes()
    """

    def __init__(self, op: Operator):
        super().__init__(split_mesh._spec().outputs, op)
        self._meshes = Output(split_mesh._spec().output_pin(0), 0, op)
        self._outputs.append(self._meshes)

    @property
    def meshes(self):
        """Allows to get meshes output of the operator

        Returns
        ----------
        my_meshes : MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.split_mesh()
        >>> # Connect inputs : op.inputs. ...
        >>> result_meshes = op.outputs.meshes()
        """  # noqa: E501
        return self._meshes
