"""
compute_stress_1
================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class compute_stress_1(Operator):
    """Computes the stress from an elastic strain field. compute_total_strain
    limitations are applicable for stress computation Get the 1st
    principal component.

    Parameters
    ----------
    scoping : Scoping, optional
        The element scoping on which the result is
        computed.
    streams_container : StreamsContainer, optional
        Needed to get mesh and material ids. optional
        if a data_sources have been
        connected.
    data_sources : DataSources, optional
        Needed to get mesh and material ids. optional
        if a streams_container have been
        connected.
    requested_location : str, optional
        Average the elemental nodal result to the
        requested location.
    strain : FieldsContainer or Field
        Field/or fields container containing only the
        elastic strain field (element nodal).


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.compute_stress_1()

    >>> # Make input connections
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_requested_location = str()
    >>> op.inputs.requested_location.connect(my_requested_location)
    >>> my_strain = dpf.FieldsContainer()
    >>> op.inputs.strain.connect(my_strain)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.compute_stress_1(
    ...     scoping=my_scoping,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     requested_location=my_requested_location,
    ...     strain=my_strain,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        scoping=None,
        streams_container=None,
        data_sources=None,
        requested_location=None,
        strain=None,
        config=None,
        server=None,
    ):
        super().__init__(name="compute_stress_1", config=config, server=server)
        self._inputs = InputsComputeStress1(self)
        self._outputs = OutputsComputeStress1(self)
        if scoping is not None:
            self.inputs.scoping.connect(scoping)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location is not None:
            self.inputs.requested_location.connect(requested_location)
        if strain is not None:
            self.inputs.strain.connect(strain)

    @staticmethod
    def _spec():
        description = """Computes the stress from an elastic strain field. compute_total_strain
            limitations are applicable for stress computation Get the
            1st principal component."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                1: PinSpecification(
                    name="scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""The element scoping on which the result is
        computed.""",
                ),
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=True,
                    document="""Needed to get mesh and material ids. optional
        if a data_sources have been
        connected.""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=True,
                    document="""Needed to get mesh and material ids. optional
        if a streams_container have been
        connected.""",
                ),
                9: PinSpecification(
                    name="requested_location",
                    type_names=["string"],
                    optional=True,
                    document="""Average the elemental nodal result to the
        requested location.""",
                ),
                10: PinSpecification(
                    name="strain",
                    type_names=["fields_container", "field"],
                    optional=False,
                    document="""Field/or fields container containing only the
        elastic strain field (element nodal).""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""The computed result fields container
        (elemental nodal).""",
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
        return Operator.default_config(name="compute_stress_1", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsComputeStress1
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsComputeStress1
        """
        return super().outputs


class InputsComputeStress1(_Inputs):
    """Intermediate class used to connect user inputs to
    compute_stress_1 operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.compute_stress_1()
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_requested_location = str()
    >>> op.inputs.requested_location.connect(my_requested_location)
    >>> my_strain = dpf.FieldsContainer()
    >>> op.inputs.strain.connect(my_strain)
    """

    def __init__(self, op: Operator):
        super().__init__(compute_stress_1._spec().inputs, op)
        self._scoping = Input(compute_stress_1._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._scoping)
        self._streams_container = Input(
            compute_stress_1._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(compute_stress_1._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)
        self._requested_location = Input(
            compute_stress_1._spec().input_pin(9), 9, op, -1
        )
        self._inputs.append(self._requested_location)
        self._strain = Input(compute_stress_1._spec().input_pin(10), 10, op, -1)
        self._inputs.append(self._strain)

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator.

        The element scoping on which the result is
        computed.

        Parameters
        ----------
        my_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_stress_1()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> # or
        >>> op.inputs.scoping(my_scoping)
        """
        return self._scoping

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator.

        Needed to get mesh and material ids. optional
        if a data_sources have been
        connected.

        Parameters
        ----------
        my_streams_container : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_stress_1()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Needed to get mesh and material ids. optional
        if a streams_container have been
        connected.

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_stress_1()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator.

        Average the elemental nodal result to the
        requested location.

        Parameters
        ----------
        my_requested_location : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_stress_1()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> # or
        >>> op.inputs.requested_location(my_requested_location)
        """
        return self._requested_location

    @property
    def strain(self):
        """Allows to connect strain input to the operator.

        Field/or fields container containing only the
        elastic strain field (element nodal).

        Parameters
        ----------
        my_strain : FieldsContainer or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_stress_1()
        >>> op.inputs.strain.connect(my_strain)
        >>> # or
        >>> op.inputs.strain(my_strain)
        """
        return self._strain


class OutputsComputeStress1(_Outputs):
    """Intermediate class used to get outputs from
    compute_stress_1 operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.compute_stress_1()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(compute_stress_1._spec().outputs, op)
        self._fields_container = Output(compute_stress_1._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.result.compute_stress_1()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
