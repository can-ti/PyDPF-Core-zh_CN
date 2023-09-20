"""
mesh_to_tetra
=============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class mesh_to_tetra(Operator):
    """Converts 3D meshes of arbitrary 3D element types into a tetrahedral
    mesh, output at pin (0). Non 3D elements are ignored. Scopings
    providing the mapping from resulting nodes & elements to their
    original ID in the input mesh are provided, output pins (1) & (2)
    respectively.

    Parameters
    ----------
    mesh : MeshedRegion
        Mesh with arbitrary element types.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.mesh_to_tetra()

    >>> # Make input connections
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.mesh_to_tetra(
    ...     mesh=my_mesh,
    ... )

    >>> # Get output data
    >>> result_mesh = op.outputs.mesh()
    >>> result_node_mapping = op.outputs.node_mapping()
    >>> result_element_mapping = op.outputs.element_mapping()
    """

    def __init__(self, mesh=None, config=None, server=None):
        super().__init__(name="mesh_to_tetra", config=config, server=server)
        self._inputs = InputsMeshToTetra(self)
        self._outputs = OutputsMeshToTetra(self)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        description = """Converts 3D meshes of arbitrary 3D element types into a tetrahedral
            mesh, output at pin (0). Non 3D elements are ignored.
            Scopings providing the mapping from resulting nodes &amp;
            elements to their original ID in the input mesh are
            provided, output pins (1) &amp; (2) respectively."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""Mesh with arbitrary element types.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="mesh",
                    type_names=["meshed_region"],
                    optional=False,
                    document="""Tetrahedralized mesh.""",
                ),
                1: PinSpecification(
                    name="node_mapping",
                    type_names=["scoping"],
                    optional=False,
                    document="""Node mapping.""",
                ),
                2: PinSpecification(
                    name="element_mapping",
                    type_names=["scoping"],
                    optional=False,
                    document="""Element mapping.""",
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
        return Operator.default_config(name="mesh_to_tetra", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMeshToTetra
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMeshToTetra
        """
        return super().outputs


class InputsMeshToTetra(_Inputs):
    """Intermediate class used to connect user inputs to
    mesh_to_tetra operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.mesh_to_tetra()
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_to_tetra._spec().inputs, op)
        self._mesh = Input(mesh_to_tetra._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._mesh)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Mesh with arbitrary element types.

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_to_tetra()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh


class OutputsMeshToTetra(_Outputs):
    """Intermediate class used to get outputs from
    mesh_to_tetra operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.mesh_to_tetra()
    >>> # Connect inputs : op.inputs. ...
    >>> result_mesh = op.outputs.mesh()
    >>> result_node_mapping = op.outputs.node_mapping()
    >>> result_element_mapping = op.outputs.element_mapping()
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_to_tetra._spec().outputs, op)
        self._mesh = Output(mesh_to_tetra._spec().output_pin(0), 0, op)
        self._outputs.append(self._mesh)
        self._node_mapping = Output(mesh_to_tetra._spec().output_pin(1), 1, op)
        self._outputs.append(self._node_mapping)
        self._element_mapping = Output(mesh_to_tetra._spec().output_pin(2), 2, op)
        self._outputs.append(self._element_mapping)

    @property
    def mesh(self):
        """Allows to get mesh output of the operator

        Returns
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_to_tetra()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh()
        """  # noqa: E501
        return self._mesh

    @property
    def node_mapping(self):
        """Allows to get node_mapping output of the operator

        Returns
        ----------
        my_node_mapping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_to_tetra()
        >>> # Connect inputs : op.inputs. ...
        >>> result_node_mapping = op.outputs.node_mapping()
        """  # noqa: E501
        return self._node_mapping

    @property
    def element_mapping(self):
        """Allows to get element_mapping output of the operator

        Returns
        ----------
        my_element_mapping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_to_tetra()
        >>> # Connect inputs : op.inputs. ...
        >>> result_element_mapping = op.outputs.element_mapping()
        """  # noqa: E501
        return self._element_mapping
