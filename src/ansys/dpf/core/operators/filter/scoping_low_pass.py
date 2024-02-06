"""
scoping_low_pass
================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class scoping_low_pass(Operator):
    """The low pass filter returns all the values below (but not equal to)
    the threshold value in input.

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container with only one field
        is expected
    threshold : float or Field
        A threshold scalar or a field containing one
        value is expected
    both : bool, optional
        The default is false. if set to true, the
        complement of the filtered fields
        container is returned on output pin
        1.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.filter.scoping_low_pass()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_threshold = float()
    >>> op.inputs.threshold.connect(my_threshold)
    >>> my_both = bool()
    >>> op.inputs.both.connect(my_both)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.filter.scoping_low_pass(
    ...     field=my_field,
    ...     threshold=my_threshold,
    ...     both=my_both,
    ... )

    >>> # Get output data
    >>> result_scoping = op.outputs.scoping()
    """

    def __init__(self, field=None, threshold=None, both=None, config=None, server=None):
        super().__init__(name="core::scoping::low_pass", config=config, server=server)
        self._inputs = InputsScopingLowPass(self)
        self._outputs = OutputsScopingLowPass(self)
        if field is not None:
            self.inputs.field.connect(field)
        if threshold is not None:
            self.inputs.threshold.connect(threshold)
        if both is not None:
            self.inputs.both.connect(both)

    @staticmethod
    def _spec():
        description = """The low pass filter returns all the values below (but not equal to)
            the threshold value in input."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
                ),
                1: PinSpecification(
                    name="threshold",
                    type_names=["double", "field"],
                    optional=False,
                    document="""A threshold scalar or a field containing one
        value is expected""",
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
        return Operator.default_config(name="core::scoping::low_pass", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsScopingLowPass
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsScopingLowPass
        """
        return super().outputs


class InputsScopingLowPass(_Inputs):
    """Intermediate class used to connect user inputs to
    scoping_low_pass operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.filter.scoping_low_pass()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_threshold = float()
    >>> op.inputs.threshold.connect(my_threshold)
    >>> my_both = bool()
    >>> op.inputs.both.connect(my_both)
    """

    def __init__(self, op: Operator):
        super().__init__(scoping_low_pass._spec().inputs, op)
        self._field = Input(scoping_low_pass._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._threshold = Input(scoping_low_pass._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._threshold)
        self._both = Input(scoping_low_pass._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._both)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_field : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.scoping_low_pass()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def threshold(self):
        """Allows to connect threshold input to the operator.

        A threshold scalar or a field containing one
        value is expected

        Parameters
        ----------
        my_threshold : float or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.scoping_low_pass()
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
        >>> op = dpf.operators.filter.scoping_low_pass()
        >>> op.inputs.both.connect(my_both)
        >>> # or
        >>> op.inputs.both(my_both)
        """
        return self._both


class OutputsScopingLowPass(_Outputs):
    """Intermediate class used to get outputs from
    scoping_low_pass operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.filter.scoping_low_pass()
    >>> # Connect inputs : op.inputs. ...
    >>> result_scoping = op.outputs.scoping()
    """

    def __init__(self, op: Operator):
        super().__init__(scoping_low_pass._spec().outputs, op)
        self._scoping = Output(scoping_low_pass._spec().output_pin(0), 0, op)
        self._outputs.append(self._scoping)

    @property
    def scoping(self):
        """Allows to get scoping output of the operator

        Returns
        ----------
        my_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.scoping_low_pass()
        >>> # Connect inputs : op.inputs. ...
        >>> result_scoping = op.outputs.scoping()
        """  # noqa: E501
        return self._scoping
