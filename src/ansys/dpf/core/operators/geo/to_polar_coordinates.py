"""
to_polar_coordinates
====================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class to_polar_coordinates(Operator):
    """Finds r, theta (rad), and z coordinates of a coordinates (nodal) field
    in a cartesian coordinates system where the input coordinate
    system defines the rotation axis and the origin.

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container with only one field
        is expected
    coordinate_system : Field, optional
        3-3 rotation matrix and origin coordinates
        must be set here to define a
        coordinate system. by default, the
        rotation axis is the z axis and the
        origin is [0,0,0].


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.geo.to_polar_coordinates()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_coordinate_system = dpf.Field()
    >>> op.inputs.coordinate_system.connect(my_coordinate_system)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.geo.to_polar_coordinates(
    ...     field=my_field,
    ...     coordinate_system=my_coordinate_system,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, field=None, coordinate_system=None, config=None, server=None):
        super().__init__(name="polar_coordinates", config=config, server=server)
        self._inputs = InputsToPolarCoordinates(self)
        self._outputs = OutputsToPolarCoordinates(self)
        if field is not None:
            self.inputs.field.connect(field)
        if coordinate_system is not None:
            self.inputs.coordinate_system.connect(coordinate_system)

    @staticmethod
    def _spec():
        description = """Finds r, theta (rad), and z coordinates of a coordinates (nodal) field
            in a cartesian coordinates system where the input
            coordinate system defines the rotation axis and the
            origin."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
                ),
                1: PinSpecification(
                    name="coordinate_system",
                    type_names=["field"],
                    optional=True,
                    document="""3-3 rotation matrix and origin coordinates
        must be set here to define a
        coordinate system. by default, the
        rotation axis is the z axis and the
        origin is [0,0,0].""",
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
        return Operator.default_config(name="polar_coordinates", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsToPolarCoordinates
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsToPolarCoordinates
        """
        return super().outputs


class InputsToPolarCoordinates(_Inputs):
    """Intermediate class used to connect user inputs to
    to_polar_coordinates operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.to_polar_coordinates()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_coordinate_system = dpf.Field()
    >>> op.inputs.coordinate_system.connect(my_coordinate_system)
    """

    def __init__(self, op: Operator):
        super().__init__(to_polar_coordinates._spec().inputs, op)
        self._field = Input(to_polar_coordinates._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._coordinate_system = Input(
            to_polar_coordinates._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._coordinate_system)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_field : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.to_polar_coordinates()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def coordinate_system(self):
        """Allows to connect coordinate_system input to the operator.

        3-3 rotation matrix and origin coordinates
        must be set here to define a
        coordinate system. by default, the
        rotation axis is the z axis and the
        origin is [0,0,0].

        Parameters
        ----------
        my_coordinate_system : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.to_polar_coordinates()
        >>> op.inputs.coordinate_system.connect(my_coordinate_system)
        >>> # or
        >>> op.inputs.coordinate_system(my_coordinate_system)
        """
        return self._coordinate_system


class OutputsToPolarCoordinates(_Outputs):
    """Intermediate class used to get outputs from
    to_polar_coordinates operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.to_polar_coordinates()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(to_polar_coordinates._spec().outputs, op)
        self._field = Output(to_polar_coordinates._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.geo.to_polar_coordinates()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
