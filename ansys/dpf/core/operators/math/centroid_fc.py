"""
centroid_fc
===========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class centroid_fc(Operator):
    """Computes the centroid of all the matching fields of a fields container at a given time or frequency, using fieldOut = field1*(1.-fact)+field2*(fact).

      available inputs:
        - fields_container (FieldsContainer)
        - time_freq (float)
        - step (int) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.centroid_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_time_freq = float()
      >>> op.inputs.time_freq.connect(my_time_freq)
      >>> my_step = int()
      >>> op.inputs.step.connect(my_step)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.centroid_fc(fields_container=my_fields_container,time_freq=my_time_freq,step=my_step)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, time_freq=None, step=None, config=None, server=None):
        super().__init__(name="centroid_fc", config = config, server = server)
        self._inputs = InputsCentroidFc(self)
        self._outputs = OutputsCentroidFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if time_freq !=None:
            self.inputs.time_freq.connect(time_freq)
        if step !=None:
            self.inputs.step.connect(step)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the centroid of all the matching fields of a fields container at a given time or frequency, using fieldOut = field1*(1.-fact)+field2*(fact).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "time_freq", type_names=["double"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "step", type_names=["int32"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "centroid_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCentroidFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCentroidFc 
        """
        return super().outputs


#internal name: centroid_fc
#scripting name: centroid_fc
class InputsCentroidFc(_Inputs):
    """Intermediate class used to connect user inputs to centroid_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.centroid_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_time_freq = float()
      >>> op.inputs.time_freq.connect(my_time_freq)
      >>> my_step = int()
      >>> op.inputs.step.connect(my_step)
    """
    def __init__(self, op: Operator):
        super().__init__(centroid_fc._spec().inputs, op)
        self._fields_container = Input(centroid_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._time_freq = Input(centroid_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._time_freq)
        self._step = Input(centroid_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._step)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.centroid_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def time_freq(self):
        """Allows to connect time_freq input to the operator

        Parameters
        ----------
        my_time_freq : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.centroid_fc()
        >>> op.inputs.time_freq.connect(my_time_freq)
        >>> #or
        >>> op.inputs.time_freq(my_time_freq)

        """
        return self._time_freq

    @property
    def step(self):
        """Allows to connect step input to the operator

        Parameters
        ----------
        my_step : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.centroid_fc()
        >>> op.inputs.step.connect(my_step)
        >>> #or
        >>> op.inputs.step(my_step)

        """
        return self._step

class OutputsCentroidFc(_Outputs):
    """Intermediate class used to get outputs from centroid_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.centroid_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(centroid_fc._spec().outputs, op)
        self._fields_container = Output(centroid_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.math.centroid_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

