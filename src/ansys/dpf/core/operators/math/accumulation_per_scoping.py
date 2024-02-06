"""
accumulation_per_scoping
========================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class accumulation_per_scoping(Operator):
    """This operator calculates the sum and the percentage of total sum of
    the input fields container for each scoping of the scopings
    container.

    Parameters
    ----------
    fields_container : FieldsContainer
    mesh_scoping : Scoping, optional
        Master scoping. all scopings in the scopings
        container will be intersected with
        this scoping.
    data_sources : DataSources
    scopings_container : ScopingsContainer
        The intersection between the of the first
        will be used.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.accumulation_per_scoping()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_scopings_container = dpf.ScopingsContainer()
    >>> op.inputs.scopings_container.connect(my_scopings_container)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.accumulation_per_scoping(
    ...     fields_container=my_fields_container,
    ...     mesh_scoping=my_mesh_scoping,
    ...     data_sources=my_data_sources,
    ...     scopings_container=my_scopings_container,
    ... )

    >>> # Get output data
    >>> result_accumulation_per_scoping = op.outputs.accumulation_per_scoping()
    >>> result_accumulation_per_scoping_percentage = op.outputs.accumulation_per_scoping_percentage()
    """

    def __init__(
        self,
        fields_container=None,
        mesh_scoping=None,
        data_sources=None,
        scopings_container=None,
        config=None,
        server=None,
    ):
        super().__init__(name="accumulation_per_scoping", config=config, server=server)
        self._inputs = InputsAccumulationPerScoping(self)
        self._outputs = OutputsAccumulationPerScoping(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if scopings_container is not None:
            self.inputs.scopings_container.connect(scopings_container)

    @staticmethod
    def _spec():
        description = """This operator calculates the sum and the percentage of total sum of
            the input fields container for each scoping of the
            scopings container."""
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
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""Master scoping. all scopings in the scopings
        container will be intersected with
        this scoping.""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""""",
                ),
                5: PinSpecification(
                    name="scopings_container",
                    type_names=["scopings_container"],
                    optional=False,
                    document="""The intersection between the of the first
        will be used.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="accumulation_per_scoping",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="accumulation_per_scoping_percentage",
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
        return Operator.default_config(name="accumulation_per_scoping", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAccumulationPerScoping
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsAccumulationPerScoping
        """
        return super().outputs


class InputsAccumulationPerScoping(_Inputs):
    """Intermediate class used to connect user inputs to
    accumulation_per_scoping operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.accumulation_per_scoping()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_scopings_container = dpf.ScopingsContainer()
    >>> op.inputs.scopings_container.connect(my_scopings_container)
    """

    def __init__(self, op: Operator):
        super().__init__(accumulation_per_scoping._spec().inputs, op)
        self._fields_container = Input(
            accumulation_per_scoping._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._mesh_scoping = Input(
            accumulation_per_scoping._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._mesh_scoping)
        self._data_sources = Input(
            accumulation_per_scoping._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)
        self._scopings_container = Input(
            accumulation_per_scoping._spec().input_pin(5), 5, op, -1
        )
        self._inputs.append(self._scopings_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.accumulation_per_scoping()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Master scoping. all scopings in the scopings
        container will be intersected with
        this scoping.

        Parameters
        ----------
        my_mesh_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.accumulation_per_scoping()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.accumulation_per_scoping()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def scopings_container(self):
        """Allows to connect scopings_container input to the operator.

        The intersection between the of the first
        will be used.

        Parameters
        ----------
        my_scopings_container : ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.accumulation_per_scoping()
        >>> op.inputs.scopings_container.connect(my_scopings_container)
        >>> # or
        >>> op.inputs.scopings_container(my_scopings_container)
        """
        return self._scopings_container


class OutputsAccumulationPerScoping(_Outputs):
    """Intermediate class used to get outputs from
    accumulation_per_scoping operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.accumulation_per_scoping()
    >>> # Connect inputs : op.inputs. ...
    >>> result_accumulation_per_scoping = op.outputs.accumulation_per_scoping()
    >>> result_accumulation_per_scoping_percentage = op.outputs.accumulation_per_scoping_percentage()
    """

    def __init__(self, op: Operator):
        super().__init__(accumulation_per_scoping._spec().outputs, op)
        self._accumulation_per_scoping = Output(
            accumulation_per_scoping._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._accumulation_per_scoping)
        self._accumulation_per_scoping_percentage = Output(
            accumulation_per_scoping._spec().output_pin(1), 1, op
        )
        self._outputs.append(self._accumulation_per_scoping_percentage)

    @property
    def accumulation_per_scoping(self):
        """Allows to get accumulation_per_scoping output of the operator

        Returns
        ----------
        my_accumulation_per_scoping : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.accumulation_per_scoping()
        >>> # Connect inputs : op.inputs. ...
        >>> result_accumulation_per_scoping = op.outputs.accumulation_per_scoping()
        """  # noqa: E501
        return self._accumulation_per_scoping

    @property
    def accumulation_per_scoping_percentage(self):
        """Allows to get accumulation_per_scoping_percentage output of the operator

        Returns
        ----------
        my_accumulation_per_scoping_percentage : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.accumulation_per_scoping()
        >>> # Connect inputs : op.inputs. ...
        >>> result_accumulation_per_scoping_percentage = op.outputs.accumulation_per_scoping_percentage()
        """  # noqa: E501
        return self._accumulation_per_scoping_percentage
