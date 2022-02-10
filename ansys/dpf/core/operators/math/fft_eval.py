"""
fft_eval
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class fft_eval(Operator):
    """Evaluate the fast fourier transforms at a given set of fields.

    Parameters
    ----------
    field_t : Field
        Field of values to evaluate
    time_scoping : Scoping, optional
        If specified only the results at these set
        ids are used


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.fft_eval()

    >>> # Make input connections
    >>> my_field_t = dpf.Field()
    >>> op.inputs.field_t.connect(my_field_t)
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.fft_eval(
    ...     field_t=my_field_t,
    ...     time_scoping=my_time_scoping,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    >>> result_offset = op.outputs.offset()
    """

    def __init__(self, field_t=None, time_scoping=None, config=None, server=None):
        super().__init__(name="fft_eval", config=config, server=server)
        self._inputs = InputsFftEval(self)
        self._outputs = OutputsFftEval(self)
        if field_t is not None:
            self.inputs.field_t.connect(field_t)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)

    @staticmethod
    def _spec():
        description = (
            """Evaluate the fast fourier transforms at a given set of fields."""
        )
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field_t",
                    type_names=["field"],
                    optional=False,
                    document="""Field of values to evaluate""",
                ),
                1: PinSpecification(
                    name="time_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""If specified only the results at these set
        ids are used""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="offset",
                    type_names=["field"],
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
        return Operator.default_config(name="fft_eval", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFftEval
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFftEval
        """
        return super().outputs


class InputsFftEval(_Inputs):
    """Intermediate class used to connect user inputs to
    fft_eval operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.fft_eval()
    >>> my_field_t = dpf.Field()
    >>> op.inputs.field_t.connect(my_field_t)
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    """

    def __init__(self, op: Operator):
        super().__init__(fft_eval._spec().inputs, op)
        self._field_t = Input(fft_eval._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field_t)
        self._time_scoping = Input(fft_eval._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._time_scoping)

    @property
    def field_t(self):
        """Allows to connect field_t input to the operator.

        Field of values to evaluate

        Parameters
        ----------
        my_field_t : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_eval()
        >>> op.inputs.field_t.connect(my_field_t)
        >>> # or
        >>> op.inputs.field_t(my_field_t)
        """
        return self._field_t

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        If specified only the results at these set
        ids are used

        Parameters
        ----------
        my_time_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_eval()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping


class OutputsFftEval(_Outputs):
    """Intermediate class used to get outputs from
    fft_eval operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.fft_eval()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    >>> result_offset = op.outputs.offset()
    """

    def __init__(self, op: Operator):
        super().__init__(fft_eval._spec().outputs, op)
        self._field = Output(fft_eval._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)
        self._offset = Output(fft_eval._spec().output_pin(2), 2, op)
        self._outputs.append(self._offset)

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_eval()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field

    @property
    def offset(self):
        """Allows to get offset output of the operator

        Returns
        ----------
        my_offset : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.fft_eval()
        >>> # Connect inputs : op.inputs. ...
        >>> result_offset = op.outputs.offset()
        """  # noqa: E501
        return self._offset
