"""
cms_dst_table_provider
======================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class cms_dst_table_provider(Operator):
    """Read CST table from a subfile.

    Parameters
    ----------
    data_sources : DataSources
        Data_sources (must contain at least one
        subfile).


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.cms_dst_table_provider()

    >>> # Make input connections
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.cms_dst_table_provider(
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_dst_table = op.outputs.dst_table()
    """

    def __init__(self, data_sources=None, config=None, server=None):
        super().__init__(name="cms_dst_table_provider", config=config, server=server)
        self._inputs = InputsCmsDstTableProvider(self)
        self._outputs = OutputsCmsDstTableProvider(self)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        description = """Read CST table from a subfile."""
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
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="dst_table",
                    type_names=["property_field"],
                    optional=False,
                    document="""Returns integer values of the dst table""",
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
        return Operator.default_config(name="cms_dst_table_provider", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCmsDstTableProvider
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCmsDstTableProvider
        """
        return super().outputs


class InputsCmsDstTableProvider(_Inputs):
    """Intermediate class used to connect user inputs to
    cms_dst_table_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.cms_dst_table_provider()
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(cms_dst_table_provider._spec().inputs, op)
        self._data_sources = Input(
            cms_dst_table_provider._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)

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
        >>> op = dpf.operators.result.cms_dst_table_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsCmsDstTableProvider(_Outputs):
    """Intermediate class used to get outputs from
    cms_dst_table_provider operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.cms_dst_table_provider()
    >>> # Connect inputs : op.inputs. ...
    >>> result_dst_table = op.outputs.dst_table()
    """

    def __init__(self, op: Operator):
        super().__init__(cms_dst_table_provider._spec().outputs, op)
        self._dst_table = Output(cms_dst_table_provider._spec().output_pin(0), 0, op)
        self._outputs.append(self._dst_table)

    @property
    def dst_table(self):
        """Allows to get dst_table output of the operator

        Returns
        ----------
        my_dst_table : PropertyField

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.cms_dst_table_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_dst_table = op.outputs.dst_table()
        """  # noqa: E501
        return self._dst_table
