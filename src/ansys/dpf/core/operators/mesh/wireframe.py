"""
wireframe
=========
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class wireframe(Operator):
    """Take a mesh and extracts its sharp edges, using pin 1 value as a
    threshold angle.

    Parameters
    ----------
    mesh : MeshedRegion
    threshold : float
        Angle threshold in radian that will trigger
        an edge detection.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.wireframe()

    >>> # Make input connections
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_threshold = float()
    >>> op.inputs.threshold.connect(my_threshold)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.wireframe(
    ...     mesh=my_mesh,
    ...     threshold=my_threshold,
    ... )

    >>> # Get output data
    >>> result_wireframe = op.outputs.wireframe()
    """

    def __init__(self, mesh=None, threshold=None, config=None, server=None):
        super().__init__(name="wireframe", config=config, server=server)
        self._inputs = InputsWireframe(self)
        self._outputs = OutputsWireframe(self)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if threshold is not None:
            self.inputs.threshold.connect(threshold)

    @staticmethod
    def _spec():
        description = """Take a mesh and extracts its sharp edges, using pin 1 value as a
            threshold angle."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="threshold",
                    type_names=["double"],
                    optional=False,
                    document="""Angle threshold in radian that will trigger
        an edge detection.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="wireframe",
                    type_names=["abstract_meshed_region"],
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
        return Operator.default_config(name="wireframe", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsWireframe
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsWireframe
        """
        return super().outputs


class InputsWireframe(_Inputs):
    """Intermediate class used to connect user inputs to
    wireframe operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.wireframe()
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_threshold = float()
    >>> op.inputs.threshold.connect(my_threshold)
    """

    def __init__(self, op: Operator):
        super().__init__(wireframe._spec().inputs, op)
        self._mesh = Input(wireframe._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._mesh)
        self._threshold = Input(wireframe._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._threshold)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.wireframe()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def threshold(self):
        """Allows to connect threshold input to the operator.

        Angle threshold in radian that will trigger
        an edge detection.

        Parameters
        ----------
        my_threshold : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.wireframe()
        >>> op.inputs.threshold.connect(my_threshold)
        >>> # or
        >>> op.inputs.threshold(my_threshold)
        """
        return self._threshold


class OutputsWireframe(_Outputs):
    """Intermediate class used to get outputs from
    wireframe operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.wireframe()
    >>> # Connect inputs : op.inputs. ...
    >>> result_wireframe = op.outputs.wireframe()
    """

    def __init__(self, op: Operator):
        super().__init__(wireframe._spec().outputs, op)
        self._wireframe = Output(wireframe._spec().output_pin(0), 0, op)
        self._outputs.append(self._wireframe)

    @property
    def wireframe(self):
        """Allows to get wireframe output of the operator

        Returns
        ----------
        my_wireframe : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.wireframe()
        >>> # Connect inputs : op.inputs. ...
        >>> result_wireframe = op.outputs.wireframe()
        """  # noqa: E501
        return self._wireframe
