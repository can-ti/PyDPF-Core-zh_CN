"""
split_on_property_type
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class split_on_property_type(Operator):
    """Splits a given scoping or the mesh scoping (nodal or elemental) on
    given properties (elshape and/or material) and returns a scopings
    container with those split scopings.

    Parameters
    ----------
    mesh_scoping : Scoping, optional
        Scoping
    mesh : MeshedRegion
        Mesh region
    requested_location : str
        Location (default is elemental)
    label1 : str, optional
        Properties to apply the filtering 'mat'
        and/or 'elshape' (default is
        'elshape')
    label2 : str, optional
        Properties to apply the filtering 'mat'
        and/or 'elshape' (default is
        'elshape')


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.scoping.split_on_property_type()

    >>> # Make input connections
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_requested_location = str()
    >>> op.inputs.requested_location.connect(my_requested_location)
    >>> my_label1 = str()
    >>> op.inputs.label1.connect(my_label1)
    >>> my_label2 = str()
    >>> op.inputs.label2.connect(my_label2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.scoping.split_on_property_type(
    ...     mesh_scoping=my_mesh_scoping,
    ...     mesh=my_mesh,
    ...     requested_location=my_requested_location,
    ...     label1=my_label1,
    ...     label2=my_label2,
    ... )

    >>> # Get output data
    >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """

    def __init__(
        self,
        mesh_scoping=None,
        mesh=None,
        requested_location=None,
        label1=None,
        label2=None,
        config=None,
        server=None,
    ):
        super().__init__(name="scoping::by_property", config=config, server=server)
        self._inputs = InputsSplitOnPropertyType(self)
        self._outputs = OutputsSplitOnPropertyType(self)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if requested_location is not None:
            self.inputs.requested_location.connect(requested_location)
        if label1 is not None:
            self.inputs.label1.connect(label1)
        if label2 is not None:
            self.inputs.label2.connect(label2)

    @staticmethod
    def _spec():
        description = """Splits a given scoping or the mesh scoping (nodal or elemental) on
            given properties (elshape and/or material) and returns a
            scopings container with those split scopings."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""Scoping""",
                ),
                7: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""Mesh region""",
                ),
                9: PinSpecification(
                    name="requested_location",
                    type_names=["string"],
                    optional=False,
                    document="""Location (default is elemental)""",
                ),
                13: PinSpecification(
                    name="label",
                    type_names=["string"],
                    optional=True,
                    document="""Properties to apply the filtering 'mat'
        and/or 'elshape' (default is
        'elshape')""",
                ),
                14: PinSpecification(
                    name="label",
                    type_names=["string"],
                    optional=True,
                    document="""Properties to apply the filtering 'mat'
        and/or 'elshape' (default is
        'elshape')""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scopings_container"],
                    optional=False,
                    document="""Scoping""",
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
        return Operator.default_config(name="scoping::by_property", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSplitOnPropertyType
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSplitOnPropertyType
        """
        return super().outputs


class InputsSplitOnPropertyType(_Inputs):
    """Intermediate class used to connect user inputs to
    split_on_property_type operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.split_on_property_type()
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_requested_location = str()
    >>> op.inputs.requested_location.connect(my_requested_location)
    >>> my_label1 = str()
    >>> op.inputs.label1.connect(my_label1)
    >>> my_label2 = str()
    >>> op.inputs.label2.connect(my_label2)
    """

    def __init__(self, op: Operator):
        super().__init__(split_on_property_type._spec().inputs, op)
        self._mesh_scoping = Input(
            split_on_property_type._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._mesh_scoping)
        self._mesh = Input(split_on_property_type._spec().input_pin(7), 7, op, -1)
        self._inputs.append(self._mesh)
        self._requested_location = Input(
            split_on_property_type._spec().input_pin(9), 9, op, -1
        )
        self._inputs.append(self._requested_location)
        self._label1 = Input(split_on_property_type._spec().input_pin(13), 13, op, 0)
        self._inputs.append(self._label1)
        self._label2 = Input(split_on_property_type._spec().input_pin(14), 14, op, 1)
        self._inputs.append(self._label2)

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Scoping

        Parameters
        ----------
        my_mesh_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.split_on_property_type()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Mesh region

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.split_on_property_type()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator.

        Location (default is elemental)

        Parameters
        ----------
        my_requested_location : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.split_on_property_type()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> # or
        >>> op.inputs.requested_location(my_requested_location)
        """
        return self._requested_location

    @property
    def label1(self):
        """Allows to connect label1 input to the operator.

        Properties to apply the filtering 'mat'
        and/or 'elshape' (default is
        'elshape')

        Parameters
        ----------
        my_label1 : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.split_on_property_type()
        >>> op.inputs.label1.connect(my_label1)
        >>> # or
        >>> op.inputs.label1(my_label1)
        """
        return self._label1

    @property
    def label2(self):
        """Allows to connect label2 input to the operator.

        Properties to apply the filtering 'mat'
        and/or 'elshape' (default is
        'elshape')

        Parameters
        ----------
        my_label2 : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.split_on_property_type()
        >>> op.inputs.label2.connect(my_label2)
        >>> # or
        >>> op.inputs.label2(my_label2)
        """
        return self._label2


class OutputsSplitOnPropertyType(_Outputs):
    """Intermediate class used to get outputs from
    split_on_property_type operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.scoping.split_on_property_type()
    >>> # Connect inputs : op.inputs. ...
    >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """

    def __init__(self, op: Operator):
        super().__init__(split_on_property_type._spec().outputs, op)
        self._mesh_scoping = Output(split_on_property_type._spec().output_pin(0), 0, op)
        self._outputs.append(self._mesh_scoping)

    @property
    def mesh_scoping(self):
        """Allows to get mesh_scoping output of the operator

        Returns
        ----------
        my_mesh_scoping : ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.scoping.split_on_property_type()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh_scoping = op.outputs.mesh_scoping()
        """  # noqa: E501
        return self._mesh_scoping
