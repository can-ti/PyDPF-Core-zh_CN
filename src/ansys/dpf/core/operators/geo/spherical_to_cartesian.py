"""
spherical_to_cartesian
======================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class spherical_to_cartesian(Operator):
    """Converts 3D field from spherical coordinates to cartesian coordinates.

    Parameters
    ----------
    field : Field or FieldsContainer


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.geo.spherical_to_cartesian()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.geo.spherical_to_cartesian(
    ...     field=my_field,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="spherical_to_cartesian", config=config, server=server)
        self._inputs = InputsSphericalToCartesian(self)
        self._outputs = OutputsSphericalToCartesian(self)
        if field is not None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        description = (
            """Converts 3D field from spherical coordinates to cartesian coordinates."""
        )
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
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
        return Operator.default_config(name="spherical_to_cartesian", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSphericalToCartesian
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSphericalToCartesian
        """
        return super().outputs


class InputsSphericalToCartesian(_Inputs):
    """Intermediate class used to connect user inputs to
    spherical_to_cartesian operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.spherical_to_cartesian()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    """

    def __init__(self, op: Operator):
        super().__init__(spherical_to_cartesian._spec().inputs, op)
        self._field = Input(spherical_to_cartesian._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Parameters
        ----------
        my_field : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.spherical_to_cartesian()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field


class OutputsSphericalToCartesian(_Outputs):
    """Intermediate class used to get outputs from
    spherical_to_cartesian operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.spherical_to_cartesian()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(spherical_to_cartesian._spec().outputs, op)
        self._field = Output(spherical_to_cartesian._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.geo.spherical_to_cartesian()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
