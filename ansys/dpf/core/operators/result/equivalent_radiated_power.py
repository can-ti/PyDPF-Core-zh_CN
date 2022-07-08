"""
equivalent_radiated_power
-------------------------
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class equivalent_radiated_power(Operator):
    """Compute the Equivalent Radiated Power (ERP)

    Parameters
    ----------
    fields_container : FieldsContainer
    abstract_meshed_region : MeshedRegion or MeshesContainer, optional
        The mesh region in this pin have to be
        boundary or skin mesh
    time_scoping : int or Scoping, optional
        Load step number (if it's specified, the erp
        is computed only on the substeps of
        this step) or time scoping


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.equivalent_radiated_power()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_abstract_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
    >>> my_time_scoping = int()
    >>> op.inputs.time_scoping.connect(my_time_scoping)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.equivalent_radiated_power(
    ...     fields_container=my_fields_container,
    ...     abstract_meshed_region=my_abstract_meshed_region,
    ...     time_scoping=my_time_scoping,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_container=None,
        abstract_meshed_region=None,
        time_scoping=None,
        config=None,
        server=None,
    ):
        super().__init__(name="ERP", config=config, server=server)
        self._inputs = InputsEquivalentRadiatedPower(self)
        self._outputs = OutputsEquivalentRadiatedPower(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if abstract_meshed_region is not None:
            self.inputs.abstract_meshed_region.connect(abstract_meshed_region)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)

    @staticmethod
    def _spec():
        description = """Compute the Equivalent Radiated Power (ERP)"""
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
                    name="abstract_meshed_region",
                    type_names=["abstract_meshed_region", "meshes_container"],
                    optional=True,
                    document="""The mesh region in this pin have to be
        boundary or skin mesh""",
                ),
                2: PinSpecification(
                    name="time_scoping",
                    type_names=["int32", "vector<int32>", "scoping"],
                    optional=True,
                    document="""Load step number (if it's specified, the erp
        is computed only on the substeps of
        this step) or time scoping""",
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
        return Operator.default_config(name="ERP", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsEquivalentRadiatedPower
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsEquivalentRadiatedPower
        """
        return super().outputs


class InputsEquivalentRadiatedPower(_Inputs):
    """Intermediate class used to connect user inputs to
    equivalent_radiated_power operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.equivalent_radiated_power()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_abstract_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
    >>> my_time_scoping = int()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    """

    def __init__(self, op: Operator):
        super().__init__(equivalent_radiated_power._spec().inputs, op)
        self._fields_container = Input(
            equivalent_radiated_power._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._abstract_meshed_region = Input(
            equivalent_radiated_power._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._abstract_meshed_region)
        self._time_scoping = Input(
            equivalent_radiated_power._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._time_scoping)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.equivalent_radiated_power()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def abstract_meshed_region(self):
        """Allows to connect abstract_meshed_region input to the operator.

        The mesh region in this pin have to be
        boundary or skin mesh

        Parameters
        ----------
        my_abstract_meshed_region : MeshedRegion or MeshesContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.equivalent_radiated_power()
        >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
        >>> # or
        >>> op.inputs.abstract_meshed_region(my_abstract_meshed_region)
        """
        return self._abstract_meshed_region

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        Load step number (if it's specified, the erp
        is computed only on the substeps of
        this step) or time scoping

        Parameters
        ----------
        my_time_scoping : int or Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.equivalent_radiated_power()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping


class OutputsEquivalentRadiatedPower(_Outputs):
    """Intermediate class used to get outputs from
    equivalent_radiated_power operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.equivalent_radiated_power()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(equivalent_radiated_power._spec().outputs, op)
        self._fields_container = Output(
            equivalent_radiated_power._spec().output_pin(0), 0, op
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
        >>> op = dpf.operators.result.equivalent_radiated_power()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
