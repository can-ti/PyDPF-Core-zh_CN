"""Autogenerated DPF operator classes.

Created on 12/06/2021, 14:29:11.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class remote_workflow_instantiate(Operator):
    """Sends a local workflow to a remote process (and keep a local image of
    it) or create a local image of an existing remote workflow
    (identified by an id and an address) for a given protocol
    registered in the streams.

    Parameters
    ----------
    workflow_to_send : Workflow or int
        Local workflow to push to a remote or id of a
        remote workflow
    streams_to_remote : StreamsContainer
    data_sources_to_remote : DataSources, optional


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.remote_workflow_instantiate()

    >>> # Make input connections
    >>> my_workflow_to_send = dpf.Workflow()
    >>> op.inputs.workflow_to_send.connect(my_workflow_to_send)
    >>> my_streams_to_remote = dpf.StreamsContainer()
    >>> op.inputs.streams_to_remote.connect(my_streams_to_remote)
    >>> my_data_sources_to_remote = dpf.DataSources()
    >>> op.inputs.data_sources_to_remote.connect(my_data_sources_to_remote)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.remote_workflow_instantiate(
    ...     workflow_to_send=my_workflow_to_send,
    ...     streams_to_remote=my_streams_to_remote,
    ...     data_sources_to_remote=my_data_sources_to_remote,
    ... )

    >>> # Get output data
    >>> result_remote_workflow = op.outputs.remote_workflow()
    """

    def __init__(
        self,
        workflow_to_send=None,
        streams_to_remote=None,
        data_sources_to_remote=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="remote_workflow_instantiate", config=config, server=server
        )
        self._inputs = InputsRemoteWorkflowInstantiate(self)
        self._outputs = OutputsRemoteWorkflowInstantiate(self)
        if workflow_to_send is not None:
            self.inputs.workflow_to_send.connect(workflow_to_send)
        if streams_to_remote is not None:
            self.inputs.streams_to_remote.connect(streams_to_remote)
        if data_sources_to_remote is not None:
            self.inputs.data_sources_to_remote.connect(data_sources_to_remote)

    @staticmethod
    def _spec():
        description = """Sends a local workflow to a remote process (and keep a local image of
            it) or create a local image of an existing remote workflow
            (identified by an id and an address) for a given protocol
            registered in the streams."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="workflow_to_send",
                    type_names=["workflow", "int32"],
                    optional=False,
                    document="""Local workflow to push to a remote or id of a
        remote workflow""",
                ),
                3: PinSpecification(
                    name="streams_to_remote",
                    type_names=["streams_container"],
                    optional=False,
                    document="""""",
                ),
                4: PinSpecification(
                    name="data_sources_to_remote",
                    type_names=["data_sources"],
                    optional=True,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="remote_workflow",
                    type_names=["workflow"],
                    optional=False,
                    document="""Remote workflow containing an image of the
        remote workflow and the protocols
        streams""",
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
        return Operator.default_config(
            name="remote_workflow_instantiate", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRemoteWorkflowInstantiate
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRemoteWorkflowInstantiate
        """
        return super().outputs


class InputsRemoteWorkflowInstantiate(_Inputs):
    """Intermediate class used to connect user inputs to
    remote_workflow_instantiate operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.remote_workflow_instantiate()
    >>> my_workflow_to_send = dpf.Workflow()
    >>> op.inputs.workflow_to_send.connect(my_workflow_to_send)
    >>> my_streams_to_remote = dpf.StreamsContainer()
    >>> op.inputs.streams_to_remote.connect(my_streams_to_remote)
    >>> my_data_sources_to_remote = dpf.DataSources()
    >>> op.inputs.data_sources_to_remote.connect(my_data_sources_to_remote)
    """

    def __init__(self, op: Operator):
        super().__init__(remote_workflow_instantiate._spec().inputs, op)
        self._workflow_to_send = Input(
            remote_workflow_instantiate._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._workflow_to_send)
        self._streams_to_remote = Input(
            remote_workflow_instantiate._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_to_remote)
        self._data_sources_to_remote = Input(
            remote_workflow_instantiate._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources_to_remote)

    @property
    def workflow_to_send(self):
        """Allows to connect workflow_to_send input to the operator.

        Local workflow to push to a remote or id of a
        remote workflow

        Parameters
        ----------
        my_workflow_to_send : Workflow or int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.remote_workflow_instantiate()
        >>> op.inputs.workflow_to_send.connect(my_workflow_to_send)
        >>> # or
        >>> op.inputs.workflow_to_send(my_workflow_to_send)
        """
        return self._workflow_to_send

    @property
    def streams_to_remote(self):
        """Allows to connect streams_to_remote input to the operator.

        Parameters
        ----------
        my_streams_to_remote : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.remote_workflow_instantiate()
        >>> op.inputs.streams_to_remote.connect(my_streams_to_remote)
        >>> # or
        >>> op.inputs.streams_to_remote(my_streams_to_remote)
        """
        return self._streams_to_remote

    @property
    def data_sources_to_remote(self):
        """Allows to connect data_sources_to_remote input to the operator.

        Parameters
        ----------
        my_data_sources_to_remote : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.remote_workflow_instantiate()
        >>> op.inputs.data_sources_to_remote.connect(my_data_sources_to_remote)
        >>> # or
        >>> op.inputs.data_sources_to_remote(my_data_sources_to_remote)
        """
        return self._data_sources_to_remote


class OutputsRemoteWorkflowInstantiate(_Outputs):
    """Intermediate class used to get outputs from
    remote_workflow_instantiate operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.remote_workflow_instantiate()
    >>> # Connect inputs : op.inputs. ...
    >>> result_remote_workflow = op.outputs.remote_workflow()
    """

    def __init__(self, op: Operator):
        super().__init__(remote_workflow_instantiate._spec().outputs, op)
        self._remote_workflow = Output(
            remote_workflow_instantiate._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._remote_workflow)

    @property
    def remote_workflow(self):
        """Allows to get remote_workflow output of the operator

        Returns
        ----------
        my_remote_workflow : Workflow

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.remote_workflow_instantiate()
        >>> # Connect inputs : op.inputs. ...
        >>> result_remote_workflow = op.outputs.remote_workflow()
        """  # noqa: E501
        return self._remote_workflow
