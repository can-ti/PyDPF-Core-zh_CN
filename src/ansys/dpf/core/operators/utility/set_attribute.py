"""
set_attribute
=============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class set_attribute(Operator):
    """Uses the FieldsContainer APIs to modify it.

    Parameters
    ----------
    fields_container : FieldsContainer
    property_name : str
        Supported property names are: "labels".
    property_identifier : LabelSpace, optional
        Value of the property to be set : vector of
        string or labelspace for "labels".


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.set_attribute()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)
    >>> my_property_identifier = dpf.LabelSpace()
    >>> op.inputs.property_identifier.connect(my_property_identifier)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.set_attribute(
    ...     fields_container=my_fields_container,
    ...     property_name=my_property_name,
    ...     property_identifier=my_property_identifier,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_container=None,
        property_name=None,
        property_identifier=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="fieldscontainer::set_attribute", config=config, server=server
        )
        self._inputs = InputsSetAttribute(self)
        self._outputs = OutputsSetAttribute(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if property_name is not None:
            self.inputs.property_name.connect(property_name)
        if property_identifier is not None:
            self.inputs.property_identifier.connect(property_identifier)

    @staticmethod
    def _spec():
        description = """Uses the FieldsContainer APIs to modify it."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="property_name",
                    type_names=["string"],
                    optional=False,
                    document="""Supported property names are: "labels".""",
                ),
                2: PinSpecification(
                    name="property_identifier",
                    type_names=["vector<string>", "label_space"],
                    optional=True,
                    document="""Value of the property to be set : vector of
        string or labelspace for "labels".""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Returns the modified fieldscontainer.""",
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
            name="fieldscontainer::set_attribute", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSetAttribute
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSetAttribute
        """
        return super().outputs


class InputsSetAttribute(_Inputs):
    """Intermediate class used to connect user inputs to
    set_attribute operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.set_attribute()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)
    >>> my_property_identifier = dpf.LabelSpace()
    >>> op.inputs.property_identifier.connect(my_property_identifier)
    """

    def __init__(self, op: Operator):
        super().__init__(set_attribute._spec().inputs, op)
        self._fields_container = Input(set_attribute._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fields_container)
        self._property_name = Input(set_attribute._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._property_name)
        self._property_identifier = Input(set_attribute._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._property_identifier)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.set_attribute()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def property_name(self):
        """Allows to connect property_name input to the operator.

        Supported property names are: "labels".

        Parameters
        ----------
        my_property_name : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.set_attribute()
        >>> op.inputs.property_name.connect(my_property_name)
        >>> # or
        >>> op.inputs.property_name(my_property_name)
        """
        return self._property_name

    @property
    def property_identifier(self):
        """Allows to connect property_identifier input to the operator.

        Value of the property to be set : vector of
        string or labelspace for "labels".

        Parameters
        ----------
        my_property_identifier : LabelSpace

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.set_attribute()
        >>> op.inputs.property_identifier.connect(my_property_identifier)
        >>> # or
        >>> op.inputs.property_identifier(my_property_identifier)
        """
        return self._property_identifier


class OutputsSetAttribute(_Outputs):
    """Intermediate class used to get outputs from
    set_attribute operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.set_attribute()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(set_attribute._spec().outputs, op)
        self._fields_container = Output(set_attribute._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.utility.set_attribute()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container