"""
transpose
---------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.outputs import _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class transpose(Operator):
    """Transposes the input scoping or scopings container (Elemental -->
    Nodal, or Nodal ---> Elemental), based on the input mesh region.

    Parameters
    ----------
    mesh_scoping : Scoping or ScopingsContainer
        Scoping or scopings container (the input type
        is the output type)
    meshed_region : MeshedRegion or MeshesContainer
    inclusive : int, optional
        If inclusive == 1 then all the elements
        adjacent to the nodes ids in input
        are added, if inclusive == 0, only
        the elements which have all their
        nodes in the scoping are included


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.scoping.transpose()

    >>> # Make input connections
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.meshed_region.connect(my_meshed_region)
    >>> my_inclusive = int()
    >>> op.inputs.inclusive.connect(my_inclusive)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.scoping.transpose(
    ...     mesh_scoping=my_mesh_scoping,
    ...     meshed_region=my_meshed_region,
    ...     inclusive=my_inclusive,
    ... )

    >>> # Get output data
    >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """

    def __init__(
        self,
        mesh_scoping=None,
        meshed_region=None,
        inclusive=None,
        config=None,
        server=None,
    ):
        super().__init__(name="transpose_scoping", config=config, server=server)
        self._inputs = InputsTranspose(self)
        self._outputs = OutputsTranspose(self)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if meshed_region is not None:
            self.inputs.meshed_region.connect(meshed_region)
        if inclusive is not None:
            self.inputs.inclusive.connect(inclusive)

    @staticmethod
    def _spec():
        description = """Transposes the input scoping or scopings container (Elemental --&gt;
            Nodal, or Nodal ---&gt; Elemental), based on the input mesh
            region."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping", "scopings_container"],
                    optional=False,
                    document="""Scoping or scopings container (the input type
        is the output type)""",
                ),
                1: PinSpecification(
                    name="meshed_region",
                    type_names=["meshed_region", "meshes_container"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="inclusive",
                    type_names=["int32"],
                    optional=True,
                    document="""If inclusive == 1 then all the elements
        adjacent to the nodes ids in input
        are added, if inclusive == 0, only
        the elements which have all their
        nodes in the scoping are included""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping", "scopings_container"],
                    optional=False,
                    document="""Scoping or scopings container (the input type
        is the output type)""",
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
        return Operator.default_config(name="transpose_scoping", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsTranspose
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsTranspose
        """
        return super().outputs


class InputsTranspose(_Inputs):
    """Intermediate class used to connect user inputs to
    transpose operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.transpose()
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.meshed_region.connect(my_meshed_region)
    >>> my_inclusive = int()
    >>> op.inputs.inclusive.connect(my_inclusive)
    """

    def __init__(self, op: Operator):
        super().__init__(transpose._spec().inputs, op)
        self._mesh_scoping = Input(transpose._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._meshed_region = Input(transpose._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._meshed_region)
        self._inclusive = Input(transpose._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._inclusive)

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Scoping or scopings container (the input type
        is the output type)

        Parameters
        ----------
        my_mesh_scoping : Scoping or ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.transpose()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def meshed_region(self):
        """Allows to connect meshed_region input to the operator.

        Parameters
        ----------
        my_meshed_region : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.transpose()
        >>> op.inputs.meshed_region.connect(my_meshed_region)
        >>> # or
        >>> op.inputs.meshed_region(my_meshed_region)
        """
        return self._meshed_region

    @property
    def inclusive(self):
        """Allows to connect inclusive input to the operator.

        If inclusive == 1 then all the elements
        adjacent to the nodes ids in input
        are added, if inclusive == 0, only
        the elements which have all their
        nodes in the scoping are included

        Parameters
        ----------
        my_inclusive : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.transpose()
        >>> op.inputs.inclusive.connect(my_inclusive)
        >>> # or
        >>> op.inputs.inclusive(my_inclusive)
        """
        return self._inclusive


class OutputsTranspose(_Outputs):
    """Intermediate class used to get outputs from
    transpose operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.transpose()
    >>> # Connect inputs : op.inputs. ...
    >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """

    def __init__(self, op: Operator):
        super().__init__(transpose._spec().outputs, op)
        self.mesh_scoping_as_scoping = Output(
            _modify_output_spec_with_one_type(
                transpose._spec().output_pin(0), "scoping"
            ),
            0,
            op,
        )
        self._outputs.append(self.mesh_scoping_as_scoping)
        self.mesh_scoping_as_scopings_container = Output(
            _modify_output_spec_with_one_type(
                transpose._spec().output_pin(0), "scopings_container"
            ),
            0,
            op,
        )
        self._outputs.append(self.mesh_scoping_as_scopings_container)
