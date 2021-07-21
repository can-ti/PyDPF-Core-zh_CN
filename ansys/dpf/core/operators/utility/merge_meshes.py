"""
merge_meshes
============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class merge_meshes(Operator):
    """Take a set of mesh and assemble them in a unique one

      available inputs:
        - meshes1 (MeshedRegion)
        - meshes2 (MeshedRegion)

      available outputs:
        - merges_mesh (MeshedRegion)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_meshes()

      >>> # Make input connections
      >>> my_meshes1 = dpf.MeshedRegion()
      >>> op.inputs.meshes1.connect(my_meshes1)
      >>> my_meshes2 = dpf.MeshedRegion()
      >>> op.inputs.meshes2.connect(my_meshes2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_meshes(meshes1=my_meshes1,meshes2=my_meshes2)

      >>> # Get output data
      >>> result_merges_mesh = op.outputs.merges_mesh()"""
    def __init__(self, meshes1=None, meshes2=None, config=None, server=None):
        super().__init__(name="merge::mesh", config = config, server = server)
        self._inputs = InputsMergeMeshes(self)
        self._outputs = OutputsMergeMeshes(self)
        if meshes1 !=None:
            self.inputs.meshes1.connect(meshes1)
        if meshes2 !=None:
            self.inputs.meshes2.connect(meshes2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of mesh and assemble them in a unique one""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "meshes", type_names=["abstract_meshed_region"], optional=False, document="""A vector of meshed region to merge or meshed region from pin 0 to ..."""), 
                                 1 : PinSpecification(name = "meshes", type_names=["abstract_meshed_region"], optional=False, document="""A vector of meshed region to merge or meshed region from pin 0 to ...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "merges_mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::mesh")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeMeshes 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeMeshes 
        """
        return super().outputs


#internal name: merge::mesh
#scripting name: merge_meshes
class InputsMergeMeshes(_Inputs):
    """Intermediate class used to connect user inputs to merge_meshes operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_meshes()
      >>> my_meshes1 = dpf.MeshedRegion()
      >>> op.inputs.meshes1.connect(my_meshes1)
      >>> my_meshes2 = dpf.MeshedRegion()
      >>> op.inputs.meshes2.connect(my_meshes2)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_meshes._spec().inputs, op)
        self._meshes1 = Input(merge_meshes._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self._meshes1)
        self._meshes2 = Input(merge_meshes._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self._meshes2)

    @property
    def meshes1(self):
        """Allows to connect meshes1 input to the operator

        - pindoc: A vector of meshed region to merge or meshed region from pin 0 to ...

        Parameters
        ----------
        my_meshes1 : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_meshes()
        >>> op.inputs.meshes1.connect(my_meshes1)
        >>> #or
        >>> op.inputs.meshes1(my_meshes1)

        """
        return self._meshes1

    @property
    def meshes2(self):
        """Allows to connect meshes2 input to the operator

        - pindoc: A vector of meshed region to merge or meshed region from pin 0 to ...

        Parameters
        ----------
        my_meshes2 : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_meshes()
        >>> op.inputs.meshes2.connect(my_meshes2)
        >>> #or
        >>> op.inputs.meshes2(my_meshes2)

        """
        return self._meshes2

class OutputsMergeMeshes(_Outputs):
    """Intermediate class used to get outputs from merge_meshes operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_meshes()
      >>> # Connect inputs : op.inputs. ...
      >>> result_merges_mesh = op.outputs.merges_mesh()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_meshes._spec().outputs, op)
        self._merges_mesh = Output(merge_meshes._spec().output_pin(0), 0, op) 
        self._outputs.append(self._merges_mesh)

    @property
    def merges_mesh(self):
        """Allows to get merges_mesh output of the operator


        Returns
        ----------
        my_merges_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_meshes()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merges_mesh = op.outputs.merges_mesh() 
        """
        return self._merges_mesh

