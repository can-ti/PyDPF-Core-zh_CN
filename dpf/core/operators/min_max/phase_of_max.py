"""
phase_of_max
============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "min_max" category
"""

class phase_of_max(Operator):
    """Evaluates phase of maximum.

      available inputs:
        - real_field (Field)
        - imaginary_field (Field)
        - abs_value (bool) (optional)
        - phase_increment (float)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.phase_of_max()

      >>> # Make input connections
      >>> my_real_field = dpf.Field()
      >>> op.inputs.real_field.connect(my_real_field)
      >>> my_imaginary_field = dpf.Field()
      >>> op.inputs.imaginary_field.connect(my_imaginary_field)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_phase_increment = float()
      >>> op.inputs.phase_increment.connect(my_phase_increment)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.min_max.phase_of_max(real_field=my_real_field,imaginary_field=my_imaginary_field,abs_value=my_abs_value,phase_increment=my_phase_increment)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, real_field=None, imaginary_field=None, abs_value=None, phase_increment=None, config=None, server=None):
        super().__init__(name="phase_of_max", config = config, server = server)
        self._inputs = InputsPhaseOfMax(self)
        self._outputs = OutputsPhaseOfMax(self)
        if real_field !=None:
            self.inputs.real_field.connect(real_field)
        if imaginary_field !=None:
            self.inputs.imaginary_field.connect(imaginary_field)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)
        if phase_increment !=None:
            self.inputs.phase_increment.connect(phase_increment)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates phase of maximum.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "real_field", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "imaginary_field", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "abs_value", type_names=["bool"], optional=True, document="""Should use absolute value."""), 
                                 3 : PinSpecification(name = "phase_increment", type_names=["double"], optional=False, document="""Phase increment.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "phase_of_max")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPhaseOfMax 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPhaseOfMax 
        """
        return super().outputs


#internal name: phase_of_max
#scripting name: phase_of_max
class InputsPhaseOfMax(_Inputs):
    """Intermediate class used to connect user inputs to phase_of_max operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.min_max.phase_of_max()
      >>> my_real_field = dpf.Field()
      >>> op.inputs.real_field.connect(my_real_field)
      >>> my_imaginary_field = dpf.Field()
      >>> op.inputs.imaginary_field.connect(my_imaginary_field)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_phase_increment = float()
      >>> op.inputs.phase_increment.connect(my_phase_increment)
    """
    def __init__(self, op: Operator):
        super().__init__(phase_of_max._spec().inputs, op)
        self._real_field = Input(phase_of_max._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._real_field)
        self._imaginary_field = Input(phase_of_max._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._imaginary_field)
        self._abs_value = Input(phase_of_max._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._abs_value)
        self._phase_increment = Input(phase_of_max._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._phase_increment)

    @property
    def real_field(self):
        """Allows to connect real_field input to the operator

        Parameters
        ----------
        my_real_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.phase_of_max()
        >>> op.inputs.real_field.connect(my_real_field)
        >>> #or
        >>> op.inputs.real_field(my_real_field)

        """
        return self._real_field

    @property
    def imaginary_field(self):
        """Allows to connect imaginary_field input to the operator

        Parameters
        ----------
        my_imaginary_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.phase_of_max()
        >>> op.inputs.imaginary_field.connect(my_imaginary_field)
        >>> #or
        >>> op.inputs.imaginary_field(my_imaginary_field)

        """
        return self._imaginary_field

    @property
    def abs_value(self):
        """Allows to connect abs_value input to the operator

        - pindoc: Should use absolute value.

        Parameters
        ----------
        my_abs_value : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.phase_of_max()
        >>> op.inputs.abs_value.connect(my_abs_value)
        >>> #or
        >>> op.inputs.abs_value(my_abs_value)

        """
        return self._abs_value

    @property
    def phase_increment(self):
        """Allows to connect phase_increment input to the operator

        - pindoc: Phase increment.

        Parameters
        ----------
        my_phase_increment : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.phase_of_max()
        >>> op.inputs.phase_increment.connect(my_phase_increment)
        >>> #or
        >>> op.inputs.phase_increment(my_phase_increment)

        """
        return self._phase_increment

class OutputsPhaseOfMax(_Outputs):
    """Intermediate class used to get outputs from phase_of_max operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.min_max.phase_of_max()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(phase_of_max._spec().outputs, op)
        self._field = Output(phase_of_max._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.min_max.phase_of_max()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

