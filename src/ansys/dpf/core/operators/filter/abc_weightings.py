"""
abc_weightings
==============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class abc_weightings(Operator):
    """Computes ABC-weightings for the amplitude spectrum in dB units.

    Parameters
    ----------
    fields_container : FieldsContainer
        Data to be weighted in db units.
    weighting_type : int
        If this pin is set to 0, the a-weighting is
        computed, 1 the b-weigting is
        computed and 2 the c-weightings is
        computed.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.filter.abc_weightings()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_weighting_type = int()
    >>> op.inputs.weighting_type.connect(my_weighting_type)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.filter.abc_weightings(
    ...     fields_container=my_fields_container,
    ...     weighting_type=my_weighting_type,
    ... )

    >>> # Get output data
    >>> result_weightings = op.outputs.weightings()
    """

    def __init__(
        self, fields_container=None, weighting_type=None, config=None, server=None
    ):
        super().__init__(name="abc_weightings", config=config, server=server)
        self._inputs = InputsAbcWeightings(self)
        self._outputs = OutputsAbcWeightings(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if weighting_type is not None:
            self.inputs.weighting_type.connect(weighting_type)

    @staticmethod
    def _spec():
        description = (
            """Computes ABC-weightings for the amplitude spectrum in dB units."""
        )
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Data to be weighted in db units.""",
                ),
                1: PinSpecification(
                    name="weighting_type",
                    type_names=["int32"],
                    optional=False,
                    document="""If this pin is set to 0, the a-weighting is
        computed, 1 the b-weigting is
        computed and 2 the c-weightings is
        computed.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="weightings",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Weighted data in db units.""",
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
        return Operator.default_config(name="abc_weightings", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAbcWeightings
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAbcWeightings
        """
        return super().outputs


class InputsAbcWeightings(_Inputs):
    """Intermediate class used to connect user inputs to
    abc_weightings operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.filter.abc_weightings()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_weighting_type = int()
    >>> op.inputs.weighting_type.connect(my_weighting_type)
    """

    def __init__(self, op: Operator):
        super().__init__(abc_weightings._spec().inputs, op)
        self._fields_container = Input(abc_weightings._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fields_container)
        self._weighting_type = Input(abc_weightings._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._weighting_type)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Data to be weighted in db units.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.abc_weightings()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def weighting_type(self):
        """Allows to connect weighting_type input to the operator.

        If this pin is set to 0, the a-weighting is
        computed, 1 the b-weigting is
        computed and 2 the c-weightings is
        computed.

        Parameters
        ----------
        my_weighting_type : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.abc_weightings()
        >>> op.inputs.weighting_type.connect(my_weighting_type)
        >>> # or
        >>> op.inputs.weighting_type(my_weighting_type)
        """
        return self._weighting_type


class OutputsAbcWeightings(_Outputs):
    """Intermediate class used to get outputs from
    abc_weightings operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.filter.abc_weightings()
    >>> # Connect inputs : op.inputs. ...
    >>> result_weightings = op.outputs.weightings()
    """

    def __init__(self, op: Operator):
        super().__init__(abc_weightings._spec().outputs, op)
        self._weightings = Output(abc_weightings._spec().output_pin(0), 0, op)
        self._outputs.append(self._weightings)

    @property
    def weightings(self):
        """Allows to get weightings output of the operator

        Returns
        ----------
        my_weightings : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.filter.abc_weightings()
        >>> # Connect inputs : op.inputs. ...
        >>> result_weightings = op.outputs.weightings()
        """  # noqa: E501
        return self._weightings