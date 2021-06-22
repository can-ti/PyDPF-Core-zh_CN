"""
scoping_on_coordinates
======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "mapping" category
"""

class scoping_on_coordinates(Operator):
    """Finds the Elemental scoping of a set of coordinates.

      available inputs:
        - coordinates (Field)
        - mesh (MeshedRegion)

      available outputs:
        - scoping (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mapping.scoping_on_coordinates()

      >>> # Make input connections
      >>> my_coordinates = dpf.Field()
      >>> op.inputs.coordinates.connect(my_coordinates)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mapping.scoping_on_coordinates(coordinates=my_coordinates,mesh=my_mesh)

      >>> # Get output data
      >>> result_scoping = op.outputs.scoping()"""
    def __init__(self, coordinates=None, mesh=None, config=None, server=None):
        super().__init__(name="scoping::on_coordinates", config = config, server = server)
        self._inputs = InputsScopingOnCoordinates(self)
        self._outputs = OutputsScopingOnCoordinates(self)
        if coordinates !=None:
            self.inputs.coordinates.connect(coordinates)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Finds the Elemental scoping of a set of coordinates.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "coordinates", type_names=["field"], optional=False, document=""""""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scoping::on_coordinates")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsScopingOnCoordinates 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsScopingOnCoordinates 
        """
        return super().outputs


#internal name: scoping::on_coordinates
#scripting name: scoping_on_coordinates
class InputsScopingOnCoordinates(_Inputs):
    """Intermediate class used to connect user inputs to scoping_on_coordinates operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.scoping_on_coordinates()
      >>> my_coordinates = dpf.Field()
      >>> op.inputs.coordinates.connect(my_coordinates)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(scoping_on_coordinates._spec().inputs, op)
        self._coordinates = Input(scoping_on_coordinates._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._coordinates)
        self._mesh = Input(scoping_on_coordinates._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def coordinates(self):
        """Allows to connect coordinates input to the operator

        Parameters
        ----------
        my_coordinates : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.scoping_on_coordinates()
        >>> op.inputs.coordinates.connect(my_coordinates)
        >>> #or
        >>> op.inputs.coordinates(my_coordinates)

        """
        return self._coordinates

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.scoping_on_coordinates()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsScopingOnCoordinates(_Outputs):
    """Intermediate class used to get outputs from scoping_on_coordinates operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.scoping_on_coordinates()
      >>> # Connect inputs : op.inputs. ...
      >>> result_scoping = op.outputs.scoping()
    """
    def __init__(self, op: Operator):
        super().__init__(scoping_on_coordinates._spec().outputs, op)
        self._scoping = Output(scoping_on_coordinates._spec().output_pin(0), 0, op) 
        self._outputs.append(self._scoping)

    @property
    def scoping(self):
        """Allows to get scoping output of the operator


        Returns
        ----------
        my_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.scoping_on_coordinates()
        >>> # Connect inputs : op.inputs. ...
        >>> result_scoping = op.outputs.scoping() 
        """
        return self._scoping

