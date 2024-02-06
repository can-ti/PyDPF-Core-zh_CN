"""
modal_participation
===================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class modal_participation(Operator):
    """Compute the modal participation factor for a given vector field V,
    defined as  sum_i ( V .dot. mode_shape_i * ponderation ).

    Parameters
    ----------
    v_real : Field
        Real part of field v
    v_imag : Field
        Imag part of field v
    mode_shapes : FieldsContainer
    ponderation : Field, optional
    force_label_space : dict, optional
        If set, will force a label space for output
        result.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.modal_participation()

    >>> # Make input connections
    >>> my_v_real = dpf.Field()
    >>> op.inputs.v_real.connect(my_v_real)
    >>> my_v_imag = dpf.Field()
    >>> op.inputs.v_imag.connect(my_v_imag)
    >>> my_mode_shapes = dpf.FieldsContainer()
    >>> op.inputs.mode_shapes.connect(my_mode_shapes)
    >>> my_ponderation = dpf.Field()
    >>> op.inputs.ponderation.connect(my_ponderation)
    >>> my_force_label_space = dict()
    >>> op.inputs.force_label_space.connect(my_force_label_space)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.modal_participation(
    ...     v_real=my_v_real,
    ...     v_imag=my_v_imag,
    ...     mode_shapes=my_mode_shapes,
    ...     ponderation=my_ponderation,
    ...     force_label_space=my_force_label_space,
    ... )

    >>> # Get output data
    >>> result_output = op.outputs.output()
    """

    def __init__(
        self,
        v_real=None,
        v_imag=None,
        mode_shapes=None,
        ponderation=None,
        force_label_space=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="harmonic::modal_participation", config=config, server=server
        )
        self._inputs = InputsModalParticipation(self)
        self._outputs = OutputsModalParticipation(self)
        if v_real is not None:
            self.inputs.v_real.connect(v_real)
        if v_imag is not None:
            self.inputs.v_imag.connect(v_imag)
        if mode_shapes is not None:
            self.inputs.mode_shapes.connect(mode_shapes)
        if ponderation is not None:
            self.inputs.ponderation.connect(ponderation)
        if force_label_space is not None:
            self.inputs.force_label_space.connect(force_label_space)

    @staticmethod
    def _spec():
        description = """Compute the modal participation factor for a given vector field V,
            defined as  sum_i ( V .dot. mode_shape_i * ponderation )."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="v_real",
                    type_names=["field"],
                    optional=False,
                    document="""Real part of field v""",
                ),
                1: PinSpecification(
                    name="v_imag",
                    type_names=["field"],
                    optional=False,
                    document="""Imag part of field v""",
                ),
                2: PinSpecification(
                    name="mode_shapes",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                3: PinSpecification(
                    name="ponderation",
                    type_names=["field"],
                    optional=True,
                    document="""""",
                ),
                4: PinSpecification(
                    name="force_label_space",
                    type_names=["label_space"],
                    optional=True,
                    document="""If set, will force a label space for output
        result.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="output",
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
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(
            name="harmonic::modal_participation", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsModalParticipation
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsModalParticipation
        """
        return super().outputs


class InputsModalParticipation(_Inputs):
    """Intermediate class used to connect user inputs to
    modal_participation operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.modal_participation()
    >>> my_v_real = dpf.Field()
    >>> op.inputs.v_real.connect(my_v_real)
    >>> my_v_imag = dpf.Field()
    >>> op.inputs.v_imag.connect(my_v_imag)
    >>> my_mode_shapes = dpf.FieldsContainer()
    >>> op.inputs.mode_shapes.connect(my_mode_shapes)
    >>> my_ponderation = dpf.Field()
    >>> op.inputs.ponderation.connect(my_ponderation)
    >>> my_force_label_space = dict()
    >>> op.inputs.force_label_space.connect(my_force_label_space)
    """

    def __init__(self, op: Operator):
        super().__init__(modal_participation._spec().inputs, op)
        self._v_real = Input(modal_participation._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._v_real)
        self._v_imag = Input(modal_participation._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._v_imag)
        self._mode_shapes = Input(modal_participation._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._mode_shapes)
        self._ponderation = Input(modal_participation._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._ponderation)
        self._force_label_space = Input(
            modal_participation._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._force_label_space)

    @property
    def v_real(self):
        """Allows to connect v_real input to the operator.

        Real part of field v

        Parameters
        ----------
        my_v_real : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_participation()
        >>> op.inputs.v_real.connect(my_v_real)
        >>> # or
        >>> op.inputs.v_real(my_v_real)
        """
        return self._v_real

    @property
    def v_imag(self):
        """Allows to connect v_imag input to the operator.

        Imag part of field v

        Parameters
        ----------
        my_v_imag : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_participation()
        >>> op.inputs.v_imag.connect(my_v_imag)
        >>> # or
        >>> op.inputs.v_imag(my_v_imag)
        """
        return self._v_imag

    @property
    def mode_shapes(self):
        """Allows to connect mode_shapes input to the operator.

        Parameters
        ----------
        my_mode_shapes : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_participation()
        >>> op.inputs.mode_shapes.connect(my_mode_shapes)
        >>> # or
        >>> op.inputs.mode_shapes(my_mode_shapes)
        """
        return self._mode_shapes

    @property
    def ponderation(self):
        """Allows to connect ponderation input to the operator.

        Parameters
        ----------
        my_ponderation : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_participation()
        >>> op.inputs.ponderation.connect(my_ponderation)
        >>> # or
        >>> op.inputs.ponderation(my_ponderation)
        """
        return self._ponderation

    @property
    def force_label_space(self):
        """Allows to connect force_label_space input to the operator.

        If set, will force a label space for output
        result.

        Parameters
        ----------
        my_force_label_space : dict

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_participation()
        >>> op.inputs.force_label_space.connect(my_force_label_space)
        >>> # or
        >>> op.inputs.force_label_space(my_force_label_space)
        """
        return self._force_label_space


class OutputsModalParticipation(_Outputs):
    """Intermediate class used to get outputs from
    modal_participation operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.modal_participation()
    >>> # Connect inputs : op.inputs. ...
    >>> result_output = op.outputs.output()
    """

    def __init__(self, op: Operator):
        super().__init__(modal_participation._spec().outputs, op)
        self._output = Output(modal_participation._spec().output_pin(0), 0, op)
        self._outputs.append(self._output)

    @property
    def output(self):
        """Allows to get output output of the operator

        Returns
        ----------
        my_output : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.modal_participation()
        >>> # Connect inputs : op.inputs. ...
        >>> result_output = op.outputs.output()
        """  # noqa: E501
        return self._output
