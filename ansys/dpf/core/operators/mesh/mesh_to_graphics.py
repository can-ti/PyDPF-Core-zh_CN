"""
mesh_to_graphics
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "mesh" category
"""

class mesh_to_graphics(Operator):
    """Generate tessellation for input mesh

      available inputs:
        - mesh_scoping (Scoping) (optional)
        - node_normals (bool) (optional)
        - mesh (MeshedRegion)

      available outputs:
        - nodes (Field)
        - normals (Field)
        - connectivity (PropertyField)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.mesh_to_graphics()

      >>> # Make input connections
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_node_normals = bool()
      >>> op.inputs.node_normals.connect(my_node_normals)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.mesh_to_graphics(mesh_scoping=my_mesh_scoping,node_normals=my_node_normals,mesh=my_mesh)

      >>> # Get output data
      >>> result_nodes = op.outputs.nodes()
      >>> result_normals = op.outputs.normals()
      >>> result_connectivity = op.outputs.connectivity()"""
    def __init__(self, mesh_scoping=None, node_normals=None, mesh=None, config=None, server=None):
        super().__init__(name="mesh_to_graphics", config = config, server = server)
        self._inputs = InputsMeshToGraphics(self)
        self._outputs = OutputsMeshToGraphics(self)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if node_normals !=None:
            self.inputs.node_normals.connect(node_normals)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Generate tessellation for input mesh""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "node_normals", type_names=["bool"], optional=True, document="""average element normals for node normals (default no, use element normals for node normals)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "nodes", type_names=["field"], optional=False, document="""node coordinates"""), 
                                 1 : PinSpecification(name = "normals", type_names=["field"], optional=False, document="""node normals"""), 
                                 2 : PinSpecification(name = "connectivity", type_names=["property_field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh_to_graphics")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMeshToGraphics 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMeshToGraphics 
        """
        return super().outputs


#internal name: mesh_to_graphics
#scripting name: mesh_to_graphics
class InputsMeshToGraphics(_Inputs):
    """Intermediate class used to connect user inputs to mesh_to_graphics operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.mesh_to_graphics()
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_node_normals = bool()
      >>> op.inputs.node_normals.connect(my_node_normals)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(mesh_to_graphics._spec().inputs, op)
        self._mesh_scoping = Input(mesh_to_graphics._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._node_normals = Input(mesh_to_graphics._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._node_normals)
        self._mesh = Input(mesh_to_graphics._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_to_graphics()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def node_normals(self):
        """Allows to connect node_normals input to the operator

        - pindoc: average element normals for node normals (default no, use element normals for node normals)

        Parameters
        ----------
        my_node_normals : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_to_graphics()
        >>> op.inputs.node_normals.connect(my_node_normals)
        >>> #or
        >>> op.inputs.node_normals(my_node_normals)

        """
        return self._node_normals

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_to_graphics()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsMeshToGraphics(_Outputs):
    """Intermediate class used to get outputs from mesh_to_graphics operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.mesh_to_graphics()
      >>> # Connect inputs : op.inputs. ...
      >>> result_nodes = op.outputs.nodes()
      >>> result_normals = op.outputs.normals()
      >>> result_connectivity = op.outputs.connectivity()
    """
    def __init__(self, op: Operator):
        super().__init__(mesh_to_graphics._spec().outputs, op)
        self._nodes = Output(mesh_to_graphics._spec().output_pin(0), 0, op) 
        self._outputs.append(self._nodes)
        self._normals = Output(mesh_to_graphics._spec().output_pin(1), 1, op) 
        self._outputs.append(self._normals)
        self._connectivity = Output(mesh_to_graphics._spec().output_pin(2), 2, op) 
        self._outputs.append(self._connectivity)

    @property
    def nodes(self):
        """Allows to get nodes output of the operator


        - pindoc: node coordinates

        Returns
        ----------
        my_nodes : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_to_graphics()
        >>> # Connect inputs : op.inputs. ...
        >>> result_nodes = op.outputs.nodes() 
        """
        return self._nodes

    @property
    def normals(self):
        """Allows to get normals output of the operator


        - pindoc: node normals

        Returns
        ----------
        my_normals : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_to_graphics()
        >>> # Connect inputs : op.inputs. ...
        >>> result_normals = op.outputs.normals() 
        """
        return self._normals

    @property
    def connectivity(self):
        """Allows to get connectivity output of the operator


        Returns
        ----------
        my_connectivity : PropertyField, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_to_graphics()
        >>> # Connect inputs : op.inputs. ...
        >>> result_connectivity = op.outputs.connectivity() 
        """
        return self._connectivity

