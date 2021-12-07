"""Autogenerated DPF operator classes.

Created on 12/06/2021, 14:29:01.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class modal_superposition(Operator):
    """Compute the solution in the time/frequency space from a modal solution
    by multiplying a modal basis (in 0) by the solution in this modal
    space (coefficients for each mode for each time/frequency) (in 1).

    Parameters
    ----------
    modal_basis : FieldsContainer
        One field by mode with each field
        representing a mode shape on nodes or
        elements
    solution_in_modal_space : FieldsContainer
        One field by time/frequency with each field
        having a ponderating coefficient for
        each mode of the modal_basis pin
    time_scoping : Scoping, optional
        This input allows to compute the result on a
        subset of the time frequency domain
        defined in the
        solution_in_modal_space fields
        container
    mesh_scoping : Scoping or ScopingsContainer, optional
        This input allows to compute the result on a
        subset of the space domain defined in
        the modal_basis fields container


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.modal_superposition()

    >>> # Make input connections
    >>> my_modal_basis = dpf.FieldsContainer()
    >>> op.inputs.modal_basis.connect(my_modal_basis)
    >>> my_solution_in_modal_space = dpf.FieldsContainer()
    >>> op.inputs.solution_in_modal_space.connect(my_solution_in_modal_space)
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.modal_superposition(
    ...     modal_basis=my_modal_basis,
    ...     solution_in_modal_space=my_solution_in_modal_space,
    ...     time_scoping=my_time_scoping,
    ...     mesh_scoping=my_mesh_scoping,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        modal_basis=None,
        solution_in_modal_space=None,
        time_scoping=None,
        mesh_scoping=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="expansion::modal_superposition", config=config, server=server
        )
        self._inputs = InputsModalSuperposition(self)
        self._outputs = OutputsModalSuperposition(self)
        if modal_basis is not None:
            self.inputs.modal_basis.connect(modal_basis)
        if solution_in_modal_space is not None:
            self.inputs.solution_in_modal_space.connect(solution_in_modal_space)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        description = """Compute the solution in the time/frequency space from a modal solution
            by multiplying a modal basis (in 0) by the solution in
            this modal space (coefficients for each mode for each
            time/frequency) (in 1)."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="modal_basis",
                    type_names=["fields_container"],
                    optional=False,
                    document="""One field by mode with each field
        representing a mode shape on nodes or
        elements""",
                ),
                1: PinSpecification(
                    name="solution_in_modal_space",
                    type_names=["fields_container"],
                    optional=False,
                    document="""One field by time/frequency with each field
        having a ponderating coefficient for
        each mode of the modal_basis pin""",
                ),
                3: PinSpecification(
                    name="time_scoping",
                    type_names=["scoping", "vector<int32>"],
                    optional=True,
                    document="""This input allows to compute the result on a
        subset of the time frequency domain
        defined in the
        solution_in_modal_space fields
        container""",
                ),
                4: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping", "scopings_container"],
                    optional=True,
                    document="""This input allows to compute the result on a
        subset of the space domain defined in
        the modal_basis fields container""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
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
        return Operator.default_config(
            name="expansion::modal_superposition", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsModalSuperposition
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsModalSuperposition
        """
        return super().outputs


class InputsModalSuperposition(_Inputs):
    """Intermediate class used to connect user inputs to
    modal_superposition operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.modal_superposition()
    >>> my_modal_basis = dpf.FieldsContainer()
    >>> op.inputs.modal_basis.connect(my_modal_basis)
    >>> my_solution_in_modal_space = dpf.FieldsContainer()
    >>> op.inputs.solution_in_modal_space.connect(my_solution_in_modal_space)
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    """

    def __init__(self, op: Operator):
        super().__init__(modal_superposition._spec().inputs, op)
        self._modal_basis = Input(modal_superposition._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._modal_basis)
        self._solution_in_modal_space = Input(
            modal_superposition._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._solution_in_modal_space)
        self._time_scoping = Input(modal_superposition._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(modal_superposition._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._mesh_scoping)

    @property
    def modal_basis(self):
        """Allows to connect modal_basis input to the operator.

        One field by mode with each field
        representing a mode shape on nodes or
        elements

        Parameters
        ----------
        my_modal_basis : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_superposition()
        >>> op.inputs.modal_basis.connect(my_modal_basis)
        >>> # or
        >>> op.inputs.modal_basis(my_modal_basis)
        """
        return self._modal_basis

    @property
    def solution_in_modal_space(self):
        """Allows to connect solution_in_modal_space input to the operator.

        One field by time/frequency with each field
        having a ponderating coefficient for
        each mode of the modal_basis pin

        Parameters
        ----------
        my_solution_in_modal_space : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_superposition()
        >>> op.inputs.solution_in_modal_space.connect(my_solution_in_modal_space)
        >>> # or
        >>> op.inputs.solution_in_modal_space(my_solution_in_modal_space)
        """
        return self._solution_in_modal_space

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        This input allows to compute the result on a
        subset of the time frequency domain
        defined in the
        solution_in_modal_space fields
        container

        Parameters
        ----------
        my_time_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_superposition()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        This input allows to compute the result on a
        subset of the space domain defined in
        the modal_basis fields container

        Parameters
        ----------
        my_mesh_scoping : Scoping or ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_superposition()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping


class OutputsModalSuperposition(_Outputs):
    """Intermediate class used to get outputs from
    modal_superposition operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.modal_superposition()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(modal_superposition._spec().outputs, op)
        self._fields_container = Output(
            modal_superposition._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator

        Returns
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_superposition()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
