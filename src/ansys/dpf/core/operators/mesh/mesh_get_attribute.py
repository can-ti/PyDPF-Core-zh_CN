"""
mesh_get_attribute
==================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.outputs import _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class mesh_get_attribute(Operator):
    """Uses the MeshedRegion APIs to return a given attribute of the mesh in
    input.

    Parameters
    ----------
    abstract_meshed_region : MeshedRegion
    property_name : str
        Supported property names are: "connectivity",
        "reverse_connectivity", "mat",
        "faces_nodes_connectivity",
        "elements_faces_connectivity" (or any
        mesh's property field),
        "coordinates", "named_selection",
        "num_named_selections",
        "named_selection_names",
        "named_selection_locations",
        "node_scoping", "element_scoping",
        ace_scoping"...
    property_identifier : int or str, optional
        Can be used to get a property at a given
        index, example: a named selection's
        number or by name, example: a named
        selection's name.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.mesh_get_attribute()

    >>> # Make input connections
    >>> my_abstract_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)
    >>> my_property_identifier = int()
    >>> op.inputs.property_identifier.connect(my_property_identifier)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.mesh_get_attribute(
    ...     abstract_meshed_region=my_abstract_meshed_region,
    ...     property_name=my_property_name,
    ...     property_identifier=my_property_identifier,
    ... )

    >>> # Get output data
    >>> result_property = op.outputs.property()
    """

    def __init__(
        self,
        abstract_meshed_region=None,
        property_name=None,
        property_identifier=None,
        config=None,
        server=None,
    ):
        super().__init__(name="mesh::get_attribute", config=config, server=server)
        self._inputs = InputsMeshGetAttribute(self)
        self._outputs = OutputsMeshGetAttribute(self)
        if abstract_meshed_region is not None:
            self.inputs.abstract_meshed_region.connect(abstract_meshed_region)
        if property_name is not None:
            self.inputs.property_name.connect(property_name)
        if property_identifier is not None:
            self.inputs.property_identifier.connect(property_identifier)

    @staticmethod
    def _spec():
        description = """Uses the MeshedRegion APIs to return a given attribute of the mesh in
            input."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="abstract_meshed_region",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="property_name",
                    type_names=["string"],
                    optional=False,
                    document="""Supported property names are: "connectivity",
        "reverse_connectivity", "mat",
        "faces_nodes_connectivity",
        "elements_faces_connectivity" (or any
        mesh's property field),
        "coordinates", "named_selection",
        "num_named_selections",
        "named_selection_names",
        "named_selection_locations",
        "node_scoping", "element_scoping",
        ace_scoping"...""",
                ),
                2: PinSpecification(
                    name="property_identifier",
                    type_names=["int32", "string"],
                    optional=True,
                    document="""Can be used to get a property at a given
        index, example: a named selection's
        number or by name, example: a named
        selection's name.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="property",
                    type_names=[
                        "scoping",
                        "field",
                        "property_field",
                        "int32",
                        "string_field",
                    ],
                    optional=False,
                    document="""Returns a property field for properties:
        "connectivity",
        "reverse_connectivity", "mat",
        "faces_nodes_connectivity",
        "elements_faces_connectivity" (or any
        mesh's property field), a field for
        property: "coordinates", a scoping
        for properties:"named_selection",
        "node_scoping", "element_scoping",
        ace_scoping", a string field for
        properties: "named_selection_names",
        "named_selection_locations" and an
        int for property:
        "num_named_selections".""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server=None):
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server : server.DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="mesh::get_attribute", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMeshGetAttribute
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMeshGetAttribute
        """
        return super().outputs


class InputsMeshGetAttribute(_Inputs):
    """Intermediate class used to connect user inputs to
    mesh_get_attribute operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.mesh_get_attribute()
    >>> my_abstract_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)
    >>> my_property_identifier = int()
    >>> op.inputs.property_identifier.connect(my_property_identifier)
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_get_attribute._spec().inputs, op)
        self._abstract_meshed_region = Input(
            mesh_get_attribute._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._abstract_meshed_region)
        self._property_name = Input(mesh_get_attribute._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._property_name)
        self._property_identifier = Input(
            mesh_get_attribute._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._property_identifier)

    @property
    def abstract_meshed_region(self):
        """Allows to connect abstract_meshed_region input to the operator.

        Parameters
        ----------
        my_abstract_meshed_region : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_get_attribute()
        >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
        >>> # or
        >>> op.inputs.abstract_meshed_region(my_abstract_meshed_region)
        """
        return self._abstract_meshed_region

    @property
    def property_name(self):
        """Allows to connect property_name input to the operator.

        Supported property names are: "connectivity",
        "reverse_connectivity", "mat",
        "faces_nodes_connectivity",
        "elements_faces_connectivity" (or any
        mesh's property field),
        "coordinates", "named_selection",
        "num_named_selections",
        "named_selection_names",
        "named_selection_locations",
        "node_scoping", "element_scoping",
        ace_scoping"...

        Parameters
        ----------
        my_property_name : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_get_attribute()
        >>> op.inputs.property_name.connect(my_property_name)
        >>> # or
        >>> op.inputs.property_name(my_property_name)
        """
        return self._property_name

    @property
    def property_identifier(self):
        """Allows to connect property_identifier input to the operator.

        Can be used to get a property at a given
        index, example: a named selection's
        number or by name, example: a named
        selection's name.

        Parameters
        ----------
        my_property_identifier : int or str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.mesh_get_attribute()
        >>> op.inputs.property_identifier.connect(my_property_identifier)
        >>> # or
        >>> op.inputs.property_identifier(my_property_identifier)
        """
        return self._property_identifier


class OutputsMeshGetAttribute(_Outputs):
    """Intermediate class used to get outputs from
    mesh_get_attribute operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.mesh_get_attribute()
    >>> # Connect inputs : op.inputs. ...
    >>> result_property = op.outputs.property()
    """

    def __init__(self, op: Operator):
        super().__init__(mesh_get_attribute._spec().outputs, op)
        self.property_as_scoping = Output(
            _modify_output_spec_with_one_type(
                mesh_get_attribute._spec().output_pin(0), "scoping"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_scoping)
        self.property_as_field = Output(
            _modify_output_spec_with_one_type(
                mesh_get_attribute._spec().output_pin(0), "field"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_field)
        self.property_as_property_field = Output(
            _modify_output_spec_with_one_type(
                mesh_get_attribute._spec().output_pin(0), "property_field"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_property_field)
        self.property_as_int32 = Output(
            _modify_output_spec_with_one_type(
                mesh_get_attribute._spec().output_pin(0), "int32"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_int32)
        self.property_as_string_field = Output(
            _modify_output_spec_with_one_type(
                mesh_get_attribute._spec().output_pin(0), "string_field"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_string_field)
