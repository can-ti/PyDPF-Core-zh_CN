"""
skin
====
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "mesh" category
"""

class skin(Operator):
    """Extracts a skin of the mesh (2D elements) in a new meshed region. Material id of initial elements are propagated to their facets.

      available inputs:
        - mesh (MeshedRegion)
        - mesh_scoping (Scoping) (optional)

      available outputs:
        - mesh (MeshedRegion)
        - nodes_mesh_scoping (Scoping)
        - map_new_elements_to_old ()
        - property_field_new_elements_to_old (PropertyField)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.skin()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.skin(mesh=my_mesh,mesh_scoping=my_mesh_scoping)

      >>> # Get output data
      >>> result_mesh = op.outputs.mesh()
      >>> result_nodes_mesh_scoping = op.outputs.nodes_mesh_scoping()
      >>> result_map_new_elements_to_old = op.outputs.map_new_elements_to_old()
      >>> result_property_field_new_elements_to_old = op.outputs.property_field_new_elements_to_old()"""
    def __init__(self, mesh=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="meshed_skin_sector", config = config, server = server)
        self._inputs = InputsSkin(self)
        self._outputs = OutputsSkin(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts a skin of the mesh (2D elements) in a new meshed region. Material id of initial elements are propagated to their facets.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""skin meshed region with facets and facets_to_ele property fields"""), 
                                 1 : PinSpecification(name = "nodes_mesh_scoping", type_names=["scoping"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "map_new_elements_to_old", type_names=[], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "property_field_new_elements_to_old", type_names=["property_field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "meshed_skin_sector")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSkin 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSkin 
        """
        return super().outputs


#internal name: meshed_skin_sector
#scripting name: skin
class InputsSkin(_Inputs):
    """Intermediate class used to connect user inputs to skin operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.skin()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(skin._spec().inputs, op)
        self._mesh = Input(skin._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mesh)
        self._mesh_scoping = Input(skin._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.skin()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.skin()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

class OutputsSkin(_Outputs):
    """Intermediate class used to get outputs from skin operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.skin()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh = op.outputs.mesh()
      >>> result_nodes_mesh_scoping = op.outputs.nodes_mesh_scoping()
    """
    def __init__(self, op: Operator):
        super().__init__(skin._spec().outputs, op)
        self._mesh = Output(skin._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mesh)
        self._nodes_mesh_scoping = Output(skin._spec().output_pin(1), 1, op) 
        self._outputs.append(self._nodes_mesh_scoping)
        pass 

    @property
    def mesh(self):
        """Allows to get mesh output of the operator


        - pindoc: skin meshed region with facets and facets_to_ele property fields

        Returns
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.skin()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh() 
        """
        return self._mesh

    @property
    def nodes_mesh_scoping(self):
        """Allows to get nodes_mesh_scoping output of the operator


        Returns
        ----------
        my_nodes_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.skin()
        >>> # Connect inputs : op.inputs. ...
        >>> result_nodes_mesh_scoping = op.outputs.nodes_mesh_scoping() 
        """
        return self._nodes_mesh_scoping

