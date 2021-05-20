"""
principal_invariants
====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "invariant" category
"""

class principal_invariants(Operator):
    """Computes the element-wise eigen values of a tensor field

      available inputs:
        - field (Field)

      available outputs:
        - field_eig_1 (Field)
        - field_eig_2 (Field)
        - field_eig_3 (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.invariant.principal_invariants()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.invariant.principal_invariants(field=my_field)

      >>> # Get output data
      >>> result_field_eig_1 = op.outputs.field_eig_1()
      >>> result_field_eig_2 = op.outputs.field_eig_2()
      >>> result_field_eig_3 = op.outputs.field_eig_3()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="invariants", config = config, server = server)
        self._inputs = InputsPrincipalInvariants(self)
        self._outputs = OutputsPrincipalInvariants(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise eigen values of a tensor field""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_eig_1", type_names=["field"], optional=False, document="""first eigen value field"""), 
                                 1 : PinSpecification(name = "field_eig_2", type_names=["field"], optional=False, document="""second eigen value field"""), 
                                 2 : PinSpecification(name = "field_eig_3", type_names=["field"], optional=False, document="""third eigen value field""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "invariants")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPrincipalInvariants 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPrincipalInvariants 
        """
        return super().outputs


#internal name: invariants
#scripting name: principal_invariants
class InputsPrincipalInvariants(_Inputs):
    """Intermediate class used to connect user inputs to principal_invariants operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.principal_invariants()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
    """
    def __init__(self, op: Operator):
        super().__init__(principal_invariants._spec().inputs, op)
        self._field = Input(principal_invariants._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)

    @property
    def field(self):
        """Allows to connect field input to the operator

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.principal_invariants()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

class OutputsPrincipalInvariants(_Outputs):
    """Intermediate class used to get outputs from principal_invariants operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.invariant.principal_invariants()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field_eig_1 = op.outputs.field_eig_1()
      >>> result_field_eig_2 = op.outputs.field_eig_2()
      >>> result_field_eig_3 = op.outputs.field_eig_3()
    """
    def __init__(self, op: Operator):
        super().__init__(principal_invariants._spec().outputs, op)
        self._field_eig_1 = Output(principal_invariants._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field_eig_1)
        self._field_eig_2 = Output(principal_invariants._spec().output_pin(1), 1, op) 
        self._outputs.append(self._field_eig_2)
        self._field_eig_3 = Output(principal_invariants._spec().output_pin(2), 2, op) 
        self._outputs.append(self._field_eig_3)

    @property
    def field_eig_1(self):
        """Allows to get field_eig_1 output of the operator


        - pindoc: first eigen value field

        Returns
        ----------
        my_field_eig_1 : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.principal_invariants()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_eig_1 = op.outputs.field_eig_1() 
        """
        return self._field_eig_1

    @property
    def field_eig_2(self):
        """Allows to get field_eig_2 output of the operator


        - pindoc: second eigen value field

        Returns
        ----------
        my_field_eig_2 : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.principal_invariants()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_eig_2 = op.outputs.field_eig_2() 
        """
        return self._field_eig_2

    @property
    def field_eig_3(self):
        """Allows to get field_eig_3 output of the operator


        - pindoc: third eigen value field

        Returns
        ----------
        my_field_eig_3 : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.invariant.principal_invariants()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_eig_3 = op.outputs.field_eig_3() 
        """
        return self._field_eig_3

