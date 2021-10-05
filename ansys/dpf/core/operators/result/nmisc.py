"""
nmisc
=====
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "result" category
"""

class nmisc(Operator):
    """Read NMISC results from the rst file.

      available inputs:
        - time_scoping (Scoping, list) (optional)
        - mesh_scoping (ScopingsContainer, Scoping, list) (optional)
        - fields_container (FieldsContainer) (optional)
        - streams_container (StreamsContainer, Stream) (optional)
        - data_sources (DataSources)
        - mesh (MeshedRegion) (optional)
        - item_index (int)
        - num_components (int) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.nmisc()

      >>> # Make input connections
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.ScopingsContainer()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_item_index = int()
      >>> op.inputs.item_index.connect(my_item_index)
      >>> my_num_components = int()
      >>> op.inputs.num_components.connect(my_num_components)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.nmisc(time_scoping=my_time_scoping,mesh_scoping=my_mesh_scoping,fields_container=my_fields_container,streams_container=my_streams_container,data_sources=my_data_sources,mesh=my_mesh,item_index=my_item_index,num_components=my_num_components)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, time_scoping=None, mesh_scoping=None, fields_container=None, streams_container=None, data_sources=None, mesh=None, item_index=None, num_components=None, config=None, server=None):
        super().__init__(name="mapdl::nmisc", config = config, server = server)
        self._inputs = InputsNmisc(self)
        self._outputs = OutputsNmisc(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if item_index !=None:
            self.inputs.item_index.connect(item_index)
        if num_components !=None:
            self.inputs.num_components.connect(num_components)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read NMISC results from the rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping","vector<int32>"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""FieldsContainer already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container","stream"], optional=True, document="""streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 10 : PinSpecification(name = "item_index", type_names=["int32"], optional=False, document="""Index of requested item."""), 
                                 11 : PinSpecification(name = "num_components", type_names=["int32"], optional=True, document="""Number of components for the requested item.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""FieldsContainer filled in""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::nmisc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNmisc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNmisc 
        """
        return super().outputs


#internal name: mapdl::nmisc
#scripting name: nmisc
class InputsNmisc(_Inputs):
    """Intermediate class used to connect user inputs to nmisc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.nmisc()
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.ScopingsContainer()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_item_index = int()
      >>> op.inputs.item_index.connect(my_item_index)
      >>> my_num_components = int()
      >>> op.inputs.num_components.connect(my_num_components)
    """
    def __init__(self, op: Operator):
        super().__init__(nmisc._spec().inputs, op)
        self._time_scoping = Input(nmisc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(nmisc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._fields_container = Input(nmisc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._fields_container)
        self._streams_container = Input(nmisc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(nmisc._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._mesh = Input(nmisc._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)
        self._item_index = Input(nmisc._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self._item_index)
        self._num_components = Input(nmisc._spec().input_pin(11), 11, op, -1) 
        self._inputs.append(self._num_components)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        Parameters
        ----------
        my_time_scoping : Scoping, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nmisc()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : ScopingsContainer, Scoping, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nmisc()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: FieldsContainer already allocated modified inplace

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nmisc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        - pindoc: streams containing the result file.

        Parameters
        ----------
        my_streams_container : StreamsContainer, Stream, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nmisc()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: data sources containing the result file.

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nmisc()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nmisc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def item_index(self):
        """Allows to connect item_index input to the operator

        - pindoc: Index of requested item.

        Parameters
        ----------
        my_item_index : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nmisc()
        >>> op.inputs.item_index.connect(my_item_index)
        >>> #or
        >>> op.inputs.item_index(my_item_index)

        """
        return self._item_index

    @property
    def num_components(self):
        """Allows to connect num_components input to the operator

        - pindoc: Number of components for the requested item.

        Parameters
        ----------
        my_num_components : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nmisc()
        >>> op.inputs.num_components.connect(my_num_components)
        >>> #or
        >>> op.inputs.num_components(my_num_components)

        """
        return self._num_components

class OutputsNmisc(_Outputs):
    """Intermediate class used to get outputs from nmisc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.nmisc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(nmisc._spec().outputs, op)
        self._fields_container = Output(nmisc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        - pindoc: FieldsContainer filled in

        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.nmisc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

