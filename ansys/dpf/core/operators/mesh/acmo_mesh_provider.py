"""
acmo_mesh_provider
==================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class acmo_mesh_provider(Operator):
    """Converts an Assembly Mesh into a DPF Meshes container

    Parameters
    ----------
    assembly_mesh : AnsDispatchHolder or Struct Iansdispatch


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.acmo_mesh_provider()

    >>> # Make input connections
    >>> my_assembly_mesh = dpf.AnsDispatchHolder()
    >>> op.inputs.assembly_mesh.connect(my_assembly_mesh)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.acmo_mesh_provider(
    ...     assembly_mesh=my_assembly_mesh,
    ... )

    >>> # Get output data
    >>> result_meshes_container = op.outputs.meshes_container()
    """

    def __init__(self, assembly_mesh=None, config=None, server=None):
        super().__init__(name="acmo_mesh_provider", config=config, server=server)
        self._inputs = InputsAcmoMeshProvider(self)
        self._outputs = OutputsAcmoMeshProvider(self)
        if assembly_mesh is not None:
            self.inputs.assembly_mesh.connect(assembly_mesh)

    @staticmethod
    def _spec():
        description = """Converts an Assembly Mesh into a DPF Meshes container"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="assembly_mesh",
                    type_names=["ans_dispatch_holder", "struct IAnsDispatch"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="meshes_container",
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
        return Operator.default_config(name="acmo_mesh_provider", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAcmoMeshProvider
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAcmoMeshProvider
        """
        return super().outputs


class InputsAcmoMeshProvider(_Inputs):
    """Intermediate class used to connect user inputs to
    acmo_mesh_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.acmo_mesh_provider()
    >>> my_assembly_mesh = dpf.AnsDispatchHolder()
    >>> op.inputs.assembly_mesh.connect(my_assembly_mesh)
    """

    def __init__(self, op: Operator):
        super().__init__(acmo_mesh_provider._spec().inputs, op)
        self._assembly_mesh = Input(acmo_mesh_provider._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._assembly_mesh)

    @property
    def assembly_mesh(self):
        """Allows to connect assembly_mesh input to the operator.

        Parameters
        ----------
        my_assembly_mesh : AnsDispatchHolder or Struct Iansdispatch

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.acmo_mesh_provider()
        >>> op.inputs.assembly_mesh.connect(my_assembly_mesh)
        >>> # or
        >>> op.inputs.assembly_mesh(my_assembly_mesh)
        """
        return self._assembly_mesh


class OutputsAcmoMeshProvider(_Outputs):
    """Intermediate class used to get outputs from
    acmo_mesh_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.acmo_mesh_provider()
    >>> # Connect inputs : op.inputs. ...
    >>> result_meshes_container = op.outputs.meshes_container()
    """

    def __init__(self, op: Operator):
        super().__init__(acmo_mesh_provider._spec().outputs, op)
        self._meshes_container = Output(acmo_mesh_provider._spec().output_pin(0), 0, op)
        self._outputs.append(self._meshes_container)

    @property
    def meshes_container(self):
        """Allows to get meshes_container output of the operator

        Returns
        ----------
        my_meshes_container : MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.acmo_mesh_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_meshes_container = op.outputs.meshes_container()
        """  # noqa: E501
        return self._meshes_container
