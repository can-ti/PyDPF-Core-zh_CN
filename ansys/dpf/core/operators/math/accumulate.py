"""
accumulate
==========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class accumulate(Operator):
    """Sum all the elementary data of a field to get one elementary data at the end.

      available inputs:
        - fieldA (Field, FieldsContainer)
        - ponderation (Field)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.accumulate()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_ponderation = dpf.Field()
      >>> op.inputs.ponderation.connect(my_ponderation)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.accumulate(fieldA=my_fieldA,ponderation=my_ponderation)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, ponderation=None, config=None, server=None):
        super().__init__(name="accumulate", config = config, server = server)
        self._inputs = InputsAccumulate(self)
        self._outputs = OutputsAccumulate(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)

    @staticmethod
    def _spec():
        spec = Specification(description="""Sum all the elementary data of a field to get one elementary data at the end.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "ponderation", type_names=["field"], optional=False, document="""field""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "accumulate")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAccumulate 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAccumulate 
        """
        return super().outputs


#internal name: accumulate
#scripting name: accumulate
class InputsAccumulate(_Inputs):
    """Intermediate class used to connect user inputs to accumulate operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.accumulate()
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_ponderation = dpf.Field()
      >>> op.inputs.ponderation.connect(my_ponderation)
    """
    def __init__(self, op: Operator):
        super().__init__(accumulate._spec().inputs, op)
        self._fieldA = Input(accumulate._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fieldA)
        self._ponderation = Input(accumulate._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._ponderation)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fieldA : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.accumulate()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> #or
        >>> op.inputs.fieldA(my_fieldA)

        """
        return self._fieldA

    @property
    def ponderation(self):
        """Allows to connect ponderation input to the operator

        - pindoc: field

        Parameters
        ----------
        my_ponderation : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.accumulate()
        >>> op.inputs.ponderation.connect(my_ponderation)
        >>> #or
        >>> op.inputs.ponderation(my_ponderation)

        """
        return self._ponderation

class OutputsAccumulate(_Outputs):
    """Intermediate class used to get outputs from accumulate operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.accumulate()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(accumulate._spec().outputs, op)
        self._field = Output(accumulate._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.accumulate()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

