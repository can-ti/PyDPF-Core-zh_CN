"""
field_to_csv
============
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class field_to_csv(Operator):
    """Exports a field or a fields container into a csv file

    Parameters
    ----------
    field_or_fields_container : FieldsContainer or Field
        Field_or_fields_container
    file_path : str
    storage_type : int, optional
        Storage type : if matrices (without any
        particularity) are included in the
        fields container, the storage format
        can be chosen. 0 : flat/line format,
        1 : ranked format. if 1 is chosen,
        the csv can not be read by "csv to
        field" operator anymore. default : 0.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.field_to_csv()

    >>> # Make input connections
    >>> my_field_or_fields_container = dpf.FieldsContainer()
    >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
    >>> my_file_path = str()
    >>> op.inputs.file_path.connect(my_file_path)
    >>> my_storage_type = int()
    >>> op.inputs.storage_type.connect(my_storage_type)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.field_to_csv(
    ...     field_or_fields_container=my_field_or_fields_container,
    ...     file_path=my_file_path,
    ...     storage_type=my_storage_type,
    ... )

    """

    def __init__(
        self,
        field_or_fields_container=None,
        file_path=None,
        storage_type=None,
        config=None,
        server=None,
    ):
        super().__init__(name="field_to_csv", config=config, server=server)
        self._inputs = InputsFieldToCsv(self)
        self._outputs = OutputsFieldToCsv(self)
        if field_or_fields_container is not None:
            self.inputs.field_or_fields_container.connect(field_or_fields_container)
        if file_path is not None:
            self.inputs.file_path.connect(file_path)
        if storage_type is not None:
            self.inputs.storage_type.connect(storage_type)

    @staticmethod
    def _spec():
        description = """Exports a field or a fields container into a csv file"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field_or_fields_container",
                    type_names=["fields_container", "field"],
                    optional=False,
                    document="""Field_or_fields_container""",
                ),
                1: PinSpecification(
                    name="file_path",
                    type_names=["string"],
                    optional=False,
                    document="""""",
                ),
                2: PinSpecification(
                    name="storage_type",
                    type_names=["int32"],
                    optional=True,
                    document="""Storage type : if matrices (without any
        particularity) are included in the
        fields container, the storage format
        can be chosen. 0 : flat/line format,
        1 : ranked format. if 1 is chosen,
        the csv can not be read by "csv to
        field" operator anymore. default : 0.""",
                ),
            },
            map_output_pin_spec={},
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
        return Operator.default_config(name="field_to_csv", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFieldToCsv
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsFieldToCsv
        """
        return super().outputs


class InputsFieldToCsv(_Inputs):
    """Intermediate class used to connect user inputs to
    field_to_csv operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.field_to_csv()
    >>> my_field_or_fields_container = dpf.FieldsContainer()
    >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
    >>> my_file_path = str()
    >>> op.inputs.file_path.connect(my_file_path)
    >>> my_storage_type = int()
    >>> op.inputs.storage_type.connect(my_storage_type)
    """

    def __init__(self, op: Operator):
        super().__init__(field_to_csv._spec().inputs, op)
        self._field_or_fields_container = Input(
            field_to_csv._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._field_or_fields_container)
        self._file_path = Input(field_to_csv._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._file_path)
        self._storage_type = Input(field_to_csv._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._storage_type)

    @property
    def field_or_fields_container(self):
        """Allows to connect field_or_fields_container input to the operator.

        Field_or_fields_container

        Parameters
        ----------
        my_field_or_fields_container : FieldsContainer or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.field_to_csv()
        >>> op.inputs.field_or_fields_container.connect(my_field_or_fields_container)
        >>> # or
        >>> op.inputs.field_or_fields_container(my_field_or_fields_container)
        """
        return self._field_or_fields_container

    @property
    def file_path(self):
        """Allows to connect file_path input to the operator.

        Parameters
        ----------
        my_file_path : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.field_to_csv()
        >>> op.inputs.file_path.connect(my_file_path)
        >>> # or
        >>> op.inputs.file_path(my_file_path)
        """
        return self._file_path

    @property
    def storage_type(self):
        """Allows to connect storage_type input to the operator.

        Storage type : if matrices (without any
        particularity) are included in the
        fields container, the storage format
        can be chosen. 0 : flat/line format,
        1 : ranked format. if 1 is chosen,
        the csv can not be read by "csv to
        field" operator anymore. default : 0.

        Parameters
        ----------
        my_storage_type : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.field_to_csv()
        >>> op.inputs.storage_type.connect(my_storage_type)
        >>> # or
        >>> op.inputs.storage_type(my_storage_type)
        """
        return self._storage_type


class OutputsFieldToCsv(_Outputs):
    """Intermediate class used to get outputs from
    field_to_csv operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.field_to_csv()
    >>> # Connect inputs : op.inputs. ...
    """

    def __init__(self, op: Operator):
        super().__init__(field_to_csv._spec().outputs, op)
