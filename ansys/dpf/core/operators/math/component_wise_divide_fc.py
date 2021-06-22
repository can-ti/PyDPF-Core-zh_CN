"""
component_wise_divide_fc
========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class component_wise_divide_fc(Operator):
    """For every two fields with the same label space (from the two input fields containers), computes component-wise fraction between two fields of same dimensionality. If one field's scoping has overall location, then these field's values are applied on the entire other field.

      available inputs:
        - fields_containerA (FieldsContainer)
        - fields_containerB (FieldsContainer)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.component_wise_divide_fc()

      >>> # Make input connections
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.component_wise_divide_fc(fields_containerA=my_fields_containerA,fields_containerB=my_fields_containerB)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_containerA=None, fields_containerB=None, config=None, server=None):
        super().__init__(name="component_wise_divide_fc", config = config, server = server)
        self._inputs = InputsComponentWiseDivideFc(self)
        self._outputs = OutputsComponentWiseDivideFc(self)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)

    @staticmethod
    def _spec():
        spec = Specification(description="""For every two fields with the same label space (from the two input fields containers), computes component-wise fraction between two fields of same dimensionality. If one field's scoping has overall location, then these field's values are applied on the entire other field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "component_wise_divide_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsComponentWiseDivideFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsComponentWiseDivideFc 
        """
        return super().outputs


#internal name: component_wise_divide_fc
#scripting name: component_wise_divide_fc
class InputsComponentWiseDivideFc(_Inputs):
    """Intermediate class used to connect user inputs to component_wise_divide_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.component_wise_divide_fc()
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)
    """
    def __init__(self, op: Operator):
        super().__init__(component_wise_divide_fc._spec().inputs, op)
        self._fields_containerA = Input(component_wise_divide_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_containerA)
        self._fields_containerB = Input(component_wise_divide_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fields_containerB)

    @property
    def fields_containerA(self):
        """Allows to connect fields_containerA input to the operator

        Parameters
        ----------
        my_fields_containerA : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.component_wise_divide_fc()
        >>> op.inputs.fields_containerA.connect(my_fields_containerA)
        >>> #or
        >>> op.inputs.fields_containerA(my_fields_containerA)

        """
        return self._fields_containerA

    @property
    def fields_containerB(self):
        """Allows to connect fields_containerB input to the operator

        Parameters
        ----------
        my_fields_containerB : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.component_wise_divide_fc()
        >>> op.inputs.fields_containerB.connect(my_fields_containerB)
        >>> #or
        >>> op.inputs.fields_containerB(my_fields_containerB)

        """
        return self._fields_containerB

class OutputsComponentWiseDivideFc(_Outputs):
    """Intermediate class used to get outputs from component_wise_divide_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.component_wise_divide_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(component_wise_divide_fc._spec().outputs, op)
        self._fields_container = Output(component_wise_divide_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.component_wise_divide_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

