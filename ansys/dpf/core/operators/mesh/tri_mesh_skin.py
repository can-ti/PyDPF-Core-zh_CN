"""
tri_mesh_skin
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "mesh" category
"""

class tri_mesh_skin(Operator):
    """Extracts a skin of the mesh in triangles (2D elements) in a new meshed region

      available inputs:
        - mesh (MeshedRegion)
        - include_surfaces (bool) (optional)

      available outputs:
        - mesh (MeshedRegion)
        - nodes_mesh_scoping (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.tri_mesh_skin()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_include_surfaces = bool()
      >>> op.inputs.include_surfaces.connect(my_include_surfaces)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.tri_mesh_skin(mesh=my_mesh,include_surfaces=my_include_surfaces)

      >>> # Get output data
      >>> result_mesh = op.outputs.mesh()
      >>> result_nodes_mesh_scoping = op.outputs.nodes_mesh_scoping()"""
    def __init__(self, mesh=None, include_surfaces=None, config=None, server=None):
        super().__init__(name="meshed_skin_sector_triangle", config = config, server = server)
        self._inputs = InputsTriMeshSkin(self)
        self._outputs = OutputsTriMeshSkin(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if include_surfaces !=None:
            self.inputs.include_surfaces.connect(include_surfaces)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts a skin of the mesh in triangles (2D elements) in a new meshed region""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "include_surfaces", type_names=["bool"], optional=True, document="""true: meshing will also take into account shell and 2D elements, false: meshing will ignore shell and 2D elements. default is false""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "nodes_mesh_scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "meshed_skin_sector_triangle")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsTriMeshSkin 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsTriMeshSkin 
        """
        return super().outputs


#internal name: meshed_skin_sector_triangle
#scripting name: tri_mesh_skin
class InputsTriMeshSkin(_Inputs):
    """Intermediate class used to connect user inputs to tri_mesh_skin operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.tri_mesh_skin()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_include_surfaces = bool()
      >>> op.inputs.include_surfaces.connect(my_include_surfaces)
    """
    def __init__(self, op: Operator):
        super().__init__(tri_mesh_skin._spec().inputs, op)
        self._mesh = Input(tri_mesh_skin._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mesh)
        self._include_surfaces = Input(tri_mesh_skin._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._include_surfaces)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.tri_mesh_skin()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def include_surfaces(self):
        """Allows to connect include_surfaces input to the operator

        - pindoc: true: meshing will also take into account shell and 2D elements, false: meshing will ignore shell and 2D elements. default is false

        Parameters
        ----------
        my_include_surfaces : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.tri_mesh_skin()
        >>> op.inputs.include_surfaces.connect(my_include_surfaces)
        >>> #or
        >>> op.inputs.include_surfaces(my_include_surfaces)

        """
        return self._include_surfaces

class OutputsTriMeshSkin(_Outputs):
    """Intermediate class used to get outputs from tri_mesh_skin operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.tri_mesh_skin()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh = op.outputs.mesh()
      >>> result_nodes_mesh_scoping = op.outputs.nodes_mesh_scoping()
    """
    def __init__(self, op: Operator):
        super().__init__(tri_mesh_skin._spec().outputs, op)
        self._mesh = Output(tri_mesh_skin._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mesh)
        self._nodes_mesh_scoping = Output(tri_mesh_skin._spec().output_pin(1), 1, op) 
        self._outputs.append(self._nodes_mesh_scoping)

    @property
    def mesh(self):
        """Allows to get mesh output of the operator


        Returns
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.tri_mesh_skin()
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

        >>> op = dpf.operators.mesh.tri_mesh_skin()
        >>> # Connect inputs : op.inputs. ...
        >>> result_nodes_mesh_scoping = op.outputs.nodes_mesh_scoping() 
        """
        return self._nodes_mesh_scoping

