"""
merge_generic_data_container
============================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class merge_generic_data_container(Operator):
    """Merges a list of generic data container. For each data entry, the
    merge operation is forwarded to the correct merge Operator.
    Primitive types cannot be merged, first instance found will be
    maintained in the result.

    Parameters
    ----------
    generic_data_container1 : GenericDataContainer
        Either a vector of generic data containers
        (sharing the same data types) or
        generic data containers from pin 0 to
        ... to merge. supported types rely on
        existing type specific merge
        operators.
    generic_data_container2 : GenericDataContainer
        Either a vector of generic data containers
        (sharing the same data types) or
        generic data containers from pin 0 to
        ... to merge. supported types rely on
        existing type specific merge
        operators.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.merge_generic_data_container()

    >>> # Make input connections
    >>> my_generic_data_container1 = dpf.GenericDataContainer()
    >>> op.inputs.generic_data_container1.connect(my_generic_data_container1)
    >>> my_generic_data_container2 = dpf.GenericDataContainer()
    >>> op.inputs.generic_data_container2.connect(my_generic_data_container2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.merge_generic_data_container(
    ...     generic_data_container1=my_generic_data_container1,
    ...     generic_data_container2=my_generic_data_container2,
    ... )

    >>> # Get output data
    >>> result_any = op.outputs.any()
    """

    def __init__(
        self,
        generic_data_container1=None,
        generic_data_container2=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="merge::generic_data_container", config=config, server=server
        )
        self._inputs = InputsMergeGenericDataContainer(self)
        self._outputs = OutputsMergeGenericDataContainer(self)
        if generic_data_container1 is not None:
            self.inputs.generic_data_container1.connect(generic_data_container1)
        if generic_data_container2 is not None:
            self.inputs.generic_data_container2.connect(generic_data_container2)

    @staticmethod
    def _spec():
        description = """Merges a list of generic data container. For each data entry, the
            merge operation is forwarded to the correct merge
            Operator. Primitive types cannot be merged, first instance
            found will be maintained in the result."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="generic_data_container",
                    type_names=["generic_data_container"],
                    optional=False,
                    document="""Either a vector of generic data containers
        (sharing the same data types) or
        generic data containers from pin 0 to
        ... to merge. supported types rely on
        existing type specific merge
        operators.""",
                ),
                1: PinSpecification(
                    name="generic_data_container",
                    type_names=["generic_data_container"],
                    optional=False,
                    document="""Either a vector of generic data containers
        (sharing the same data types) or
        generic data containers from pin 0 to
        ... to merge. supported types rely on
        existing type specific merge
        operators.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="any",
                    type_names=["any"],
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
            name="merge::generic_data_container", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeGenericDataContainer
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMergeGenericDataContainer
        """
        return super().outputs


class InputsMergeGenericDataContainer(_Inputs):
    """Intermediate class used to connect user inputs to
    merge_generic_data_container operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.merge_generic_data_container()
    >>> my_generic_data_container1 = dpf.GenericDataContainer()
    >>> op.inputs.generic_data_container1.connect(my_generic_data_container1)
    >>> my_generic_data_container2 = dpf.GenericDataContainer()
    >>> op.inputs.generic_data_container2.connect(my_generic_data_container2)
    """

    def __init__(self, op: Operator):
        super().__init__(merge_generic_data_container._spec().inputs, op)
        self._generic_data_container1 = Input(
            merge_generic_data_container._spec().input_pin(0), 0, op, 0
        )
        self._inputs.append(self._generic_data_container1)
        self._generic_data_container2 = Input(
            merge_generic_data_container._spec().input_pin(1), 1, op, 1
        )
        self._inputs.append(self._generic_data_container2)

    @property
    def generic_data_container1(self):
        """Allows to connect generic_data_container1 input to the operator.

        Either a vector of generic data containers
        (sharing the same data types) or
        generic data containers from pin 0 to
        ... to merge. supported types rely on
        existing type specific merge
        operators.

        Parameters
        ----------
        my_generic_data_container1 : GenericDataContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_generic_data_container()
        >>> op.inputs.generic_data_container1.connect(my_generic_data_container1)
        >>> # or
        >>> op.inputs.generic_data_container1(my_generic_data_container1)
        """
        return self._generic_data_container1

    @property
    def generic_data_container2(self):
        """Allows to connect generic_data_container2 input to the operator.

        Either a vector of generic data containers
        (sharing the same data types) or
        generic data containers from pin 0 to
        ... to merge. supported types rely on
        existing type specific merge
        operators.

        Parameters
        ----------
        my_generic_data_container2 : GenericDataContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_generic_data_container()
        >>> op.inputs.generic_data_container2.connect(my_generic_data_container2)
        >>> # or
        >>> op.inputs.generic_data_container2(my_generic_data_container2)
        """
        return self._generic_data_container2


class OutputsMergeGenericDataContainer(_Outputs):
    """Intermediate class used to get outputs from
    merge_generic_data_container operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.merge_generic_data_container()
    >>> # Connect inputs : op.inputs. ...
    >>> result_any = op.outputs.any()
    """

    def __init__(self, op: Operator):
        super().__init__(merge_generic_data_container._spec().outputs, op)
        self._any = Output(merge_generic_data_container._spec().output_pin(0), 0, op)
        self._outputs.append(self._any)

    @property
    def any(self):
        """Allows to get any output of the operator

        Returns
        ----------
        my_any : Any

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_generic_data_container()
        >>> # Connect inputs : op.inputs. ...
        >>> result_any = op.outputs.any()
        """  # noqa: E501
        return self._any
