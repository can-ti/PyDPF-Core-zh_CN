"""
zfp_on_results_workflow
=======================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class zfp_on_results_workflow(Operator):
    """Creates a compression workflow that will compress results using ZFP
    method.

    Parameters
    ----------
    mode : str or Char
        Zfp mode: fixed-rate ('r'), fixed-precision
        ('p'), fixed-accuracy ('a')
    mode_parameter : int or float
        Mode-corresponding parameter: rate (double) /
        precision (int) / accuracy (double)
    dim : int, optional
        Dimension (1d/2d/3d) for data organization
        before the compression (int; default:
        2)
    order : int, optional
        Xyz dimensions order, where x (row)
        corresponds to number of elementary
        data, y (col) - number of time steps,
        z - number of components (applicable
        only for 3d data) : 0=xyz, 1=yxz
        (int; default: 0)


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.compression.zfp_on_results_workflow()

    >>> # Make input connections
    >>> my_mode = str()
    >>> op.inputs.mode.connect(my_mode)
    >>> my_mode_parameter = int()
    >>> op.inputs.mode_parameter.connect(my_mode_parameter)
    >>> my_dim = int()
    >>> op.inputs.dim.connect(my_dim)
    >>> my_order = int()
    >>> op.inputs.order.connect(my_order)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.compression.zfp_on_results_workflow(
    ...     mode=my_mode,
    ...     mode_parameter=my_mode_parameter,
    ...     dim=my_dim,
    ...     order=my_order,
    ... )

    >>> # Get output data
    >>> result_workflow = op.outputs.workflow()
    """

    def __init__(
        self,
        mode=None,
        mode_parameter=None,
        dim=None,
        order=None,
        config=None,
        server=None,
    ):
        super().__init__(name="zfp_on_results_workflow", config=config, server=server)
        self._inputs = InputsZfpOnResultsWorkflow(self)
        self._outputs = OutputsZfpOnResultsWorkflow(self)
        if mode is not None:
            self.inputs.mode.connect(mode)
        if mode_parameter is not None:
            self.inputs.mode_parameter.connect(mode_parameter)
        if dim is not None:
            self.inputs.dim.connect(dim)
        if order is not None:
            self.inputs.order.connect(order)

    @staticmethod
    def _spec():
        description = """Creates a compression workflow that will compress results using ZFP
            method."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                1: PinSpecification(
                    name="mode",
                    type_names=["string", "char"],
                    optional=False,
                    document="""Zfp mode: fixed-rate ('r'), fixed-precision
        ('p'), fixed-accuracy ('a')""",
                ),
                2: PinSpecification(
                    name="mode_parameter",
                    type_names=["int32", "double"],
                    optional=False,
                    document="""Mode-corresponding parameter: rate (double) /
        precision (int) / accuracy (double)""",
                ),
                3: PinSpecification(
                    name="dim",
                    type_names=["int32"],
                    optional=True,
                    document="""Dimension (1d/2d/3d) for data organization
        before the compression (int; default:
        2)""",
                ),
                4: PinSpecification(
                    name="order",
                    type_names=["int32"],
                    optional=True,
                    document="""Xyz dimensions order, where x (row)
        corresponds to number of elementary
        data, y (col) - number of time steps,
        z - number of components (applicable
        only for 3d data) : 0=xyz, 1=yxz
        (int; default: 0)""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="workflow",
                    type_names=["workflow"],
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
        return Operator.default_config(name="zfp_on_results_workflow", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsZfpOnResultsWorkflow
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsZfpOnResultsWorkflow
        """
        return super().outputs


class InputsZfpOnResultsWorkflow(_Inputs):
    """Intermediate class used to connect user inputs to
    zfp_on_results_workflow operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.compression.zfp_on_results_workflow()
    >>> my_mode = str()
    >>> op.inputs.mode.connect(my_mode)
    >>> my_mode_parameter = int()
    >>> op.inputs.mode_parameter.connect(my_mode_parameter)
    >>> my_dim = int()
    >>> op.inputs.dim.connect(my_dim)
    >>> my_order = int()
    >>> op.inputs.order.connect(my_order)
    """

    def __init__(self, op: Operator):
        super().__init__(zfp_on_results_workflow._spec().inputs, op)
        self._mode = Input(zfp_on_results_workflow._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mode)
        self._mode_parameter = Input(
            zfp_on_results_workflow._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._mode_parameter)
        self._dim = Input(zfp_on_results_workflow._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._dim)
        self._order = Input(zfp_on_results_workflow._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._order)

    @property
    def mode(self):
        """Allows to connect mode input to the operator.

        Zfp mode: fixed-rate ('r'), fixed-precision
        ('p'), fixed-accuracy ('a')

        Parameters
        ----------
        my_mode : str or Char

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.compression.zfp_on_results_workflow()
        >>> op.inputs.mode.connect(my_mode)
        >>> # or
        >>> op.inputs.mode(my_mode)
        """
        return self._mode

    @property
    def mode_parameter(self):
        """Allows to connect mode_parameter input to the operator.

        Mode-corresponding parameter: rate (double) /
        precision (int) / accuracy (double)

        Parameters
        ----------
        my_mode_parameter : int or float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.compression.zfp_on_results_workflow()
        >>> op.inputs.mode_parameter.connect(my_mode_parameter)
        >>> # or
        >>> op.inputs.mode_parameter(my_mode_parameter)
        """
        return self._mode_parameter

    @property
    def dim(self):
        """Allows to connect dim input to the operator.

        Dimension (1d/2d/3d) for data organization
        before the compression (int; default:
        2)

        Parameters
        ----------
        my_dim : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.compression.zfp_on_results_workflow()
        >>> op.inputs.dim.connect(my_dim)
        >>> # or
        >>> op.inputs.dim(my_dim)
        """
        return self._dim

    @property
    def order(self):
        """Allows to connect order input to the operator.

        Xyz dimensions order, where x (row)
        corresponds to number of elementary
        data, y (col) - number of time steps,
        z - number of components (applicable
        only for 3d data) : 0=xyz, 1=yxz
        (int; default: 0)

        Parameters
        ----------
        my_order : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.compression.zfp_on_results_workflow()
        >>> op.inputs.order.connect(my_order)
        >>> # or
        >>> op.inputs.order(my_order)
        """
        return self._order


class OutputsZfpOnResultsWorkflow(_Outputs):
    """Intermediate class used to get outputs from
    zfp_on_results_workflow operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.compression.zfp_on_results_workflow()
    >>> # Connect inputs : op.inputs. ...
    >>> result_workflow = op.outputs.workflow()
    """

    def __init__(self, op: Operator):
        super().__init__(zfp_on_results_workflow._spec().outputs, op)
        self._workflow = Output(zfp_on_results_workflow._spec().output_pin(0), 0, op)
        self._outputs.append(self._workflow)

    @property
    def workflow(self):
        """Allows to get workflow output of the operator

        Returns
        ----------
        my_workflow : Workflow

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.compression.zfp_on_results_workflow()
        >>> # Connect inputs : op.inputs. ...
        >>> result_workflow = op.outputs.workflow()
        """  # noqa: E501
        return self._workflow
