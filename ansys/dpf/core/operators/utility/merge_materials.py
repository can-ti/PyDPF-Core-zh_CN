"""
merge_materials
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class merge_materials(Operator):
    """Take a set of materials and assemble them in a unique one

      available inputs:
        - materials1 (Materials)
        - materials2 (Materials)

      available outputs:
        - merged_materials (Materials)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_materials()

      >>> # Make input connections
      >>> my_materials1 = dpf.Materials()
      >>> op.inputs.materials1.connect(my_materials1)
      >>> my_materials2 = dpf.Materials()
      >>> op.inputs.materials2.connect(my_materials2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_materials(materials1=my_materials1,materials2=my_materials2)

      >>> # Get output data
      >>> result_merged_materials = op.outputs.merged_materials()"""
    def __init__(self, materials1=None, materials2=None, config=None, server=None):
        super().__init__(name="merge::materials", config = config, server = server)
        self._inputs = InputsMergeMaterials(self)
        self._outputs = OutputsMergeMaterials(self)
        if materials1 !=None:
            self.inputs.materials1.connect(materials1)
        if materials2 !=None:
            self.inputs.materials2.connect(materials2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of materials and assemble them in a unique one""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "materials", type_names=["materials"], optional=False, document="""A vector of materials to merge or materials from pin 0 to ..."""), 
                                 1 : PinSpecification(name = "materials", type_names=["materials"], optional=False, document="""A vector of materials to merge or materials from pin 0 to ...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "merged_materials", type_names=["materials"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::materials")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeMaterials 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeMaterials 
        """
        return super().outputs


#internal name: merge::materials
#scripting name: merge_materials
class InputsMergeMaterials(_Inputs):
    """Intermediate class used to connect user inputs to merge_materials operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_materials()
      >>> my_materials1 = dpf.Materials()
      >>> op.inputs.materials1.connect(my_materials1)
      >>> my_materials2 = dpf.Materials()
      >>> op.inputs.materials2.connect(my_materials2)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_materials._spec().inputs, op)
        self._materials1 = Input(merge_materials._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self._materials1)
        self._materials2 = Input(merge_materials._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self._materials2)

    @property
    def materials1(self):
        """Allows to connect materials1 input to the operator

        - pindoc: A vector of materials to merge or materials from pin 0 to ...

        Parameters
        ----------
        my_materials1 : Materials, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_materials()
        >>> op.inputs.materials1.connect(my_materials1)
        >>> #or
        >>> op.inputs.materials1(my_materials1)

        """
        return self._materials1

    @property
    def materials2(self):
        """Allows to connect materials2 input to the operator

        - pindoc: A vector of materials to merge or materials from pin 0 to ...

        Parameters
        ----------
        my_materials2 : Materials, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_materials()
        >>> op.inputs.materials2.connect(my_materials2)
        >>> #or
        >>> op.inputs.materials2(my_materials2)

        """
        return self._materials2

class OutputsMergeMaterials(_Outputs):
    """Intermediate class used to get outputs from merge_materials operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_materials()
      >>> # Connect inputs : op.inputs. ...
      >>> result_merged_materials = op.outputs.merged_materials()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_materials._spec().outputs, op)
        self._merged_materials = Output(merge_materials._spec().output_pin(0), 0, op) 
        self._outputs.append(self._merged_materials)

    @property
    def merged_materials(self):
        """Allows to get merged_materials output of the operator


        Returns
        ----------
        my_merged_materials : Materials, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_materials()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_materials = op.outputs.merged_materials() 
        """
        return self._merged_materials

