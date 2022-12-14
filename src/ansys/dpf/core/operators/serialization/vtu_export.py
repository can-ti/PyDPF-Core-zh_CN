"""
vtu_export
==========
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class vtu_export(Operator):
    """Export DPF data into vtu format.

    Parameters
    ----------
    directory : str
        Directory path
    base_name : str, optional
        Vtu base file name, (default is file)
    mesh : MeshedRegion
        Mesh
    fields1 : Field or FieldsContainer
        Nodal or elemental fields (over time) to
        export
    fields2 : Field or FieldsContainer
        Nodal or elemental fields (over time) to
        export
    write_mode : str, optional
        Available are rawbinarycompressed, rawbinary,
        base64appended, base64inline, ascii,
        default is (rawbinarycompressed)


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.vtu_export()

    >>> # Make input connections
    >>> my_directory = str()
    >>> op.inputs.directory.connect(my_directory)
    >>> my_base_name = str()
    >>> op.inputs.base_name.connect(my_base_name)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_fields1 = dpf.Field()
    >>> op.inputs.fields1.connect(my_fields1)
    >>> my_fields2 = dpf.Field()
    >>> op.inputs.fields2.connect(my_fields2)
    >>> my_write_mode = str()
    >>> op.inputs.write_mode.connect(my_write_mode)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.vtu_export(
    ...     directory=my_directory,
    ...     base_name=my_base_name,
    ...     mesh=my_mesh,
    ...     fields1=my_fields1,
    ...     fields2=my_fields2,
    ...     write_mode=my_write_mode,
    ... )

    >>> # Get output data
    >>> result_path = op.outputs.path()
    """

    def __init__(
        self,
        directory=None,
        base_name=None,
        mesh=None,
        fields1=None,
        fields2=None,
        write_mode=None,
        config=None,
        server=None,
    ):
        super().__init__(name="vtu_export", config=config, server=server)
        self._inputs = InputsVtuExport(self)
        self._outputs = OutputsVtuExport(self)
        if directory is not None:
            self.inputs.directory.connect(directory)
        if base_name is not None:
            self.inputs.base_name.connect(base_name)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if fields1 is not None:
            self.inputs.fields1.connect(fields1)
        if fields2 is not None:
            self.inputs.fields2.connect(fields2)
        if write_mode is not None:
            self.inputs.write_mode.connect(write_mode)

    @staticmethod
    def _spec():
        description = """Export DPF data into vtu format."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="directory",
                    type_names=["string"],
                    optional=False,
                    document="""Directory path""",
                ),
                1: PinSpecification(
                    name="base_name",
                    type_names=["string"],
                    optional=True,
                    document="""Vtu base file name, (default is file)""",
                ),
                2: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""Mesh""",
                ),
                3: PinSpecification(
                    name="fields",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Nodal or elemental fields (over time) to
        export""",
                ),
                4: PinSpecification(
                    name="fields",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Nodal or elemental fields (over time) to
        export""",
                ),
                100: PinSpecification(
                    name="write_mode",
                    type_names=["string"],
                    optional=True,
                    document="""Available are rawbinarycompressed, rawbinary,
        base64appended, base64inline, ascii,
        default is (rawbinarycompressed)""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="path",
                    type_names=["data_sources"],
                    optional=False,
                    document="""List of output vtu file path""",
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
        return Operator.default_config(name="vtu_export", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsVtuExport
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsVtuExport
        """
        return super().outputs


class InputsVtuExport(_Inputs):
    """Intermediate class used to connect user inputs to
    vtu_export operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.vtu_export()
    >>> my_directory = str()
    >>> op.inputs.directory.connect(my_directory)
    >>> my_base_name = str()
    >>> op.inputs.base_name.connect(my_base_name)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_fields1 = dpf.Field()
    >>> op.inputs.fields1.connect(my_fields1)
    >>> my_fields2 = dpf.Field()
    >>> op.inputs.fields2.connect(my_fields2)
    >>> my_write_mode = str()
    >>> op.inputs.write_mode.connect(my_write_mode)
    """

    def __init__(self, op: Operator):
        super().__init__(vtu_export._spec().inputs, op)
        self._directory = Input(vtu_export._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._directory)
        self._base_name = Input(vtu_export._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._base_name)
        self._mesh = Input(vtu_export._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._mesh)
        self._fields1 = Input(vtu_export._spec().input_pin(3), 3, op, 0)
        self._inputs.append(self._fields1)
        self._fields2 = Input(vtu_export._spec().input_pin(4), 4, op, 1)
        self._inputs.append(self._fields2)
        self._write_mode = Input(vtu_export._spec().input_pin(100), 100, op, -1)
        self._inputs.append(self._write_mode)

    @property
    def directory(self):
        """Allows to connect directory input to the operator.

        Directory path

        Parameters
        ----------
        my_directory : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.vtu_export()
        >>> op.inputs.directory.connect(my_directory)
        >>> # or
        >>> op.inputs.directory(my_directory)
        """
        return self._directory

    @property
    def base_name(self):
        """Allows to connect base_name input to the operator.

        Vtu base file name, (default is file)

        Parameters
        ----------
        my_base_name : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.vtu_export()
        >>> op.inputs.base_name.connect(my_base_name)
        >>> # or
        >>> op.inputs.base_name(my_base_name)
        """
        return self._base_name

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Mesh

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.vtu_export()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def fields1(self):
        """Allows to connect fields1 input to the operator.

        Nodal or elemental fields (over time) to
        export

        Parameters
        ----------
        my_fields1 : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.vtu_export()
        >>> op.inputs.fields1.connect(my_fields1)
        >>> # or
        >>> op.inputs.fields1(my_fields1)
        """
        return self._fields1

    @property
    def fields2(self):
        """Allows to connect fields2 input to the operator.

        Nodal or elemental fields (over time) to
        export

        Parameters
        ----------
        my_fields2 : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.vtu_export()
        >>> op.inputs.fields2.connect(my_fields2)
        >>> # or
        >>> op.inputs.fields2(my_fields2)
        """
        return self._fields2

    @property
    def write_mode(self):
        """Allows to connect write_mode input to the operator.

        Available are rawbinarycompressed, rawbinary,
        base64appended, base64inline, ascii,
        default is (rawbinarycompressed)

        Parameters
        ----------
        my_write_mode : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.vtu_export()
        >>> op.inputs.write_mode.connect(my_write_mode)
        >>> # or
        >>> op.inputs.write_mode(my_write_mode)
        """
        return self._write_mode


class OutputsVtuExport(_Outputs):
    """Intermediate class used to get outputs from
    vtu_export operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.vtu_export()
    >>> # Connect inputs : op.inputs. ...
    >>> result_path = op.outputs.path()
    """

    def __init__(self, op: Operator):
        super().__init__(vtu_export._spec().outputs, op)
        self._path = Output(vtu_export._spec().output_pin(0), 0, op)
        self._outputs.append(self._path)

    @property
    def path(self):
        """Allows to get path output of the operator

        Returns
        ----------
        my_path : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.vtu_export()
        >>> # Connect inputs : op.inputs. ...
        >>> result_path = op.outputs.path()
        """  # noqa: E501
        return self._path