"""
find_reduced_coordinates
------------------------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class find_reduced_coordinates(Operator):
    """Find the elements corresponding to the given coordinates in input and
    compute their reduced coordinates in those elements.

    Parameters
    ----------
    coordinates : Field or FieldsContainer or MeshedRegion or MeshesContainer
    mesh : MeshedRegion or MeshesContainer, optional
        If the first field in input has no mesh in
        support, then the mesh in this pin is
        expected (default is false), if a
        meshes container with several meshes
        is set, it should be on the same
        label spaces as the coordinates
        fields container
    use_quadratic_elements : bool
        If this pin is set to true reduced
        coordinates are computed on the
        quadratic element if the element is
        quadratic (default is false)


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mapping.find_reduced_coordinates()

    >>> # Make input connections
    >>> my_coordinates = dpf.Field()
    >>> op.inputs.coordinates.connect(my_coordinates)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_use_quadratic_elements = bool()
    >>> op.inputs.use_quadratic_elements.connect(my_use_quadratic_elements)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mapping.find_reduced_coordinates(
    ...     coordinates=my_coordinates,
    ...     mesh=my_mesh,
    ...     use_quadratic_elements=my_use_quadratic_elements,
    ... )

    >>> # Get output data
    >>> result_reduced_coordinates = op.outputs.reduced_coordinates()
    >>> result_element_ids = op.outputs.element_ids()
    """

    def __init__(
        self,
        coordinates=None,
        mesh=None,
        use_quadratic_elements=None,
        config=None,
        server=None,
    ):
        super().__init__(name="find_reduced_coordinates", config=config, server=server)
        self._inputs = InputsFindReducedCoordinates(self)
        self._outputs = OutputsFindReducedCoordinates(self)
        if coordinates is not None:
            self.inputs.coordinates.connect(coordinates)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if use_quadratic_elements is not None:
            self.inputs.use_quadratic_elements.connect(use_quadratic_elements)

    @staticmethod
    def _spec():
        description = """Find the elements corresponding to the given coordinates in input and
            compute their reduced coordinates in those elements."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                1: PinSpecification(
                    name="coordinates",
                    type_names=[
                        "field",
                        "fields_container",
                        "abstract_meshed_region",
                        "meshes_container",
                    ],
                    optional=False,
                    document="""""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document="""If the first field in input has no mesh in
        support, then the mesh in this pin is
        expected (default is false), if a
        meshes container with several meshes
        is set, it should be on the same
        label spaces as the coordinates
        fields container""",
                ),
                200: PinSpecification(
                    name="use_quadratic_elements",
                    type_names=["bool"],
                    optional=False,
                    document="""If this pin is set to true reduced
        coordinates are computed on the
        quadratic element if the element is
        quadratic (default is false)""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="reduced_coordinates",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Coordinates in the reference elements""",
                ),
                1: PinSpecification(
                    name="element_ids",
                    type_names=["scopings_container"],
                    optional=False,
                    document="""Ids of the elements where each set of reduced
        coordinates is found""",
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
        return Operator.default_config(name="find_reduced_coordinates", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFindReducedCoordinates
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFindReducedCoordinates
        """
        return super().outputs


class InputsFindReducedCoordinates(_Inputs):
    """Intermediate class used to connect user inputs to
    find_reduced_coordinates operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mapping.find_reduced_coordinates()
    >>> my_coordinates = dpf.Field()
    >>> op.inputs.coordinates.connect(my_coordinates)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_use_quadratic_elements = bool()
    >>> op.inputs.use_quadratic_elements.connect(my_use_quadratic_elements)
    """

    def __init__(self, op: Operator):
        super().__init__(find_reduced_coordinates._spec().inputs, op)
        self._coordinates = Input(
            find_reduced_coordinates._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._coordinates)
        self._mesh = Input(find_reduced_coordinates._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)
        self._use_quadratic_elements = Input(
            find_reduced_coordinates._spec().input_pin(200), 200, op, -1
        )
        self._inputs.append(self._use_quadratic_elements)

    @property
    def coordinates(self):
        """Allows to connect coordinates input to the operator.

        Parameters
        ----------
        my_coordinates : Field or FieldsContainer or MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.find_reduced_coordinates()
        >>> op.inputs.coordinates.connect(my_coordinates)
        >>> # or
        >>> op.inputs.coordinates(my_coordinates)
        """
        return self._coordinates

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        If the first field in input has no mesh in
        support, then the mesh in this pin is
        expected (default is false), if a
        meshes container with several meshes
        is set, it should be on the same
        label spaces as the coordinates
        fields container

        Parameters
        ----------
        my_mesh : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.find_reduced_coordinates()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def use_quadratic_elements(self):
        """Allows to connect use_quadratic_elements input to the operator.

        If this pin is set to true reduced
        coordinates are computed on the
        quadratic element if the element is
        quadratic (default is false)

        Parameters
        ----------
        my_use_quadratic_elements : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.find_reduced_coordinates()
        >>> op.inputs.use_quadratic_elements.connect(my_use_quadratic_elements)
        >>> # or
        >>> op.inputs.use_quadratic_elements(my_use_quadratic_elements)
        """
        return self._use_quadratic_elements


class OutputsFindReducedCoordinates(_Outputs):
    """Intermediate class used to get outputs from
    find_reduced_coordinates operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mapping.find_reduced_coordinates()
    >>> # Connect inputs : op.inputs. ...
    >>> result_reduced_coordinates = op.outputs.reduced_coordinates()
    >>> result_element_ids = op.outputs.element_ids()
    """

    def __init__(self, op: Operator):
        super().__init__(find_reduced_coordinates._spec().outputs, op)
        self._reduced_coordinates = Output(
            find_reduced_coordinates._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._reduced_coordinates)
        self._element_ids = Output(
            find_reduced_coordinates._spec().output_pin(1), 1, op
        )
        self._outputs.append(self._element_ids)

    @property
    def reduced_coordinates(self):
        """Allows to get reduced_coordinates output of the operator

        Returns
        ----------
        my_reduced_coordinates : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.find_reduced_coordinates()
        >>> # Connect inputs : op.inputs. ...
        >>> result_reduced_coordinates = op.outputs.reduced_coordinates()
        """  # noqa: E501
        return self._reduced_coordinates

    @property
    def element_ids(self):
        """Allows to get element_ids output of the operator

        Returns
        ----------
        my_element_ids : ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.find_reduced_coordinates()
        >>> # Connect inputs : op.inputs. ...
        >>> result_element_ids = op.outputs.element_ids()
        """  # noqa: E501
        return self._element_ids
