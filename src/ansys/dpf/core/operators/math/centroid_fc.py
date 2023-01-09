"""
centroid_fc
===========
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class centroid_fc(Operator):
    """Computes the centroid of all the matching fields of a fields container
    at a given time or frequency, using fieldOut =
    field1*(1.-fact)+field2*(fact).

    Parameters
    ----------
    fields_container : FieldsContainer
    time_freq : float
    step : int, optional
    time_freq_support : TimeFreqSupport, optional


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.centroid_fc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_time_freq = float()
    >>> op.inputs.time_freq.connect(my_time_freq)
    >>> my_step = int()
    >>> op.inputs.step.connect(my_step)
    >>> my_time_freq_support = dpf.TimeFreqSupport()
    >>> op.inputs.time_freq_support.connect(my_time_freq_support)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.centroid_fc(
    ...     fields_container=my_fields_container,
    ...     time_freq=my_time_freq,
    ...     step=my_step,
    ...     time_freq_support=my_time_freq_support,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_container=None,
        time_freq=None,
        step=None,
        time_freq_support=None,
        config=None,
        server=None,
    ):
        super().__init__(name="centroid_fc", config=config, server=server)
        self._inputs = InputsCentroidFc(self)
        self._outputs = OutputsCentroidFc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if time_freq is not None:
            self.inputs.time_freq.connect(time_freq)
        if step is not None:
            self.inputs.step.connect(step)
        if time_freq_support is not None:
            self.inputs.time_freq_support.connect(time_freq_support)

    @staticmethod
    def _spec():
        description = """Computes the centroid of all the matching fields of a fields container
            at a given time or frequency, using fieldOut =
            field1*(1.-fact)+field2*(fact)."""
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
                    name="time_freq",
                    type_names=["double"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="step",
                    type_names=["int32"],
                    optional=True,
                    document="""""",
                ),
                8: PinSpecification(
                    name="time_freq_support",
                    type_names=["time_freq_support"],
                    optional=True,
                    document="""""",
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
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="centroid_fc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCentroidFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCentroidFc
        """
        return super().outputs


class InputsCentroidFc(_Inputs):
    """Intermediate class used to connect user inputs to
    centroid_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.centroid_fc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_time_freq = float()
    >>> op.inputs.time_freq.connect(my_time_freq)
    >>> my_step = int()
    >>> op.inputs.step.connect(my_step)
    >>> my_time_freq_support = dpf.TimeFreqSupport()
    >>> op.inputs.time_freq_support.connect(my_time_freq_support)
    """

    def __init__(self, op: Operator):
        super().__init__(centroid_fc._spec().inputs, op)
        self._fields_container = Input(centroid_fc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fields_container)
        self._time_freq = Input(centroid_fc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._time_freq)
        self._step = Input(centroid_fc._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._step)
        self._time_freq_support = Input(centroid_fc._spec().input_pin(8), 8, op, -1)
        self._inputs.append(self._time_freq_support)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.centroid_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def time_freq(self):
        """Allows to connect time_freq input to the operator.

        Parameters
        ----------
        my_time_freq : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.centroid_fc()
        >>> op.inputs.time_freq.connect(my_time_freq)
        >>> # or
        >>> op.inputs.time_freq(my_time_freq)
        """
        return self._time_freq

    @property
    def step(self):
        """Allows to connect step input to the operator.

        Parameters
        ----------
        my_step : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.centroid_fc()
        >>> op.inputs.step.connect(my_step)
        >>> # or
        >>> op.inputs.step(my_step)
        """
        return self._step

    @property
    def time_freq_support(self):
        """Allows to connect time_freq_support input to the operator.

        Parameters
        ----------
        my_time_freq_support : TimeFreqSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.centroid_fc()
        >>> op.inputs.time_freq_support.connect(my_time_freq_support)
        >>> # or
        >>> op.inputs.time_freq_support(my_time_freq_support)
        """
        return self._time_freq_support


class OutputsCentroidFc(_Outputs):
    """Intermediate class used to get outputs from
    centroid_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.centroid_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(centroid_fc._spec().outputs, op)
        self._fields_container = Output(centroid_fc._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.centroid_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
