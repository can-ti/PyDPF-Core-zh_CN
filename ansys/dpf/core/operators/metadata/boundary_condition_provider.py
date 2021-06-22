"""
boundary_condition_provider
===========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "metadata" category
"""

class boundary_condition_provider(Operator):
    """Read boundary conditions from the results files contained in the streams or data sources.

      available inputs:
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)

      available outputs:
        - results_info (Field ,FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.boundary_condition_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.metadata.boundary_condition_provider(streams_container=my_streams_container,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_results_info = op.outputs.results_info()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="boundary_conditions", config = config, server = server)
        self._inputs = InputsBoundaryConditionProvider(self)
        self._outputs = OutputsBoundaryConditionProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read boundary conditions from the results files contained in the streams or data sources.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "results_info", type_names=["field","fields_container"], optional=False, document="""results info""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "boundary_conditions")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsBoundaryConditionProvider 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsBoundaryConditionProvider 
        """
        return super().outputs


#internal name: boundary_conditions
#scripting name: boundary_condition_provider
class InputsBoundaryConditionProvider(_Inputs):
    """Intermediate class used to connect user inputs to boundary_condition_provider operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.boundary_condition_provider()
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(boundary_condition_provider._spec().inputs, op)
        self._streams_container = Input(boundary_condition_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(boundary_condition_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.boundary_condition_provider()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.boundary_condition_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsBoundaryConditionProvider(_Outputs):
    """Intermediate class used to get outputs from boundary_condition_provider operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.boundary_condition_provider()
      >>> # Connect inputs : op.inputs. ...
      >>> result_results_info = op.outputs.results_info()
    """
    def __init__(self, op: Operator):
        super().__init__(boundary_condition_provider._spec().outputs, op)
        self.results_info_as_field = Output( _modify_output_spec_with_one_type(boundary_condition_provider._spec().output_pin(0), "field"), 0, op) 
        self._outputs.append(self.results_info_as_field)
        self.results_info_as_fields_container = Output( _modify_output_spec_with_one_type(boundary_condition_provider._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.results_info_as_fields_container)

