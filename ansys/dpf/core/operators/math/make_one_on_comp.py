"""
make_one_on_comp
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "math" category
"""

class make_one_on_comp(Operator):
    """take the input field's scoping and create a field full of zeros, except for the indexes from pin 1 that will hold 1.0.

      available inputs:
        - fieldA (Field)
        - scalar_int (int)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.make_one_on_comp()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_scalar_int = int()
      >>> op.inputs.scalar_int.connect(my_scalar_int)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.make_one_on_comp(fieldA=my_fieldA,scalar_int=my_scalar_int)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, scalar_int=None, config=None, server=None):
        super().__init__(name="make_one_on_comp", config = config, server = server)
        self._inputs = InputsMakeOneOnComp(self)
        self._outputs = OutputsMakeOneOnComp(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if scalar_int !=None:
            self.inputs.scalar_int.connect(scalar_int)

    @staticmethod
    def _spec():
        spec = Specification(description="""take the input field's scoping and create a field full of zeros, except for the indexes from pin 1 that will hold 1.0.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scalar_int", type_names=["int32"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "make_one_on_comp")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMakeOneOnComp 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMakeOneOnComp 
        """
        return super().outputs


#internal name: make_one_on_comp
#scripting name: make_one_on_comp
class InputsMakeOneOnComp(_Inputs):
    """Intermediate class used to connect user inputs to make_one_on_comp operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.make_one_on_comp()
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_scalar_int = int()
      >>> op.inputs.scalar_int.connect(my_scalar_int)
    """
    def __init__(self, op: Operator):
        super().__init__(make_one_on_comp._spec().inputs, op)
        self._fieldA = Input(make_one_on_comp._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fieldA)
        self._scalar_int = Input(make_one_on_comp._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._scalar_int)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator

        Parameters
        ----------
        my_fieldA : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.make_one_on_comp()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> #or
        >>> op.inputs.fieldA(my_fieldA)

        """
        return self._fieldA

    @property
    def scalar_int(self):
        """Allows to connect scalar_int input to the operator

        Parameters
        ----------
        my_scalar_int : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.make_one_on_comp()
        >>> op.inputs.scalar_int.connect(my_scalar_int)
        >>> #or
        >>> op.inputs.scalar_int(my_scalar_int)

        """
        return self._scalar_int

class OutputsMakeOneOnComp(_Outputs):
    """Intermediate class used to get outputs from make_one_on_comp operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.make_one_on_comp()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(make_one_on_comp._spec().outputs, op)
        self._field = Output(make_one_on_comp._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.make_one_on_comp()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

