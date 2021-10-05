"""
correlation
===========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "math" category
"""

class correlation(Operator):
    """take two fields and a weighting and compute their correlation: aMb/(||aMa||.||bMb||)

      available inputs:
        - fieldA (Field, float, list)
        - fieldB (Field, FieldsContainer)
        - ponderation (Field)

      available outputs:
        - field (Field)
        - index (int)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.correlation()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
      >>> my_ponderation = dpf.Field()
      >>> op.inputs.ponderation.connect(my_ponderation)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.correlation(fieldA=my_fieldA,fieldB=my_fieldB,ponderation=my_ponderation)

      >>> # Get output data
      >>> result_field = op.outputs.field()
      >>> result_index = op.outputs.index()"""
    def __init__(self, fieldA=None, fieldB=None, ponderation=None, config=None, server=None):
        super().__init__(name="correlation", config = config, server = server)
        self._inputs = InputsCorrelation(self)
        self._outputs = OutputsCorrelation(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)

    @staticmethod
    def _spec():
        spec = Specification(description="""take two fields and a weighting and compute their correlation: aMb/(||aMa||.||bMb||)""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","double","vector<double>"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "ponderation", type_names=["field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "index", type_names=["int32"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "correlation")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCorrelation 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCorrelation 
        """
        return super().outputs


#internal name: correlation
#scripting name: correlation
class InputsCorrelation(_Inputs):
    """Intermediate class used to connect user inputs to correlation operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.correlation()
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
      >>> my_ponderation = dpf.Field()
      >>> op.inputs.ponderation.connect(my_ponderation)
    """
    def __init__(self, op: Operator):
        super().__init__(correlation._spec().inputs, op)
        self._fieldA = Input(correlation._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fieldA)
        self._fieldB = Input(correlation._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fieldB)
        self._ponderation = Input(correlation._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._ponderation)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator

        Parameters
        ----------
        my_fieldA : Field, float, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.correlation()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> #or
        >>> op.inputs.fieldA(my_fieldA)

        """
        return self._fieldA

    @property
    def fieldB(self):
        """Allows to connect fieldB input to the operator

        Parameters
        ----------
        my_fieldB : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.correlation()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> #or
        >>> op.inputs.fieldB(my_fieldB)

        """
        return self._fieldB

    @property
    def ponderation(self):
        """Allows to connect ponderation input to the operator

        Parameters
        ----------
        my_ponderation : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.correlation()
        >>> op.inputs.ponderation.connect(my_ponderation)
        >>> #or
        >>> op.inputs.ponderation(my_ponderation)

        """
        return self._ponderation

class OutputsCorrelation(_Outputs):
    """Intermediate class used to get outputs from correlation operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.correlation()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
      >>> result_index = op.outputs.index()
    """
    def __init__(self, op: Operator):
        super().__init__(correlation._spec().outputs, op)
        self._field = Output(correlation._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)
        self._index = Output(correlation._spec().output_pin(1), 1, op) 
        self._outputs.append(self._index)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.correlation()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

    @property
    def index(self):
        """Allows to get index output of the operator


        Returns
        ----------
        my_index : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.correlation()
        >>> # Connect inputs : op.inputs. ...
        >>> result_index = op.outputs.index() 
        """
        return self._index

