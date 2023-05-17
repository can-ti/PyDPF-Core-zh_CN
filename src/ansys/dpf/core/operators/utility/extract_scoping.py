"""
extract_scoping
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.outputs import _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class extract_scoping(Operator):
    """Takes a field or a fields container and extracts its scoping or
    scopings container.

    Parameters
    ----------
    field_or_fields_container : Field or FieldsContainer, optional


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.extract_scoping()

    >>> # Make input connections
    >>> my_field_or_fields_container = dpf.Field()
    >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.extract_scoping(
    ...     field_or_fields_container=my_field_or_fields_container,
    ... )

    >>> # Get output data
    >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """

    def __init__(self, field_or_fields_container=None, config=None, server=None):
        super().__init__(name="extract_scoping", config=config, server=server)
        self._inputs = InputsExtractScoping(self)
        self._outputs = OutputsExtractScoping(self)
        if field_or_fields_container is not None:
            self.inputs.field_or_fields_container.connect(field_or_fields_container)

    @staticmethod
    def _spec():
        description = """Takes a field or a fields container and extracts its scoping or
            scopings container."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field_or_fields_container",
                    type_names=["field", "fields_container"],
                    optional=True,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping", "scopings_container"],
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
        return Operator.default_config(name="extract_scoping", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsExtractScoping
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsExtractScoping
        """
        return super().outputs


class InputsExtractScoping(_Inputs):
    """Intermediate class used to connect user inputs to
    extract_scoping operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.extract_scoping()
    >>> my_field_or_fields_container = dpf.Field()
    >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
    """

    def __init__(self, op: Operator):
        super().__init__(extract_scoping._spec().inputs, op)
        self._field_or_fields_container = Input(
            extract_scoping._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._field_or_fields_container)

    @property
    def field_or_fields_container(self):
        """Allows to connect field_or_fields_container input to the operator.

        Parameters
        ----------
        my_field_or_fields_container : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.extract_scoping()
        >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
        >>> # or
        >>> op.inputs.field_or_fields_container(my_field_or_fields_container)
        """
        return self._field_or_fields_container


class OutputsExtractScoping(_Outputs):
    """Intermediate class used to get outputs from
    extract_scoping operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.extract_scoping()
    >>> # Connect inputs : op.inputs. ...
    >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """

    def __init__(self, op: Operator):
        super().__init__(extract_scoping._spec().outputs, op)
        self.mesh_scoping_as_scoping = Output(
            _modify_output_spec_with_one_type(
                extract_scoping._spec().output_pin(0), "scoping"
            ),
            0,
            op,
        )
        self._outputs.append(self.mesh_scoping_as_scoping)
        self.mesh_scoping_as_scopings_container = Output(
            _modify_output_spec_with_one_type(
                extract_scoping._spec().output_pin(0), "scopings_container"
            ),
            0,
            op,
        )
        self._outputs.append(self.mesh_scoping_as_scopings_container)
