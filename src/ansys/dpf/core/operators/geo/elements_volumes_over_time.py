"""
elements_volumes_over_time
==========================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class elements_volumes_over_time(Operator):
    """Calculates for a mesh, the volume of each element over time for each
    specified time step.

    Parameters
    ----------
    scoping : Scoping, optional
    displacement : FieldsContainer, optional
        Displacement field's container. must contain
        the mesh if mesh not specified in
        input.
    mesh : MeshedRegion, optional
        Mesh must be defined if the displacement
        field's container does not contain
        it, or if there is no displacement.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.geo.elements_volumes_over_time()

    >>> # Make input connections
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_displacement = dpf.FieldsContainer()
    >>> op.inputs.displacement.connect(my_displacement)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.geo.elements_volumes_over_time(
    ...     scoping=my_scoping,
    ...     displacement=my_displacement,
    ...     mesh=my_mesh,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self, scoping=None, displacement=None, mesh=None, config=None, server=None
    ):
        super().__init__(name="volumes_provider", config=config, server=server)
        self._inputs = InputsElementsVolumesOverTime(self)
        self._outputs = OutputsElementsVolumesOverTime(self)
        if scoping is not None:
            self.inputs.scoping.connect(scoping)
        if displacement is not None:
            self.inputs.displacement.connect(displacement)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        description = """Calculates for a mesh, the volume of each element over time for each
            specified time step."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                1: PinSpecification(
                    name="scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""""",
                ),
                2: PinSpecification(
                    name="displacement",
                    type_names=["fields_container"],
                    optional=True,
                    document="""Displacement field's container. must contain
        the mesh if mesh not specified in
        input.""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=True,
                    document="""Mesh must be defined if the displacement
        field's container does not contain
        it, or if there is no displacement.""",
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
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="volumes_provider", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementsVolumesOverTime
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsElementsVolumesOverTime
        """
        return super().outputs


class InputsElementsVolumesOverTime(_Inputs):
    """Intermediate class used to connect user inputs to
    elements_volumes_over_time operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.elements_volumes_over_time()
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_displacement = dpf.FieldsContainer()
    >>> op.inputs.displacement.connect(my_displacement)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    """

    def __init__(self, op: Operator):
        super().__init__(elements_volumes_over_time._spec().inputs, op)
        self._scoping = Input(
            elements_volumes_over_time._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._scoping)
        self._displacement = Input(
            elements_volumes_over_time._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._displacement)
        self._mesh = Input(elements_volumes_over_time._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator.

        Parameters
        ----------
        my_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.elements_volumes_over_time()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> # or
        >>> op.inputs.scoping(my_scoping)
        """
        return self._scoping

    @property
    def displacement(self):
        """Allows to connect displacement input to the operator.

        Displacement field's container. must contain
        the mesh if mesh not specified in
        input.

        Parameters
        ----------
        my_displacement : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.elements_volumes_over_time()
        >>> op.inputs.displacement.connect(my_displacement)
        >>> # or
        >>> op.inputs.displacement(my_displacement)
        """
        return self._displacement

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Mesh must be defined if the displacement
        field's container does not contain
        it, or if there is no displacement.

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.elements_volumes_over_time()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh


class OutputsElementsVolumesOverTime(_Outputs):
    """Intermediate class used to get outputs from
    elements_volumes_over_time operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.elements_volumes_over_time()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(elements_volumes_over_time._spec().outputs, op)
        self._fields_container = Output(
            elements_volumes_over_time._spec().output_pin(0), 0, op
        )
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
        >>> op = dpf.operators.geo.elements_volumes_over_time()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
