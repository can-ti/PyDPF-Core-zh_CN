"""
principal_invariants_fc
-----------------------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class principal_invariants_fc(Operator):
    """Computes the element-wise eigen values of all the tensor fields of a
    fields container.

    Parameters
    ----------
    fields_container : FieldsContainer


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.invariant.principal_invariants_fc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.invariant.principal_invariants_fc(
    ...     fields_container=my_fields_container,
    ... )

    >>> # Get output data
    >>> result_fields_eig_1 = op.outputs.fields_eig_1()
    >>> result_fields_eig_2 = op.outputs.fields_eig_2()
    >>> result_fields_eig_3 = op.outputs.fields_eig_3()
    """

    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="invariants_fc", config=config, server=server)
        self._inputs = InputsPrincipalInvariantsFc(self)
        self._outputs = OutputsPrincipalInvariantsFc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        description = """Computes the element-wise eigen values of all the tensor fields of a
            fields container."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_eig_1",
                    type_names=["fields_container"],
                    optional=False,
                    document="""First eigen value fields""",
                ),
                1: PinSpecification(
                    name="fields_eig_2",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Second eigen value fields""",
                ),
                2: PinSpecification(
                    name="fields_eig_3",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Third eigen value fields""",
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
        return Operator.default_config(name="invariants_fc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPrincipalInvariantsFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPrincipalInvariantsFc
        """
        return super().outputs


class InputsPrincipalInvariantsFc(_Inputs):
    """Intermediate class used to connect user inputs to
    principal_invariants_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.invariant.principal_invariants_fc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    """

    def __init__(self, op: Operator):
        super().__init__(principal_invariants_fc._spec().inputs, op)
        self._fields_container = Input(
            principal_invariants_fc._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.principal_invariants_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container


class OutputsPrincipalInvariantsFc(_Outputs):
    """Intermediate class used to get outputs from
    principal_invariants_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.invariant.principal_invariants_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_eig_1 = op.outputs.fields_eig_1()
    >>> result_fields_eig_2 = op.outputs.fields_eig_2()
    >>> result_fields_eig_3 = op.outputs.fields_eig_3()
    """

    def __init__(self, op: Operator):
        super().__init__(principal_invariants_fc._spec().outputs, op)
        self._fields_eig_1 = Output(
            principal_invariants_fc._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._fields_eig_1)
        self._fields_eig_2 = Output(
            principal_invariants_fc._spec().output_pin(1), 1, op
        )
        self._outputs.append(self._fields_eig_2)
        self._fields_eig_3 = Output(
            principal_invariants_fc._spec().output_pin(2), 2, op
        )
        self._outputs.append(self._fields_eig_3)

    @property
    def fields_eig_1(self):
        """Allows to get fields_eig_1 output of the operator

        Returns
        ----------
        my_fields_eig_1 : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.principal_invariants_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_eig_1 = op.outputs.fields_eig_1()
        """  # noqa: E501
        return self._fields_eig_1

    @property
    def fields_eig_2(self):
        """Allows to get fields_eig_2 output of the operator

        Returns
        ----------
        my_fields_eig_2 : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.principal_invariants_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_eig_2 = op.outputs.fields_eig_2()
        """  # noqa: E501
        return self._fields_eig_2

    @property
    def fields_eig_3(self):
        """Allows to get fields_eig_3 output of the operator

        Returns
        ----------
        my_fields_eig_3 : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.invariant.principal_invariants_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_eig_3 = op.outputs.fields_eig_3()
        """  # noqa: E501
        return self._fields_eig_3
