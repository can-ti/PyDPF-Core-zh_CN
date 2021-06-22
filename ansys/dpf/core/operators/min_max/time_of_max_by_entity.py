"""
time_of_max_by_entity
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "min_max" category
"""

class time_of_max_by_entity(Operator):
    """Evaluates time/frequency of maximum.

      available inputs:
        - fields_container (FieldsContainer)
        - abs_value (bool) (optional)
        - compute_amplitude (bool) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.time_of_max_by_entity()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_compute_amplitude = bool()
      >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.min_max.time_of_max_by_entity(fields_container=my_fields_container,abs_value=my_abs_value,compute_amplitude=my_compute_amplitude)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, abs_value=None, compute_amplitude=None, config=None, server=None):
        super().__init__(name="time_of_max_by_entity", config = config, server = server)
        self._inputs = InputsTimeOfMaxByEntity(self)
        self._outputs = OutputsTimeOfMaxByEntity(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)
        if compute_amplitude !=None:
            self.inputs.compute_amplitude.connect(compute_amplitude)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates time/frequency of maximum.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "abs_value", type_names=["bool"], optional=True, document="""Should use absolute value."""), 
                                 4 : PinSpecification(name = "compute_amplitude", type_names=["bool"], optional=True, document="""Do calculate amplitude.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "time_of_max_by_entity")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsTimeOfMaxByEntity 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsTimeOfMaxByEntity 
        """
        return super().outputs


#internal name: time_of_max_by_entity
#scripting name: time_of_max_by_entity
class InputsTimeOfMaxByEntity(_Inputs):
    """Intermediate class used to connect user inputs to time_of_max_by_entity operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.min_max.time_of_max_by_entity()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_compute_amplitude = bool()
      >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)
    """
    def __init__(self, op: Operator):
        super().__init__(time_of_max_by_entity._spec().inputs, op)
        self._fields_container = Input(time_of_max_by_entity._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._abs_value = Input(time_of_max_by_entity._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._abs_value)
        self._compute_amplitude = Input(time_of_max_by_entity._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._compute_amplitude)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.time_of_max_by_entity()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

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

        >>> op = dpf.operators.min_max.time_of_max_by_entity()
        >>> op.inputs.abs_value.connect(my_abs_value)
        >>> #or
        >>> op.inputs.abs_value(my_abs_value)

        """
        return self._abs_value

    @property
    def compute_amplitude(self):
        """Allows to connect compute_amplitude input to the operator

        - pindoc: Do calculate amplitude.

        Parameters
        ----------
        my_compute_amplitude : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.time_of_max_by_entity()
        >>> op.inputs.compute_amplitude.connect(my_compute_amplitude)
        >>> #or
        >>> op.inputs.compute_amplitude(my_compute_amplitude)

        """
        return self._compute_amplitude

class OutputsTimeOfMaxByEntity(_Outputs):
    """Intermediate class used to get outputs from time_of_max_by_entity operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.min_max.time_of_max_by_entity()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(time_of_max_by_entity._spec().outputs, op)
        self._fields_container = Output(time_of_max_by_entity._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.min_max.time_of_max_by_entity()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

