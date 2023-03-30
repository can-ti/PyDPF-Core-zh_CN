"""
reduce_sampling
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class reduce_sampling(Operator):
    """Take a scoping and remove half of it's content.

    Parameters
    ----------
    mesh_scoping : Scoping
    denominator : int, optional
        Set the number of time the scoping is reduced
        (default is 2). must be integer value
        above 1.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.scoping.reduce_sampling()

    >>> # Make input connections
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_denominator = int()
    >>> op.inputs.denominator.connect(my_denominator)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.scoping.reduce_sampling(
    ...     mesh_scoping=my_mesh_scoping,
    ...     denominator=my_denominator,
    ... )

    >>> # Get output data
    >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """

    def __init__(self, mesh_scoping=None, denominator=None, config=None, server=None):
        super().__init__(name="scoping::reduce_sampling", config=config, server=server)
        self._inputs = InputsReduceSampling(self)
        self._outputs = OutputsReduceSampling(self)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if denominator is not None:
            self.inputs.denominator.connect(denominator)

    @staticmethod
    def _spec():
        description = """Take a scoping and remove half of it's content."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="denominator",
                    type_names=["int32"],
                    optional=True,
                    document="""Set the number of time the scoping is reduced
        (default is 2). must be integer value
        above 1.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="mesh_scoping",
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
        return Operator.default_config(name="scoping::reduce_sampling", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsReduceSampling
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsReduceSampling
        """
        return super().outputs


class InputsReduceSampling(_Inputs):
    """Intermediate class used to connect user inputs to
    reduce_sampling operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.reduce_sampling()
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_denominator = int()
    >>> op.inputs.denominator.connect(my_denominator)
    """

    def __init__(self, op: Operator):
        super().__init__(reduce_sampling._spec().inputs, op)
        self._mesh_scoping = Input(reduce_sampling._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._denominator = Input(reduce_sampling._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._denominator)

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Parameters
        ----------
        my_mesh_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.reduce_sampling()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def denominator(self):
        """Allows to connect denominator input to the operator.

        Set the number of time the scoping is reduced
        (default is 2). must be integer value
        above 1.

        Parameters
        ----------
        my_denominator : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.reduce_sampling()
        >>> op.inputs.denominator.connect(my_denominator)
        >>> # or
        >>> op.inputs.denominator(my_denominator)
        """
        return self._denominator


class OutputsReduceSampling(_Outputs):
    """Intermediate class used to get outputs from
    reduce_sampling operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.reduce_sampling()
    >>> # Connect inputs : op.inputs. ...
    >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """

    def __init__(self, op: Operator):
        super().__init__(reduce_sampling._spec().outputs, op)
        self._mesh_scoping = Output(reduce_sampling._spec().output_pin(0), 0, op)
        self._outputs.append(self._mesh_scoping)

    @property
    def mesh_scoping(self):
        """Allows to get mesh_scoping output of the operator

        Returns
        ----------
        my_mesh_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.reduce_sampling()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh_scoping = op.outputs.mesh_scoping()
        """  # noqa: E501
        return self._mesh_scoping