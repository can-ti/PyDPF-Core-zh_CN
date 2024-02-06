"""
timefreq_signed_high_pass
=========================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class timefreq_signed_high_pass(Operator):
    """The high pass filter returns all the values above, or equal, in
    absolute value to the threshold value in input.

    Parameters
    ----------
    time_freq_support : TimeFreqSupport
    threshold : float or Field
        A threshold scalar or a field containing one
        value is expected.
    both : bool, optional
        The default is false. if set to true, the
        complement of the filtered fields
        container is returned on output pin
        1.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.filter.timefreq_signed_high_pass()

    >>> # Make input connections
    >>> my_time_freq_support = dpf.TimeFreqSupport()
    >>> op.inputs.time_freq_support.connect(my_time_freq_support)
    >>> my_threshold = float()
    >>> op.inputs.threshold.connect(my_threshold)
    >>> my_both = bool()
    >>> op.inputs.both.connect(my_both)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.filter.timefreq_signed_high_pass(
    ...     time_freq_support=my_time_freq_support,
    ...     threshold=my_threshold,
    ...     both=my_both,
    ... )

    >>> # Get output data
    >>> result_time_freq_support = op.outputs.time_freq_support()
    >>> result_scoping = op.outputs.scoping()
    """

    def __init__(
        self,
        time_freq_support=None,
        threshold=None,
        both=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="core::timefreq::signed_high_pass", config=config, server=server
        )
        self._inputs = InputsTimefreqSignedHighPass(self)
        self._outputs = OutputsTimefreqSignedHighPass(self)
        if time_freq_support is not None:
            self.inputs.time_freq_support.connect(time_freq_support)
        if threshold is not None:
            self.inputs.threshold.connect(threshold)
        if both is not None:
            self.inputs.both.connect(both)

    @staticmethod
    def _spec():
        description = """The high pass filter returns all the values above, or equal, in
            absolute value to the threshold value in input."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_freq_support",
                    type_names=["time_freq_support"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="threshold",
                    type_names=["double", "field"],
                    optional=False,
                    document="""A threshold scalar or a field containing one
        value is expected.""",
                ),
                2: PinSpecification(
                    name="both",
                    type_names=["bool"],
                    optional=True,
                    document="""The default is false. if set to true, the
        complement of the filtered fields
        container is returned on output pin
        1.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="time_freq_support",
                    type_names=["time_freq_support"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="scoping",
                    type_names=["scoping"],
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
        return Operator.default_config(
            name="core::timefreq::signed_high_pass", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsTimefreqSignedHighPass
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsTimefreqSignedHighPass
        """
        return super().outputs


class InputsTimefreqSignedHighPass(_Inputs):
    """Intermediate class used to connect user inputs to
    timefreq_signed_high_pass operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.filter.timefreq_signed_high_pass()
    >>> my_time_freq_support = dpf.TimeFreqSupport()
    >>> op.inputs.time_freq_support.connect(my_time_freq_support)
    >>> my_threshold = float()
    >>> op.inputs.threshold.connect(my_threshold)
    >>> my_both = bool()
    >>> op.inputs.both.connect(my_both)
    """

    def __init__(self, op: Operator):
        super().__init__(timefreq_signed_high_pass._spec().inputs, op)
        self._time_freq_support = Input(
            timefreq_signed_high_pass._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._time_freq_support)
        self._threshold = Input(
            timefreq_signed_high_pass._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._threshold)
        self._both = Input(timefreq_signed_high_pass._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._both)

    @property
    def time_freq_support(self):
        """Allows to connect time_freq_support input to the operator.

        Parameters
        ----------
        my_time_freq_support : TimeFreqSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.timefreq_signed_high_pass()
        >>> op.inputs.time_freq_support.connect(my_time_freq_support)
        >>> # or
        >>> op.inputs.time_freq_support(my_time_freq_support)
        """
        return self._time_freq_support

    @property
    def threshold(self):
        """Allows to connect threshold input to the operator.

        A threshold scalar or a field containing one
        value is expected.

        Parameters
        ----------
        my_threshold : float or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.timefreq_signed_high_pass()
        >>> op.inputs.threshold.connect(my_threshold)
        >>> # or
        >>> op.inputs.threshold(my_threshold)
        """
        return self._threshold

    @property
    def both(self):
        """Allows to connect both input to the operator.

        The default is false. if set to true, the
        complement of the filtered fields
        container is returned on output pin
        1.

        Parameters
        ----------
        my_both : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.timefreq_signed_high_pass()
        >>> op.inputs.both.connect(my_both)
        >>> # or
        >>> op.inputs.both(my_both)
        """
        return self._both


class OutputsTimefreqSignedHighPass(_Outputs):
    """Intermediate class used to get outputs from
    timefreq_signed_high_pass operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.filter.timefreq_signed_high_pass()
    >>> # Connect inputs : op.inputs. ...
    >>> result_time_freq_support = op.outputs.time_freq_support()
    >>> result_scoping = op.outputs.scoping()
    """

    def __init__(self, op: Operator):
        super().__init__(timefreq_signed_high_pass._spec().outputs, op)
        self._time_freq_support = Output(
            timefreq_signed_high_pass._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._time_freq_support)
        self._scoping = Output(timefreq_signed_high_pass._spec().output_pin(1), 1, op)
        self._outputs.append(self._scoping)

    @property
    def time_freq_support(self):
        """Allows to get time_freq_support output of the operator

        Returns
        ----------
        my_time_freq_support : TimeFreqSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.timefreq_signed_high_pass()
        >>> # Connect inputs : op.inputs. ...
        >>> result_time_freq_support = op.outputs.time_freq_support()
        """  # noqa: E501
        return self._time_freq_support

    @property
    def scoping(self):
        """Allows to get scoping output of the operator

        Returns
        ----------
        my_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.timefreq_signed_high_pass()
        >>> # Connect inputs : op.inputs. ...
        >>> result_scoping = op.outputs.scoping()
        """  # noqa: E501
        return self._scoping
