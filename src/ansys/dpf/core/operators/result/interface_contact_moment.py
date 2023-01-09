"""
interface_contact_moment
========================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class interface_contact_moment(Operator):
    """Read Interface Contact Moment (LSDyna) by calling the readers defined
    by the datasources.

    Parameters
    ----------
    streams_container : StreamsContainer, optional
        Result file container allowed to be kept open
        to cache data
    data_sources : DataSources
        Result file path container, used if no
        streams are set
    entity_scoping : Scoping, optional
        Entity (part for matsum, interface for
        rcforc) where the result will be
        scoped
    unit_system : int or str, optional
        Unit system id (int) or semicolon-separated
        list of base unit strings


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.interface_contact_moment()

    >>> # Make input connections
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_entity_scoping = dpf.Scoping()
    >>> op.inputs.entity_scoping.connect(my_entity_scoping)
    >>> my_unit_system = int()
    >>> op.inputs.unit_system.connect(my_unit_system)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.interface_contact_moment(
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     entity_scoping=my_entity_scoping,
    ...     unit_system=my_unit_system,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        streams_container=None,
        data_sources=None,
        entity_scoping=None,
        unit_system=None,
        config=None,
        server=None,
    ):
        super().__init__(name="R_CM", config=config, server=server)
        self._inputs = InputsInterfaceContactMoment(self)
        self._outputs = OutputsInterfaceContactMoment(self)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if entity_scoping is not None:
            self.inputs.entity_scoping.connect(entity_scoping)
        if unit_system is not None:
            self.inputs.unit_system.connect(unit_system)

    @staticmethod
    def _spec():
        description = """Read Interface Contact Moment (LSDyna) by calling the readers defined
            by the datasources."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=True,
                    document="""Result file container allowed to be kept open
        to cache data""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""Result file path container, used if no
        streams are set""",
                ),
                6: PinSpecification(
                    name="entity_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""Entity (part for matsum, interface for
        rcforc) where the result will be
        scoped""",
                ),
                50: PinSpecification(
                    name="unit_system",
                    type_names=["int32", "string"],
                    optional=True,
                    document="""Unit system id (int) or semicolon-separated
        list of base unit strings""",
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
        return Operator.default_config(name="R_CM", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsInterfaceContactMoment
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsInterfaceContactMoment
        """
        return super().outputs


class InputsInterfaceContactMoment(_Inputs):
    """Intermediate class used to connect user inputs to
    interface_contact_moment operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.interface_contact_moment()
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_entity_scoping = dpf.Scoping()
    >>> op.inputs.entity_scoping.connect(my_entity_scoping)
    >>> my_unit_system = int()
    >>> op.inputs.unit_system.connect(my_unit_system)
    """

    def __init__(self, op: Operator):
        super().__init__(interface_contact_moment._spec().inputs, op)
        self._streams_container = Input(
            interface_contact_moment._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(
            interface_contact_moment._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)
        self._entity_scoping = Input(
            interface_contact_moment._spec().input_pin(6), 6, op, -1
        )
        self._inputs.append(self._entity_scoping)
        self._unit_system = Input(
            interface_contact_moment._spec().input_pin(50), 50, op, -1
        )
        self._inputs.append(self._unit_system)

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator.

        Result file container allowed to be kept open
        to cache data

        Parameters
        ----------
        my_streams_container : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.interface_contact_moment()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Result file path container, used if no
        streams are set

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.interface_contact_moment()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def entity_scoping(self):
        """Allows to connect entity_scoping input to the operator.

        Entity (part for matsum, interface for
        rcforc) where the result will be
        scoped

        Parameters
        ----------
        my_entity_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.interface_contact_moment()
        >>> op.inputs.entity_scoping.connect(my_entity_scoping)
        >>> # or
        >>> op.inputs.entity_scoping(my_entity_scoping)
        """
        return self._entity_scoping

    @property
    def unit_system(self):
        """Allows to connect unit_system input to the operator.

        Unit system id (int) or semicolon-separated
        list of base unit strings

        Parameters
        ----------
        my_unit_system : int or str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.interface_contact_moment()
        >>> op.inputs.unit_system.connect(my_unit_system)
        >>> # or
        >>> op.inputs.unit_system(my_unit_system)
        """
        return self._unit_system


class OutputsInterfaceContactMoment(_Outputs):
    """Intermediate class used to get outputs from
    interface_contact_moment operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.interface_contact_moment()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(interface_contact_moment._spec().outputs, op)
        self._fields_container = Output(
            interface_contact_moment._spec().output_pin(0), 0, op
        )
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
        >>> op = dpf.operators.result.interface_contact_moment()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
