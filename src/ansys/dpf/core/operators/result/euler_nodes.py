"""
euler_nodes
===========
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class euler_nodes(Operator):
    """read a field made of 3 coordinates and 3 Euler angles (6 dofs) by node
    from the rst file.

    Parameters
    ----------
    streams_container : StreamsContainer or Stream or Class
        Dataprocessing::Crstfilewrapper, optional
    data_sources : DataSources
    coord_and_euler : bool
        If true, then the field has ncomp=6 with 3
        oords and 3 euler angles, else there
        is only the euler angles (default is
        true)
    mesh : MeshedRegion, optional


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.euler_nodes()

    >>> # Make input connections
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_coord_and_euler = bool()
    >>> op.inputs.coord_and_euler.connect(my_coord_and_euler)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.euler_nodes(
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     coord_and_euler=my_coord_and_euler,
    ...     mesh=my_mesh,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        streams_container=None,
        data_sources=None,
        coord_and_euler=None,
        mesh=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="mapdl::rst::coords_and_euler_nodes", config=config, server=server
        )
        self._inputs = InputsEulerNodes(self)
        self._outputs = OutputsEulerNodes(self)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if coord_and_euler is not None:
            self.inputs.coord_and_euler.connect(coord_and_euler)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        description = """read a field made of 3 coordinates and 3 Euler angles (6 dofs) by node
            from the rst file."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                3: PinSpecification(
                    name="streams_container",
                    type_names=[
                        "streams_container",
                        "stream",
                        "class dataProcessing::CRstFileWrapper",
                    ],
                    optional=True,
                    document="""""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""""",
                ),
                6: PinSpecification(
                    name="coord_and_euler",
                    type_names=["bool"],
                    optional=False,
                    document="""If true, then the field has ncomp=6 with 3
        oords and 3 euler angles, else there
        is only the euler angles (default is
        true)""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=True,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
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
        return Operator.default_config(
            name="mapdl::rst::coords_and_euler_nodes", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsEulerNodes
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsEulerNodes
        """
        return super().outputs


class InputsEulerNodes(_Inputs):
    """Intermediate class used to connect user inputs to
    euler_nodes operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.euler_nodes()
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_coord_and_euler = bool()
    >>> op.inputs.coord_and_euler.connect(my_coord_and_euler)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    """

    def __init__(self, op: Operator):
        super().__init__(euler_nodes._spec().inputs, op)
        self._streams_container = Input(euler_nodes._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._streams_container)
        self._data_sources = Input(euler_nodes._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)
        self._coord_and_euler = Input(euler_nodes._spec().input_pin(6), 6, op, -1)
        self._inputs.append(self._coord_and_euler)
        self._mesh = Input(euler_nodes._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator.

        Parameters
        ----------
        my_streams_container : StreamsContainer or Stream or Class
        Dataprocessing::Crstfilewrapper

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_nodes()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_nodes()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def coord_and_euler(self):
        """Allows to connect coord_and_euler input to the operator.

        If true, then the field has ncomp=6 with 3
        oords and 3 euler angles, else there
        is only the euler angles (default is
        true)

        Parameters
        ----------
        my_coord_and_euler : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_nodes()
        >>> op.inputs.coord_and_euler.connect(my_coord_and_euler)
        >>> # or
        >>> op.inputs.coord_and_euler(my_coord_and_euler)
        """
        return self._coord_and_euler

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_nodes()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh


class OutputsEulerNodes(_Outputs):
    """Intermediate class used to get outputs from
    euler_nodes operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.euler_nodes()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(euler_nodes._spec().outputs, op)
        self._fields_container = Output(euler_nodes._spec().output_pin(0), 0, op)
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator

        Returns
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.euler_nodes()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
