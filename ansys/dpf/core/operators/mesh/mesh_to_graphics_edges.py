"""
mesh_to_graphics_edges
======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "mesh" category
"""

class mesh_to_graphics_edges(Operator):
    """Generate edges of surface elements for input mesh

      available inputs:
        - mesh_scoping (Scoping) (optional)
        - mesh (MeshedRegion)

      available outputs:
        - nodes (Field)
        - connectivity (PropertyField)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.mesh_to_graphics_edges()

      >>> # Make input connections
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.mesh_to_graphics_edges(mesh_scoping=my_mesh_scoping,mesh=my_mesh)

      >>> # Get output data
      >>> result_nodes = op.outputs.nodes()
      >>> result_connectivity = op.outputs.connectivity()"""
    def __init__(self, mesh_scoping=None, mesh=None, config=None, server=None):
        super().__init__(name="mesh_to_graphics_edges", config = config, server = server)
        self._inputs = InputsMeshToGraphicsEdges(self)
        self._outputs = OutputsMeshToGraphicsEdges(self)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Generate edges of surface elements for input mesh""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "nodes", type_names=["field"], optional=False, document="""node coordinates"""), 
                                 2 : PinSpecification(name = "connectivity", type_names=["property_field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh_to_graphics_edges")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMeshToGraphicsEdges 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMeshToGraphicsEdges 
        """
        return super().outputs


#internal name: mesh_to_graphics_edges
#scripting name: mesh_to_graphics_edges
class InputsMeshToGraphicsEdges(_Inputs):
    """Intermediate class used to connect user inputs to mesh_to_graphics_edges operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(mesh_to_graphics_edges._spec().inputs, op)
        self._mesh_scoping = Input(mesh_to_graphics_edges._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._mesh = Input(mesh_to_graphics_edges._spec().input_pin(7), 7, op, -1) 
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

        >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsMeshToGraphicsEdges(_Outputs):
    """Intermediate class used to get outputs from mesh_to_graphics_edges operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
      >>> # Connect inputs : op.inputs. ...
      >>> result_nodes = op.outputs.nodes()
      >>> result_connectivity = op.outputs.connectivity()
    """
    def __init__(self, op: Operator):
        super().__init__(mesh_to_graphics_edges._spec().outputs, op)
        self._nodes = Output(mesh_to_graphics_edges._spec().output_pin(0), 0, op) 
        self._outputs.append(self._nodes)
        self._connectivity = Output(mesh_to_graphics_edges._spec().output_pin(2), 2, op) 
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

        >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
        >>> # Connect inputs : op.inputs. ...
        >>> result_nodes = op.outputs.nodes() 
        """
        return self._nodes

    @property
    def connectivity(self):
        """Allows to get connectivity output of the operator


        Returns
        ----------
        my_connectivity : PropertyField, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_to_graphics_edges()
        >>> # Connect inputs : op.inputs. ...
        >>> result_connectivity = op.outputs.connectivity() 
        """
        return self._connectivity

