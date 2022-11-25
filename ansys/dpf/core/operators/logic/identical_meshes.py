"""
identical_meshes
================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class identical_meshes(Operator):
    """Take two meshes and compare them. Note: When comparing mesh properties
    the current behaviour is to verify that the properties in the
    first mesh (pin 0) are included in the second mesh (pin 1).

    Parameters
    ----------
    meshA : MeshedRegion
    meshB : MeshedRegion
    small_value : float
        Define what is a small value for numeric
        comparison.
    tolerance : float
        Define the relative tolerance ceil for
        numeric comparison.
    compare_auxiliary : bool
        Compare auxiliary data (i.e property fields,
        scopings...). default value is
        'false'.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.logic.identical_meshes()

    >>> # Make input connections
    >>> my_meshA = dpf.MeshedRegion()
    >>> op.inputs.meshA.connect(my_meshA)
    >>> my_meshB = dpf.MeshedRegion()
    >>> op.inputs.meshB.connect(my_meshB)
    >>> my_small_value = float()
    >>> op.inputs.small_value.connect(my_small_value)
    >>> my_tolerance = float()
    >>> op.inputs.tolerance.connect(my_tolerance)
    >>> my_compare_auxiliary = bool()
    >>> op.inputs.compare_auxiliary.connect(my_compare_auxiliary)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.logic.identical_meshes(
    ...     meshA=my_meshA,
    ...     meshB=my_meshB,
    ...     small_value=my_small_value,
    ...     tolerance=my_tolerance,
    ...     compare_auxiliary=my_compare_auxiliary,
    ... )

    >>> # Get output data
    >>> result_are_identical = op.outputs.are_identical()
    """

    def __init__(
        self,
        meshA=None,
        meshB=None,
        small_value=None,
        tolerance=None,
        compare_auxiliary=None,
        config=None,
        server=None,
    ):
        super().__init__(name="compare::mesh", config=config, server=server)
        self._inputs = InputsIdenticalMeshes(self)
        self._outputs = OutputsIdenticalMeshes(self)
        if meshA is not None:
            self.inputs.meshA.connect(meshA)
        if meshB is not None:
            self.inputs.meshB.connect(meshB)
        if small_value is not None:
            self.inputs.small_value.connect(small_value)
        if tolerance is not None:
            self.inputs.tolerance.connect(tolerance)
        if compare_auxiliary is not None:
            self.inputs.compare_auxiliary.connect(compare_auxiliary)

    @staticmethod
    def _spec():
        description = """Take two meshes and compare them. Note: When comparing mesh properties
            the current behaviour is to verify that the properties in
            the first mesh (pin 0) are included in the second mesh
            (pin 1)."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="meshA",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="meshB",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="small_value",
                    type_names=["double"],
                    optional=False,
                    document="""Define what is a small value for numeric
        comparison.""",
                ),
                3: PinSpecification(
                    name="tolerance",
                    type_names=["double"],
                    optional=False,
                    document="""Define the relative tolerance ceil for
        numeric comparison.""",
                ),
                4: PinSpecification(
                    name="compare_auxiliary",
                    type_names=["bool"],
                    optional=False,
                    document="""Compare auxiliary data (i.e property fields,
        scopings...). default value is
        'false'.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="are_identical",
                    type_names=["bool"],
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
        return Operator.default_config(name="compare::mesh", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsIdenticalMeshes
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsIdenticalMeshes
        """
        return super().outputs


class InputsIdenticalMeshes(_Inputs):
    """Intermediate class used to connect user inputs to
    identical_meshes operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.identical_meshes()
    >>> my_meshA = dpf.MeshedRegion()
    >>> op.inputs.meshA.connect(my_meshA)
    >>> my_meshB = dpf.MeshedRegion()
    >>> op.inputs.meshB.connect(my_meshB)
    >>> my_small_value = float()
    >>> op.inputs.small_value.connect(my_small_value)
    >>> my_tolerance = float()
    >>> op.inputs.tolerance.connect(my_tolerance)
    >>> my_compare_auxiliary = bool()
    >>> op.inputs.compare_auxiliary.connect(my_compare_auxiliary)
    """

    def __init__(self, op: Operator):
        super().__init__(identical_meshes._spec().inputs, op)
        self._meshA = Input(identical_meshes._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._meshA)
        self._meshB = Input(identical_meshes._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._meshB)
        self._small_value = Input(identical_meshes._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._small_value)
        self._tolerance = Input(identical_meshes._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._tolerance)
        self._compare_auxiliary = Input(
            identical_meshes._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._compare_auxiliary)

    @property
    def meshA(self):
        """Allows to connect meshA input to the operator.

        Parameters
        ----------
        my_meshA : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_meshes()
        >>> op.inputs.meshA.connect(my_meshA)
        >>> # or
        >>> op.inputs.meshA(my_meshA)
        """
        return self._meshA

    @property
    def meshB(self):
        """Allows to connect meshB input to the operator.

        Parameters
        ----------
        my_meshB : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_meshes()
        >>> op.inputs.meshB.connect(my_meshB)
        >>> # or
        >>> op.inputs.meshB(my_meshB)
        """
        return self._meshB

    @property
    def small_value(self):
        """Allows to connect small_value input to the operator.

        Define what is a small value for numeric
        comparison.

        Parameters
        ----------
        my_small_value : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_meshes()
        >>> op.inputs.small_value.connect(my_small_value)
        >>> # or
        >>> op.inputs.small_value(my_small_value)
        """
        return self._small_value

    @property
    def tolerance(self):
        """Allows to connect tolerance input to the operator.

        Define the relative tolerance ceil for
        numeric comparison.

        Parameters
        ----------
        my_tolerance : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_meshes()
        >>> op.inputs.tolerance.connect(my_tolerance)
        >>> # or
        >>> op.inputs.tolerance(my_tolerance)
        """
        return self._tolerance

    @property
    def compare_auxiliary(self):
        """Allows to connect compare_auxiliary input to the operator.

        Compare auxiliary data (i.e property fields,
        scopings...). default value is
        'false'.

        Parameters
        ----------
        my_compare_auxiliary : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_meshes()
        >>> op.inputs.compare_auxiliary.connect(my_compare_auxiliary)
        >>> # or
        >>> op.inputs.compare_auxiliary(my_compare_auxiliary)
        """
        return self._compare_auxiliary


class OutputsIdenticalMeshes(_Outputs):
    """Intermediate class used to get outputs from
    identical_meshes operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.identical_meshes()
    >>> # Connect inputs : op.inputs. ...
    >>> result_are_identical = op.outputs.are_identical()
    """

    def __init__(self, op: Operator):
        super().__init__(identical_meshes._spec().outputs, op)
        self._are_identical = Output(identical_meshes._spec().output_pin(0), 0, op)
        self._outputs.append(self._are_identical)

    @property
    def are_identical(self):
        """Allows to get are_identical output of the operator

        Returns
        ----------
        my_are_identical : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.identical_meshes()
        >>> # Connect inputs : op.inputs. ...
        >>> result_are_identical = op.outputs.are_identical()
        """  # noqa: E501
        return self._are_identical
