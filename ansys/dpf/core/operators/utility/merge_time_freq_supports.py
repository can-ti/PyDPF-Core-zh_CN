"""
merge_time_freq_supports
========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class merge_time_freq_supports(Operator):
    """Take a set of time/freq support and assemble them in a unique one

      available inputs:
        - time_freq_supports1 (TimeFreqSupport)
        - time_freq_supports2 (TimeFreqSupport)

      available outputs:
        - merged_support (TimeFreqSupport)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_time_freq_supports()

      >>> # Make input connections
      >>> my_time_freq_supports1 = dpf.TimeFreqSupport()
      >>> op.inputs.time_freq_supports1.connect(my_time_freq_supports1)
      >>> my_time_freq_supports2 = dpf.TimeFreqSupport()
      >>> op.inputs.time_freq_supports2.connect(my_time_freq_supports2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_time_freq_supports(time_freq_supports1=my_time_freq_supports1,time_freq_supports2=my_time_freq_supports2)

      >>> # Get output data
      >>> result_merged_support = op.outputs.merged_support()"""
    def __init__(self, time_freq_supports1=None, time_freq_supports2=None, config=None, server=None):
        super().__init__(name="merge::time_freq_support", config = config, server = server)
        self._inputs = InputsMergeTimeFreqSupports(self)
        self._outputs = OutputsMergeTimeFreqSupports(self)
        if time_freq_supports1 !=None:
            self.inputs.time_freq_supports1.connect(time_freq_supports1)
        if time_freq_supports2 !=None:
            self.inputs.time_freq_supports2.connect(time_freq_supports2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of time/freq support and assemble them in a unique one""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_freq_supports", type_names=["time_freq_support"], optional=False, document="""A vector of time/freq supports to merge or time/freq supports from pin 0 to ..."""), 
                                 1 : PinSpecification(name = "time_freq_supports", type_names=["time_freq_support"], optional=False, document="""A vector of time/freq supports to merge or time/freq supports from pin 0 to ...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "merged_support", type_names=["time_freq_support"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::time_freq_support")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeTimeFreqSupports 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeTimeFreqSupports 
        """
        return super().outputs


#internal name: merge::time_freq_support
#scripting name: merge_time_freq_supports
class InputsMergeTimeFreqSupports(_Inputs):
    """Intermediate class used to connect user inputs to merge_time_freq_supports operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_time_freq_supports()
      >>> my_time_freq_supports1 = dpf.TimeFreqSupport()
      >>> op.inputs.time_freq_supports1.connect(my_time_freq_supports1)
      >>> my_time_freq_supports2 = dpf.TimeFreqSupport()
      >>> op.inputs.time_freq_supports2.connect(my_time_freq_supports2)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_time_freq_supports._spec().inputs, op)
        self._time_freq_supports1 = Input(merge_time_freq_supports._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self._time_freq_supports1)
        self._time_freq_supports2 = Input(merge_time_freq_supports._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self._time_freq_supports2)

    @property
    def time_freq_supports1(self):
        """Allows to connect time_freq_supports1 input to the operator

        - pindoc: A vector of time/freq supports to merge or time/freq supports from pin 0 to ...

        Parameters
        ----------
        my_time_freq_supports1 : TimeFreqSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_time_freq_supports()
        >>> op.inputs.time_freq_supports1.connect(my_time_freq_supports1)
        >>> #or
        >>> op.inputs.time_freq_supports1(my_time_freq_supports1)

        """
        return self._time_freq_supports1

    @property
    def time_freq_supports2(self):
        """Allows to connect time_freq_supports2 input to the operator

        - pindoc: A vector of time/freq supports to merge or time/freq supports from pin 0 to ...

        Parameters
        ----------
        my_time_freq_supports2 : TimeFreqSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_time_freq_supports()
        >>> op.inputs.time_freq_supports2.connect(my_time_freq_supports2)
        >>> #or
        >>> op.inputs.time_freq_supports2(my_time_freq_supports2)

        """
        return self._time_freq_supports2

class OutputsMergeTimeFreqSupports(_Outputs):
    """Intermediate class used to get outputs from merge_time_freq_supports operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_time_freq_supports()
      >>> # Connect inputs : op.inputs. ...
      >>> result_merged_support = op.outputs.merged_support()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_time_freq_supports._spec().outputs, op)
        self._merged_support = Output(merge_time_freq_supports._spec().output_pin(0), 0, op) 
        self._outputs.append(self._merged_support)

    @property
    def merged_support(self):
        """Allows to get merged_support output of the operator


        Returns
        ----------
        my_merged_support : TimeFreqSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_time_freq_supports()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_support = op.outputs.merged_support() 
        """
        return self._merged_support

