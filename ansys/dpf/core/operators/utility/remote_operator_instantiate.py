"""
remote_operator_instantiate
===========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class remote_operator_instantiate(Operator):
    """Create a local image of an existing remote operator (identified by an id and an address) for a given protocol registered in the streams. A workflow is created with this operator and returned in output

      available inputs:
        - operator_to_send (int)
        - output_pin (int)
        - streams_to_remote (StreamsContainer)
        - data_sources_to_remote (DataSources) (optional)
        - output_name (str)

      available outputs:
        - remote_workflow (Workflow)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.remote_operator_instantiate()

      >>> # Make input connections
      >>> my_operator_to_send = int()
      >>> op.inputs.operator_to_send.connect(my_operator_to_send)
      >>> my_output_pin = int()
      >>> op.inputs.output_pin.connect(my_output_pin)
      >>> my_streams_to_remote = dpf.StreamsContainer()
      >>> op.inputs.streams_to_remote.connect(my_streams_to_remote)
      >>> my_data_sources_to_remote = dpf.DataSources()
      >>> op.inputs.data_sources_to_remote.connect(my_data_sources_to_remote)
      >>> my_output_name = str()
      >>> op.inputs.output_name.connect(my_output_name)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.remote_operator_instantiate(operator_to_send=my_operator_to_send,output_pin=my_output_pin,streams_to_remote=my_streams_to_remote,data_sources_to_remote=my_data_sources_to_remote,output_name=my_output_name)

      >>> # Get output data
      >>> result_remote_workflow = op.outputs.remote_workflow()"""
    def __init__(self, operator_to_send=None, output_pin=None, streams_to_remote=None, data_sources_to_remote=None, output_name=None, config=None, server=None):
        super().__init__(name="remote_operator_instantiate", config = config, server = server)
        self._inputs = InputsRemoteOperatorInstantiate(self)
        self._outputs = OutputsRemoteOperatorInstantiate(self)
        if operator_to_send !=None:
            self.inputs.operator_to_send.connect(operator_to_send)
        if output_pin !=None:
            self.inputs.output_pin.connect(output_pin)
        if streams_to_remote !=None:
            self.inputs.streams_to_remote.connect(streams_to_remote)
        if data_sources_to_remote !=None:
            self.inputs.data_sources_to_remote.connect(data_sources_to_remote)
        if output_name !=None:
            self.inputs.output_name.connect(output_name)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create a local image of an existing remote operator (identified by an id and an address) for a given protocol registered in the streams. A workflow is created with this operator and returned in output""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "operator_to_send", type_names=["int32"], optional=False, document="""local workflow to push to a remote or id of a remote workflow"""), 
                                 1 : PinSpecification(name = "output_pin", type_names=["int32"], optional=False, document="""pin number of the output to name"""), 
                                 3 : PinSpecification(name = "streams_to_remote", type_names=["streams_container"], optional=False, document=""""""), 
                                 4 : PinSpecification(name = "data_sources_to_remote", type_names=["data_sources"], optional=True, document=""""""), 
                                 5 : PinSpecification(name = "output_name", type_names=["string"], optional=False, document="""output's name of the workflow to return""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "remote_workflow", type_names=["workflow"], optional=False, document="""remote workflow containing an image of the remote workflow and the protocols streams""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "remote_operator_instantiate")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRemoteOperatorInstantiate 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRemoteOperatorInstantiate 
        """
        return super().outputs


#internal name: remote_operator_instantiate
#scripting name: remote_operator_instantiate
class InputsRemoteOperatorInstantiate(_Inputs):
    """Intermediate class used to connect user inputs to remote_operator_instantiate operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.remote_operator_instantiate()
      >>> my_operator_to_send = int()
      >>> op.inputs.operator_to_send.connect(my_operator_to_send)
      >>> my_output_pin = int()
      >>> op.inputs.output_pin.connect(my_output_pin)
      >>> my_streams_to_remote = dpf.StreamsContainer()
      >>> op.inputs.streams_to_remote.connect(my_streams_to_remote)
      >>> my_data_sources_to_remote = dpf.DataSources()
      >>> op.inputs.data_sources_to_remote.connect(my_data_sources_to_remote)
      >>> my_output_name = str()
      >>> op.inputs.output_name.connect(my_output_name)
    """
    def __init__(self, op: Operator):
        super().__init__(remote_operator_instantiate._spec().inputs, op)
        self._operator_to_send = Input(remote_operator_instantiate._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._operator_to_send)
        self._output_pin = Input(remote_operator_instantiate._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._output_pin)
        self._streams_to_remote = Input(remote_operator_instantiate._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_to_remote)
        self._data_sources_to_remote = Input(remote_operator_instantiate._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources_to_remote)
        self._output_name = Input(remote_operator_instantiate._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._output_name)

    @property
    def operator_to_send(self):
        """Allows to connect operator_to_send input to the operator

        - pindoc: local workflow to push to a remote or id of a remote workflow

        Parameters
        ----------
        my_operator_to_send : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.remote_operator_instantiate()
        >>> op.inputs.operator_to_send.connect(my_operator_to_send)
        >>> #or
        >>> op.inputs.operator_to_send(my_operator_to_send)

        """
        return self._operator_to_send

    @property
    def output_pin(self):
        """Allows to connect output_pin input to the operator

        - pindoc: pin number of the output to name

        Parameters
        ----------
        my_output_pin : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.remote_operator_instantiate()
        >>> op.inputs.output_pin.connect(my_output_pin)
        >>> #or
        >>> op.inputs.output_pin(my_output_pin)

        """
        return self._output_pin

    @property
    def streams_to_remote(self):
        """Allows to connect streams_to_remote input to the operator

        Parameters
        ----------
        my_streams_to_remote : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.remote_operator_instantiate()
        >>> op.inputs.streams_to_remote.connect(my_streams_to_remote)
        >>> #or
        >>> op.inputs.streams_to_remote(my_streams_to_remote)

        """
        return self._streams_to_remote

    @property
    def data_sources_to_remote(self):
        """Allows to connect data_sources_to_remote input to the operator

        Parameters
        ----------
        my_data_sources_to_remote : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.remote_operator_instantiate()
        >>> op.inputs.data_sources_to_remote.connect(my_data_sources_to_remote)
        >>> #or
        >>> op.inputs.data_sources_to_remote(my_data_sources_to_remote)

        """
        return self._data_sources_to_remote

    @property
    def output_name(self):
        """Allows to connect output_name input to the operator

        - pindoc: output's name of the workflow to return

        Parameters
        ----------
        my_output_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.remote_operator_instantiate()
        >>> op.inputs.output_name.connect(my_output_name)
        >>> #or
        >>> op.inputs.output_name(my_output_name)

        """
        return self._output_name

class OutputsRemoteOperatorInstantiate(_Outputs):
    """Intermediate class used to get outputs from remote_operator_instantiate operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.remote_operator_instantiate()
      >>> # Connect inputs : op.inputs. ...
      >>> result_remote_workflow = op.outputs.remote_workflow()
    """
    def __init__(self, op: Operator):
        super().__init__(remote_operator_instantiate._spec().outputs, op)
        self._remote_workflow = Output(remote_operator_instantiate._spec().output_pin(0), 0, op) 
        self._outputs.append(self._remote_workflow)

    @property
    def remote_workflow(self):
        """Allows to get remote_workflow output of the operator


        - pindoc: remote workflow containing an image of the remote workflow and the protocols streams

        Returns
        ----------
        my_remote_workflow : Workflow, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.remote_operator_instantiate()
        >>> # Connect inputs : op.inputs. ...
        >>> result_remote_workflow = op.outputs.remote_workflow() 
        """
        return self._remote_workflow

