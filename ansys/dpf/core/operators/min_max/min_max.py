"""
min_max
=======
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "min_max" category
"""

class min_max(Operator):
    """Compute the component-wise minimum (out 0) and maximum (out 1) over a field.

      available inputs:
        - field (Field, FieldsContainer)

      available outputs:
        - field_min (Field)
        - field_max (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.min_max.min_max(field=my_field)

      >>> # Get output data
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="min_max", config = config, server = server)
        self._inputs = InputsMinMax(self)
        self._outputs = OutputsMinMax(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the component-wise minimum (out 0) and maximum (out 1) over a field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_min", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "field_max", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMinMax 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMinMax 
        """
        return super().outputs


#internal name: min_max
#scripting name: min_max
class InputsMinMax(_Inputs):
    """Intermediate class used to connect user inputs to min_max operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.min_max.min_max()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
    """
    def __init__(self, op: Operator):
        super().__init__(min_max._spec().inputs, op)
        self._field = Input(min_max._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

class OutputsMinMax(_Outputs):
    """Intermediate class used to get outputs from min_max operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.min_max.min_max()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()
    """
    def __init__(self, op: Operator):
        super().__init__(min_max._spec().outputs, op)
        self._field_min = Output(min_max._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field_min)
        self._field_max = Output(min_max._spec().output_pin(1), 1, op) 
        self._outputs.append(self._field_max)

    @property
    def field_min(self):
        """Allows to get field_min output of the operator


        Returns
        ----------
        my_field_min : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_min = op.outputs.field_min() 
        """
        return self._field_min

    @property
    def field_max(self):
        """Allows to get field_max output of the operator


        Returns
        ----------
        my_field_max : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_max = op.outputs.field_max() 
        """
        return self._field_max

