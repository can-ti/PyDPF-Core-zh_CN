"""
deserializer
============
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class deserializer(Operator):
    """Takes a file generated by the serializer and deserializes it into
    DPF's entities.

    Parameters
    ----------
    file_path : str
        File path


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.deserializer()

    >>> # Make input connections
    >>> my_file_path = str()
    >>> op.inputs.file_path.connect(my_file_path)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.deserializer(
    ...     file_path=my_file_path,
    ... )

    >>> # Get output data
    >>> result_any_output1 = op.outputs.any_output1()
    >>> result_any_output2 = op.outputs.any_output2()
    """

    def __init__(self, file_path=None, config=None, server=None):
        super().__init__(name="deserializer", config=config, server=server)
        self._inputs = InputsDeserializer(self)
        self._outputs = OutputsDeserializer(self)
        if file_path is not None:
            self.inputs.file_path.connect(file_path)

    @staticmethod
    def _spec():
        description = """Takes a file generated by the serializer and deserializes it into
            DPF's entities."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="file_path",
                    type_names=["string"],
                    optional=False,
                    document="""File path""",
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
        return Operator.default_config(name="deserializer", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsDeserializer
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsDeserializer
        """
        return super().outputs


class InputsDeserializer(_Inputs):
    """Intermediate class used to connect user inputs to
    deserializer operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.deserializer()
    >>> my_file_path = str()
    >>> op.inputs.file_path.connect(my_file_path)
    """

    def __init__(self, op: Operator):
        super().__init__(deserializer._spec().inputs, op)
        self._file_path = Input(deserializer._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._file_path)

    @property
    def file_path(self):
        """Allows to connect file_path input to the operator.

        File path

        Parameters
        ----------
        my_file_path : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.deserializer()
        >>> op.inputs.file_path.connect(my_file_path)
        >>> # or
        >>> op.inputs.file_path(my_file_path)
        """
        return self._file_path


class OutputsDeserializer(_Outputs):
    """Intermediate class used to get outputs from
    deserializer operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.deserializer()
    >>> # Connect inputs : op.inputs. ...
    >>> result_any_output1 = op.outputs.any_output1()
    >>> result_any_output2 = op.outputs.any_output2()
    """

    def __init__(self, op: Operator):
        super().__init__(deserializer._spec().outputs, op)
        self._any_output1 = Output(deserializer._spec().output_pin(1), 1, op)
        self._outputs.append(self._any_output1)
        self._any_output2 = Output(deserializer._spec().output_pin(2), 2, op)
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
        >>> op = dpf.operators.serialization.deserializer()
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
        >>> op = dpf.operators.serialization.deserializer()
        >>> # Connect inputs : op.inputs. ...
        >>> result_any_output2 = op.outputs.any_output2()
        """  # noqa: E501
        return self._any_output2
