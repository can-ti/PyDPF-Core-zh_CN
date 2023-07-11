"""
hdf5dpf_generate_result_file
============================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class hdf5dpf_generate_result_file(Operator):
    """Generate a dpf result file from provided information.

    Parameters
    ----------
    filename : str
        Name of the output file that will be
        generated (utf8).
    mesh_provider_out : MeshedRegion, optional
        Defines the meshedregion that is exported and
        provided by meshprovider.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()

    >>> # Make input connections
    >>> my_filename = str()
    >>> op.inputs.filename.connect(my_filename)
    >>> my_mesh_provider_out = dpf.MeshedRegion()
    >>> op.inputs.mesh_provider_out.connect(my_mesh_provider_out)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file(
    ...     filename=my_filename,
    ...     mesh_provider_out=my_mesh_provider_out,
    ... )

    >>> # Get output data
    >>> result_time_freq_support_out = op.outputs.time_freq_support_out()
    >>> result_ansys_unit_system_id = op.outputs.ansys_unit_system_id()
    """

    def __init__(self, filename=None, mesh_provider_out=None, config=None, server=None):
        super().__init__(
            name="hdf5::h5dpf::make_result_file", config=config, server=server
        )
        self._inputs = InputsHdf5DpfGenerateResultFile(self)
        self._outputs = OutputsHdf5DpfGenerateResultFile(self)
        if filename is not None:
            self.inputs.filename.connect(filename)
        if mesh_provider_out is not None:
            self.inputs.mesh_provider_out.connect(mesh_provider_out)

    @staticmethod
    def _spec():
        description = """Generate a dpf result file from provided information."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="filename",
                    type_names=["string"],
                    optional=False,
                    document="""Name of the output file that will be
        generated (utf8).""",
                ),
                1: PinSpecification(
                    name="mesh_provider_out",
                    type_names=["abstract_meshed_region"],
                    optional=True,
                    document="""Defines the meshedregion that is exported and
        provided by meshprovider.""",
                ),
            },
            map_output_pin_spec={
                2: PinSpecification(
                    name="time_freq_support_out",
                    type_names=["time_freq_support"],
                    optional=True,
                    document="""Defines the timefreqsupport that is exported
        and provided by
        timefreqsupportprovider.""",
                ),
                3: PinSpecification(
                    name="ansys_unit_system_id",
                    type_names=["int32"],
                    optional=True,
                    document="""Defines the unitsystem the results are
        exported with.""",
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
        return Operator.default_config(
            name="hdf5::h5dpf::make_result_file", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsHdf5DpfGenerateResultFile
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsHdf5DpfGenerateResultFile
        """
        return super().outputs


class InputsHdf5DpfGenerateResultFile(_Inputs):
    """Intermediate class used to connect user inputs to
    hdf5dpf_generate_result_file operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
    >>> my_filename = str()
    >>> op.inputs.filename.connect(my_filename)
    >>> my_mesh_provider_out = dpf.MeshedRegion()
    >>> op.inputs.mesh_provider_out.connect(my_mesh_provider_out)
    """

    def __init__(self, op: Operator):
        super().__init__(hdf5dpf_generate_result_file._spec().inputs, op)
        self._filename = Input(
            hdf5dpf_generate_result_file._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._filename)
        self._mesh_provider_out = Input(
            hdf5dpf_generate_result_file._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._mesh_provider_out)

    @property
    def filename(self):
        """Allows to connect filename input to the operator.

        Name of the output file that will be
        generated (utf8).

        Parameters
        ----------
        my_filename : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.filename.connect(my_filename)
        >>> # or
        >>> op.inputs.filename(my_filename)
        """
        return self._filename

    @property
    def mesh_provider_out(self):
        """Allows to connect mesh_provider_out input to the operator.

        Defines the meshedregion that is exported and
        provided by meshprovider.

        Parameters
        ----------
        my_mesh_provider_out : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.mesh_provider_out.connect(my_mesh_provider_out)
        >>> # or
        >>> op.inputs.mesh_provider_out(my_mesh_provider_out)
        """
        return self._mesh_provider_out


class OutputsHdf5DpfGenerateResultFile(_Outputs):
    """Intermediate class used to get outputs from
    hdf5dpf_generate_result_file operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
    >>> # Connect inputs : op.inputs. ...
    >>> result_time_freq_support_out = op.outputs.time_freq_support_out()
    >>> result_ansys_unit_system_id = op.outputs.ansys_unit_system_id()
    """

    def __init__(self, op: Operator):
        super().__init__(hdf5dpf_generate_result_file._spec().outputs, op)
        self._time_freq_support_out = Output(
            hdf5dpf_generate_result_file._spec().output_pin(2), 2, op
        )
        self._outputs.append(self._time_freq_support_out)
        self._ansys_unit_system_id = Output(
            hdf5dpf_generate_result_file._spec().output_pin(3), 3, op
        )
        self._outputs.append(self._ansys_unit_system_id)

    @property
    def time_freq_support_out(self):
        """Allows to get time_freq_support_out output of the operator

        Returns
        ----------
        my_time_freq_support_out : TimeFreqSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_time_freq_support_out = op.outputs.time_freq_support_out()
        """  # noqa: E501
        return self._time_freq_support_out

    @property
    def ansys_unit_system_id(self):
        """Allows to get ansys_unit_system_id output of the operator

        Returns
        ----------
        my_ansys_unit_system_id : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> # Connect inputs : op.inputs. ...
        >>> result_ansys_unit_system_id = op.outputs.ansys_unit_system_id()
        """  # noqa: E501
        return self._ansys_unit_system_id
