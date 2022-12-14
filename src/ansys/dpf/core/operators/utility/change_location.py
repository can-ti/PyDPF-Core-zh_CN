"""
change_location
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class change_location(Operator):
    """change the location of a field.

    Parameters
    ----------
    field : Field
    new_location : str
        New location of the output field ex 'nodal',
        'elementalnodal', 'elemental'...


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.change_location()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_new_location = str()
    >>> op.inputs.new_location.connect(my_new_location)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.change_location(
    ...     field=my_field,
    ...     new_location=my_new_location,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, field=None, new_location=None, config=None, server=None):
        super().__init__(name="change_location", config=config, server=server)
        self._inputs = InputsChangeLocation(self)
        self._outputs = OutputsChangeLocation(self)
        if field is not None:
            self.inputs.field.connect(field)
        if new_location is not None:
            self.inputs.new_location.connect(new_location)

    @staticmethod
    def _spec():
        description = """change the location of a field."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="new_location",
                    type_names=["string"],
                    optional=False,
                    document="""New location of the output field ex 'nodal',
        'elementalnodal', 'elemental'...""",
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
        return Operator.default_config(name="change_location", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsChangeLocation
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsChangeLocation
        """
        return super().outputs


class InputsChangeLocation(_Inputs):
    """Intermediate class used to connect user inputs to
    change_location operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.change_location()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_new_location = str()
    >>> op.inputs.new_location.connect(my_new_location)
    """

    def __init__(self, op: Operator):
        super().__init__(change_location._spec().inputs, op)
        self._field = Input(change_location._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._new_location = Input(change_location._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._new_location)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Parameters
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.change_location()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def new_location(self):
        """Allows to connect new_location input to the operator.

        New location of the output field ex 'nodal',
        'elementalnodal', 'elemental'...

        Parameters
        ----------
        my_new_location : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.change_location()
        >>> op.inputs.new_location.connect(my_new_location)
        >>> # or
        >>> op.inputs.new_location(my_new_location)
        """
        return self._new_location


class OutputsChangeLocation(_Outputs):
    """Intermediate class used to get outputs from
    change_location operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.change_location()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(change_location._spec().outputs, op)
        self._field = Output(change_location._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.utility.change_location()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field