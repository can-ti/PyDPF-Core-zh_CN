"""
global_energy_ratio_wo_eroded
=============================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class global_energy_ratio_wo_eroded(Operator):
    """Read Global Energy ratio without Eroded Energy (LSDyna) by calling the
    readers defined by the datasources.

    Parameters
    ----------
    streams_container : StreamsContainer, optional
        Result file container allowed to be kept open
        to cache data
    data_sources : DataSources
        Result file path container, used if no
        streams are set
    unit_system : int or str or UnitSystem, optional
        Unit system id (int), semicolon-separated
        list of base unit strings (str) or
        unitsystem instance


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.global_energy_ratio_wo_eroded()

    >>> # Make input connections
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_unit_system = int()
    >>> op.inputs.unit_system.connect(my_unit_system)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.global_energy_ratio_wo_eroded(
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     unit_system=my_unit_system,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        streams_container=None,
        data_sources=None,
        unit_system=None,
        config=None,
        server=None,
    ):
        super().__init__(name="GLOB_ENG_ER", config=config, server=server)
        self._inputs = InputsGlobalEnergyRatioWoEroded(self)
        self._outputs = OutputsGlobalEnergyRatioWoEroded(self)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if unit_system is not None:
            self.inputs.unit_system.connect(unit_system)

    @staticmethod
    def _spec():
        description = """Read Global Energy ratio without Eroded Energy (LSDyna) by calling the
            readers defined by the datasources."""
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
                50: PinSpecification(
                    name="unit_system",
                    type_names=[
                        "int32",
                        "string",
                        "class dataProcessing::unit::CUnitSystem",
                    ],
                    optional=True,
                    document="""Unit system id (int), semicolon-separated
        list of base unit strings (str) or
        unitsystem instance""",
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
        return Operator.default_config(name="GLOB_ENG_ER", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsGlobalEnergyRatioWoEroded
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsGlobalEnergyRatioWoEroded
        """
        return super().outputs


class InputsGlobalEnergyRatioWoEroded(_Inputs):
    """Intermediate class used to connect user inputs to
    global_energy_ratio_wo_eroded operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.global_energy_ratio_wo_eroded()
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_unit_system = int()
    >>> op.inputs.unit_system.connect(my_unit_system)
    """

    def __init__(self, op: Operator):
        super().__init__(global_energy_ratio_wo_eroded._spec().inputs, op)
        self._streams_container = Input(
            global_energy_ratio_wo_eroded._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(
            global_energy_ratio_wo_eroded._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)
        self._unit_system = Input(
            global_energy_ratio_wo_eroded._spec().input_pin(50), 50, op, -1
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
        >>> op = dpf.operators.result.global_energy_ratio_wo_eroded()
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
        >>> op = dpf.operators.result.global_energy_ratio_wo_eroded()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def unit_system(self):
        """Allows to connect unit_system input to the operator.

        Unit system id (int), semicolon-separated
        list of base unit strings (str) or
        unitsystem instance

        Parameters
        ----------
        my_unit_system : int or str or UnitSystem

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.global_energy_ratio_wo_eroded()
        >>> op.inputs.unit_system.connect(my_unit_system)
        >>> # or
        >>> op.inputs.unit_system(my_unit_system)
        """
        return self._unit_system


class OutputsGlobalEnergyRatioWoEroded(_Outputs):
    """Intermediate class used to get outputs from
    global_energy_ratio_wo_eroded operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.global_energy_ratio_wo_eroded()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(global_energy_ratio_wo_eroded._spec().outputs, op)
        self._fields_container = Output(
            global_energy_ratio_wo_eroded._spec().output_pin(0), 0, op
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
        >>> op = dpf.operators.result.global_energy_ratio_wo_eroded()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
