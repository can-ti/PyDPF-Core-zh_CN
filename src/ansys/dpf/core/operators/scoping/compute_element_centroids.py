"""
compute_element_centroids
=========================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class compute_element_centroids(Operator):
    """Computes the element centroids of the mesh. It also outputs the
    element measure.

    Parameters
    ----------
    element_scoping : Scoping, optional
        If provided, only the centroids of the
        elements in the scoping are computed.
    mesh : MeshedRegion
        Mesh to compute centroids


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.scoping.compute_element_centroids()

    >>> # Make input connections
    >>> my_element_scoping = dpf.Scoping()
    >>> op.inputs.element_scoping.connect(my_element_scoping)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.scoping.compute_element_centroids(
    ...     element_scoping=my_element_scoping,
    ...     mesh=my_mesh,
    ... )

    >>> # Get output data
    >>> result_centroids = op.outputs.centroids()
    >>> result_measure = op.outputs.measure()
    """

    def __init__(self, element_scoping=None, mesh=None, config=None, server=None):
        super().__init__(name="compute_element_centroids", config=config, server=server)
        self._inputs = InputsComputeElementCentroids(self)
        self._outputs = OutputsComputeElementCentroids(self)
        if element_scoping is not None:
            self.inputs.element_scoping.connect(element_scoping)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        description = """Computes the element centroids of the mesh. It also outputs the
            element measure."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                1: PinSpecification(
                    name="element_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""If provided, only the centroids of the
        elements in the scoping are computed.""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""Mesh to compute centroids""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="centroids",
                    type_names=["field"],
                    optional=False,
                    document="""Element centroids.""",
                ),
                1: PinSpecification(
                    name="measure",
                    type_names=["field"],
                    optional=False,
                    document="""Element measure (length, surface or volume
        depending on the dimension of the
        element).""",
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
        return Operator.default_config(name="compute_element_centroids", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsComputeElementCentroids
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsComputeElementCentroids
        """
        return super().outputs


class InputsComputeElementCentroids(_Inputs):
    """Intermediate class used to connect user inputs to
    compute_element_centroids operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.compute_element_centroids()
    >>> my_element_scoping = dpf.Scoping()
    >>> op.inputs.element_scoping.connect(my_element_scoping)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    """

    def __init__(self, op: Operator):
        super().__init__(compute_element_centroids._spec().inputs, op)
        self._element_scoping = Input(
            compute_element_centroids._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._element_scoping)
        self._mesh = Input(compute_element_centroids._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)

    @property
    def element_scoping(self):
        """Allows to connect element_scoping input to the operator.

        If provided, only the centroids of the
        elements in the scoping are computed.

        Parameters
        ----------
        my_element_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.compute_element_centroids()
        >>> op.inputs.element_scoping.connect(my_element_scoping)
        >>> # or
        >>> op.inputs.element_scoping(my_element_scoping)
        """
        return self._element_scoping

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Mesh to compute centroids

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.compute_element_centroids()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh


class OutputsComputeElementCentroids(_Outputs):
    """Intermediate class used to get outputs from
    compute_element_centroids operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.compute_element_centroids()
    >>> # Connect inputs : op.inputs. ...
    >>> result_centroids = op.outputs.centroids()
    >>> result_measure = op.outputs.measure()
    """

    def __init__(self, op: Operator):
        super().__init__(compute_element_centroids._spec().outputs, op)
        self._centroids = Output(compute_element_centroids._spec().output_pin(0), 0, op)
        self._outputs.append(self._centroids)
        self._measure = Output(compute_element_centroids._spec().output_pin(1), 1, op)
        self._outputs.append(self._measure)

    @property
    def centroids(self):
        """Allows to get centroids output of the operator

        Returns
        ----------
        my_centroids : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.compute_element_centroids()
        >>> # Connect inputs : op.inputs. ...
        >>> result_centroids = op.outputs.centroids()
        """  # noqa: E501
        return self._centroids

    @property
    def measure(self):
        """Allows to get measure output of the operator

        Returns
        ----------
        my_measure : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.compute_element_centroids()
        >>> # Connect inputs : op.inputs. ...
        >>> result_measure = op.outputs.measure()
        """  # noqa: E501
        return self._measure
