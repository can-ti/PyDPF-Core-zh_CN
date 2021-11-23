"""
on_reduced_coordinates
======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "mapping" category
"""

class on_reduced_coordinates(Operator):
    """Evaluates a result on specified reduced coordinates of given elements (interpolates results inside elements with shape functions).

      available inputs:
        - fields_container (FieldsContainer)
        - reduced_coordinates (Field, FieldsContainer)
        - element_ids (ScopingsContainer)
        - mesh (MeshedRegion, MeshesContainer) (optional)
        - use_quadratic_elements (bool)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mapping.on_reduced_coordinates()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_reduced_coordinates = dpf.Field()
      >>> op.inputs.reduced_coordinates.connect(my_reduced_coordinates)
      >>> my_element_ids = dpf.ScopingsContainer()
      >>> op.inputs.element_ids.connect(my_element_ids)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_use_quadratic_elements = bool()
      >>> op.inputs.use_quadratic_elements.connect(my_use_quadratic_elements)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mapping.on_reduced_coordinates(fields_container=my_fields_container,reduced_coordinates=my_reduced_coordinates,element_ids=my_element_ids,mesh=my_mesh,use_quadratic_elements=my_use_quadratic_elements)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, reduced_coordinates=None, element_ids=None, mesh=None, use_quadratic_elements=None, config=None, server=None):
        super().__init__(name="interpolation_operator", config = config, server = server)
        self._inputs = InputsOnReducedCoordinates(self)
        self._outputs = OutputsOnReducedCoordinates(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if reduced_coordinates !=None:
            self.inputs.reduced_coordinates.connect(reduced_coordinates)
        if element_ids !=None:
            self.inputs.element_ids.connect(element_ids)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if use_quadratic_elements !=None:
            self.inputs.use_quadratic_elements.connect(use_quadratic_elements)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates a result on specified reduced coordinates of given elements (interpolates results inside elements with shape functions).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "reduced_coordinates", type_names=["field","fields_container"], optional=False, document="""coordinates in the reference elements to find (found with the operator "find_reduced_coordinates")"""), 
                                 2 : PinSpecification(name = "element_ids", type_names=["scopings_container"], optional=False, document="""Ids of the elements where each set of reduced coordinates is found (found with the operator "find_reduced_coordinates")"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""if the first field in input has no mesh in support, then the mesh in this pin is expected (default is false), if a meshes container with several meshes is set, it should be on the same label spaces as the coordinates fields container"""), 
                                 200 : PinSpecification(name = "use_quadratic_elements", type_names=["bool"], optional=False, document="""If this pin is set to true interpolation is computed on the quadratic element if the element is quadratic (default is false). To use only when results have mid side nodes values.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "interpolation_operator")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsOnReducedCoordinates 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsOnReducedCoordinates 
        """
        return super().outputs


#internal name: interpolation_operator
#scripting name: on_reduced_coordinates
class InputsOnReducedCoordinates(_Inputs):
    """Intermediate class used to connect user inputs to on_reduced_coordinates operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.on_reduced_coordinates()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_reduced_coordinates = dpf.Field()
      >>> op.inputs.reduced_coordinates.connect(my_reduced_coordinates)
      >>> my_element_ids = dpf.ScopingsContainer()
      >>> op.inputs.element_ids.connect(my_element_ids)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_use_quadratic_elements = bool()
      >>> op.inputs.use_quadratic_elements.connect(my_use_quadratic_elements)
    """
    def __init__(self, op: Operator):
        super().__init__(on_reduced_coordinates._spec().inputs, op)
        self._fields_container = Input(on_reduced_coordinates._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._reduced_coordinates = Input(on_reduced_coordinates._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._reduced_coordinates)
        self._element_ids = Input(on_reduced_coordinates._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._element_ids)
        self._mesh = Input(on_reduced_coordinates._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)
        self._use_quadratic_elements = Input(on_reduced_coordinates._spec().input_pin(200), 200, op, -1) 
        self._inputs.append(self._use_quadratic_elements)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_reduced_coordinates()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def reduced_coordinates(self):
        """Allows to connect reduced_coordinates input to the operator

        - pindoc: coordinates in the reference elements to find (found with the operator "find_reduced_coordinates")

        Parameters
        ----------
        my_reduced_coordinates : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_reduced_coordinates()
        >>> op.inputs.reduced_coordinates.connect(my_reduced_coordinates)
        >>> #or
        >>> op.inputs.reduced_coordinates(my_reduced_coordinates)

        """
        return self._reduced_coordinates

    @property
    def element_ids(self):
        """Allows to connect element_ids input to the operator

        - pindoc: Ids of the elements where each set of reduced coordinates is found (found with the operator "find_reduced_coordinates")

        Parameters
        ----------
        my_element_ids : ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_reduced_coordinates()
        >>> op.inputs.element_ids.connect(my_element_ids)
        >>> #or
        >>> op.inputs.element_ids(my_element_ids)

        """
        return self._element_ids

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: if the first field in input has no mesh in support, then the mesh in this pin is expected (default is false), if a meshes container with several meshes is set, it should be on the same label spaces as the coordinates fields container

        Parameters
        ----------
        my_mesh : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_reduced_coordinates()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def use_quadratic_elements(self):
        """Allows to connect use_quadratic_elements input to the operator

        - pindoc: If this pin is set to true interpolation is computed on the quadratic element if the element is quadratic (default is false). To use only when results have mid side nodes values.

        Parameters
        ----------
        my_use_quadratic_elements : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_reduced_coordinates()
        >>> op.inputs.use_quadratic_elements.connect(my_use_quadratic_elements)
        >>> #or
        >>> op.inputs.use_quadratic_elements(my_use_quadratic_elements)

        """
        return self._use_quadratic_elements

class OutputsOnReducedCoordinates(_Outputs):
    """Intermediate class used to get outputs from on_reduced_coordinates operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.on_reduced_coordinates()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(on_reduced_coordinates._spec().outputs, op)
        self._fields_container = Output(on_reduced_coordinates._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_reduced_coordinates()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

