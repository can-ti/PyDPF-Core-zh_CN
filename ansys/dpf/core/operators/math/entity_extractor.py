"""
entity_extractor
================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class entity_extractor(Operator):
    """Extract an entity from a field, based on its Id.

    Parameters
    ----------
    fieldA : Field
    scalar_int : int


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.entity_extractor()

    >>> # Make input connections
    >>> my_fieldA = dpf.Field()
    >>> op.inputs.fieldA.connect(my_fieldA)
    >>> my_scalar_int = int()
    >>> op.inputs.scalar_int.connect(my_scalar_int)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.entity_extractor(
    ...     fieldA=my_fieldA,
    ...     scalar_int=my_scalar_int,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, fieldA=None, scalar_int=None, config=None, server=None):
        super().__init__(name="entity_extractor", config=config, server=server)
        self._inputs = InputsEntityExtractor(self)
        self._outputs = OutputsEntityExtractor(self)
        if fieldA is not None:
            self.inputs.fieldA.connect(fieldA)
        if scalar_int is not None:
            self.inputs.scalar_int.connect(scalar_int)

    @staticmethod
    def _spec():
        description = """Extract an entity from a field, based on its Id."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fieldA",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="scalar_int",
                    type_names=["int32"],
                    optional=False,
                    document="""""",
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
        return Operator.default_config(name="entity_extractor", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsEntityExtractor
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsEntityExtractor
        """
        return super().outputs


class InputsEntityExtractor(_Inputs):
    """Intermediate class used to connect user inputs to
    entity_extractor operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.entity_extractor()
    >>> my_fieldA = dpf.Field()
    >>> op.inputs.fieldA.connect(my_fieldA)
    >>> my_scalar_int = int()
    >>> op.inputs.scalar_int.connect(my_scalar_int)
    """

    def __init__(self, op: Operator):
        super().__init__(entity_extractor._spec().inputs, op)
        self._fieldA = Input(entity_extractor._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fieldA)
        self._scalar_int = Input(entity_extractor._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._scalar_int)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator.

        Parameters
        ----------
        my_fieldA : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.entity_extractor()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> # or
        >>> op.inputs.fieldA(my_fieldA)
        """
        return self._fieldA

    @property
    def scalar_int(self):
        """Allows to connect scalar_int input to the operator.

        Parameters
        ----------
        my_scalar_int : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.entity_extractor()
        >>> op.inputs.scalar_int.connect(my_scalar_int)
        >>> # or
        >>> op.inputs.scalar_int(my_scalar_int)
        """
        return self._scalar_int


class OutputsEntityExtractor(_Outputs):
    """Intermediate class used to get outputs from
    entity_extractor operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.entity_extractor()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(entity_extractor._spec().outputs, op)
        self._field = Output(entity_extractor._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.math.entity_extractor()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
