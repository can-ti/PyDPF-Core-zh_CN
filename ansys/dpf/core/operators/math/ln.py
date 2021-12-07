"""Autogenerated DPF operator classes.

Created on 12/06/2021, 14:28:56.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class ln(Operator):
    """Computes element-wise ln(field[i]).

    Parameters
    ----------
    field : Field or FieldsContainer or float
        Field or fields container with only one field
        is expected


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.ln()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.ln(
    ...     field=my_field,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="ln", config=config, server=server)
        self._inputs = InputsLn(self)
        self._outputs = OutputsLn(self)
        if field is not None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        description = """Computes element-wise ln(field[i])."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=[
                        "field",
                        "fields_container",
                        "double",
                        "vector<double>",
                    ],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
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
            ``None``, attempts to use the the global server.
        """
        return Operator.default_config(name="ln", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsLn
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsLn
        """
        return super().outputs


class InputsLn(_Inputs):
    """Intermediate class used to connect user inputs to
    ln operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.ln()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    """

    def __init__(self, op: Operator):
        super().__init__(ln._spec().inputs, op)
        self._field = Input(ln._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_field : Field or FieldsContainer or float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.ln()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field


class OutputsLn(_Outputs):
    """Intermediate class used to get outputs from
    ln operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.ln()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(ln._spec().outputs, op)
        self._field = Output(ln._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.ln()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
