"""
gauss_to_node_fc
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class gauss_to_node_fc(Operator):
    """Extrapolating results available at Gauss or quadrature points to nodal
    points for a field container. The available elements are : Linear
    quadrangle , parabolique quadrangle,Linear Hexagonal, quadratic
    hexagonal , linear tetrahedral, quadratic tetrahedral

    Parameters
    ----------
    fields_container : FieldsContainer
    mesh : MeshedRegion or MeshesContainer, optional
        The mesh region in this pin is used for
        extrapolating results available at
        gauss or quadrature points to nodal
        points.
    scoping : Scoping, optional
        Extrapolating results on the scoping selected
        by the user, if it is scoping
        container, the label must correspond
        to the one of the fields container


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.averaging.gauss_to_node_fc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.averaging.gauss_to_node_fc(
    ...     fields_container=my_fields_container,
    ...     mesh=my_mesh,
    ...     scoping=my_scoping,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self, fields_container=None, mesh=None, scoping=None, config=None, server=None
    ):
        super().__init__(name="gauss_to_node_fc", config=config, server=server)
        self._inputs = InputsGaussToNodeFc(self)
        self._outputs = OutputsGaussToNodeFc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if scoping is not None:
            self.inputs.scoping.connect(scoping)

    @staticmethod
    def _spec():
        description = """Extrapolating results available at Gauss or quadrature points to nodal
            points for a field container. The available elements are :
            Linear quadrangle , parabolique quadrangle,Linear
            Hexagonal, quadratic hexagonal , linear tetrahedral,
            quadratic tetrahedral"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document="""The mesh region in this pin is used for
        extrapolating results available at
        gauss or quadrature points to nodal
        points.""",
                ),
                3: PinSpecification(
                    name="scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""Extrapolating results on the scoping selected
        by the user, if it is scoping
        container, the label must correspond
        to the one of the fields container""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
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
            ``None``, attempts to use the the global server.
        """
        return Operator.default_config(name="gauss_to_node_fc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsGaussToNodeFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsGaussToNodeFc
        """
        return super().outputs


class InputsGaussToNodeFc(_Inputs):
    """Intermediate class used to connect user inputs to
    gauss_to_node_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.averaging.gauss_to_node_fc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    """

    def __init__(self, op: Operator):
        super().__init__(gauss_to_node_fc._spec().inputs, op)
        self._fields_container = Input(gauss_to_node_fc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._fields_container)
        self._mesh = Input(gauss_to_node_fc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh)
        self._scoping = Input(gauss_to_node_fc._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._scoping)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.gauss_to_node_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        The mesh region in this pin is used for
        extrapolating results available at
        gauss or quadrature points to nodal
        points.

        Parameters
        ----------
        my_mesh : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.gauss_to_node_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator.

        Extrapolating results on the scoping selected
        by the user, if it is scoping
        container, the label must correspond
        to the one of the fields container

        Parameters
        ----------
        my_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.gauss_to_node_fc()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> # or
        >>> op.inputs.scoping(my_scoping)
        """
        return self._scoping


class OutputsGaussToNodeFc(_Outputs):
    """Intermediate class used to get outputs from
    gauss_to_node_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.averaging.gauss_to_node_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(gauss_to_node_fc._spec().outputs, op)
        self._fields_container = Output(gauss_to_node_fc._spec().output_pin(0), 0, op)
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator

        Returns
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.averaging.gauss_to_node_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
