"""Autogenerated DPF operator classes.

Created on 12/06/2021, 14:29:17.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class poynting_vector_surface(Operator):
    """Compute the Poynting Vector surface integral

    Parameters
    ----------
    fields_containerA : FieldsContainer
    fields_containerB : FieldsContainer
    fields_containerC : FieldsContainer
    fields_containerD : FieldsContainer
    abstract_meshed_region : MeshedRegion, optional
        The mesh region in this pin have to be
        boundary or skin mesh
    int32 : int, optional
        Load step number, if it's specified, the
        poynting vector is computed only on
        the substeps of this step


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.poynting_vector_surface()

    >>> # Make input connections
    >>> my_fields_containerA = dpf.FieldsContainer()
    >>> op.inputs.fields_containerA.connect(my_fields_containerA)
    >>> my_fields_containerB = dpf.FieldsContainer()
    >>> op.inputs.fields_containerB.connect(my_fields_containerB)
    >>> my_fields_containerC = dpf.FieldsContainer()
    >>> op.inputs.fields_containerC.connect(my_fields_containerC)
    >>> my_fields_containerD = dpf.FieldsContainer()
    >>> op.inputs.fields_containerD.connect(my_fields_containerD)
    >>> my_abstract_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
    >>> my_int32 = int()
    >>> op.inputs.int32.connect(my_int32)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.poynting_vector_surface(
    ...     fields_containerA=my_fields_containerA,
    ...     fields_containerB=my_fields_containerB,
    ...     fields_containerC=my_fields_containerC,
    ...     fields_containerD=my_fields_containerD,
    ...     abstract_meshed_region=my_abstract_meshed_region,
    ...     int32=my_int32,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_containerA=None,
        fields_containerB=None,
        fields_containerC=None,
        fields_containerD=None,
        abstract_meshed_region=None,
        int32=None,
        config=None,
        server=None,
    ):
        super().__init__(name="PoyntingVectorSurface", config=config, server=server)
        self._inputs = InputsPoyntingVectorSurface(self)
        self._outputs = OutputsPoyntingVectorSurface(self)
        if fields_containerA is not None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB is not None:
            self.inputs.fields_containerB.connect(fields_containerB)
        if fields_containerC is not None:
            self.inputs.fields_containerC.connect(fields_containerC)
        if fields_containerD is not None:
            self.inputs.fields_containerD.connect(fields_containerD)
        if abstract_meshed_region is not None:
            self.inputs.abstract_meshed_region.connect(abstract_meshed_region)
        if int32 is not None:
            self.inputs.int32.connect(int32)

    @staticmethod
    def _spec():
        description = """Compute the Poynting Vector surface integral"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_containerA",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="fields_containerB",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="fields_containerC",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                3: PinSpecification(
                    name="fields_containerD",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                4: PinSpecification(
                    name="abstract_meshed_region",
                    type_names=["abstract_meshed_region"],
                    optional=True,
                    document="""The mesh region in this pin have to be
        boundary or skin mesh""",
                ),
                5: PinSpecification(
                    name="int32",
                    type_names=["int32"],
                    optional=True,
                    document="""Load step number, if it's specified, the
        poynting vector is computed only on
        the substeps of this step""",
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
        return Operator.default_config(name="PoyntingVectorSurface", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPoyntingVectorSurface
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPoyntingVectorSurface
        """
        return super().outputs


class InputsPoyntingVectorSurface(_Inputs):
    """Intermediate class used to connect user inputs to
    poynting_vector_surface operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.poynting_vector_surface()
    >>> my_fields_containerA = dpf.FieldsContainer()
    >>> op.inputs.fields_containerA.connect(my_fields_containerA)
    >>> my_fields_containerB = dpf.FieldsContainer()
    >>> op.inputs.fields_containerB.connect(my_fields_containerB)
    >>> my_fields_containerC = dpf.FieldsContainer()
    >>> op.inputs.fields_containerC.connect(my_fields_containerC)
    >>> my_fields_containerD = dpf.FieldsContainer()
    >>> op.inputs.fields_containerD.connect(my_fields_containerD)
    >>> my_abstract_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
    >>> my_int32 = int()
    >>> op.inputs.int32.connect(my_int32)
    """

    def __init__(self, op: Operator):
        super().__init__(poynting_vector_surface._spec().inputs, op)
        self._fields_containerA = Input(
            poynting_vector_surface._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_containerA)
        self._fields_containerB = Input(
            poynting_vector_surface._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._fields_containerB)
        self._fields_containerC = Input(
            poynting_vector_surface._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._fields_containerC)
        self._fields_containerD = Input(
            poynting_vector_surface._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._fields_containerD)
        self._abstract_meshed_region = Input(
            poynting_vector_surface._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._abstract_meshed_region)
        self._int32 = Input(poynting_vector_surface._spec().input_pin(5), 5, op, -1)
        self._inputs.append(self._int32)

    @property
    def fields_containerA(self):
        """Allows to connect fields_containerA input to the operator.

        Parameters
        ----------
        my_fields_containerA : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.poynting_vector_surface()
        >>> op.inputs.fields_containerA.connect(my_fields_containerA)
        >>> # or
        >>> op.inputs.fields_containerA(my_fields_containerA)
        """
        return self._fields_containerA

    @property
    def fields_containerB(self):
        """Allows to connect fields_containerB input to the operator.

        Parameters
        ----------
        my_fields_containerB : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.poynting_vector_surface()
        >>> op.inputs.fields_containerB.connect(my_fields_containerB)
        >>> # or
        >>> op.inputs.fields_containerB(my_fields_containerB)
        """
        return self._fields_containerB

    @property
    def fields_containerC(self):
        """Allows to connect fields_containerC input to the operator.

        Parameters
        ----------
        my_fields_containerC : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.poynting_vector_surface()
        >>> op.inputs.fields_containerC.connect(my_fields_containerC)
        >>> # or
        >>> op.inputs.fields_containerC(my_fields_containerC)
        """
        return self._fields_containerC

    @property
    def fields_containerD(self):
        """Allows to connect fields_containerD input to the operator.

        Parameters
        ----------
        my_fields_containerD : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.poynting_vector_surface()
        >>> op.inputs.fields_containerD.connect(my_fields_containerD)
        >>> # or
        >>> op.inputs.fields_containerD(my_fields_containerD)
        """
        return self._fields_containerD

    @property
    def abstract_meshed_region(self):
        """Allows to connect abstract_meshed_region input to the operator.

        The mesh region in this pin have to be
        boundary or skin mesh

        Parameters
        ----------
        my_abstract_meshed_region : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.poynting_vector_surface()
        >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
        >>> # or
        >>> op.inputs.abstract_meshed_region(my_abstract_meshed_region)
        """
        return self._abstract_meshed_region

    @property
    def int32(self):
        """Allows to connect int32 input to the operator.

        Load step number, if it's specified, the
        poynting vector is computed only on
        the substeps of this step

        Parameters
        ----------
        my_int32 : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.poynting_vector_surface()
        >>> op.inputs.int32.connect(my_int32)
        >>> # or
        >>> op.inputs.int32(my_int32)
        """
        return self._int32


class OutputsPoyntingVectorSurface(_Outputs):
    """Intermediate class used to get outputs from
    poynting_vector_surface operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.poynting_vector_surface()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(poynting_vector_surface._spec().outputs, op)
        self._fields_container = Output(
            poynting_vector_surface._spec().output_pin(0), 0, op
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
        >>> op = dpf.operators.result.poynting_vector_surface()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
