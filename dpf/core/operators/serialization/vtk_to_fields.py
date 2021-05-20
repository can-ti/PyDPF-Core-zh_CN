"""
vtk_to_fields
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "serialization" category
"""

class vtk_to_fields(Operator):
    """Write a field based on a vtk file.

      available inputs:
        - field_name (str) (optional)
        - streams (StreamsContainer) (optional)
        - data_sources (DataSources)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.serialization.vtk_to_fields()

      >>> # Make input connections
      >>> my_field_name = str()
      >>> op.inputs.field_name.connect(my_field_name)
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.serialization.vtk_to_fields(field_name=my_field_name,streams=my_streams,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, field_name=None, streams=None, data_sources=None, config=None, server=None):
        super().__init__(name="vtk::vtk::FieldProvider", config = config, server = server)
        self._inputs = InputsVtkToFields(self)
        self._outputs = OutputsVtkToFields(self)
        if field_name !=None:
            self.inputs.field_name.connect(field_name)
        if streams !=None:
            self.inputs.streams.connect(streams)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Write a field based on a vtk file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field_name", type_names=["string"], optional=True, document="""name of the field in the vtk file"""), 
                                 3 : PinSpecification(name = "streams", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""fields_container""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "vtk::vtk::FieldProvider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsVtkToFields 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsVtkToFields 
        """
        return super().outputs


#internal name: vtk::vtk::FieldProvider
#scripting name: vtk_to_fields
class InputsVtkToFields(_Inputs):
    """Intermediate class used to connect user inputs to vtk_to_fields operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.vtk_to_fields()
      >>> my_field_name = str()
      >>> op.inputs.field_name.connect(my_field_name)
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(vtk_to_fields._spec().inputs, op)
        self._field_name = Input(vtk_to_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field_name)
        self._streams = Input(vtk_to_fields._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams)
        self._data_sources = Input(vtk_to_fields._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def field_name(self):
        """Allows to connect field_name input to the operator

        - pindoc: name of the field in the vtk file

        Parameters
        ----------
        my_field_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.vtk_to_fields()
        >>> op.inputs.field_name.connect(my_field_name)
        >>> #or
        >>> op.inputs.field_name(my_field_name)

        """
        return self._field_name

    @property
    def streams(self):
        """Allows to connect streams input to the operator

        Parameters
        ----------
        my_streams : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.vtk_to_fields()
        >>> op.inputs.streams.connect(my_streams)
        >>> #or
        >>> op.inputs.streams(my_streams)

        """
        return self._streams

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.vtk_to_fields()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsVtkToFields(_Outputs):
    """Intermediate class used to get outputs from vtk_to_fields operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.vtk_to_fields()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(vtk_to_fields._spec().outputs, op)
        self._fields_container = Output(vtk_to_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        - pindoc: fields_container

        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.vtk_to_fields()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

