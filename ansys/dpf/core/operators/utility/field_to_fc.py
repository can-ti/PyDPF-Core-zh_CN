"""Autogenerated DPF operator classes.

Created on 12/06/2021, 14:28:55.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class field_to_fc(Operator):
    """Create a field container containing the field in input.

    Parameters
    ----------
    field : Field or FieldsContainer
        If a fields container is set in input, it is
        pass on as output.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.field_to_fc()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.field_to_fc(
    ...     field=my_field,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="InjectToFieldContainer", config=config, server=server)
        self._inputs = InputsFieldToFc(self)
        self._outputs = OutputsFieldToFc(self)
        if field is not None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        description = """Create a field container containing the field in input."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""If a fields container is set in input, it is
        pass on as output.""",
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
            ``None``, attempts to use the the global server.
        """
        return Operator.default_config(name="InjectToFieldContainer", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFieldToFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFieldToFc
        """
        return super().outputs


class InputsFieldToFc(_Inputs):
    """Intermediate class used to connect user inputs to
    field_to_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.field_to_fc()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    """

    def __init__(self, op: Operator):
        super().__init__(field_to_fc._spec().inputs, op)
        self._field = Input(field_to_fc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        If a fields container is set in input, it is
        pass on as output.

        Parameters
        ----------
        my_field : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.field_to_fc()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field


class OutputsFieldToFc(_Outputs):
    """Intermediate class used to get outputs from
    field_to_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.field_to_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(field_to_fc._spec().outputs, op)
        self._fields_container = Output(field_to_fc._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.utility.field_to_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
