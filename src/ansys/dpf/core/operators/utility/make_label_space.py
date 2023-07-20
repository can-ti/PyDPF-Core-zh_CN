"""
make_label_space
================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class make_label_space(Operator):
    """Assemble strings and integers to make a label space.

    Parameters
    ----------
    base_label : dict or FieldsContainer or ScopingsContainer, optional
        Used as a base label (extracted from
        fields/scoping container, or directly
        from label space) that is
        concatenated with provided values.
    label_name : str
    label_value1 : int
    label_value2 : int


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.make_label_space()

    >>> # Make input connections
    >>> my_base_label = dict()
    >>> op.inputs.base_label.connect(my_base_label)
    >>> my_label_name = str()
    >>> op.inputs.label_name.connect(my_label_name)
    >>> my_label_value1 = int()
    >>> op.inputs.label_value1.connect(my_label_value1)
    >>> my_label_value2 = int()
    >>> op.inputs.label_value2.connect(my_label_value2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.make_label_space(
    ...     base_label=my_base_label,
    ...     label_name=my_label_name,
    ...     label_value1=my_label_value1,
    ...     label_value2=my_label_value2,
    ... )

    >>> # Get output data
    >>> result_label = op.outputs.label()
    """

    def __init__(
        self,
        base_label=None,
        label_name=None,
        label_value1=None,
        label_value2=None,
        config=None,
        server=None,
    ):
        super().__init__(name="make_label_space", config=config, server=server)
        self._inputs = InputsMakeLabelSpace(self)
        self._outputs = OutputsMakeLabelSpace(self)
        if base_label is not None:
            self.inputs.base_label.connect(base_label)
        if label_name is not None:
            self.inputs.label_name.connect(label_name)
        if label_value1 is not None:
            self.inputs.label_value1.connect(label_value1)
        if label_value2 is not None:
            self.inputs.label_value2.connect(label_value2)

    @staticmethod
    def _spec():
        description = """Assemble strings and integers to make a label space."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="base_label",
                    type_names=[
                        "label_space",
                        "fields_container",
                        "scopings_container",
                    ],
                    optional=True,
                    document="""Used as a base label (extracted from
        fields/scoping container, or directly
        from label space) that is
        concatenated with provided values.""",
                ),
                1: PinSpecification(
                    name="label_name",
                    type_names=["string"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="label_value",
                    type_names=["int32"],
                    optional=False,
                    document="""""",
                ),
                3: PinSpecification(
                    name="label_value",
                    type_names=["int32"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="label",
                    type_names=["label_space"],
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
        return Operator.default_config(name="make_label_space", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMakeLabelSpace
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMakeLabelSpace
        """
        return super().outputs


class InputsMakeLabelSpace(_Inputs):
    """Intermediate class used to connect user inputs to
    make_label_space operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.make_label_space()
    >>> my_base_label = dict()
    >>> op.inputs.base_label.connect(my_base_label)
    >>> my_label_name = str()
    >>> op.inputs.label_name.connect(my_label_name)
    >>> my_label_value1 = int()
    >>> op.inputs.label_value1.connect(my_label_value1)
    >>> my_label_value2 = int()
    >>> op.inputs.label_value2.connect(my_label_value2)
    """

    def __init__(self, op: Operator):
        super().__init__(make_label_space._spec().inputs, op)
        self._base_label = Input(make_label_space._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._base_label)
        self._label_name = Input(make_label_space._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._label_name)
        self._label_value1 = Input(make_label_space._spec().input_pin(2), 2, op, 0)
        self._inputs.append(self._label_value1)
        self._label_value2 = Input(make_label_space._spec().input_pin(3), 3, op, 1)
        self._inputs.append(self._label_value2)

    @property
    def base_label(self):
        """Allows to connect base_label input to the operator.

        Used as a base label (extracted from
        fields/scoping container, or directly
        from label space) that is
        concatenated with provided values.

        Parameters
        ----------
        my_base_label : dict or FieldsContainer or ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_label_space()
        >>> op.inputs.base_label.connect(my_base_label)
        >>> # or
        >>> op.inputs.base_label(my_base_label)
        """
        return self._base_label

    @property
    def label_name(self):
        """Allows to connect label_name input to the operator.

        Parameters
        ----------
        my_label_name : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_label_space()
        >>> op.inputs.label_name.connect(my_label_name)
        >>> # or
        >>> op.inputs.label_name(my_label_name)
        """
        return self._label_name

    @property
    def label_value1(self):
        """Allows to connect label_value1 input to the operator.

        Parameters
        ----------
        my_label_value1 : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_label_space()
        >>> op.inputs.label_value1.connect(my_label_value1)
        >>> # or
        >>> op.inputs.label_value1(my_label_value1)
        """
        return self._label_value1

    @property
    def label_value2(self):
        """Allows to connect label_value2 input to the operator.

        Parameters
        ----------
        my_label_value2 : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_label_space()
        >>> op.inputs.label_value2.connect(my_label_value2)
        >>> # or
        >>> op.inputs.label_value2(my_label_value2)
        """
        return self._label_value2


class OutputsMakeLabelSpace(_Outputs):
    """Intermediate class used to get outputs from
    make_label_space operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.make_label_space()
    >>> # Connect inputs : op.inputs. ...
    >>> result_label = op.outputs.label()
    """

    def __init__(self, op: Operator):
        super().__init__(make_label_space._spec().outputs, op)
        self._label = Output(make_label_space._spec().output_pin(0), 0, op)
        self._outputs.append(self._label)

    @property
    def label(self):
        """Allows to get label output of the operator

        Returns
        ----------
        my_label : dict

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_label_space()
        >>> # Connect inputs : op.inputs. ...
        >>> result_label = op.outputs.label()
        """  # noqa: E501
        return self._label
