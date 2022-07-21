"""
merge_scopings
==============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class merge_scopings(Operator):
    """Take a set of scoping and assemble them in a unique one

    Parameters
    ----------
    scopings : Scoping
        A vector of result info containers to merge
        or scopings from pin 0 to ...


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.merge_scopings()

    >>> # Make input connections
    >>> my_scopings = dpf.Scoping()
    >>> op.inputs.scopings.connect(my_scopings)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.merge_scopings(
    ...     scopings=my_scopings,
    ... )

    >>> # Get output data
    >>> result_merged_scoping = op.outputs.merged_scoping()
    """

    def __init__(self, scopings=None, config=None, server=None):
        super().__init__(name="merge::scoping", config=config, server=server)
        self._inputs = InputsMergeScopings(self)
        self._outputs = OutputsMergeScopings(self)
        if scopings is not None:
            self.inputs.scopings.connect(scopings)

    @staticmethod
    def _spec():
        description = """Take a set of scoping and assemble them in a unique one"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="scopings",
                    type_names=["vector<shared_ptr<scoping>>", "scoping"],
                    optional=False,
                    document="""A vector of result info containers to merge
        or scopings from pin 0 to ...""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="merged_scoping",
                    type_names=["scoping"],
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
        return Operator.default_config(name="merge::scoping", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeScopings
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeScopings
        """
        return super().outputs


class InputsMergeScopings(_Inputs):
    """Intermediate class used to connect user inputs to
    merge_scopings operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.merge_scopings()
    >>> my_scopings = dpf.Scoping()
    >>> op.inputs.scopings.connect(my_scopings)
    """

    def __init__(self, op: Operator):
        super().__init__(merge_scopings._spec().inputs, op)
        self._scopings = Input(merge_scopings._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._scopings)

    @property
    def scopings(self):
        """Allows to connect scopings input to the operator.

        A vector of result info containers to merge
        or scopings from pin 0 to ...

        Parameters
        ----------
        my_scopings : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_scopings()
        >>> op.inputs.scopings.connect(my_scopings)
        >>> # or
        >>> op.inputs.scopings(my_scopings)
        """
        return self._scopings


class OutputsMergeScopings(_Outputs):
    """Intermediate class used to get outputs from
    merge_scopings operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.merge_scopings()
    >>> # Connect inputs : op.inputs. ...
    >>> result_merged_scoping = op.outputs.merged_scoping()
    """

    def __init__(self, op: Operator):
        super().__init__(merge_scopings._spec().outputs, op)
        self._merged_scoping = Output(merge_scopings._spec().output_pin(0), 0, op)
        self._outputs.append(self._merged_scoping)

    @property
    def merged_scoping(self):
        """Allows to get merged_scoping output of the operator

        Returns
        ----------
        my_merged_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_scopings()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_scoping = op.outputs.merged_scoping()
        """  # noqa: E501
        return self._merged_scoping
