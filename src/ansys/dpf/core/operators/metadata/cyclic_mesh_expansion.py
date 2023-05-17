"""
cyclic_mesh_expansion
=====================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class cyclic_mesh_expansion(Operator):
    """Expand the mesh.

    Parameters
    ----------
    sector_meshed_region : MeshedRegion or MeshesContainer, optional
    cyclic_support : CyclicSupport
    sectors_to_expand : Scoping or ScopingsContainer, optional
        Sectors to expand (start at 0), for
        multistage: use scopings container
        with 'stage' label.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.metadata.cyclic_mesh_expansion()

    >>> # Make input connections
    >>> my_sector_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)
    >>> my_cyclic_support = dpf.CyclicSupport()
    >>> op.inputs.cyclic_support.connect(my_cyclic_support)
    >>> my_sectors_to_expand = dpf.Scoping()
    >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.metadata.cyclic_mesh_expansion(
    ...     sector_meshed_region=my_sector_meshed_region,
    ...     cyclic_support=my_cyclic_support,
    ...     sectors_to_expand=my_sectors_to_expand,
    ... )

    >>> # Get output data
    >>> result_meshed_region = op.outputs.meshed_region()
    >>> result_cyclic_support = op.outputs.cyclic_support()
    """

    def __init__(
        self,
        sector_meshed_region=None,
        cyclic_support=None,
        sectors_to_expand=None,
        config=None,
        server=None,
    ):
        super().__init__(name="cyclic_expansion_mesh", config=config, server=server)
        self._inputs = InputsCyclicMeshExpansion(self)
        self._outputs = OutputsCyclicMeshExpansion(self)
        if sector_meshed_region is not None:
            self.inputs.sector_meshed_region.connect(sector_meshed_region)
        if cyclic_support is not None:
            self.inputs.cyclic_support.connect(cyclic_support)
        if sectors_to_expand is not None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)

    @staticmethod
    def _spec():
        description = """Expand the mesh."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                7: PinSpecification(
                    name="sector_meshed_region",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document="""""",
                ),
                16: PinSpecification(
                    name="cyclic_support",
                    type_names=["cyclic_support"],
                    optional=False,
                    document="""""",
                ),
                18: PinSpecification(
                    name="sectors_to_expand",
                    type_names=["vector<int32>", "scoping", "scopings_container"],
                    optional=True,
                    document="""Sectors to expand (start at 0), for
        multistage: use scopings container
        with 'stage' label.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="meshed_region",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""Expanded meshed region.""",
                ),
                1: PinSpecification(
                    name="cyclic_support",
                    type_names=["cyclic_support"],
                    optional=False,
                    document="""Input cyclic support modified in place
        containing the new expanded meshed
        regions.""",
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
        return Operator.default_config(name="cyclic_expansion_mesh", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCyclicMeshExpansion
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsCyclicMeshExpansion
        """
        return super().outputs


class InputsCyclicMeshExpansion(_Inputs):
    """Intermediate class used to connect user inputs to
    cyclic_mesh_expansion operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
    >>> my_sector_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)
    >>> my_cyclic_support = dpf.CyclicSupport()
    >>> op.inputs.cyclic_support.connect(my_cyclic_support)
    >>> my_sectors_to_expand = dpf.Scoping()
    >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
    """

    def __init__(self, op: Operator):
        super().__init__(cyclic_mesh_expansion._spec().inputs, op)
        self._sector_meshed_region = Input(
            cyclic_mesh_expansion._spec().input_pin(7), 7, op, -1
        )
        self._inputs.append(self._sector_meshed_region)
        self._cyclic_support = Input(
            cyclic_mesh_expansion._spec().input_pin(16), 16, op, -1
        )
        self._inputs.append(self._cyclic_support)
        self._sectors_to_expand = Input(
            cyclic_mesh_expansion._spec().input_pin(18), 18, op, -1
        )
        self._inputs.append(self._sectors_to_expand)

    @property
    def sector_meshed_region(self):
        """Allows to connect sector_meshed_region input to the operator.

        Parameters
        ----------
        my_sector_meshed_region : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
        >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)
        >>> # or
        >>> op.inputs.sector_meshed_region(my_sector_meshed_region)
        """
        return self._sector_meshed_region

    @property
    def cyclic_support(self):
        """Allows to connect cyclic_support input to the operator.

        Parameters
        ----------
        my_cyclic_support : CyclicSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
        >>> op.inputs.cyclic_support.connect(my_cyclic_support)
        >>> # or
        >>> op.inputs.cyclic_support(my_cyclic_support)
        """
        return self._cyclic_support

    @property
    def sectors_to_expand(self):
        """Allows to connect sectors_to_expand input to the operator.

        Sectors to expand (start at 0), for
        multistage: use scopings container
        with 'stage' label.

        Parameters
        ----------
        my_sectors_to_expand : Scoping or ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
        >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
        >>> # or
        >>> op.inputs.sectors_to_expand(my_sectors_to_expand)
        """
        return self._sectors_to_expand


class OutputsCyclicMeshExpansion(_Outputs):
    """Intermediate class used to get outputs from
    cyclic_mesh_expansion operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
    >>> # Connect inputs : op.inputs. ...
    >>> result_meshed_region = op.outputs.meshed_region()
    >>> result_cyclic_support = op.outputs.cyclic_support()
    """

    def __init__(self, op: Operator):
        super().__init__(cyclic_mesh_expansion._spec().outputs, op)
        self._meshed_region = Output(cyclic_mesh_expansion._spec().output_pin(0), 0, op)
        self._outputs.append(self._meshed_region)
        self._cyclic_support = Output(
            cyclic_mesh_expansion._spec().output_pin(1), 1, op
        )
        self._outputs.append(self._cyclic_support)

    @property
    def meshed_region(self):
        """Allows to get meshed_region output of the operator

        Returns
        ----------
        my_meshed_region : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_meshed_region = op.outputs.meshed_region()
        """  # noqa: E501
        return self._meshed_region

    @property
    def cyclic_support(self):
        """Allows to get cyclic_support output of the operator

        Returns
        ----------
        my_cyclic_support : CyclicSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.metadata.cyclic_mesh_expansion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_cyclic_support = op.outputs.cyclic_support()
        """  # noqa: E501
        return self._cyclic_support
