"""
min_max_fc_inc
--------------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class min_max_fc_inc(Operator):
    """Compute the component-wise minimum (out 0) and maximum (out 1) over a
    fields container.

    Parameters
    ----------
    fields_container : FieldsContainer


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.min_max.min_max_fc_inc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.min_max.min_max_fc_inc(
    ...     fields_container=my_fields_container,
    ... )

    >>> # Get output data
    >>> result_field_min = op.outputs.field_min()
    >>> result_field_max = op.outputs.field_max()
    """

    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="min_max_fc_inc", config=config, server=server)
        self._inputs = InputsMinMaxFcInc(self)
        self._outputs = OutputsMinMaxFcInc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        description = """Compute the component-wise minimum (out 0) and maximum (out 1) over a
            fields container."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field_min",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="field_max",
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
        return Operator.default_config(name="min_max_fc_inc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMinMaxFcInc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMinMaxFcInc
        """
        return super().outputs


class InputsMinMaxFcInc(_Inputs):
    """Intermediate class used to connect user inputs to
    min_max_fc_inc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.min_max.min_max_fc_inc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    """

    def __init__(self, op: Operator):
        super().__init__(min_max_fc_inc._spec().inputs, op)
        self._fields_container = Input(min_max_fc_inc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_max_fc_inc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container


class OutputsMinMaxFcInc(_Outputs):
    """Intermediate class used to get outputs from
    min_max_fc_inc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.min_max.min_max_fc_inc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field_min = op.outputs.field_min()
    >>> result_field_max = op.outputs.field_max()
    """

    def __init__(self, op: Operator):
        super().__init__(min_max_fc_inc._spec().outputs, op)
        self._field_min = Output(min_max_fc_inc._spec().output_pin(0), 0, op)
        self._outputs.append(self._field_min)
        self._field_max = Output(min_max_fc_inc._spec().output_pin(1), 1, op)
        self._outputs.append(self._field_max)

    @property
    def field_min(self):
        """Allows to get field_min output of the operator

        Returns
        ----------
        my_field_min : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_max_fc_inc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_min = op.outputs.field_min()
        """  # noqa: E501
        return self._field_min

    @property
    def field_max(self):
        """Allows to get field_max output of the operator

        Returns
        ----------
        my_field_max : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_max_fc_inc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_max = op.outputs.field_max()
        """  # noqa: E501
        return self._field_max
