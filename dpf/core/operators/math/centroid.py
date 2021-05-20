"""
centroid
========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class centroid(Operator):
    """Computes centroid of field1 and field2, using fieldOut = field1*(1.-fact)+field2*(fact).

      available inputs:
        - fieldA (Field, FieldsContainer)
        - fieldB (Field, FieldsContainer)
        - factor (float)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.centroid()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
      >>> my_factor = float()
      >>> op.inputs.factor.connect(my_factor)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.centroid(fieldA=my_fieldA,fieldB=my_fieldB,factor=my_factor)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, factor=None, config=None, server=None):
        super().__init__(name="centroid", config = config, server = server)
        self._inputs = InputsCentroid(self)
        self._outputs = OutputsCentroid(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)
        if factor !=None:
            self.inputs.factor.connect(factor)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes centroid of field1 and field2, using fieldOut = field1*(1.-fact)+field2*(fact).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 2 : PinSpecification(name = "factor", type_names=["double"], optional=False, document="""Scalar""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "centroid")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCentroid 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCentroid 
        """
        return super().outputs


#internal name: centroid
#scripting name: centroid
class InputsCentroid(_Inputs):
    """Intermediate class used to connect user inputs to centroid operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.centroid()
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
      >>> my_factor = float()
      >>> op.inputs.factor.connect(my_factor)
    """
    def __init__(self, op: Operator):
        super().__init__(centroid._spec().inputs, op)
        self._fieldA = Input(centroid._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fieldA)
        self._fieldB = Input(centroid._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fieldB)
        self._factor = Input(centroid._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._factor)

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

        >>> op = dpf.operators.math.centroid()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> #or
        >>> op.inputs.fieldA(my_fieldA)

        """
        return self._fieldA

    @property
    def fieldB(self):
        """Allows to connect fieldB input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fieldB : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.centroid()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> #or
        >>> op.inputs.fieldB(my_fieldB)

        """
        return self._fieldB

    @property
    def factor(self):
        """Allows to connect factor input to the operator

        - pindoc: Scalar

        Parameters
        ----------
        my_factor : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.centroid()
        >>> op.inputs.factor.connect(my_factor)
        >>> #or
        >>> op.inputs.factor(my_factor)

        """
        return self._factor

class OutputsCentroid(_Outputs):
    """Intermediate class used to get outputs from centroid operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.centroid()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(centroid._spec().outputs, op)
        self._field = Output(centroid._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.centroid()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

