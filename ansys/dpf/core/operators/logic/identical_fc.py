"""
identical_fc
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class identical_fc(Operator):
    """Check if two fields container are identical.

    Parameters
    ----------
    fields_containerA : FieldsContainer
    fields_containerB : FieldsContainer
    small_value : float, optional
        Double positive small value.smallest value
        which will be considered during the
        comparison step : all the abs(values)
        in field less than this value is
        considered as null, (default
        value:1.0e-14).
    tolerance : float, optional
        Double relative tolerance. maximum tolerance
        gap between to compared values:
        values within relative tolerance are
        considered identical (v1-v2)/v2 <
        relativetol (default is 0.001).


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.logic.identical_fc()

    >>> # Make input connections
    >>> my_fields_containerA = dpf.FieldsContainer()
    >>> op.inputs.fields_containerA.connect(my_fields_containerA)
    >>> my_fields_containerB = dpf.FieldsContainer()
    >>> op.inputs.fields_containerB.connect(my_fields_containerB)
    >>> my_small_value = float()
    >>> op.inputs.small_value.connect(my_small_value)
    >>> my_tolerance = float()
    >>> op.inputs.tolerance.connect(my_tolerance)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.logic.identical_fc(
    ...     fields_containerA=my_fields_containerA,
    ...     fields_containerB=my_fields_containerB,
    ...     small_value=my_small_value,
    ...     tolerance=my_tolerance,
    ... )

    >>> # Get output data
    >>> result_boolean = op.outputs.boolean()
    >>> result_message = op.outputs.message()
    """

    def __init__(
        self,
        fields_containerA=None,
        fields_containerB=None,
        small_value=None,
        tolerance=None,
        config=None,
        server=None,
    ):
        super().__init__(name="AreFieldsIdentical_fc", config=config, server=server)
        self._inputs = InputsIdenticalFc(self)
        self._outputs = OutputsIdenticalFc(self)
        if fields_containerA is not None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB is not None:
            self.inputs.fields_containerB.connect(fields_containerB)
        if small_value is not None:
            self.inputs.small_value.connect(small_value)
        if tolerance is not None:
            self.inputs.tolerance.connect(tolerance)

    @staticmethod
    def _spec():
        description = """Check if two fields container are identical."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_containerA",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="fields_containerB",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="small_value",
                    type_names=["double"],
                    optional=True,
                    document="""Double positive small value.smallest value
        which will be considered during the
        comparison step : all the abs(values)
        in field less than this value is
        considered as null, (default
        value:1.0e-14).""",
                ),
                3: PinSpecification(
                    name="tolerance",
                    type_names=["double"],
                    optional=True,
                    document="""Double relative tolerance. maximum tolerance
        gap between to compared values:
        values within relative tolerance are
        considered identical (v1-v2)/v2 <
        relativetol (default is 0.001).""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="boolean",
                    type_names=["bool"],
                    optional=False,
                    document="""Bool (true if identical...)""",
                ),
                1: PinSpecification(
                    name="message",
                    type_names=["string"],
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
        return Operator.default_config(name="AreFieldsIdentical_fc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsIdenticalFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsIdenticalFc
        """
        return super().outputs


class InputsIdenticalFc(_Inputs):
    """Intermediate class used to connect user inputs to
    identical_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.identical_fc()
    >>> my_fields_containerA = dpf.FieldsContainer()
    >>> op.inputs.fields_containerA.connect(my_fields_containerA)
    >>> my_fields_containerB = dpf.FieldsContainer()
    >>> op.inputs.fields_containerB.connect(my_fields_containerB)
    >>> my_small_value = float()
    >>> op.inputs.small_value.connect(my_small_value)
    >>> my_tolerance = float()
    >>> op.inputs.tolerance.connect(my_tolerance)
    """

    def __init__(self, op: Operator):
        super().__init__(identical_fc._spec().inputs, op)
        self._fields_containerA = Input(identical_fc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fields_containerA)
        self._fields_containerB = Input(identical_fc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._fields_containerB)
        self._small_value = Input(identical_fc._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._small_value)
        self._tolerance = Input(identical_fc._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._tolerance)

    @property
    def fields_containerA(self):
        """Allows to connect fields_containerA input to the operator.

        Parameters
        ----------
        my_fields_containerA : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_fc()
        >>> op.inputs.fields_containerA.connect(my_fields_containerA)
        >>> # or
        >>> op.inputs.fields_containerA(my_fields_containerA)
        """
        return self._fields_containerA

    @property
    def fields_containerB(self):
        """Allows to connect fields_containerB input to the operator.

        Parameters
        ----------
        my_fields_containerB : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_fc()
        >>> op.inputs.fields_containerB.connect(my_fields_containerB)
        >>> # or
        >>> op.inputs.fields_containerB(my_fields_containerB)
        """
        return self._fields_containerB

    @property
    def small_value(self):
        """Allows to connect small_value input to the operator.

        Double positive small value.smallest value
        which will be considered during the
        comparison step : all the abs(values)
        in field less than this value is
        considered as null, (default
        value:1.0e-14).

        Parameters
        ----------
        my_small_value : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_fc()
        >>> op.inputs.small_value.connect(my_small_value)
        >>> # or
        >>> op.inputs.small_value(my_small_value)
        """
        return self._small_value

    @property
    def tolerance(self):
        """Allows to connect tolerance input to the operator.

        Double relative tolerance. maximum tolerance
        gap between to compared values:
        values within relative tolerance are
        considered identical (v1-v2)/v2 <
        relativetol (default is 0.001).

        Parameters
        ----------
        my_tolerance : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_fc()
        >>> op.inputs.tolerance.connect(my_tolerance)
        >>> # or
        >>> op.inputs.tolerance(my_tolerance)
        """
        return self._tolerance


class OutputsIdenticalFc(_Outputs):
    """Intermediate class used to get outputs from
    identical_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.identical_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_boolean = op.outputs.boolean()
    >>> result_message = op.outputs.message()
    """

    def __init__(self, op: Operator):
        super().__init__(identical_fc._spec().outputs, op)
        self._boolean = Output(identical_fc._spec().output_pin(0), 0, op)
        self._outputs.append(self._boolean)
        self._message = Output(identical_fc._spec().output_pin(1), 1, op)
        self._outputs.append(self._message)

    @property
    def boolean(self):
        """Allows to get boolean output of the operator

        Returns
        ----------
        my_boolean : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_boolean = op.outputs.boolean()
        """  # noqa: E501
        return self._boolean

    @property
    def message(self):
        """Allows to get message output of the operator

        Returns
        ----------
        my_message : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_message = op.outputs.message()
        """  # noqa: E501
        return self._message
