"""
solid_to_skin
=============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class solid_to_skin(Operator):
    """Maps a field defined on solid elements to a field defined on skin
    elements.

    Parameters
    ----------
    field : Field or FieldsContainer
        Field or fields container with only one field
        is expected
    mesh : MeshedRegion, optional
        Skin mesh region expected


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mapping.solid_to_skin()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mapping.solid_to_skin(
    ...     field=my_field,
    ...     mesh=my_mesh,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, field=None, mesh=None, config=None, server=None):
        super().__init__(name="solid_to_skin", config=config, server=server)
        self._inputs = InputsSolidToSkin(self)
        self._outputs = OutputsSolidToSkin(self)
        if field is not None:
            self.inputs.field.connect(field)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        description = """Maps a field defined on solid elements to a field defined on skin
            elements."""
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
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=True,
                    document="""Skin mesh region expected""",
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
        return Operator.default_config(name="solid_to_skin", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSolidToSkin
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsSolidToSkin
        """
        return super().outputs


class InputsSolidToSkin(_Inputs):
    """Intermediate class used to connect user inputs to
    solid_to_skin operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mapping.solid_to_skin()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    """

    def __init__(self, op: Operator):
        super().__init__(solid_to_skin._spec().inputs, op)
        self._field = Input(solid_to_skin._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._mesh = Input(solid_to_skin._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh)

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
        >>> op = dpf.operators.mapping.solid_to_skin()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Skin mesh region expected

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mapping.solid_to_skin()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh


class OutputsSolidToSkin(_Outputs):
    """Intermediate class used to get outputs from
    solid_to_skin operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mapping.solid_to_skin()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(solid_to_skin._spec().outputs, op)
        self._field = Output(solid_to_skin._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.mapping.solid_to_skin()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
