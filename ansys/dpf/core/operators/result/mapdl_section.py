"""
mapdl_section
-------------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class mapdl_section(Operator):
    """Read the values of the section properties for a given section property
    field(property field that contains section information for each
    element of a mesh).The following keys can be used: Thickness,
    NumLayers

    Parameters
    ----------
    properties_name : str
    section : PropertyField, optional
        Property field that contains a section id per
        element.(optional)
    streams_container : StreamsContainer
    data_sources : DataSources


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.mapdl_section()

    >>> # Make input connections
    >>> my_properties_name = str()
    >>> op.inputs.properties_name.connect(my_properties_name)
    >>> my_section = dpf.PropertyField()
    >>> op.inputs.section.connect(my_section)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.mapdl_section(
    ...     properties_name=my_properties_name,
    ...     section=my_section,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_properties_value = op.outputs.properties_value()
    """

    def __init__(
        self,
        properties_name=None,
        section=None,
        streams_container=None,
        data_sources=None,
        config=None,
        server=None,
    ):
        super().__init__(name="mapdl_section_properties", config=config, server=server)
        self._inputs = InputsMapdlSection(self)
        self._outputs = OutputsMapdlSection(self)
        if properties_name is not None:
            self.inputs.properties_name.connect(properties_name)
        if section is not None:
            self.inputs.section.connect(section)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        description = """Read the values of the section properties for a given section property
            field(property field that contains section information for
            each element of a mesh).The following keys can be used:
            Thickness, NumLayers"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="properties_name",
                    type_names=["string", "vector<string>"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="section",
                    type_names=["property_field"],
                    optional=True,
                    document="""Property field that contains a section id per
        element.(optional)""",
                ),
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=False,
                    document="""""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="properties_value",
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
        return Operator.default_config(name="mapdl_section_properties", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMapdlSection
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMapdlSection
        """
        return super().outputs


class InputsMapdlSection(_Inputs):
    """Intermediate class used to connect user inputs to
    mapdl_section operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.mapdl_section()
    >>> my_properties_name = str()
    >>> op.inputs.properties_name.connect(my_properties_name)
    >>> my_section = dpf.PropertyField()
    >>> op.inputs.section.connect(my_section)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(mapdl_section._spec().inputs, op)
        self._properties_name = Input(mapdl_section._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._properties_name)
        self._section = Input(mapdl_section._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._section)
        self._streams_container = Input(mapdl_section._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._streams_container)
        self._data_sources = Input(mapdl_section._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)

    @property
    def properties_name(self):
        """Allows to connect properties_name input to the operator.

        Parameters
        ----------
        my_properties_name : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mapdl_section()
        >>> op.inputs.properties_name.connect(my_properties_name)
        >>> # or
        >>> op.inputs.properties_name(my_properties_name)
        """
        return self._properties_name

    @property
    def section(self):
        """Allows to connect section input to the operator.

        Property field that contains a section id per
        element.(optional)

        Parameters
        ----------
        my_section : PropertyField

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mapdl_section()
        >>> op.inputs.section.connect(my_section)
        >>> # or
        >>> op.inputs.section(my_section)
        """
        return self._section

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator.

        Parameters
        ----------
        my_streams_container : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mapdl_section()
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
        >>> op = dpf.operators.result.mapdl_section()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsMapdlSection(_Outputs):
    """Intermediate class used to get outputs from
    mapdl_section operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.mapdl_section()
    >>> # Connect inputs : op.inputs. ...
    >>> result_properties_value = op.outputs.properties_value()
    """

    def __init__(self, op: Operator):
        super().__init__(mapdl_section._spec().outputs, op)
        self._properties_value = Output(mapdl_section._spec().output_pin(0), 0, op)
        self._outputs.append(self._properties_value)

    @property
    def properties_value(self):
        """Allows to get properties_value output of the operator

        Returns
        ----------
        my_properties_value : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.mapdl_section()
        >>> # Connect inputs : op.inputs. ...
        >>> result_properties_value = op.outputs.properties_value()
        """  # noqa: E501
        return self._properties_value
