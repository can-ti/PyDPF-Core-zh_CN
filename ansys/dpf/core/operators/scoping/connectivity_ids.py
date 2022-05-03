"""
connectivity_ids
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class connectivity_ids(Operator):
    """Returns the ordered node ids corresponding to the element ids scoping
    in input. For each element the node ids are its connectivity.

    Parameters
    ----------
    mesh_scoping : Scoping
        Elemental scoping
    mesh : MeshedRegion, optional
        The support of the scoping is expected if
        there is no mesh in input
    take_mid_nodes : bool, optional
        Default is true


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.scoping.connectivity_ids()

    >>> # Make input connections
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_take_mid_nodes = bool()
    >>> op.inputs.take_mid_nodes.connect(my_take_mid_nodes)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.scoping.connectivity_ids(
    ...     mesh_scoping=my_mesh_scoping,
    ...     mesh=my_mesh,
    ...     take_mid_nodes=my_take_mid_nodes,
    ... )

    >>> # Get output data
    >>> result_mesh_scoping = op.outputs.mesh_scoping()
    >>> result_elemental_scoping = op.outputs.elemental_scoping()
    """

    def __init__(
        self,
        mesh_scoping=None,
        mesh=None,
        take_mid_nodes=None,
        config=None,
        server=None,
    ):
        super().__init__(name="scoping::connectivity_ids", config=config, server=server)
        self._inputs = InputsConnectivityIds(self)
        self._outputs = OutputsConnectivityIds(self)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if take_mid_nodes is not None:
            self.inputs.take_mid_nodes.connect(take_mid_nodes)

    @staticmethod
    def _spec():
        description = """Returns the ordered node ids corresponding to the element ids scoping
            in input. For each element the node ids are its
            connectivity."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=False,
                    document="""Elemental scoping""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=True,
                    document="""The support of the scoping is expected if
        there is no mesh in input""",
                ),
                10: PinSpecification(
                    name="take_mid_nodes",
                    type_names=["bool"],
                    optional=True,
                    document="""Default is true""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="elemental_scoping",
                    type_names=["scoping"],
                    optional=False,
                    document="""Same as the input scoping but with ids
        duplicated to have the same size as
        nodal output scoping""",
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
        return Operator.default_config(name="scoping::connectivity_ids", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsConnectivityIds
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsConnectivityIds
        """
        return super().outputs


class InputsConnectivityIds(_Inputs):
    """Intermediate class used to connect user inputs to
    connectivity_ids operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.connectivity_ids()
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_take_mid_nodes = bool()
    >>> op.inputs.take_mid_nodes.connect(my_take_mid_nodes)
    """

    def __init__(self, op: Operator):
        super().__init__(connectivity_ids._spec().inputs, op)
        self._mesh_scoping = Input(connectivity_ids._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._mesh = Input(connectivity_ids._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)
        self._take_mid_nodes = Input(connectivity_ids._spec().input_pin(10), 10, op, -1)
        self._inputs.append(self._take_mid_nodes)

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Elemental scoping

        Parameters
        ----------
        my_mesh_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.connectivity_ids()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        The support of the scoping is expected if
        there is no mesh in input

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.connectivity_ids()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def take_mid_nodes(self):
        """Allows to connect take_mid_nodes input to the operator.

        Default is true

        Parameters
        ----------
        my_take_mid_nodes : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.connectivity_ids()
        >>> op.inputs.take_mid_nodes.connect(my_take_mid_nodes)
        >>> # or
        >>> op.inputs.take_mid_nodes(my_take_mid_nodes)
        """
        return self._take_mid_nodes


class OutputsConnectivityIds(_Outputs):
    """Intermediate class used to get outputs from
    connectivity_ids operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.connectivity_ids()
    >>> # Connect inputs : op.inputs. ...
    >>> result_mesh_scoping = op.outputs.mesh_scoping()
    >>> result_elemental_scoping = op.outputs.elemental_scoping()
    """

    def __init__(self, op: Operator):
        super().__init__(connectivity_ids._spec().outputs, op)
        self._mesh_scoping = Output(connectivity_ids._spec().output_pin(0), 0, op)
        self._outputs.append(self._mesh_scoping)
        self._elemental_scoping = Output(connectivity_ids._spec().output_pin(1), 1, op)
        self._outputs.append(self._elemental_scoping)

    @property
    def mesh_scoping(self):
        """Allows to get mesh_scoping output of the operator

        Returns
        ----------
        my_mesh_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.connectivity_ids()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh_scoping = op.outputs.mesh_scoping()
        """  # noqa: E501
        return self._mesh_scoping

    @property
    def elemental_scoping(self):
        """Allows to get elemental_scoping output of the operator

        Returns
        ----------
        my_elemental_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.connectivity_ids()
        >>> # Connect inputs : op.inputs. ...
        >>> result_elemental_scoping = op.outputs.elemental_scoping()
        """  # noqa: E501
        return self._elemental_scoping
