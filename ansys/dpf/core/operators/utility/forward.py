"""Autogenerated DPF operator classes.

Created on 12/06/2021, 14:28:59.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class forward(Operator):
    """Return all the inputs as outputs.

    Parameters
    ----------
    any : Any
        Any type of input


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.forward()

    >>> # Make input connections
    >>> my_any = dpf.Any()
    >>> op.inputs.any.connect(my_any)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.forward(
    ...     any=my_any,
    ... )

    >>> # Get output data
    >>> result_any = op.outputs.any()
    """

    def __init__(self, any=None, config=None, server=None):
        super().__init__(name="forward", config=config, server=server)
        self._inputs = InputsForward(self)
        self._outputs = OutputsForward(self)
        if any is not None:
            self.inputs.any.connect(any)

    @staticmethod
    def _spec():
        description = """Return all the inputs as outputs."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="any",
                    type_names=["any"],
                    optional=False,
                    document="""Any type of input""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="any",
                    type_names=["any"],
                    optional=False,
                    document="""Same types as inputs""",
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
        return Operator.default_config(name="forward", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsForward
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsForward
        """
        return super().outputs


class InputsForward(_Inputs):
    """Intermediate class used to connect user inputs to
    forward operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.forward()
    >>> my_any = dpf.Any()
    >>> op.inputs.any.connect(my_any)
    """

    def __init__(self, op: Operator):
        super().__init__(forward._spec().inputs, op)
        self._any = Input(forward._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._any)

    @property
    def any(self):
        """Allows to connect any input to the operator.

        Any type of input

        Parameters
        ----------
        my_any : Any

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.forward()
        >>> op.inputs.any.connect(my_any)
        >>> # or
        >>> op.inputs.any(my_any)
        """
        return self._any


class OutputsForward(_Outputs):
    """Intermediate class used to get outputs from
    forward operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.forward()
    >>> # Connect inputs : op.inputs. ...
    >>> result_any = op.outputs.any()
    """

    def __init__(self, op: Operator):
        super().__init__(forward._spec().outputs, op)
        self._any = Output(forward._spec().output_pin(0), 0, op)
        self._outputs.append(self._any)

    @property
    def any(self):
        """Allows to get any output of the operator

        Returns
        ----------
        my_any : Any

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.forward()
        >>> # Connect inputs : op.inputs. ...
        >>> result_any = op.outputs.any()
        """  # noqa: E501
        return self._any
