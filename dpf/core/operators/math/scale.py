"""
scale
=====
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class scale(Operator):
    """Scales a field by a constant factor.

      available inputs:
        - field (Field, FieldsContainer)
        - ponderation (float, Field)
        - boolean (bool) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.scale()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)
      >>> my_boolean = bool()
      >>> op.inputs.boolean.connect(my_boolean)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.scale(field=my_field,ponderation=my_ponderation,boolean=my_boolean)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, ponderation=None, boolean=None, config=None, server=None):
        super().__init__(name="scale", config = config, server = server)
        self._inputs = InputsScale(self)
        self._outputs = OutputsScale(self)
        if field !=None:
            self.inputs.field.connect(field)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)
        if boolean !=None:
            self.inputs.boolean.connect(boolean)

    @staticmethod
    def _spec():
        spec = Specification(description="""Scales a field by a constant factor.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "ponderation", type_names=["double","field"], optional=False, document="""Double/Field scoped on overall"""), 
                                 2 : PinSpecification(name = "boolean", type_names=["bool"], optional=True, document="""bool(optional, default false) if set to true, output of scale is mane dimensionless""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scale")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsScale 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsScale 
        """
        return super().outputs


#internal name: scale
#scripting name: scale
class InputsScale(_Inputs):
    """Intermediate class used to connect user inputs to scale operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.scale()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)
      >>> my_boolean = bool()
      >>> op.inputs.boolean.connect(my_boolean)
    """
    def __init__(self, op: Operator):
        super().__init__(scale._spec().inputs, op)
        self._field = Input(scale._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._ponderation = Input(scale._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._ponderation)
        self._boolean = Input(scale._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._boolean)

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

        >>> op = dpf.operators.math.scale()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def ponderation(self):
        """Allows to connect ponderation input to the operator

        - pindoc: Double/Field scoped on overall

        Parameters
        ----------
        my_ponderation : float, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.scale()
        >>> op.inputs.ponderation.connect(my_ponderation)
        >>> #or
        >>> op.inputs.ponderation(my_ponderation)

        """
        return self._ponderation

    @property
    def boolean(self):
        """Allows to connect boolean input to the operator

        - pindoc: bool(optional, default false) if set to true, output of scale is mane dimensionless

        Parameters
        ----------
        my_boolean : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.scale()
        >>> op.inputs.boolean.connect(my_boolean)
        >>> #or
        >>> op.inputs.boolean(my_boolean)

        """
        return self._boolean

class OutputsScale(_Outputs):
    """Intermediate class used to get outputs from scale operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.scale()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(scale._spec().outputs, op)
        self._field = Output(scale._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.scale()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

