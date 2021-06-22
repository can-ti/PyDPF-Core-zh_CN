"""
elemental_nodal_to_nodal_elemental
==================================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class elemental_nodal_to_nodal_elemental(Operator):
    """Transform ElementalNodal field to NodalElemental, compute result on a given node scoping.

      available inputs:
        - field (Field, FieldsContainer)
        - mesh_scoping (Scoping) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental(field=my_field,mesh_scoping=my_mesh_scoping)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="ElementalNodal_To_NodalElemental", config = config, server = server)
        self._inputs = InputsElementalNodalToNodalElemental(self)
        self._outputs = OutputsElementalNodalToNodalElemental(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal field to NodalElemental, compute result on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ElementalNodal_To_NodalElemental")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementalNodalToNodalElemental 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsElementalNodalToNodalElemental 
        """
        return super().outputs


#internal name: ElementalNodal_To_NodalElemental
#scripting name: elemental_nodal_to_nodal_elemental
class InputsElementalNodalToNodalElemental(_Inputs):
    """Intermediate class used to connect user inputs to elemental_nodal_to_nodal_elemental operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_elemental._spec().inputs, op)
        self._field = Input(elemental_nodal_to_nodal_elemental._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._mesh_scoping = Input(elemental_nodal_to_nodal_elemental._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)

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

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental()
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

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

class OutputsElementalNodalToNodalElemental(_Outputs):
    """Intermediate class used to get outputs from elemental_nodal_to_nodal_elemental operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_elemental._spec().outputs, op)
        self._field = Output(elemental_nodal_to_nodal_elemental._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_elemental()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

