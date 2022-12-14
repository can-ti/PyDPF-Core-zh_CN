"""
element_nodal_contribution
==========================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class element_nodal_contribution(Operator):
    """Compute the fraction of volume attributed to each node of each
    element.

    Parameters
    ----------
    mesh : MeshedRegion
    scoping : Scoping, optional
        Integrate the input field over a specific
        scoping.
    volume_fraction : bool, optional
        If true, returns influence volume, if false,
        return influence volume fraction
        (i.e. integrated value of shape
        function for each node).


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.geo.element_nodal_contribution()

    >>> # Make input connections
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_volume_fraction = bool()
    >>> op.inputs.volume_fraction.connect(my_volume_fraction)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.geo.element_nodal_contribution(
    ...     mesh=my_mesh,
    ...     scoping=my_scoping,
    ...     volume_fraction=my_volume_fraction,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self, mesh=None, scoping=None, volume_fraction=None, config=None, server=None
    ):
        super().__init__(
            name="element::nodal_contribution", config=config, server=server
        )
        self._inputs = InputsElementNodalContribution(self)
        self._outputs = OutputsElementNodalContribution(self)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if scoping is not None:
            self.inputs.scoping.connect(scoping)
        if volume_fraction is not None:
            self.inputs.volume_fraction.connect(volume_fraction)

    @staticmethod
    def _spec():
        description = """Compute the fraction of volume attributed to each node of each
            element."""
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
                    name="scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""Integrate the input field over a specific
        scoping.""",
                ),
                2: PinSpecification(
                    name="volume_fraction",
                    type_names=["bool"],
                    optional=True,
                    document="""If true, returns influence volume, if false,
        return influence volume fraction
        (i.e. integrated value of shape
        function for each node).""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
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
            name="element::nodal_contribution", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementNodalContribution
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsElementNodalContribution
        """
        return super().outputs


class InputsElementNodalContribution(_Inputs):
    """Intermediate class used to connect user inputs to
    element_nodal_contribution operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.element_nodal_contribution()
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_volume_fraction = bool()
    >>> op.inputs.volume_fraction.connect(my_volume_fraction)
    """

    def __init__(self, op: Operator):
        super().__init__(element_nodal_contribution._spec().inputs, op)
        self._mesh = Input(element_nodal_contribution._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._mesh)
        self._scoping = Input(
            element_nodal_contribution._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._scoping)
        self._volume_fraction = Input(
            element_nodal_contribution._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._volume_fraction)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.element_nodal_contribution()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator.

        Integrate the input field over a specific
        scoping.

        Parameters
        ----------
        my_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.element_nodal_contribution()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> # or
        >>> op.inputs.scoping(my_scoping)
        """
        return self._scoping

    @property
    def volume_fraction(self):
        """Allows to connect volume_fraction input to the operator.

        If true, returns influence volume, if false,
        return influence volume fraction
        (i.e. integrated value of shape
        function for each node).

        Parameters
        ----------
        my_volume_fraction : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.element_nodal_contribution()
        >>> op.inputs.volume_fraction.connect(my_volume_fraction)
        >>> # or
        >>> op.inputs.volume_fraction(my_volume_fraction)
        """
        return self._volume_fraction


class OutputsElementNodalContribution(_Outputs):
    """Intermediate class used to get outputs from
    element_nodal_contribution operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.element_nodal_contribution()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(element_nodal_contribution._spec().outputs, op)
        self._field = Output(element_nodal_contribution._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.element_nodal_contribution()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field