"""
string_deserializer
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class string_deserializer(Operator):
    """Takes a string generated by the serializer and deserializes it into
    DPF's entities.

    Parameters
    ----------
    serialized_string : str


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.string_deserializer()

    >>> # Make input connections
    >>> my_serialized_string = str()
    >>> op.inputs.serialized_string.connect(my_serialized_string)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.string_deserializer(
    ...     serialized_string=my_serialized_string,
    ... )

    >>> # Get output data
    >>> result_any_output1 = op.outputs.any_output1()
    >>> result_any_output2 = op.outputs.any_output2()
    """

    def __init__(self, serialized_string=None, config=None, server=None):
        super().__init__(name="string_deserializer", config=config, server=server)
        self._inputs = InputsStringDeserializer(self)
        self._outputs = OutputsStringDeserializer(self)
        if serialized_string is not None:
            self.inputs.serialized_string.connect(serialized_string)

    @staticmethod
    def _spec():
        description = """Takes a string generated by the serializer and deserializes it into
            DPF's entities."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="serialized_string",
                    type_names=["string"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                1: PinSpecification(
                    name="any_output1",
                    type_names=["any"],
                    optional=False,
                    document="""Number and types of outputs corresponding of
        the inputs used in the serialization""",
                ),
                2: PinSpecification(
                    name="any_output2",
                    type_names=["any"],
                    optional=False,
                    document="""Number and types of outputs corresponding of
        the inputs used in the serialization""",
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
        return Operator.default_config(name="string_deserializer", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsStringDeserializer
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsStringDeserializer
        """
        return super().outputs


class InputsStringDeserializer(_Inputs):
    """Intermediate class used to connect user inputs to
    string_deserializer operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.string_deserializer()
    >>> my_serialized_string = str()
    >>> op.inputs.serialized_string.connect(my_serialized_string)
    """

    def __init__(self, op: Operator):
        super().__init__(string_deserializer._spec().inputs, op)
        self._serialized_string = Input(
            string_deserializer._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._serialized_string)

    @property
    def serialized_string(self):
        """Allows to connect serialized_string input to the operator.

        Parameters
        ----------
        my_serialized_string : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.string_deserializer()
        >>> op.inputs.serialized_string.connect(my_serialized_string)
        >>> # or
        >>> op.inputs.serialized_string(my_serialized_string)
        """
        return self._serialized_string


class OutputsStringDeserializer(_Outputs):
    """Intermediate class used to get outputs from
    string_deserializer operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.string_deserializer()
    >>> # Connect inputs : op.inputs. ...
    >>> result_any_output1 = op.outputs.any_output1()
    >>> result_any_output2 = op.outputs.any_output2()
    """

    def __init__(self, op: Operator):
        super().__init__(string_deserializer._spec().outputs, op)
        self._any_output1 = Output(string_deserializer._spec().output_pin(1), 1, op)
        self._outputs.append(self._any_output1)
        self._any_output2 = Output(string_deserializer._spec().output_pin(2), 2, op)
        self._outputs.append(self._any_output2)

    @property
    def any_output1(self):
        """Allows to get any_output1 output of the operator

        Returns
        ----------
        my_any_output1 : Any

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.string_deserializer()
        >>> # Connect inputs : op.inputs. ...
        >>> result_any_output1 = op.outputs.any_output1()
        """  # noqa: E501
        return self._any_output1

    @property
    def any_output2(self):
        """Allows to get any_output2 output of the operator

        Returns
        ----------
        my_any_output2 : Any

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.string_deserializer()
        >>> # Connect inputs : op.inputs. ...
        >>> result_any_output2 = op.outputs.any_output2()
        """  # noqa: E501
        return self._any_output2
