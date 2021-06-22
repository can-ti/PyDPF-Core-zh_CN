"""
von_mises_eqv_fc
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "invariant" category
"""

class von_mises_eqv_fc(Operator):
    """Computes the element-wise Von-Mises criteria on all the tensor fields of a fields container.

      available inputs:
        - fields_container (FieldsContainer)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.invariant.von_mises_eqv_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.invariant.von_mises_eqv_fc(fields_container=my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="eqv_fc", config = config, server = server)
        self._inputs = InputsVonMisesEqvFc(self)
        self._outputs = OutputsVonMisesEqvFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise Von-Mises criteria on all the tensor fields of a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "eqv_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsVonMisesEqvFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsVonMisesEqvFc 
        """
        return super().outputs


#internal name: eqv_fc
#scripting name: von_mises_eqv_fc
class InputsVonMisesEqvFc(_Inputs):
    """Intermediate class used to connect user inputs to von_mises_eqv_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.von_mises_eqv_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
    """
    def __init__(self, op: Operator):
        super().__init__(von_mises_eqv_fc._spec().inputs, op)
        self._fields_container = Input(von_mises_eqv_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.von_mises_eqv_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

class OutputsVonMisesEqvFc(_Outputs):
    """Intermediate class used to get outputs from von_mises_eqv_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.von_mises_eqv_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(von_mises_eqv_fc._spec().outputs, op)
        self._fields_container = Output(von_mises_eqv_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.invariant.von_mises_eqv_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

