"""
migrate_file_to_vtk
===================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "serialization" category
"""

class migrate_file_to_vtk(Operator):
    """Take an input data sources or streams and convert as much data as possible to vtk.

      available inputs:
        - output_filename (str) (optional)
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources) (optional)

      available outputs:
        - data_sources (DataSources)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.serialization.migrate_file_to_vtk()

      >>> # Make input connections
      >>> my_output_filename = str()
      >>> op.inputs.output_filename.connect(my_output_filename)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.serialization.migrate_file_to_vtk(output_filename=my_output_filename,streams_container=my_streams_container,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_data_sources = op.outputs.data_sources()"""
    def __init__(self, output_filename=None, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="vtk::migrate_file", config = config, server = server)
        self._inputs = InputsMigrateFileToVtk(self)
        self._outputs = OutputsMigrateFileToVtk(self)
        if output_filename !=None:
            self.inputs.output_filename.connect(output_filename)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take an input data sources or streams and convert as much data as possible to vtk.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "output_filename", type_names=["string"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""Generated output vtk file""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "vtk::migrate_file")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMigrateFileToVtk 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMigrateFileToVtk 
        """
        return super().outputs


#internal name: vtk::migrate_file
#scripting name: migrate_file_to_vtk
class InputsMigrateFileToVtk(_Inputs):
    """Intermediate class used to connect user inputs to migrate_file_to_vtk operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.migrate_file_to_vtk()
      >>> my_output_filename = str()
      >>> op.inputs.output_filename.connect(my_output_filename)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(migrate_file_to_vtk._spec().inputs, op)
        self._output_filename = Input(migrate_file_to_vtk._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._output_filename)
        self._streams_container = Input(migrate_file_to_vtk._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(migrate_file_to_vtk._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def output_filename(self):
        """Allows to connect output_filename input to the operator

        Parameters
        ----------
        my_output_filename : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.migrate_file_to_vtk()
        >>> op.inputs.output_filename.connect(my_output_filename)
        >>> #or
        >>> op.inputs.output_filename(my_output_filename)

        """
        return self._output_filename

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.migrate_file_to_vtk()
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

        >>> op = dpf.operators.serialization.migrate_file_to_vtk()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsMigrateFileToVtk(_Outputs):
    """Intermediate class used to get outputs from migrate_file_to_vtk operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.migrate_file_to_vtk()
      >>> # Connect inputs : op.inputs. ...
      >>> result_data_sources = op.outputs.data_sources()
    """
    def __init__(self, op: Operator):
        super().__init__(migrate_file_to_vtk._spec().outputs, op)
        self._data_sources = Output(migrate_file_to_vtk._spec().output_pin(0), 0, op) 
        self._outputs.append(self._data_sources)

    @property
    def data_sources(self):
        """Allows to get data_sources output of the operator


        - pindoc: Generated output vtk file

        Returns
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.migrate_file_to_vtk()
        >>> # Connect inputs : op.inputs. ...
        >>> result_data_sources = op.outputs.data_sources() 
        """
        return self._data_sources

