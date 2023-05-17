"""
scoping_get_attribute
=====================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.outputs import _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class scoping_get_attribute(Operator):
    """Uses the Scoping APIs to return a given attribute of the scoping in
    input.

    Parameters
    ----------
    scoping : Scoping
    property_name : str
        Supported property names are: "ids",
        "location".


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.scoping.scoping_get_attribute()

    >>> # Make input connections
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.scoping.scoping_get_attribute(
    ...     scoping=my_scoping,
    ...     property_name=my_property_name,
    ... )

    >>> # Get output data
    >>> result_property = op.outputs.property()
    """

    def __init__(self, scoping=None, property_name=None, config=None, server=None):
        super().__init__(name="scoping::get_attribute", config=config, server=server)
        self._inputs = InputsScopingGetAttribute(self)
        self._outputs = OutputsScopingGetAttribute(self)
        if scoping is not None:
            self.inputs.scoping.connect(scoping)
        if property_name is not None:
            self.inputs.property_name.connect(property_name)

    @staticmethod
    def _spec():
        description = """Uses the Scoping APIs to return a given attribute of the scoping in
            input."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="scoping",
                    type_names=["scoping"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="property_name",
                    type_names=["string"],
                    optional=False,
                    document="""Supported property names are: "ids",
        "location".""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="property",
                    type_names=["vector<int32>", "string"],
                    optional=False,
                    document="""Returns a vector of int for property: "ids"
        and a string for property:
        "location".""",
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
        return Operator.default_config(name="scoping::get_attribute", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsScopingGetAttribute
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsScopingGetAttribute
        """
        return super().outputs


class InputsScopingGetAttribute(_Inputs):
    """Intermediate class used to connect user inputs to
    scoping_get_attribute operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.scoping_get_attribute()
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)
    """

    def __init__(self, op: Operator):
        super().__init__(scoping_get_attribute._spec().inputs, op)
        self._scoping = Input(scoping_get_attribute._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._scoping)
        self._property_name = Input(
            scoping_get_attribute._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._property_name)

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator.

        Parameters
        ----------
        my_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.scoping_get_attribute()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> # or
        >>> op.inputs.scoping(my_scoping)
        """
        return self._scoping

    @property
    def property_name(self):
        """Allows to connect property_name input to the operator.

        Supported property names are: "ids",
        "location".

        Parameters
        ----------
        my_property_name : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.scoping_get_attribute()
        >>> op.inputs.property_name.connect(my_property_name)
        >>> # or
        >>> op.inputs.property_name(my_property_name)
        """
        return self._property_name


class OutputsScopingGetAttribute(_Outputs):
    """Intermediate class used to get outputs from
    scoping_get_attribute operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.scoping_get_attribute()
    >>> # Connect inputs : op.inputs. ...
    >>> result_property = op.outputs.property()
    """

    def __init__(self, op: Operator):
        super().__init__(scoping_get_attribute._spec().outputs, op)
        self.property_as_vector_int32_ = Output(
            _modify_output_spec_with_one_type(
                scoping_get_attribute._spec().output_pin(0), "vector_int32_"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_vector_int32_)
        self.property_as_string = Output(
            _modify_output_spec_with_one_type(
                scoping_get_attribute._spec().output_pin(0), "string"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_string)
