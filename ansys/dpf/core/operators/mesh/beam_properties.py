"""
beam_properties
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "mesh" category
"""

class beam_properties(Operator):
    """Read beam's properties from the result files contained in the streams or data sources.

      available inputs:
        - streams (StreamsContainer) (optional)
        - data_sources (DataSources)

      available outputs:
        - mesh_out (MeshedRegion)
        - field_type_section_id (Field)
        - field_area (Field)
        - field_moment_inertia (Field)
        - field_geometry (Field)
        - field_young_modulus (Field)
        - field_poisson_ratio (Field)
        - field_shear_modulus (Field)
        - field_beam_length (Field)
        - field_torsion_constant (Field)
        - field_warping_constant (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.beam_properties()

      >>> # Make input connections
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.beam_properties(streams=my_streams,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_mesh_out = op.outputs.mesh_out()
      >>> result_field_type_section_id = op.outputs.field_type_section_id()
      >>> result_field_area = op.outputs.field_area()
      >>> result_field_moment_inertia = op.outputs.field_moment_inertia()
      >>> result_field_geometry = op.outputs.field_geometry()
      >>> result_field_young_modulus = op.outputs.field_young_modulus()
      >>> result_field_poisson_ratio = op.outputs.field_poisson_ratio()
      >>> result_field_shear_modulus = op.outputs.field_shear_modulus()
      >>> result_field_beam_length = op.outputs.field_beam_length()
      >>> result_field_torsion_constant = op.outputs.field_torsion_constant()
      >>> result_field_warping_constant = op.outputs.field_warping_constant()"""
    def __init__(self, streams=None, data_sources=None, config=None, server=None):
        super().__init__(name="beam_properties", config = config, server = server)
        self._inputs = InputsBeamProperties(self)
        self._outputs = OutputsBeamProperties(self)
        if streams !=None:
            self.inputs.streams.connect(streams)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read beam's properties from the result files contained in the streams or data sources.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams", type_names=["streams_container"], optional=True, document=""" result file container allowed to be kept open to cache data."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_out", type_names=["abstract_meshed_region"], optional=False, document="""This mesh updates a new map containing field of beam's properties if there is at least 1 beam in mesh."""), 
                                 1 : PinSpecification(name = "field_type_section_id", type_names=["field"], optional=False, document="""This field contains section ID of beams. 1:REC; 3:CSOLID, 4:CTUBE, 5:CHAN, 6:Z, 7:L, 8:I, 9:T, 11:HATS, 12:HREC."""), 
                                 2 : PinSpecification(name = "field_area", type_names=["field"], optional=False, document="""This field contains area of beams."""), 
                                 3 : PinSpecification(name = "field_moment_inertia", type_names=["field"], optional=False, document="""This field contains inertia moment of beams. Iyy, Iyz, Izz"""), 
                                 4 : PinSpecification(name = "field_geometry", type_names=["field"], optional=False, document="""This field contains geometry of beams. REC:b,h. CSOLID:Ri. CTUBE:Ri, Re. CHAN:w1,w2,w3,t1,t2,t3. Z:w1,w2,w3,t1,t2,t3. L:w1,w2,t1,t2. I:w1,w2,w3,t1,t2,t3. T:w1,w2,t1,t2. HATS: w1,w2,w3,w4,t1,t2,t3,t4. HREC:w1,w2,t1,t2,t3,t4."""), 
                                 5 : PinSpecification(name = "field_young_modulus", type_names=["field"], optional=False, document="""This field contains Young's modulus of beams."""), 
                                 6 : PinSpecification(name = "field_poisson_ratio", type_names=["field"], optional=False, document="""This field contains Poisson's ratio of beams."""), 
                                 7 : PinSpecification(name = "field_shear_modulus", type_names=["field"], optional=False, document="""This field contains Shear Modulus of beams."""), 
                                 8 : PinSpecification(name = "field_beam_length", type_names=["field"], optional=False, document="""This field contains length of beams."""), 
                                 9 : PinSpecification(name = "field_torsion_constant", type_names=["field"], optional=False, document="""This field contains Torsion Constant of beams."""), 
                                 10 : PinSpecification(name = "field_warping_constant", type_names=["field"], optional=False, document="""This field contains Warping Constant of beams.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "beam_properties")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsBeamProperties 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsBeamProperties 
        """
        return super().outputs


#internal name: beam_properties
#scripting name: beam_properties
class InputsBeamProperties(_Inputs):
    """Intermediate class used to connect user inputs to beam_properties operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.beam_properties()
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(beam_properties._spec().inputs, op)
        self._streams = Input(beam_properties._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams)
        self._data_sources = Input(beam_properties._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def streams(self):
        """Allows to connect streams input to the operator

        - pindoc:  result file container allowed to be kept open to cache data.

        Parameters
        ----------
        my_streams : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> op.inputs.streams.connect(my_streams)
        >>> #or
        >>> op.inputs.streams(my_streams)

        """
        return self._streams

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: result file path container, used if no streams are set.

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsBeamProperties(_Outputs):
    """Intermediate class used to get outputs from beam_properties operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.beam_properties()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh_out = op.outputs.mesh_out()
      >>> result_field_type_section_id = op.outputs.field_type_section_id()
      >>> result_field_area = op.outputs.field_area()
      >>> result_field_moment_inertia = op.outputs.field_moment_inertia()
      >>> result_field_geometry = op.outputs.field_geometry()
      >>> result_field_young_modulus = op.outputs.field_young_modulus()
      >>> result_field_poisson_ratio = op.outputs.field_poisson_ratio()
      >>> result_field_shear_modulus = op.outputs.field_shear_modulus()
      >>> result_field_beam_length = op.outputs.field_beam_length()
      >>> result_field_torsion_constant = op.outputs.field_torsion_constant()
      >>> result_field_warping_constant = op.outputs.field_warping_constant()
    """
    def __init__(self, op: Operator):
        super().__init__(beam_properties._spec().outputs, op)
        self._mesh_out = Output(beam_properties._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mesh_out)
        self._field_type_section_id = Output(beam_properties._spec().output_pin(1), 1, op) 
        self._outputs.append(self._field_type_section_id)
        self._field_area = Output(beam_properties._spec().output_pin(2), 2, op) 
        self._outputs.append(self._field_area)
        self._field_moment_inertia = Output(beam_properties._spec().output_pin(3), 3, op) 
        self._outputs.append(self._field_moment_inertia)
        self._field_geometry = Output(beam_properties._spec().output_pin(4), 4, op) 
        self._outputs.append(self._field_geometry)
        self._field_young_modulus = Output(beam_properties._spec().output_pin(5), 5, op) 
        self._outputs.append(self._field_young_modulus)
        self._field_poisson_ratio = Output(beam_properties._spec().output_pin(6), 6, op) 
        self._outputs.append(self._field_poisson_ratio)
        self._field_shear_modulus = Output(beam_properties._spec().output_pin(7), 7, op) 
        self._outputs.append(self._field_shear_modulus)
        self._field_beam_length = Output(beam_properties._spec().output_pin(8), 8, op) 
        self._outputs.append(self._field_beam_length)
        self._field_torsion_constant = Output(beam_properties._spec().output_pin(9), 9, op) 
        self._outputs.append(self._field_torsion_constant)
        self._field_warping_constant = Output(beam_properties._spec().output_pin(10), 10, op) 
        self._outputs.append(self._field_warping_constant)

    @property
    def mesh_out(self):
        """Allows to get mesh_out output of the operator


        - pindoc: This mesh updates a new map containing field of beam's properties if there is at least 1 beam in mesh.

        Returns
        ----------
        my_mesh_out : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh_out = op.outputs.mesh_out() 
        """
        return self._mesh_out

    @property
    def field_type_section_id(self):
        """Allows to get field_type_section_id output of the operator


        - pindoc: This field contains section ID of beams. 1:REC; 3:CSOLID, 4:CTUBE, 5:CHAN, 6:Z, 7:L, 8:I, 9:T, 11:HATS, 12:HREC.

        Returns
        ----------
        my_field_type_section_id : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_type_section_id = op.outputs.field_type_section_id() 
        """
        return self._field_type_section_id

    @property
    def field_area(self):
        """Allows to get field_area output of the operator


        - pindoc: This field contains area of beams.

        Returns
        ----------
        my_field_area : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_area = op.outputs.field_area() 
        """
        return self._field_area

    @property
    def field_moment_inertia(self):
        """Allows to get field_moment_inertia output of the operator


        - pindoc: This field contains inertia moment of beams. Iyy, Iyz, Izz

        Returns
        ----------
        my_field_moment_inertia : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_moment_inertia = op.outputs.field_moment_inertia() 
        """
        return self._field_moment_inertia

    @property
    def field_geometry(self):
        """Allows to get field_geometry output of the operator


        - pindoc: This field contains geometry of beams. REC:b,h. CSOLID:Ri. CTUBE:Ri, Re. CHAN:w1,w2,w3,t1,t2,t3. Z:w1,w2,w3,t1,t2,t3. L:w1,w2,t1,t2. I:w1,w2,w3,t1,t2,t3. T:w1,w2,t1,t2. HATS: w1,w2,w3,w4,t1,t2,t3,t4. HREC:w1,w2,t1,t2,t3,t4.

        Returns
        ----------
        my_field_geometry : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_geometry = op.outputs.field_geometry() 
        """
        return self._field_geometry

    @property
    def field_young_modulus(self):
        """Allows to get field_young_modulus output of the operator


        - pindoc: This field contains Young's modulus of beams.

        Returns
        ----------
        my_field_young_modulus : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_young_modulus = op.outputs.field_young_modulus() 
        """
        return self._field_young_modulus

    @property
    def field_poisson_ratio(self):
        """Allows to get field_poisson_ratio output of the operator


        - pindoc: This field contains Poisson's ratio of beams.

        Returns
        ----------
        my_field_poisson_ratio : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_poisson_ratio = op.outputs.field_poisson_ratio() 
        """
        return self._field_poisson_ratio

    @property
    def field_shear_modulus(self):
        """Allows to get field_shear_modulus output of the operator


        - pindoc: This field contains Shear Modulus of beams.

        Returns
        ----------
        my_field_shear_modulus : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_shear_modulus = op.outputs.field_shear_modulus() 
        """
        return self._field_shear_modulus

    @property
    def field_beam_length(self):
        """Allows to get field_beam_length output of the operator


        - pindoc: This field contains length of beams.

        Returns
        ----------
        my_field_beam_length : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_beam_length = op.outputs.field_beam_length() 
        """
        return self._field_beam_length

    @property
    def field_torsion_constant(self):
        """Allows to get field_torsion_constant output of the operator


        - pindoc: This field contains Torsion Constant of beams.

        Returns
        ----------
        my_field_torsion_constant : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_torsion_constant = op.outputs.field_torsion_constant() 
        """
        return self._field_torsion_constant

    @property
    def field_warping_constant(self):
        """Allows to get field_warping_constant output of the operator


        - pindoc: This field contains Warping Constant of beams.

        Returns
        ----------
        my_field_warping_constant : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.beam_properties()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_warping_constant = op.outputs.field_warping_constant() 
        """
        return self._field_warping_constant

