"""
merge_meshes
============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class merge_meshes(Operator):
    """Take a set of mesh and assemble them in a unique one

    Parameters
    ----------
    meshes1 : MeshedRegion
        A vector of meshed region to merge or meshed
        region from pin 0 to ...
    meshes2 : MeshedRegion
        A vector of meshed region to merge or meshed
        region from pin 0 to ...
    merge_method : int, optional
        0: merge by distance, 1: merge by node id
        (default)
    box_size : float, optional
        Box size used when merging by distance.
        default value is 1e-10.
    remove_duplicate_elements : int, optional
        0: keep duplicate elements (default), 1:
        remove duplicate elements


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.merge_meshes()

    >>> # Make input connections
    >>> my_meshes1 = dpf.MeshedRegion()
    >>> op.inputs.meshes1.connect(my_meshes1)
    >>> my_meshes2 = dpf.MeshedRegion()
    >>> op.inputs.meshes2.connect(my_meshes2)
    >>> my_merge_method = int()
    >>> op.inputs.merge_method.connect(my_merge_method)
    >>> my_box_size = float()
    >>> op.inputs.box_size.connect(my_box_size)
    >>> my_remove_duplicate_elements = int()
    >>> op.inputs.remove_duplicate_elements.connect(my_remove_duplicate_elements)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.merge_meshes(
    ...     meshes1=my_meshes1,
    ...     meshes2=my_meshes2,
    ...     merge_method=my_merge_method,
    ...     box_size=my_box_size,
    ...     remove_duplicate_elements=my_remove_duplicate_elements,
    ... )

    >>> # Get output data
    >>> result_merges_mesh = op.outputs.merges_mesh()
    """

    def __init__(
        self,
        meshes1=None,
        meshes2=None,
        merge_method=None,
        box_size=None,
        remove_duplicate_elements=None,
        config=None,
        server=None,
    ):
        super().__init__(name="merge::mesh", config=config, server=server)
        self._inputs = InputsMergeMeshes(self)
        self._outputs = OutputsMergeMeshes(self)
        if meshes1 is not None:
            self.inputs.meshes1.connect(meshes1)
        if meshes2 is not None:
            self.inputs.meshes2.connect(meshes2)
        if merge_method is not None:
            self.inputs.merge_method.connect(merge_method)
        if box_size is not None:
            self.inputs.box_size.connect(box_size)
        if remove_duplicate_elements is not None:
            self.inputs.remove_duplicate_elements.connect(remove_duplicate_elements)

    @staticmethod
    def _spec():
        description = """Take a set of mesh and assemble them in a unique one"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="meshes",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""A vector of meshed region to merge or meshed
        region from pin 0 to ...""",
                ),
                1: PinSpecification(
                    name="meshes",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""A vector of meshed region to merge or meshed
        region from pin 0 to ...""",
                ),
                101: PinSpecification(
                    name="merge_method",
                    type_names=["int32"],
                    optional=True,
                    document="""0: merge by distance, 1: merge by node id
        (default)""",
                ),
                102: PinSpecification(
                    name="box_size",
                    type_names=["double"],
                    optional=True,
                    document="""Box size used when merging by distance.
        default value is 1e-10.""",
                ),
                103: PinSpecification(
                    name="remove_duplicate_elements",
                    type_names=["int32"],
                    optional=True,
                    document="""0: keep duplicate elements (default), 1:
        remove duplicate elements""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="merges_mesh",
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
        return Operator.default_config(name="merge::mesh", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeMeshes
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeMeshes
        """
        return super().outputs


class InputsMergeMeshes(_Inputs):
    """Intermediate class used to connect user inputs to
    merge_meshes operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.merge_meshes()
    >>> my_meshes1 = dpf.MeshedRegion()
    >>> op.inputs.meshes1.connect(my_meshes1)
    >>> my_meshes2 = dpf.MeshedRegion()
    >>> op.inputs.meshes2.connect(my_meshes2)
    >>> my_merge_method = int()
    >>> op.inputs.merge_method.connect(my_merge_method)
    >>> my_box_size = float()
    >>> op.inputs.box_size.connect(my_box_size)
    >>> my_remove_duplicate_elements = int()
    >>> op.inputs.remove_duplicate_elements.connect(my_remove_duplicate_elements)
    """

    def __init__(self, op: Operator):
        super().__init__(merge_meshes._spec().inputs, op)
        self._meshes1 = Input(merge_meshes._spec().input_pin(0), 0, op, 0)
        self._inputs.append(self._meshes1)
        self._meshes2 = Input(merge_meshes._spec().input_pin(1), 1, op, 1)
        self._inputs.append(self._meshes2)
        self._merge_method = Input(merge_meshes._spec().input_pin(101), 101, op, -1)
        self._inputs.append(self._merge_method)
        self._box_size = Input(merge_meshes._spec().input_pin(102), 102, op, -1)
        self._inputs.append(self._box_size)
        self._remove_duplicate_elements = Input(
            merge_meshes._spec().input_pin(103), 103, op, -1
        )
        self._inputs.append(self._remove_duplicate_elements)

    @property
    def meshes1(self):
        """Allows to connect meshes1 input to the operator.

        A vector of meshed region to merge or meshed
        region from pin 0 to ...

        Parameters
        ----------
        my_meshes1 : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.merge_meshes()
        >>> op.inputs.meshes1.connect(my_meshes1)
        >>> # or
        >>> op.inputs.meshes1(my_meshes1)
        """
        return self._meshes1

    @property
    def meshes2(self):
        """Allows to connect meshes2 input to the operator.

        A vector of meshed region to merge or meshed
        region from pin 0 to ...

        Parameters
        ----------
        my_meshes2 : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.merge_meshes()
        >>> op.inputs.meshes2.connect(my_meshes2)
        >>> # or
        >>> op.inputs.meshes2(my_meshes2)
        """
        return self._meshes2

    @property
    def merge_method(self):
        """Allows to connect merge_method input to the operator.

        0: merge by distance, 1: merge by node id
        (default)

        Parameters
        ----------
        my_merge_method : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.merge_meshes()
        >>> op.inputs.merge_method.connect(my_merge_method)
        >>> # or
        >>> op.inputs.merge_method(my_merge_method)
        """
        return self._merge_method

    @property
    def box_size(self):
        """Allows to connect box_size input to the operator.

        Box size used when merging by distance.
        default value is 1e-10.

        Parameters
        ----------
        my_box_size : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.merge_meshes()
        >>> op.inputs.box_size.connect(my_box_size)
        >>> # or
        >>> op.inputs.box_size(my_box_size)
        """
        return self._box_size

    @property
    def remove_duplicate_elements(self):
        """Allows to connect remove_duplicate_elements input to the operator.

        0: keep duplicate elements (default), 1:
        remove duplicate elements

        Parameters
        ----------
        my_remove_duplicate_elements : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.merge_meshes()
        >>> op.inputs.remove_duplicate_elements.connect(my_remove_duplicate_elements)
        >>> # or
        >>> op.inputs.remove_duplicate_elements(my_remove_duplicate_elements)
        """
        return self._remove_duplicate_elements


class OutputsMergeMeshes(_Outputs):
    """Intermediate class used to get outputs from
    merge_meshes operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.merge_meshes()
    >>> # Connect inputs : op.inputs. ...
    >>> result_merges_mesh = op.outputs.merges_mesh()
    """

    def __init__(self, op: Operator):
        super().__init__(merge_meshes._spec().outputs, op)
        self._merges_mesh = Output(merge_meshes._spec().output_pin(0), 0, op)
        self._outputs.append(self._merges_mesh)

    @property
    def merges_mesh(self):
        """Allows to get merges_mesh output of the operator

        Returns
        ----------
        my_merges_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.merge_meshes()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merges_mesh = op.outputs.merges_mesh()
        """  # noqa: E501
        return self._merges_mesh
