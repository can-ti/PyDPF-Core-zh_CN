"""
part_eroded_kinetic_energy
==========================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class part_eroded_kinetic_energy(Operator):
    """Read Part Eroded Kinetic Energy (LSDyna) by calling the readers
    defined by the datasources.

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


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.part_eroded_kinetic_energy()

    >>> # Make input connections
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_entity_scoping = dpf.Scoping()
    >>> op.inputs.entity_scoping.connect(my_entity_scoping)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.part_eroded_kinetic_energy(
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     entity_scoping=my_entity_scoping,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        streams_container=None,
        data_sources=None,
        entity_scoping=None,
        config=None,
        server=None,
    ):
        super().__init__(name="M_ERKE", config=config, server=server)
        self._inputs = InputsPartErodedKineticEnergy(self)
        self._outputs = OutputsPartErodedKineticEnergy(self)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if entity_scoping is not None:
            self.inputs.entity_scoping.connect(entity_scoping)

    @staticmethod
    def _spec():
        description = """Read Part Eroded Kinetic Energy (LSDyna) by calling the readers
            defined by the datasources."""
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
        return Operator.default_config(name="M_ERKE", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPartErodedKineticEnergy
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPartErodedKineticEnergy
        """
        return super().outputs


class InputsPartErodedKineticEnergy(_Inputs):
    """Intermediate class used to connect user inputs to
    part_eroded_kinetic_energy operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.part_eroded_kinetic_energy()
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_entity_scoping = dpf.Scoping()
    >>> op.inputs.entity_scoping.connect(my_entity_scoping)
    """

    def __init__(self, op: Operator):
        super().__init__(part_eroded_kinetic_energy._spec().inputs, op)
        self._streams_container = Input(
            part_eroded_kinetic_energy._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(
            part_eroded_kinetic_energy._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)
        self._entity_scoping = Input(
            part_eroded_kinetic_energy._spec().input_pin(6), 6, op, -1
        )
        self._inputs.append(self._entity_scoping)

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
        >>> op = dpf.operators.result.part_eroded_kinetic_energy()
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
        >>> op = dpf.operators.result.part_eroded_kinetic_energy()
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
        >>> op = dpf.operators.result.part_eroded_kinetic_energy()
        >>> op.inputs.entity_scoping.connect(my_entity_scoping)
        >>> # or
        >>> op.inputs.entity_scoping(my_entity_scoping)
        """
        return self._entity_scoping


class OutputsPartErodedKineticEnergy(_Outputs):
    """Intermediate class used to get outputs from
    part_eroded_kinetic_energy operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.part_eroded_kinetic_energy()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(part_eroded_kinetic_energy._spec().outputs, op)
        self._fields_container = Output(
            part_eroded_kinetic_energy._spec().output_pin(0), 0, op
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
        >>> op = dpf.operators.result.part_eroded_kinetic_energy()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
