"""
serializer
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class serializer(Operator):
    """Take any input and serialize them in a file.

    Parameters
    ----------
    file_path : str
    any_input1 : Any
        Any input
    any_input2 : Any
        Any input


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.serializer()

    >>> # Make input connections
    >>> my_file_path = str()
    >>> op.inputs.file_path.connect(my_file_path)
    >>> my_any_input1 = dpf.Any()
    >>> op.inputs.any_input1.connect(my_any_input1)
    >>> my_any_input2 = dpf.Any()
    >>> op.inputs.any_input2.connect(my_any_input2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.serializer(
    ...     file_path=my_file_path,
    ...     any_input1=my_any_input1,
    ...     any_input2=my_any_input2,
    ... )

    >>> # Get output data
    >>> result_file_path = op.outputs.file_path()
    """

    def __init__(
        self, file_path=None, any_input1=None, any_input2=None, config=None, server=None
    ):
        super().__init__(name="serializer", config=config, server=server)
        self._inputs = InputsSerializer(self)
        self._outputs = OutputsSerializer(self)
        if file_path is not None:
            self.inputs.file_path.connect(file_path)
        if any_input1 is not None:
            self.inputs.any_input1.connect(any_input1)
        if any_input2 is not None:
            self.inputs.any_input2.connect(any_input2)

    @staticmethod
    def _spec():
        description = """Take any input and serialize them in a file."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="file_path",
                    type_names=["string"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="any_input",
                    type_names=["any"],
                    optional=False,
                    document="""Any input""",
                ),
                2: PinSpecification(
                    name="any_input",
                    type_names=["any"],
                    optional=False,
                    document="""Any input""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="file_path",
                    type_names=["string"],
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
        return Operator.default_config(name="serializer", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSerializer
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSerializer
        """
        return super().outputs


class InputsSerializer(_Inputs):
    """Intermediate class used to connect user inputs to
    serializer operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.serializer()
    >>> my_file_path = str()
    >>> op.inputs.file_path.connect(my_file_path)
    >>> my_any_input1 = dpf.Any()
    >>> op.inputs.any_input1.connect(my_any_input1)
    >>> my_any_input2 = dpf.Any()
    >>> op.inputs.any_input2.connect(my_any_input2)
    """

    def __init__(self, op: Operator):
        super().__init__(serializer._spec().inputs, op)
        self._file_path = Input(serializer._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._file_path)
        self._any_input1 = Input(serializer._spec().input_pin(1), 1, op, 0)
        self._inputs.append(self._any_input1)
        self._any_input2 = Input(serializer._spec().input_pin(2), 2, op, 1)
        self._inputs.append(self._any_input2)

    @property
    def file_path(self):
        """Allows to connect file_path input to the operator.

        Parameters
        ----------
        my_file_path : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.serializer()
        >>> op.inputs.file_path.connect(my_file_path)
        >>> # or
        >>> op.inputs.file_path(my_file_path)
        """
        return self._file_path

    @property
    def any_input1(self):
        """Allows to connect any_input1 input to the operator.

        Any input

        Parameters
        ----------
        my_any_input1 : Any

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.serializer()
        >>> op.inputs.any_input1.connect(my_any_input1)
        >>> # or
        >>> op.inputs.any_input1(my_any_input1)
        """
        return self._any_input1

    @property
    def any_input2(self):
        """Allows to connect any_input2 input to the operator.

        Any input

        Parameters
        ----------
        my_any_input2 : Any

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.serializer()
        >>> op.inputs.any_input2.connect(my_any_input2)
        >>> # or
        >>> op.inputs.any_input2(my_any_input2)
        """
        return self._any_input2


class OutputsSerializer(_Outputs):
    """Intermediate class used to get outputs from
    serializer operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.serializer()
    >>> # Connect inputs : op.inputs. ...
    >>> result_file_path = op.outputs.file_path()
    """

    def __init__(self, op: Operator):
        super().__init__(serializer._spec().outputs, op)
        self._file_path = Output(serializer._spec().output_pin(0), 0, op)
        self._outputs.append(self._file_path)

    @property
    def file_path(self):
        """Allows to get file_path output of the operator

        Returns
        ----------
        my_file_path : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.serializer()
        >>> # Connect inputs : op.inputs. ...
        >>> result_file_path = op.outputs.file_path()
        """  # noqa: E501
        return self._file_path
