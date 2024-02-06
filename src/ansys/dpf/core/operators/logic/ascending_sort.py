"""
ascending_sort
==============
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class ascending_sort(Operator):
    """Sort a field (in 0) in ascending order with an optional component
    priority table, or a boolean, to enable sort by scoping (in 1).
    This operator does not support multiple elementary data per
    entity.

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container with only one field
        is expected
    component_priority_table : optional
        Component priority table (vector of int)
    sort_by_scoping : bool, optional
        If true, uses scoping to sort the field
        (default is false)


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.logic.ascending_sort()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_component_priority_table = dpf.()
    >>> op.inputs.component_priority_table.connect(my_component_priority_table)
    >>> my_sort_by_scoping = bool()
    >>> op.inputs.sort_by_scoping.connect(my_sort_by_scoping)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.logic.ascending_sort(
    ...     field=my_field,
    ...     component_priority_table=my_component_priority_table,
    ...     sort_by_scoping=my_sort_by_scoping,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        field=None,
        component_priority_table=None,
        sort_by_scoping=None,
        config=None,
        server=None,
    ):
        super().__init__(name="ascending_sort", config=config, server=server)
        self._inputs = InputsAscendingSort(self)
        self._outputs = OutputsAscendingSort(self)
        if field is not None:
            self.inputs.field.connect(field)
        if component_priority_table is not None:
            self.inputs.component_priority_table.connect(component_priority_table)
        if sort_by_scoping is not None:
            self.inputs.sort_by_scoping.connect(sort_by_scoping)

    @staticmethod
    def _spec():
        description = """Sort a field (in 0) in ascending order with an optional component
            priority table, or a boolean, to enable sort by scoping
            (in 1). This operator does not support multiple elementary
            data per entity."""
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
                    name="component_priority_table",
                    type_names=["vector<int32>"],
                    optional=True,
                    document="""Component priority table (vector of int)""",
                ),
                2: PinSpecification(
                    name="sort_by_scoping",
                    type_names=["bool"],
                    optional=True,
                    document="""If true, uses scoping to sort the field
        (default is false)""",
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
        return Operator.default_config(name="ascending_sort", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAscendingSort
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsAscendingSort
        """
        return super().outputs


class InputsAscendingSort(_Inputs):
    """Intermediate class used to connect user inputs to
    ascending_sort operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.ascending_sort()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_component_priority_table = dpf.()
    >>> op.inputs.component_priority_table.connect(my_component_priority_table)
    >>> my_sort_by_scoping = bool()
    >>> op.inputs.sort_by_scoping.connect(my_sort_by_scoping)
    """

    def __init__(self, op: Operator):
        super().__init__(ascending_sort._spec().inputs, op)
        self._field = Input(ascending_sort._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._component_priority_table = Input(
            ascending_sort._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._component_priority_table)
        self._sort_by_scoping = Input(ascending_sort._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._sort_by_scoping)

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
        >>> op = dpf.operators.logic.ascending_sort()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def component_priority_table(self):
        """Allows to connect component_priority_table input to the operator.

        Component priority table (vector of int)

        Parameters
        ----------
        my_component_priority_table :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.ascending_sort()
        >>> op.inputs.component_priority_table.connect(my_component_priority_table)
        >>> # or
        >>> op.inputs.component_priority_table(my_component_priority_table)
        """
        return self._component_priority_table

    @property
    def sort_by_scoping(self):
        """Allows to connect sort_by_scoping input to the operator.

        If true, uses scoping to sort the field
        (default is false)

        Parameters
        ----------
        my_sort_by_scoping : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.ascending_sort()
        >>> op.inputs.sort_by_scoping.connect(my_sort_by_scoping)
        >>> # or
        >>> op.inputs.sort_by_scoping(my_sort_by_scoping)
        """
        return self._sort_by_scoping


class OutputsAscendingSort(_Outputs):
    """Intermediate class used to get outputs from
    ascending_sort operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.ascending_sort()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(ascending_sort._spec().outputs, op)
        self._field = Output(ascending_sort._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.logic.ascending_sort()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
