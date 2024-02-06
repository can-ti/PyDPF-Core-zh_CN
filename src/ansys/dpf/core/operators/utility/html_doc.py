"""
html_doc
========
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class html_doc(Operator):
    """Create dpf's html documentation. Only on Windows.

    Parameters
    ----------
    output_path : str, optional
        Default is {working
        directory}/dataprocessingdoc.html
    exposure_level : int, optional
        Generate the documentation depending on
        exposure level : 0 (default) for
        public operators, 1 includes hidden
        operator, 2 includes private
        operator, 3 includes operator without
        specifications.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.html_doc()

    >>> # Make input connections
    >>> my_output_path = str()
    >>> op.inputs.output_path.connect(my_output_path)
    >>> my_exposure_level = int()
    >>> op.inputs.exposure_level.connect(my_exposure_level)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.html_doc(
    ...     output_path=my_output_path,
    ...     exposure_level=my_exposure_level,
    ... )

    """

    def __init__(self, output_path=None, exposure_level=None, config=None, server=None):
        super().__init__(name="html_doc", config=config, server=server)
        self._inputs = InputsHtmlDoc(self)
        self._outputs = OutputsHtmlDoc(self)
        if output_path is not None:
            self.inputs.output_path.connect(output_path)
        if exposure_level is not None:
            self.inputs.exposure_level.connect(exposure_level)

    @staticmethod
    def _spec():
        description = """Create dpf's html documentation. Only on Windows."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="output_path",
                    type_names=["string"],
                    optional=True,
                    document="""Default is {working
        directory}/dataprocessingdoc.html""",
                ),
                1: PinSpecification(
                    name="exposure_level",
                    type_names=["int32"],
                    optional=True,
                    document="""Generate the documentation depending on
        exposure level : 0 (default) for
        public operators, 1 includes hidden
        operator, 2 includes private
        operator, 3 includes operator without
        specifications.""",
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
        return Operator.default_config(name="html_doc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsHtmlDoc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsHtmlDoc
        """
        return super().outputs


class InputsHtmlDoc(_Inputs):
    """Intermediate class used to connect user inputs to
    html_doc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.html_doc()
    >>> my_output_path = str()
    >>> op.inputs.output_path.connect(my_output_path)
    >>> my_exposure_level = int()
    >>> op.inputs.exposure_level.connect(my_exposure_level)
    """

    def __init__(self, op: Operator):
        super().__init__(html_doc._spec().inputs, op)
        self._output_path = Input(html_doc._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._output_path)
        self._exposure_level = Input(html_doc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._exposure_level)

    @property
    def output_path(self):
        """Allows to connect output_path input to the operator.

        Default is {working
        directory}/dataprocessingdoc.html

        Parameters
        ----------
        my_output_path : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.html_doc()
        >>> op.inputs.output_path.connect(my_output_path)
        >>> # or
        >>> op.inputs.output_path(my_output_path)
        """
        return self._output_path

    @property
    def exposure_level(self):
        """Allows to connect exposure_level input to the operator.

        Generate the documentation depending on
        exposure level : 0 (default) for
        public operators, 1 includes hidden
        operator, 2 includes private
        operator, 3 includes operator without
        specifications.

        Parameters
        ----------
        my_exposure_level : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.html_doc()
        >>> op.inputs.exposure_level.connect(my_exposure_level)
        >>> # or
        >>> op.inputs.exposure_level(my_exposure_level)
        """
        return self._exposure_level


class OutputsHtmlDoc(_Outputs):
    """Intermediate class used to get outputs from
    html_doc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.html_doc()
    >>> # Connect inputs : op.inputs. ...
    """

    def __init__(self, op: Operator):
        super().__init__(html_doc._spec().outputs, op)
