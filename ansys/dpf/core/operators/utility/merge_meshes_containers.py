"""
merge_meshes_containers
=======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class merge_meshes_containers(Operator):
    """Take a set of meshes containers and assemble them in a unique one

      available inputs:
        - meshes_containers1 (MeshesContainer)
        - meshes_containers2 (MeshesContainer)

      available outputs:
        - merged_meshes_container (MeshesContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_meshes_containers()

      >>> # Make input connections
      >>> my_meshes_containers1 = dpf.MeshesContainer()
      >>> op.inputs.meshes_containers1.connect(my_meshes_containers1)
      >>> my_meshes_containers2 = dpf.MeshesContainer()
      >>> op.inputs.meshes_containers2.connect(my_meshes_containers2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_meshes_containers(meshes_containers1=my_meshes_containers1,meshes_containers2=my_meshes_containers2)

      >>> # Get output data
      >>> result_merged_meshes_container = op.outputs.merged_meshes_container()"""
    def __init__(self, meshes_containers1=None, meshes_containers2=None, config=None, server=None):
        super().__init__(name="merge::meshes_container", config = config, server = server)
        self._inputs = InputsMergeMeshesContainers(self)
        self._outputs = OutputsMergeMeshesContainers(self)
        if meshes_containers1 !=None:
            self.inputs.meshes_containers1.connect(meshes_containers1)
        if meshes_containers2 !=None:
            self.inputs.meshes_containers2.connect(meshes_containers2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of meshes containers and assemble them in a unique one""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "meshes_containers", type_names=["meshes_container"], optional=False, document="""a vector of meshes containers to merge or meshes containers from pin 0 to ..."""), 
                                 1 : PinSpecification(name = "meshes_containers", type_names=["meshes_container"], optional=False, document="""a vector of meshes containers to merge or meshes containers from pin 0 to ...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "merged_meshes_container", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::meshes_container")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeMeshesContainers 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeMeshesContainers 
        """
        return super().outputs


#internal name: merge::meshes_container
#scripting name: merge_meshes_containers
class InputsMergeMeshesContainers(_Inputs):
    """Intermediate class used to connect user inputs to merge_meshes_containers operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_meshes_containers()
      >>> my_meshes_containers1 = dpf.MeshesContainer()
      >>> op.inputs.meshes_containers1.connect(my_meshes_containers1)
      >>> my_meshes_containers2 = dpf.MeshesContainer()
      >>> op.inputs.meshes_containers2.connect(my_meshes_containers2)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_meshes_containers._spec().inputs, op)
        self._meshes_containers1 = Input(merge_meshes_containers._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self._meshes_containers1)
        self._meshes_containers2 = Input(merge_meshes_containers._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self._meshes_containers2)

    @property
    def meshes_containers1(self):
        """Allows to connect meshes_containers1 input to the operator

        - pindoc: a vector of meshes containers to merge or meshes containers from pin 0 to ...

        Parameters
        ----------
        my_meshes_containers1 : MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_meshes_containers()
        >>> op.inputs.meshes_containers1.connect(my_meshes_containers1)
        >>> #or
        >>> op.inputs.meshes_containers1(my_meshes_containers1)

        """
        return self._meshes_containers1

    @property
    def meshes_containers2(self):
        """Allows to connect meshes_containers2 input to the operator

        - pindoc: a vector of meshes containers to merge or meshes containers from pin 0 to ...

        Parameters
        ----------
        my_meshes_containers2 : MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_meshes_containers()
        >>> op.inputs.meshes_containers2.connect(my_meshes_containers2)
        >>> #or
        >>> op.inputs.meshes_containers2(my_meshes_containers2)

        """
        return self._meshes_containers2

class OutputsMergeMeshesContainers(_Outputs):
    """Intermediate class used to get outputs from merge_meshes_containers operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_meshes_containers()
      >>> # Connect inputs : op.inputs. ...
      >>> result_merged_meshes_container = op.outputs.merged_meshes_container()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_meshes_containers._spec().outputs, op)
        self._merged_meshes_container = Output(merge_meshes_containers._spec().output_pin(0), 0, op) 
        self._outputs.append(self._merged_meshes_container)

    @property
    def merged_meshes_container(self):
        """Allows to get merged_meshes_container output of the operator


        Returns
        ----------
        my_merged_meshes_container : MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_meshes_containers()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_meshes_container = op.outputs.merged_meshes_container() 
        """
        return self._merged_meshes_container

