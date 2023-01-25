"""
weighted_merge_fields_by_label
==============================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class weighted_merge_fields_by_label(Operator):
    """Takes a fields container and makes an weighted merge with its fields
    that share the same label value.

    Parameters
    ----------
    fields_container : FieldsContainer
    label : str
        Label identifier that should be merged.
    merged_field_support : AbstractFieldSupport, optional
        The fieldscontainer's support that has
        already been merged.
    sum_merge : bool, optional
        Default is false. if true redundant
        quantities are summed instead of
        being ignored.
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
    >>> op = dpf.operators.utility.weighted_merge_fields_by_label()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_label = str()
    >>> op.inputs.label.connect(my_label)
    >>> my_merged_field_support = dpf.AbstractFieldSupport()
    >>> op.inputs.merged_field_support.connect(my_merged_field_support)
    >>> my_sum_merge = bool()
    >>> op.inputs.sum_merge.connect(my_sum_merge)
    >>> my_weights1 = dpf.PropertyField()
    >>> op.inputs.weights1.connect(my_weights1)
    >>> my_weights2 = dpf.PropertyField()
    >>> op.inputs.weights2.connect(my_weights2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.weighted_merge_fields_by_label(
    ...     fields_container=my_fields_container,
    ...     label=my_label,
    ...     merged_field_support=my_merged_field_support,
    ...     sum_merge=my_sum_merge,
    ...     weights1=my_weights1,
    ...     weights2=my_weights2,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_container=None,
        label=None,
        merged_field_support=None,
        sum_merge=None,
        weights1=None,
        weights2=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="merge::weighted_fields_container_label", config=config, server=server
        )
        self._inputs = InputsWeightedMergeFieldsByLabel(self)
        self._outputs = OutputsWeightedMergeFieldsByLabel(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if label is not None:
            self.inputs.label.connect(label)
        if merged_field_support is not None:
            self.inputs.merged_field_support.connect(merged_field_support)
        if sum_merge is not None:
            self.inputs.sum_merge.connect(sum_merge)
        if weights1 is not None:
            self.inputs.weights1.connect(weights1)
        if weights2 is not None:
            self.inputs.weights2.connect(weights2)

    @staticmethod
    def _spec():
        description = """Takes a fields container and makes an weighted merge with its fields
            that share the same label value."""
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
                    name="label",
                    type_names=["string"],
                    optional=False,
                    document="""Label identifier that should be merged.""",
                ),
                2: PinSpecification(
                    name="merged_field_support",
                    type_names=["abstract_field_support"],
                    optional=True,
                    document="""The fieldscontainer's support that has
        already been merged.""",
                ),
                3: PinSpecification(
                    name="sum_merge",
                    type_names=["bool"],
                    optional=True,
                    document="""Default is false. if true redundant
        quantities are summed instead of
        being ignored.""",
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
        return Operator.default_config(
            name="merge::weighted_fields_container_label", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsWeightedMergeFieldsByLabel
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsWeightedMergeFieldsByLabel
        """
        return super().outputs


class InputsWeightedMergeFieldsByLabel(_Inputs):
    """Intermediate class used to connect user inputs to
    weighted_merge_fields_by_label operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.weighted_merge_fields_by_label()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_label = str()
    >>> op.inputs.label.connect(my_label)
    >>> my_merged_field_support = dpf.AbstractFieldSupport()
    >>> op.inputs.merged_field_support.connect(my_merged_field_support)
    >>> my_sum_merge = bool()
    >>> op.inputs.sum_merge.connect(my_sum_merge)
    >>> my_weights1 = dpf.PropertyField()
    >>> op.inputs.weights1.connect(my_weights1)
    >>> my_weights2 = dpf.PropertyField()
    >>> op.inputs.weights2.connect(my_weights2)
    """

    def __init__(self, op: Operator):
        super().__init__(weighted_merge_fields_by_label._spec().inputs, op)
        self._fields_container = Input(
            weighted_merge_fields_by_label._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._label = Input(
            weighted_merge_fields_by_label._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._label)
        self._merged_field_support = Input(
            weighted_merge_fields_by_label._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._merged_field_support)
        self._sum_merge = Input(
            weighted_merge_fields_by_label._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._sum_merge)
        self._weights1 = Input(
            weighted_merge_fields_by_label._spec().input_pin(1000), 1000, op, 0
        )
        self._inputs.append(self._weights1)
        self._weights2 = Input(
            weighted_merge_fields_by_label._spec().input_pin(1001), 1001, op, 1
        )
        self._inputs.append(self._weights2)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.weighted_merge_fields_by_label()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def label(self):
        """Allows to connect label input to the operator.

        Label identifier that should be merged.

        Parameters
        ----------
        my_label : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.weighted_merge_fields_by_label()
        >>> op.inputs.label.connect(my_label)
        >>> # or
        >>> op.inputs.label(my_label)
        """
        return self._label

    @property
    def merged_field_support(self):
        """Allows to connect merged_field_support input to the operator.

        The fieldscontainer's support that has
        already been merged.

        Parameters
        ----------
        my_merged_field_support : AbstractFieldSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.weighted_merge_fields_by_label()
        >>> op.inputs.merged_field_support.connect(my_merged_field_support)
        >>> # or
        >>> op.inputs.merged_field_support(my_merged_field_support)
        """
        return self._merged_field_support

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
        >>> op = dpf.operators.utility.weighted_merge_fields_by_label()
        >>> op.inputs.sum_merge.connect(my_sum_merge)
        >>> # or
        >>> op.inputs.sum_merge(my_sum_merge)
        """
        return self._sum_merge

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
        >>> op = dpf.operators.utility.weighted_merge_fields_by_label()
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
        >>> op = dpf.operators.utility.weighted_merge_fields_by_label()
        >>> op.inputs.weights2.connect(my_weights2)
        >>> # or
        >>> op.inputs.weights2(my_weights2)
        """
        return self._weights2


class OutputsWeightedMergeFieldsByLabel(_Outputs):
    """Intermediate class used to get outputs from
    weighted_merge_fields_by_label operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.weighted_merge_fields_by_label()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(weighted_merge_fields_by_label._spec().outputs, op)
        self._fields_container = Output(
            weighted_merge_fields_by_label._spec().output_pin(0), 0, op
        )
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
        >>> op = dpf.operators.utility.weighted_merge_fields_by_label()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container