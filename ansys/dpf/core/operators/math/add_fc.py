"""
add_fc
------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class add_fc(Operator):
    """Select all fields having the same label space in the input fields
    container, and add those together. If fields, doubles, or vectors
    of doubles are put in input, they are added to all the fields.

    Parameters
    ----------
    fields_container1 : FieldsContainer or Field or float
    fields_container2 : FieldsContainer or Field or float


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.add_fc()

    >>> # Make input connections
    >>> my_fields_container1 = dpf.FieldsContainer()
    >>> op.inputs.fields_container1.connect(my_fields_container1)
    >>> my_fields_container2 = dpf.FieldsContainer()
    >>> op.inputs.fields_container2.connect(my_fields_container2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.add_fc(
    ...     fields_container1=my_fields_container1,
    ...     fields_container2=my_fields_container2,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self, fields_container1=None, fields_container2=None, config=None, server=None
    ):
        super().__init__(name="add_fc", config=config, server=server)
        self._inputs = InputsAddFc(self)
        self._outputs = OutputsAddFc(self)
        if fields_container1 is not None:
            self.inputs.fields_container1.connect(fields_container1)
        if fields_container2 is not None:
            self.inputs.fields_container2.connect(fields_container2)

    @staticmethod
    def _spec():
        description = """Select all fields having the same label space in the input fields
            container, and add those together. If fields, doubles, or
            vectors of doubles are put in input, they are added to all
            the fields."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=[
                        "fields_container",
                        "field",
                        "double",
                        "vector<double>",
                    ],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="fields_container",
                    type_names=[
                        "fields_container",
                        "field",
                        "double",
                        "vector<double>",
                    ],
                    optional=False,
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
        return Operator.default_config(name="add_fc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAddFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAddFc
        """
        return super().outputs


class InputsAddFc(_Inputs):
    """Intermediate class used to connect user inputs to
    add_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.add_fc()
    >>> my_fields_container1 = dpf.FieldsContainer()
    >>> op.inputs.fields_container1.connect(my_fields_container1)
    >>> my_fields_container2 = dpf.FieldsContainer()
    >>> op.inputs.fields_container2.connect(my_fields_container2)
    """

    def __init__(self, op: Operator):
        super().__init__(add_fc._spec().inputs, op)
        self._fields_container1 = Input(add_fc._spec().input_pin(0), 0, op, 0)
        self._inputs.append(self._fields_container1)
        self._fields_container2 = Input(add_fc._spec().input_pin(1), 1, op, 1)
        self._inputs.append(self._fields_container2)

    @property
    def fields_container1(self):
        """Allows to connect fields_container1 input to the operator.

        Parameters
        ----------
        my_fields_container1 : FieldsContainer or Field or float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.add_fc()
        >>> op.inputs.fields_container1.connect(my_fields_container1)
        >>> # or
        >>> op.inputs.fields_container1(my_fields_container1)
        """
        return self._fields_container1

    @property
    def fields_container2(self):
        """Allows to connect fields_container2 input to the operator.

        Parameters
        ----------
        my_fields_container2 : FieldsContainer or Field or float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.add_fc()
        >>> op.inputs.fields_container2.connect(my_fields_container2)
        >>> # or
        >>> op.inputs.fields_container2(my_fields_container2)
        """
        return self._fields_container2


class OutputsAddFc(_Outputs):
    """Intermediate class used to get outputs from
    add_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.add_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(add_fc._spec().outputs, op)
        self._fields_container = Output(add_fc._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.add_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
