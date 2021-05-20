"""
min_max_over_label_fc
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "min_max" category
"""

class min_max_over_label_fc(Operator):
    """Create two fields (0 min 1 max) by looping over the fields container in input and taking the min/max value by component through all the fields having the same id for the label set in input (in pin 1). If no label is specified or if the specified label doesn't exist, the operation is done over all the fields. The fields out are located on the label set in input, so their scoping are the labels ids.For each min max value, the label id for one other fields container labels is kept and returned in a scoping in pin 2 (min) and 3 (max).The field's scoping ids of the value kept in min max are also returned in the scopings in pin 4 (min) and 5 (max).

      available inputs:
        - fields_container (FieldsContainer)
        - label (str)

      available outputs:
        - field_min (Field)
        - field_max (Field)
        - domain_ids_min (Scoping)
        - domain_ids_max (Scoping)
        - scoping_ids_min (Scoping)
        - scoping_ids_max (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.min_max.min_max_over_label_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_label = str()
      >>> op.inputs.label.connect(my_label)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.min_max.min_max_over_label_fc(fields_container=my_fields_container,label=my_label)

      >>> # Get output data
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()
      >>> result_domain_ids_min = op.outputs.domain_ids_min()
      >>> result_domain_ids_max = op.outputs.domain_ids_max()
      >>> result_scoping_ids_min = op.outputs.scoping_ids_min()
      >>> result_scoping_ids_max = op.outputs.scoping_ids_max()"""
    def __init__(self, fields_container=None, label=None, config=None, server=None):
        super().__init__(name="min_max_over_label_fc", config = config, server = server)
        self._inputs = InputsMinMaxOverLabelFc(self)
        self._outputs = OutputsMinMaxOverLabelFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if label !=None:
            self.inputs.label.connect(label)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create two fields (0 min 1 max) by looping over the fields container in input and taking the min/max value by component through all the fields having the same id for the label set in input (in pin 1). If no label is specified or if the specified label doesn't exist, the operation is done over all the fields. The fields out are located on the label set in input, so their scoping are the labels ids.For each min max value, the label id for one other fields container labels is kept and returned in a scoping in pin 2 (min) and 3 (max).The field's scoping ids of the value kept in min max are also returned in the scopings in pin 4 (min) and 5 (max).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "label", type_names=["string"], optional=False, document="""label name from the fields container""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_min", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "field_max", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "domain_ids_min", type_names=["scoping"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "domain_ids_max", type_names=["scoping"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "scoping_ids_min", type_names=["scoping"], optional=False, document=""""""), 
                                 5 : PinSpecification(name = "scoping_ids_max", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "min_max_over_label_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMinMaxOverLabelFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMinMaxOverLabelFc 
        """
        return super().outputs


#internal name: min_max_over_label_fc
#scripting name: min_max_over_label_fc
class InputsMinMaxOverLabelFc(_Inputs):
    """Intermediate class used to connect user inputs to min_max_over_label_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.min_max.min_max_over_label_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_label = str()
      >>> op.inputs.label.connect(my_label)
    """
    def __init__(self, op: Operator):
        super().__init__(min_max_over_label_fc._spec().inputs, op)
        self._fields_container = Input(min_max_over_label_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._label = Input(min_max_over_label_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._label)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_label_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def label(self):
        """Allows to connect label input to the operator

        - pindoc: label name from the fields container

        Parameters
        ----------
        my_label : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_label_fc()
        >>> op.inputs.label.connect(my_label)
        >>> #or
        >>> op.inputs.label(my_label)

        """
        return self._label

class OutputsMinMaxOverLabelFc(_Outputs):
    """Intermediate class used to get outputs from min_max_over_label_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.min_max.min_max_over_label_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()
      >>> result_domain_ids_min = op.outputs.domain_ids_min()
      >>> result_domain_ids_max = op.outputs.domain_ids_max()
      >>> result_scoping_ids_min = op.outputs.scoping_ids_min()
      >>> result_scoping_ids_max = op.outputs.scoping_ids_max()
    """
    def __init__(self, op: Operator):
        super().__init__(min_max_over_label_fc._spec().outputs, op)
        self._field_min = Output(min_max_over_label_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field_min)
        self._field_max = Output(min_max_over_label_fc._spec().output_pin(1), 1, op) 
        self._outputs.append(self._field_max)
        self._domain_ids_min = Output(min_max_over_label_fc._spec().output_pin(2), 2, op) 
        self._outputs.append(self._domain_ids_min)
        self._domain_ids_max = Output(min_max_over_label_fc._spec().output_pin(3), 3, op) 
        self._outputs.append(self._domain_ids_max)
        self._scoping_ids_min = Output(min_max_over_label_fc._spec().output_pin(4), 4, op) 
        self._outputs.append(self._scoping_ids_min)
        self._scoping_ids_max = Output(min_max_over_label_fc._spec().output_pin(5), 5, op) 
        self._outputs.append(self._scoping_ids_max)

    @property
    def field_min(self):
        """Allows to get field_min output of the operator


        Returns
        ----------
        my_field_min : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_label_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_min = op.outputs.field_min() 
        """
        return self._field_min

    @property
    def field_max(self):
        """Allows to get field_max output of the operator


        Returns
        ----------
        my_field_max : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_label_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_max = op.outputs.field_max() 
        """
        return self._field_max

    @property
    def domain_ids_min(self):
        """Allows to get domain_ids_min output of the operator


        Returns
        ----------
        my_domain_ids_min : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_label_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_domain_ids_min = op.outputs.domain_ids_min() 
        """
        return self._domain_ids_min

    @property
    def domain_ids_max(self):
        """Allows to get domain_ids_max output of the operator


        Returns
        ----------
        my_domain_ids_max : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_label_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_domain_ids_max = op.outputs.domain_ids_max() 
        """
        return self._domain_ids_max

    @property
    def scoping_ids_min(self):
        """Allows to get scoping_ids_min output of the operator


        Returns
        ----------
        my_scoping_ids_min : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_label_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_scoping_ids_min = op.outputs.scoping_ids_min() 
        """
        return self._scoping_ids_min

    @property
    def scoping_ids_max(self):
        """Allows to get scoping_ids_max output of the operator


        Returns
        ----------
        my_scoping_ids_max : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.min_max.min_max_over_label_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_scoping_ids_max = op.outputs.scoping_ids_max() 
        """
        return self._scoping_ids_max

