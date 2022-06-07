"""
python_generator
----------------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class python_generator(Operator):
    """Generates .py file with specifications for loaded plugin(s).

    Parameters
    ----------
    dll_source_path : str
    output_path : str
    load_symbol : str, optional
    library_key : str, optional


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.python_generator()

    >>> # Make input connections
    >>> my_dll_source_path = str()
    >>> op.inputs.dll_source_path.connect(my_dll_source_path)
    >>> my_output_path = str()
    >>> op.inputs.output_path.connect(my_output_path)
    >>> my_load_symbol = str()
    >>> op.inputs.load_symbol.connect(my_load_symbol)
    >>> my_library_key = str()
    >>> op.inputs.library_key.connect(my_library_key)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.python_generator(
    ...     dll_source_path=my_dll_source_path,
    ...     output_path=my_output_path,
    ...     load_symbol=my_load_symbol,
    ...     library_key=my_library_key,
    ... )

    """

    def __init__(
        self,
        dll_source_path=None,
        output_path=None,
        load_symbol=None,
        library_key=None,
        config=None,
        server=None,
    ):
        super().__init__(name="python_generator", config=config, server=server)
        self._inputs = InputsPythonGenerator(self)
        self._outputs = OutputsPythonGenerator(self)
        if dll_source_path is not None:
            self.inputs.dll_source_path.connect(dll_source_path)
        if output_path is not None:
            self.inputs.output_path.connect(output_path)
        if load_symbol is not None:
            self.inputs.load_symbol.connect(load_symbol)
        if library_key is not None:
            self.inputs.library_key.connect(library_key)

    @staticmethod
    def _spec():
        description = """Generates .py file with specifications for loaded plugin(s)."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="dll_source_path",
                    type_names=["string"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="output_path",
                    type_names=["string"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="load_symbol",
                    type_names=["string"],
                    optional=True,
                    document="""""",
                ),
                3: PinSpecification(
                    name="library_key",
                    type_names=["string"],
                    optional=True,
                    document="""""",
                ),
            },
            map_output_pin_spec={},
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
        return Operator.default_config(name="python_generator", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPythonGenerator
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPythonGenerator
        """
        return super().outputs


class InputsPythonGenerator(_Inputs):
    """Intermediate class used to connect user inputs to
    python_generator operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.python_generator()
    >>> my_dll_source_path = str()
    >>> op.inputs.dll_source_path.connect(my_dll_source_path)
    >>> my_output_path = str()
    >>> op.inputs.output_path.connect(my_output_path)
    >>> my_load_symbol = str()
    >>> op.inputs.load_symbol.connect(my_load_symbol)
    >>> my_library_key = str()
    >>> op.inputs.library_key.connect(my_library_key)
    """

    def __init__(self, op: Operator):
        super().__init__(python_generator._spec().inputs, op)
        self._dll_source_path = Input(python_generator._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._dll_source_path)
        self._output_path = Input(python_generator._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._output_path)
        self._load_symbol = Input(python_generator._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._load_symbol)
        self._library_key = Input(python_generator._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._library_key)

    @property
    def dll_source_path(self):
        """Allows to connect dll_source_path input to the operator.

        Parameters
        ----------
        my_dll_source_path : str or os.PathLike

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.python_generator()
        >>> op.inputs.dll_source_path.connect(my_dll_source_path)
        >>> # or
        >>> op.inputs.dll_source_path(my_dll_source_path)
        """
        return self._dll_source_path

    @property
    def output_path(self):
        """Allows to connect output_path input to the operator.

        Parameters
        ----------
        my_output_path : str or os.PathLike

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.python_generator()
        >>> op.inputs.output_path.connect(my_output_path)
        >>> # or
        >>> op.inputs.output_path(my_output_path)
        """
        return self._output_path

    @property
    def load_symbol(self):
        """Allows to connect load_symbol input to the operator.

        Parameters
        ----------
        my_load_symbol : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.python_generator()
        >>> op.inputs.load_symbol.connect(my_load_symbol)
        >>> # or
        >>> op.inputs.load_symbol(my_load_symbol)
        """
        return self._load_symbol

    @property
    def library_key(self):
        """Allows to connect library_key input to the operator.

        Parameters
        ----------
        my_library_key : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.python_generator()
        >>> op.inputs.library_key.connect(my_library_key)
        >>> # or
        >>> op.inputs.library_key(my_library_key)
        """
        return self._library_key


class OutputsPythonGenerator(_Outputs):
    """Intermediate class used to get outputs from
    python_generator operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.python_generator()
    >>> # Connect inputs : op.inputs. ...
    """

    def __init__(self, op: Operator):
        super().__init__(python_generator._spec().outputs, op)
