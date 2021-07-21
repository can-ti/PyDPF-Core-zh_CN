"""
on_mesh_property
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "scoping" category
"""

class on_mesh_property(Operator):
    """Provides a scoping on a given property name and a property number.

      available inputs:
        - requested_location (str) (optional)
        - property_name (str)
        - property_id (int) (optional)
        - inclusive (int) (optional)
        - mesh (MeshedRegion)

      available outputs:
        - mesh_scoping (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.scoping.on_mesh_property()

      >>> # Make input connections
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
      >>> my_property_name = str()
      >>> op.inputs.property_name.connect(my_property_name)
      >>> my_property_id = int()
      >>> op.inputs.property_id.connect(my_property_id)
      >>> my_inclusive = int()
      >>> op.inputs.inclusive.connect(my_inclusive)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.scoping.on_mesh_property(requested_location=my_requested_location,property_name=my_property_name,property_id=my_property_id,inclusive=my_inclusive,mesh=my_mesh)

      >>> # Get output data
      >>> result_mesh_scoping = op.outputs.mesh_scoping()"""
    def __init__(self, requested_location=None, property_name=None, property_id=None, inclusive=None, mesh=None, config=None, server=None):
        super().__init__(name="meshscoping_provider_by_prop", config = config, server = server)
        self._inputs = InputsOnMeshProperty(self)
        self._outputs = OutputsOnMeshProperty(self)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if property_name !=None:
            self.inputs.property_name.connect(property_name)
        if property_id !=None:
            self.inputs.property_id.connect(property_id)
        if inclusive !=None:
            self.inputs.inclusive.connect(inclusive)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Provides a scoping on a given property name and a property number.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""Nodal or Elemental location are expected"""), 
                                 1 : PinSpecification(name = "property_name", type_names=["string"], optional=False, document="""ex "mapdl_element_type", "apdl_type_index", "mapdl_type_id", "material", "shell_elements", "solid_elements", "skin_elements", "beam_elements", "point_elements"..."""), 
                                 2 : PinSpecification(name = "property_id", type_names=["int32"], optional=True, document=""""""), 
                                 5 : PinSpecification(name = "inclusive", type_names=["int32"], optional=True, document="""If element scoping is requested on a nodal named selection, if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document="""Scoping""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "meshscoping_provider_by_prop")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsOnMeshProperty 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsOnMeshProperty 
        """
        return super().outputs


#internal name: meshscoping_provider_by_prop
#scripting name: on_mesh_property
class InputsOnMeshProperty(_Inputs):
    """Intermediate class used to connect user inputs to on_mesh_property operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.on_mesh_property()
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
      >>> my_property_name = str()
      >>> op.inputs.property_name.connect(my_property_name)
      >>> my_property_id = int()
      >>> op.inputs.property_id.connect(my_property_id)
      >>> my_inclusive = int()
      >>> op.inputs.inclusive.connect(my_inclusive)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(on_mesh_property._spec().inputs, op)
        self._requested_location = Input(on_mesh_property._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._requested_location)
        self._property_name = Input(on_mesh_property._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._property_name)
        self._property_id = Input(on_mesh_property._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._property_id)
        self._inclusive = Input(on_mesh_property._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._inclusive)
        self._mesh = Input(on_mesh_property._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator

        - pindoc: Nodal or Elemental location are expected

        Parameters
        ----------
        my_requested_location : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_mesh_property()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> #or
        >>> op.inputs.requested_location(my_requested_location)

        """
        return self._requested_location

    @property
    def property_name(self):
        """Allows to connect property_name input to the operator

        - pindoc: ex "mapdl_element_type", "apdl_type_index", "mapdl_type_id", "material", "shell_elements", "solid_elements", "skin_elements", "beam_elements", "point_elements"...

        Parameters
        ----------
        my_property_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_mesh_property()
        >>> op.inputs.property_name.connect(my_property_name)
        >>> #or
        >>> op.inputs.property_name(my_property_name)

        """
        return self._property_name

    @property
    def property_id(self):
        """Allows to connect property_id input to the operator

        Parameters
        ----------
        my_property_id : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_mesh_property()
        >>> op.inputs.property_id.connect(my_property_id)
        >>> #or
        >>> op.inputs.property_id(my_property_id)

        """
        return self._property_id

    @property
    def inclusive(self):
        """Allows to connect inclusive input to the operator

        - pindoc: If element scoping is requested on a nodal named selection, if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included

        Parameters
        ----------
        my_inclusive : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_mesh_property()
        >>> op.inputs.inclusive.connect(my_inclusive)
        >>> #or
        >>> op.inputs.inclusive(my_inclusive)

        """
        return self._inclusive

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_mesh_property()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsOnMeshProperty(_Outputs):
    """Intermediate class used to get outputs from on_mesh_property operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.on_mesh_property()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """
    def __init__(self, op: Operator):
        super().__init__(on_mesh_property._spec().outputs, op)
        self._mesh_scoping = Output(on_mesh_property._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mesh_scoping)

    @property
    def mesh_scoping(self):
        """Allows to get mesh_scoping output of the operator


        - pindoc: Scoping

        Returns
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_mesh_property()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh_scoping = op.outputs.mesh_scoping() 
        """
        return self._mesh_scoping

