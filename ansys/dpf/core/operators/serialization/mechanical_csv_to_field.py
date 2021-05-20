"""
mechanical_csv_to_field
=======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "serialization" category
"""

class mechanical_csv_to_field(Operator):
    """Reads mechanical exported csv file

      available inputs:
        - unit ()
        - mesh (MeshedRegion) (optional)
        - data_sources (DataSources)
        - requested_location (str, FieldDefinition)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.serialization.mechanical_csv_to_field()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.serialization.mechanical_csv_to_field(mesh=my_mesh,data_sources=my_data_sources,requested_location=my_requested_location)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, mesh=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="mechanical_csv_to_field", config = config, server = server)
        self._inputs = InputsMechanicalCsvToField(self)
        self._outputs = OutputsMechanicalCsvToField(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Reads mechanical exported csv file""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "unit", type_names=[], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document=""""""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string","field_definition"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mechanical_csv_to_field")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMechanicalCsvToField 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMechanicalCsvToField 
        """
        return super().outputs


#internal name: mechanical_csv_to_field
#scripting name: mechanical_csv_to_field
class InputsMechanicalCsvToField(_Inputs):
    """Intermediate class used to connect user inputs to mechanical_csv_to_field operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.mechanical_csv_to_field()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
    """
    def __init__(self, op: Operator):
        super().__init__(mechanical_csv_to_field._spec().inputs, op)
        self._mesh = Input(mechanical_csv_to_field._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)
        self._data_sources = Input(mechanical_csv_to_field._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._requested_location = Input(mechanical_csv_to_field._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self._requested_location)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.mechanical_csv_to_field()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.mechanical_csv_to_field()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator

        Parameters
        ----------
        my_requested_location : str, FieldDefinition, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.mechanical_csv_to_field()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> #or
        >>> op.inputs.requested_location(my_requested_location)

        """
        return self._requested_location

class OutputsMechanicalCsvToField(_Outputs):
    """Intermediate class used to get outputs from mechanical_csv_to_field operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.mechanical_csv_to_field()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(mechanical_csv_to_field._spec().outputs, op)
        self._field = Output(mechanical_csv_to_field._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.serialization.mechanical_csv_to_field()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

