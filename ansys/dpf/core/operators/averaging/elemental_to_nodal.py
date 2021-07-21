"""
elemental_to_nodal
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class elemental_to_nodal(Operator):
    """Transform ElementalNodal field to Nodal field, compute result on a given node scoping.

      available inputs:
        - field (Field, FieldsContainer)
        - mesh_scoping (Scoping) (optional)
        - force_averaging (int) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_to_nodal()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_force_averaging = int()
      >>> op.inputs.force_averaging.connect(my_force_averaging)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.elemental_to_nodal(field=my_field,mesh_scoping=my_mesh_scoping,force_averaging=my_force_averaging)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, mesh_scoping=None, force_averaging=None, config=None, server=None):
        super().__init__(name="elemental_to_nodal", config = config, server = server)
        self._inputs = InputsElementalToNodal(self)
        self._outputs = OutputsElementalToNodal(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if force_averaging !=None:
            self.inputs.force_averaging.connect(force_averaging)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal field to Nodal field, compute result on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "force_averaging", type_names=["int32"], optional=True, document="""averaging on nodes is used if this pin is set to 1 (default is 1 for integrated results and 0 for discrete ones)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_to_nodal")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementalToNodal 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsElementalToNodal 
        """
        return super().outputs


#internal name: elemental_to_nodal
#scripting name: elemental_to_nodal
class InputsElementalToNodal(_Inputs):
    """Intermediate class used to connect user inputs to elemental_to_nodal operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_to_nodal()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_force_averaging = int()
      >>> op.inputs.force_averaging.connect(my_force_averaging)
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_to_nodal._spec().inputs, op)
        self._field = Input(elemental_to_nodal._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._mesh_scoping = Input(elemental_to_nodal._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._force_averaging = Input(elemental_to_nodal._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._force_averaging)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_to_nodal()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_to_nodal()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def force_averaging(self):
        """Allows to connect force_averaging input to the operator

        - pindoc: averaging on nodes is used if this pin is set to 1 (default is 1 for integrated results and 0 for discrete ones)

        Parameters
        ----------
        my_force_averaging : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_to_nodal()
        >>> op.inputs.force_averaging.connect(my_force_averaging)
        >>> #or
        >>> op.inputs.force_averaging(my_force_averaging)

        """
        return self._force_averaging

class OutputsElementalToNodal(_Outputs):
    """Intermediate class used to get outputs from elemental_to_nodal operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_to_nodal()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_to_nodal._spec().outputs, op)
        self._field = Output(elemental_to_nodal._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.averaging.elemental_to_nodal()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

