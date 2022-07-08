"""
min_max_over_time
-----------------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class min_max_over_time(Operator):
    """Evaluates minimum/maximum over time/frequency.

    Parameters
    ----------
    fields_container : FieldsContainer
    int32 : int
        Define min or max.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.min_max_over_time()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_int32 = int()
    >>> op.inputs.int32.connect(my_int32)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.min_max_over_time(
    ...     fields_container=my_fields_container,
    ...     int32=my_int32,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, fields_container=None, int32=None, config=None, server=None):
        super().__init__(
            name="mechanical::min_max_over_time", config=config, server=server
        )
        self._inputs = InputsMinMaxOverTime(self)
        self._outputs = OutputsMinMaxOverTime(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if int32 is not None:
            self.inputs.int32.connect(int32)

    @staticmethod
    def _spec():
        description = """Evaluates minimum/maximum over time/frequency."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                5: PinSpecification(
                    name="int32",
                    type_names=["int32"],
                    optional=False,
                    document="""Define min or max.""",
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
            name="mechanical::min_max_over_time", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMinMaxOverTime
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMinMaxOverTime
        """
        return super().outputs


class InputsMinMaxOverTime(_Inputs):
    """Intermediate class used to connect user inputs to
    min_max_over_time operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.min_max_over_time()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_int32 = int()
    >>> op.inputs.int32.connect(my_int32)
    """

    def __init__(self, op: Operator):
        super().__init__(min_max_over_time._spec().inputs, op)
        self._fields_container = Input(
            min_max_over_time._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._int32 = Input(min_max_over_time._spec().input_pin(5), 5, op, -1)
        self._inputs.append(self._int32)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.min_max_over_time()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def int32(self):
        """Allows to connect int32 input to the operator.

        Define min or max.

        Parameters
        ----------
        my_int32 : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.min_max_over_time()
        >>> op.inputs.int32.connect(my_int32)
        >>> # or
        >>> op.inputs.int32(my_int32)
        """
        return self._int32


class OutputsMinMaxOverTime(_Outputs):
    """Intermediate class used to get outputs from
    min_max_over_time operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.min_max_over_time()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(min_max_over_time._spec().outputs, op)
        self._fields_container = Output(min_max_over_time._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.min_max_over_time()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
