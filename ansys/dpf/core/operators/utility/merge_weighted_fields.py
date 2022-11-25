"""
merge_weighted_fields
=====================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class merge_weighted_fields(Operator):
    """Take a set of fields and assemble them in a unique one applying a
    weight on the sum of the fields.

    Parameters
    ----------
    sum_merge : bool, optional
        Default is false. if true redundant
        quantities are summed instead of
        being ignored.
    merged_support : AbstractFieldSupport, optional
        Already merged field support.
    fields1 : Field or FieldsContainer
        Either a fields container, a vector of fields
        to merge or fields from pin 0 to ...
    fields2 : Field or FieldsContainer
        Either a fields container, a vector of fields
        to merge or fields from pin 0 to ...
    weights1 : PropertyField
        Weights to apply to each field from pin 1000
        to ...
    weights2 : PropertyField
        Weights to apply to each field from pin 1000
        to ...


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.merge_weighted_fields()

    >>> # Make input connections
    >>> my_sum_merge = bool()
    >>> op.inputs.sum_merge.connect(my_sum_merge)
    >>> my_merged_support = dpf.AbstractFieldSupport()
    >>> op.inputs.merged_support.connect(my_merged_support)
    >>> my_fields1 = dpf.Field()
    >>> op.inputs.fields1.connect(my_fields1)
    >>> my_fields2 = dpf.Field()
    >>> op.inputs.fields2.connect(my_fields2)
    >>> my_weights1 = dpf.PropertyField()
    >>> op.inputs.weights1.connect(my_weights1)
    >>> my_weights2 = dpf.PropertyField()
    >>> op.inputs.weights2.connect(my_weights2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.merge_weighted_fields(
    ...     sum_merge=my_sum_merge,
    ...     merged_support=my_merged_support,
    ...     fields1=my_fields1,
    ...     fields2=my_fields2,
    ...     weights1=my_weights1,
    ...     weights2=my_weights2,
    ... )

    >>> # Get output data
    >>> result_merged_field = op.outputs.merged_field()
    """

    def __init__(
        self,
        sum_merge=None,
        merged_support=None,
        fields1=None,
        fields2=None,
        weights1=None,
        weights2=None,
        config=None,
        server=None,
    ):
        super().__init__(name="merge::weighted_field", config=config, server=server)
        self._inputs = InputsMergeWeightedFields(self)
        self._outputs = OutputsMergeWeightedFields(self)
        if sum_merge is not None:
            self.inputs.sum_merge.connect(sum_merge)
        if merged_support is not None:
            self.inputs.merged_support.connect(merged_support)
        if fields1 is not None:
            self.inputs.fields1.connect(fields1)
        if fields2 is not None:
            self.inputs.fields2.connect(fields2)
        if weights1 is not None:
            self.inputs.weights1.connect(weights1)
        if weights2 is not None:
            self.inputs.weights2.connect(weights2)

    @staticmethod
    def _spec():
        description = """Take a set of fields and assemble them in a unique one applying a
            weight on the sum of the fields."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                -2: PinSpecification(
                    name="sum_merge",
                    type_names=["bool"],
                    optional=True,
                    document="""Default is false. if true redundant
        quantities are summed instead of
        being ignored.""",
                ),
                -1: PinSpecification(
                    name="merged_support",
                    type_names=["abstract_field_support"],
                    optional=True,
                    document="""Already merged field support.""",
                ),
                0: PinSpecification(
                    name="fields",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Either a fields container, a vector of fields
        to merge or fields from pin 0 to ...""",
                ),
                1: PinSpecification(
                    name="fields",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Either a fields container, a vector of fields
        to merge or fields from pin 0 to ...""",
                ),
                1000: PinSpecification(
                    name="weights",
                    type_names=["property_field"],
                    optional=False,
                    document="""Weights to apply to each field from pin 1000
        to ...""",
                ),
                1001: PinSpecification(
                    name="weights",
                    type_names=["property_field"],
                    optional=False,
                    document="""Weights to apply to each field from pin 1000
        to ...""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="merged_field",
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
        return Operator.default_config(name="merge::weighted_field", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeWeightedFields
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeWeightedFields
        """
        return super().outputs


class InputsMergeWeightedFields(_Inputs):
    """Intermediate class used to connect user inputs to
    merge_weighted_fields operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.merge_weighted_fields()
    >>> my_sum_merge = bool()
    >>> op.inputs.sum_merge.connect(my_sum_merge)
    >>> my_merged_support = dpf.AbstractFieldSupport()
    >>> op.inputs.merged_support.connect(my_merged_support)
    >>> my_fields1 = dpf.Field()
    >>> op.inputs.fields1.connect(my_fields1)
    >>> my_fields2 = dpf.Field()
    >>> op.inputs.fields2.connect(my_fields2)
    >>> my_weights1 = dpf.PropertyField()
    >>> op.inputs.weights1.connect(my_weights1)
    >>> my_weights2 = dpf.PropertyField()
    >>> op.inputs.weights2.connect(my_weights2)
    """

    def __init__(self, op: Operator):
        super().__init__(merge_weighted_fields._spec().inputs, op)
        self._sum_merge = Input(merge_weighted_fields._spec().input_pin(-2), -2, op, -1)
        self._inputs.append(self._sum_merge)
        self._merged_support = Input(
            merge_weighted_fields._spec().input_pin(-1), -1, op, -1
        )
        self._inputs.append(self._merged_support)
        self._fields1 = Input(merge_weighted_fields._spec().input_pin(0), 0, op, 0)
        self._inputs.append(self._fields1)
        self._fields2 = Input(merge_weighted_fields._spec().input_pin(1), 1, op, 1)
        self._inputs.append(self._fields2)
        self._weights1 = Input(
            merge_weighted_fields._spec().input_pin(1000), 1000, op, 0
        )
        self._inputs.append(self._weights1)
        self._weights2 = Input(
            merge_weighted_fields._spec().input_pin(1001), 1001, op, 1
        )
        self._inputs.append(self._weights2)

    @property
    def sum_merge(self):
        """Allows to connect sum_merge input to the operator.

        Default is false. if true redundant
        quantities are summed instead of
        being ignored.

        Parameters
        ----------
        my_sum_merge : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_weighted_fields()
        >>> op.inputs.sum_merge.connect(my_sum_merge)
        >>> # or
        >>> op.inputs.sum_merge(my_sum_merge)
        """
        return self._sum_merge

    @property
    def merged_support(self):
        """Allows to connect merged_support input to the operator.

        Already merged field support.

        Parameters
        ----------
        my_merged_support : AbstractFieldSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_weighted_fields()
        >>> op.inputs.merged_support.connect(my_merged_support)
        >>> # or
        >>> op.inputs.merged_support(my_merged_support)
        """
        return self._merged_support

    @property
    def fields1(self):
        """Allows to connect fields1 input to the operator.

        Either a fields container, a vector of fields
        to merge or fields from pin 0 to ...

        Parameters
        ----------
        my_fields1 : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_weighted_fields()
        >>> op.inputs.fields1.connect(my_fields1)
        >>> # or
        >>> op.inputs.fields1(my_fields1)
        """
        return self._fields1

    @property
    def fields2(self):
        """Allows to connect fields2 input to the operator.

        Either a fields container, a vector of fields
        to merge or fields from pin 0 to ...

        Parameters
        ----------
        my_fields2 : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_weighted_fields()
        >>> op.inputs.fields2.connect(my_fields2)
        >>> # or
        >>> op.inputs.fields2(my_fields2)
        """
        return self._fields2

    @property
    def weights1(self):
        """Allows to connect weights1 input to the operator.

        Weights to apply to each field from pin 1000
        to ...

        Parameters
        ----------
        my_weights1 : PropertyField

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_weighted_fields()
        >>> op.inputs.weights1.connect(my_weights1)
        >>> # or
        >>> op.inputs.weights1(my_weights1)
        """
        return self._weights1

    @property
    def weights2(self):
        """Allows to connect weights2 input to the operator.

        Weights to apply to each field from pin 1000
        to ...

        Parameters
        ----------
        my_weights2 : PropertyField

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_weighted_fields()
        >>> op.inputs.weights2.connect(my_weights2)
        >>> # or
        >>> op.inputs.weights2(my_weights2)
        """
        return self._weights2


class OutputsMergeWeightedFields(_Outputs):
    """Intermediate class used to get outputs from
    merge_weighted_fields operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.merge_weighted_fields()
    >>> # Connect inputs : op.inputs. ...
    >>> result_merged_field = op.outputs.merged_field()
    """

    def __init__(self, op: Operator):
        super().__init__(merge_weighted_fields._spec().outputs, op)
        self._merged_field = Output(merge_weighted_fields._spec().output_pin(0), 0, op)
        self._outputs.append(self._merged_field)

    @property
    def merged_field(self):
        """Allows to get merged_field output of the operator

        Returns
        ----------
        my_merged_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_weighted_fields()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_field = op.outputs.merged_field()
        """  # noqa: E501
        return self._merged_field
