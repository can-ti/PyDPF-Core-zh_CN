"""
txt_file_to_dpf
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class txt_file_to_dpf(Operator):
    """Take an input string and parse it into dataProcessing type.

    Parameters
    ----------
    input_string : str
        Ex: 'double:1.0', 'int:1',
        'vector<double>:1.0;1.0'


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.txt_file_to_dpf()

    >>> # Make input connections
    >>> my_input_string = str()
    >>> op.inputs.input_string.connect(my_input_string)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.txt_file_to_dpf(
    ...     input_string=my_input_string,
    ... )

    >>> # Get output data
    >>> result_any_output1 = op.outputs.any_output1()
    >>> result_any_output2 = op.outputs.any_output2()
    """

    def __init__(self, input_string=None, config=None, server=None):
        super().__init__(name="text_parser", config=config, server=server)
        self._inputs = InputsTxtFileToDpf(self)
        self._outputs = OutputsTxtFileToDpf(self)
        if input_string is not None:
            self.inputs.input_string.connect(input_string)

    @staticmethod
    def _spec():
        description = """Take an input string and parse it into dataProcessing type."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="input_string",
                    type_names=["string"],
                    optional=False,
                    document="""Ex: 'double:1.0', 'int:1',
        'vector<double>:1.0;1.0'""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="any_output1",
                    optional=False,
                    document="""Any output""",
                ),
                1: PinSpecification(
                    name="any_output2",
                    optional=False,
                    document="""Any output""",
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
        return Operator.default_config(name="text_parser", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsTxtFileToDpf
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsTxtFileToDpf
        """
        return super().outputs


class InputsTxtFileToDpf(_Inputs):
    """Intermediate class used to connect user inputs to
    txt_file_to_dpf operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.txt_file_to_dpf()
    >>> my_input_string = str()
    >>> op.inputs.input_string.connect(my_input_string)
    """

    def __init__(self, op: Operator):
        super().__init__(txt_file_to_dpf._spec().inputs, op)
        self._input_string = Input(txt_file_to_dpf._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._input_string)

    @property
    def input_string(self):
        """Allows to connect input_string input to the operator.

        Ex: 'double:1.0', 'int:1',
        'vector<double>:1.0;1.0'

        Parameters
        ----------
        my_input_string : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.txt_file_to_dpf()
        >>> op.inputs.input_string.connect(my_input_string)
        >>> # or
        >>> op.inputs.input_string(my_input_string)
        """
        return self._input_string


class OutputsTxtFileToDpf(_Outputs):
    """Intermediate class used to get outputs from
    txt_file_to_dpf operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.txt_file_to_dpf()
    >>> # Connect inputs : op.inputs. ...
    >>> result_any_output1 = op.outputs.any_output1()
    >>> result_any_output2 = op.outputs.any_output2()
    """

    def __init__(self, op: Operator):
        super().__init__(txt_file_to_dpf._spec().outputs, op)
        self._any_output1 = Output(txt_file_to_dpf._spec().output_pin(0), 0, op)
        self._outputs.append(self._any_output1)
        self._any_output2 = Output(txt_file_to_dpf._spec().output_pin(1), 1, op)
        self._outputs.append(self._any_output2)

    @property
    def any_output1(self):
        """Allows to get any_output1 output of the operator

        Returns
        ----------
        my_any_output1 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.txt_file_to_dpf()
        >>> # Connect inputs : op.inputs. ...
        >>> result_any_output1 = op.outputs.any_output1()
        """  # noqa: E501
        return self._any_output1

    @property
    def any_output2(self):
        """Allows to get any_output2 output of the operator

        Returns
        ----------
        my_any_output2 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.txt_file_to_dpf()
        >>> # Connect inputs : op.inputs. ...
        >>> result_any_output2 = op.outputs.any_output2()
        """  # noqa: E501
        return self._any_output2
