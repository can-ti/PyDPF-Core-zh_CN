"""
field_band_pass
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class field_band_pass(Operator):
    """The band pass filter returns all the values above (but not equal to)
    the minimum threshold value and below (but not equal to) the
    maximum threshold value in input.

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container with only one field
        is expected
    min_threshold : float or Field
        A minimum threshold scalar or a field
        containing one value is expected.
    max_threshold : float or Field, optional
        A maximum threshold scalar or a field
        containing one value is expected.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.filter.field_band_pass()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_min_threshold = float()
    >>> op.inputs.min_threshold.connect(my_min_threshold)
    >>> my_max_threshold = float()
    >>> op.inputs.max_threshold.connect(my_max_threshold)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.filter.field_band_pass(
    ...     field=my_field,
    ...     min_threshold=my_min_threshold,
    ...     max_threshold=my_max_threshold,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        field=None,
        min_threshold=None,
        max_threshold=None,
        config=None,
        server=None,
    ):
        super().__init__(name="core::field::band_pass", config=config, server=server)
        self._inputs = InputsFieldBandPass(self)
        self._outputs = OutputsFieldBandPass(self)
        if field is not None:
            self.inputs.field.connect(field)
        if min_threshold is not None:
            self.inputs.min_threshold.connect(min_threshold)
        if max_threshold is not None:
            self.inputs.max_threshold.connect(max_threshold)

    @staticmethod
    def _spec():
        description = """The band pass filter returns all the values above (but not equal to)
            the minimum threshold value and below (but not equal to)
            the maximum threshold value in input."""
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
                    name="min_threshold",
                    type_names=["double", "field"],
                    optional=False,
                    document="""A minimum threshold scalar or a field
        containing one value is expected.""",
                ),
                2: PinSpecification(
                    name="max_threshold",
                    type_names=["double", "field"],
                    optional=True,
                    document="""A maximum threshold scalar or a field
        containing one value is expected.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
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
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="core::field::band_pass", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFieldBandPass
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsFieldBandPass
        """
        return super().outputs


class InputsFieldBandPass(_Inputs):
    """Intermediate class used to connect user inputs to
    field_band_pass operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.filter.field_band_pass()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_min_threshold = float()
    >>> op.inputs.min_threshold.connect(my_min_threshold)
    >>> my_max_threshold = float()
    >>> op.inputs.max_threshold.connect(my_max_threshold)
    """

    def __init__(self, op: Operator):
        super().__init__(field_band_pass._spec().inputs, op)
        self._field = Input(field_band_pass._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._min_threshold = Input(field_band_pass._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._min_threshold)
        self._max_threshold = Input(field_band_pass._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._max_threshold)

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
        >>> op = dpf.operators.filter.field_band_pass()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def min_threshold(self):
        """Allows to connect min_threshold input to the operator.

        A minimum threshold scalar or a field
        containing one value is expected.

        Parameters
        ----------
        my_min_threshold : float or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.field_band_pass()
        >>> op.inputs.min_threshold.connect(my_min_threshold)
        >>> # or
        >>> op.inputs.min_threshold(my_min_threshold)
        """
        return self._min_threshold

    @property
    def max_threshold(self):
        """Allows to connect max_threshold input to the operator.

        A maximum threshold scalar or a field
        containing one value is expected.

        Parameters
        ----------
        my_max_threshold : float or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.field_band_pass()
        >>> op.inputs.max_threshold.connect(my_max_threshold)
        >>> # or
        >>> op.inputs.max_threshold(my_max_threshold)
        """
        return self._max_threshold


class OutputsFieldBandPass(_Outputs):
    """Intermediate class used to get outputs from
    field_band_pass operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.filter.field_band_pass()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(field_band_pass._spec().outputs, op)
        self._field = Output(field_band_pass._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.field_band_pass()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
