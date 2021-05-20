"""
bind_support_fc
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class bind_support_fc(Operator):
    """Tie a support to a fields container.

      available inputs:
        - fields_container (FieldsContainer)
        - support (MeshedRegion, AbstractFieldSupport)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.bind_support_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_support = dpf.MeshedRegion()
      >>> op.inputs.support.connect(my_support)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.bind_support_fc(fields_container=my_fields_container,support=my_support)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, support=None, config=None, server=None):
        super().__init__(name="BindSupportFC", config = config, server = server)
        self._inputs = InputsBindSupportFc(self)
        self._outputs = OutputsBindSupportFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if support !=None:
            self.inputs.support.connect(support)

    @staticmethod
    def _spec():
        spec = Specification(description="""Tie a support to a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "support", type_names=["abstract_meshed_region","abstract_field_support"], optional=False, document="""meshed region or a support of the field""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "BindSupportFC")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsBindSupportFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsBindSupportFc 
        """
        return super().outputs


#internal name: BindSupportFC
#scripting name: bind_support_fc
class InputsBindSupportFc(_Inputs):
    """Intermediate class used to connect user inputs to bind_support_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.bind_support_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_support = dpf.MeshedRegion()
      >>> op.inputs.support.connect(my_support)
    """
    def __init__(self, op: Operator):
        super().__init__(bind_support_fc._spec().inputs, op)
        self._fields_container = Input(bind_support_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._support = Input(bind_support_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._support)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.bind_support_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def support(self):
        """Allows to connect support input to the operator

        - pindoc: meshed region or a support of the field

        Parameters
        ----------
        my_support : MeshedRegion, AbstractFieldSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.bind_support_fc()
        >>> op.inputs.support.connect(my_support)
        >>> #or
        >>> op.inputs.support(my_support)

        """
        return self._support

class OutputsBindSupportFc(_Outputs):
    """Intermediate class used to get outputs from bind_support_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.bind_support_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(bind_support_fc._spec().outputs, op)
        self._fields_container = Output(bind_support_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.bind_support_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

