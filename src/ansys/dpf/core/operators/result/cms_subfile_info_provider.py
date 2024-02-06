"""
cms_subfile_info_provider
=========================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class cms_subfile_info_provider(Operator):
    """Read required information from a subfile.

    Parameters
    ----------
    data_sources : DataSources
        Data_sources (must contain at least one
        subfile).
    cms_subfile_data : bool
        If this pin i set to true, data are return in
        a field.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.cms_subfile_info_provider()

    >>> # Make input connections
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_cms_subfile_data = bool()
    >>> op.inputs.cms_subfile_data.connect(my_cms_subfile_data)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.cms_subfile_info_provider(
    ...     data_sources=my_data_sources,
    ...     cms_subfile_data=my_cms_subfile_data,
    ... )

    >>> # Get output data
    >>> result_int32 = op.outputs.int32()
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self, data_sources=None, cms_subfile_data=None, config=None, server=None
    ):
        super().__init__(name="cms_subfile_info_provider", config=config, server=server)
        self._inputs = InputsCmsSubfileInfoProvider(self)
        self._outputs = OutputsCmsSubfileInfoProvider(self)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if cms_subfile_data is not None:
            self.inputs.cms_subfile_data.connect(cms_subfile_data)

    @staticmethod
    def _spec():
        description = """Read required information from a subfile."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""Data_sources (must contain at least one
        subfile).""",
                ),
                200: PinSpecification(
                    name="cms_subfile_data",
                    type_names=["bool"],
                    optional=False,
                    document="""If this pin i set to true, data are return in
        a field.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="int32",
                    type_names=["int32"],
                    optional=False,
                    document="""Returns integer values in the order : unit
        system used, stiffness matrix present
        key, damping matrix present key, mass
        matrix present key, number of master
        nodes, number of virtual nodes""",
                ),
                1: PinSpecification(
                    name="field",
                    type_names=["property_field"],
                    optional=False,
                    document="""Returns integer values in the order : number
        of load vectors (nvects), number of
        nodes (nnod), number of virtual nodes
        (nvnodes), number of modes (nvmodes)""",
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
        return Operator.default_config(name="cms_subfile_info_provider", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCmsSubfileInfoProvider
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsCmsSubfileInfoProvider
        """
        return super().outputs


class InputsCmsSubfileInfoProvider(_Inputs):
    """Intermediate class used to connect user inputs to
    cms_subfile_info_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.cms_subfile_info_provider()
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_cms_subfile_data = bool()
    >>> op.inputs.cms_subfile_data.connect(my_cms_subfile_data)
    """

    def __init__(self, op: Operator):
        super().__init__(cms_subfile_info_provider._spec().inputs, op)
        self._data_sources = Input(
            cms_subfile_info_provider._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)
        self._cms_subfile_data = Input(
            cms_subfile_info_provider._spec().input_pin(200), 200, op, -1
        )
        self._inputs.append(self._cms_subfile_data)

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Data_sources (must contain at least one
        subfile).

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cms_subfile_info_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def cms_subfile_data(self):
        """Allows to connect cms_subfile_data input to the operator.

        If this pin i set to true, data are return in
        a field.

        Parameters
        ----------
        my_cms_subfile_data : bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cms_subfile_info_provider()
        >>> op.inputs.cms_subfile_data.connect(my_cms_subfile_data)
        >>> # or
        >>> op.inputs.cms_subfile_data(my_cms_subfile_data)
        """
        return self._cms_subfile_data


class OutputsCmsSubfileInfoProvider(_Outputs):
    """Intermediate class used to get outputs from
    cms_subfile_info_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.cms_subfile_info_provider()
    >>> # Connect inputs : op.inputs. ...
    >>> result_int32 = op.outputs.int32()
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(cms_subfile_info_provider._spec().outputs, op)
        self._int32 = Output(cms_subfile_info_provider._spec().output_pin(0), 0, op)
        self._outputs.append(self._int32)
        self._field = Output(cms_subfile_info_provider._spec().output_pin(1), 1, op)
        self._outputs.append(self._field)

    @property
    def int32(self):
        """Allows to get int32 output of the operator

        Returns
        ----------
        my_int32 : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cms_subfile_info_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_int32 = op.outputs.int32()
        """  # noqa: E501
        return self._int32

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : PropertyField

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cms_subfile_info_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
