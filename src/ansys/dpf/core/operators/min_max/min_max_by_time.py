"""
min_max_by_time
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class min_max_by_time(Operator):
    """Evaluates minimum, maximum by time or frequency over all the entities
    of each field

    Parameters
    ----------
    fields_container : FieldsContainer


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.min_max.min_max_by_time()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.min_max.min_max_by_time(
    ...     fields_container=my_fields_container,
    ... )

    >>> # Get output data
    >>> result_min = op.outputs.min()
    >>> result_max = op.outputs.max()
    """

    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="min_max_by_time", config=config, server=server)
        self._inputs = InputsMinMaxByTime(self)
        self._outputs = OutputsMinMaxByTime(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        description = """Evaluates minimum, maximum by time or frequency over all the entities
            of each field"""
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
                    name="min",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="max",
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
        return Operator.default_config(name="min_max_by_time", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMinMaxByTime
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMinMaxByTime
        """
        return super().outputs


class InputsMinMaxByTime(_Inputs):
    """Intermediate class used to connect user inputs to
    min_max_by_time operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.min_max.min_max_by_time()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    """

    def __init__(self, op: Operator):
        super().__init__(min_max_by_time._spec().inputs, op)
        self._fields_container = Input(min_max_by_time._spec().input_pin(0), 0, op, -1)
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
        >>> op = dpf.operators.min_max.min_max_by_time()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container


class OutputsMinMaxByTime(_Outputs):
    """Intermediate class used to get outputs from
    min_max_by_time operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.min_max.min_max_by_time()
    >>> # Connect inputs : op.inputs. ...
    >>> result_min = op.outputs.min()
    >>> result_max = op.outputs.max()
    """

    def __init__(self, op: Operator):
        super().__init__(min_max_by_time._spec().outputs, op)
        self._min = Output(min_max_by_time._spec().output_pin(0), 0, op)
        self._outputs.append(self._min)
        self._max = Output(min_max_by_time._spec().output_pin(1), 1, op)
        self._outputs.append(self._max)

    @property
    def min(self):
        """Allows to get min output of the operator

        Returns
        ----------
        my_min : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_max_by_time()
        >>> # Connect inputs : op.inputs. ...
        >>> result_min = op.outputs.min()
        """  # noqa: E501
        return self._min

    @property
    def max(self):
        """Allows to get max output of the operator

        Returns
        ----------
        my_max : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.min_max.min_max_by_time()
        >>> # Connect inputs : op.inputs. ...
        >>> result_max = op.outputs.max()
        """  # noqa: E501
        return self._max
