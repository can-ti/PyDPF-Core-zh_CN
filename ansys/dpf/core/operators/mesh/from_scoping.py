"""
from_scoping
============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "mesh" category
"""

class from_scoping(Operator):
    """Extracts a meshed region from an other meshed region base on a scoping

      available inputs:
        - scoping (Scoping)
        - inclusive (int) (optional)
        - mesh (MeshedRegion)

      available outputs:
        - mesh (MeshedRegion)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.from_scoping()

      >>> # Make input connections
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_inclusive = int()
      >>> op.inputs.inclusive.connect(my_inclusive)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.from_scoping(scoping=my_scoping,inclusive=my_inclusive,mesh=my_mesh)

      >>> # Get output data
      >>> result_mesh = op.outputs.mesh()"""
    def __init__(self, scoping=None, inclusive=None, mesh=None, config=None, server=None):
        super().__init__(name="mesh::by_scoping", config = config, server = server)
        self._inputs = InputsFromScoping(self)
        self._outputs = OutputsFromScoping(self)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if inclusive !=None:
            self.inputs.inclusive.connect(inclusive)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extracts a meshed region from an other meshed region base on a scoping""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "scoping", type_names=["scoping"], optional=False, document="""if nodal scoping, then the scoping is transposed respecting the inclusive pin"""), 
                                 2 : PinSpecification(name = "inclusive", type_names=["int32"], optional=True, document="""if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh::by_scoping")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFromScoping 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFromScoping 
        """
        return super().outputs


#internal name: mesh::by_scoping
#scripting name: from_scoping
class InputsFromScoping(_Inputs):
    """Intermediate class used to connect user inputs to from_scoping operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.from_scoping()
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_inclusive = int()
      >>> op.inputs.inclusive.connect(my_inclusive)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(from_scoping._spec().inputs, op)
        self._scoping = Input(from_scoping._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._scoping)
        self._inclusive = Input(from_scoping._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._inclusive)
        self._mesh = Input(from_scoping._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator

        - pindoc: if nodal scoping, then the scoping is transposed respecting the inclusive pin

        Parameters
        ----------
        my_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.from_scoping()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> #or
        >>> op.inputs.scoping(my_scoping)

        """
        return self._scoping

    @property
    def inclusive(self):
        """Allows to connect inclusive input to the operator

        - pindoc: if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included

        Parameters
        ----------
        my_inclusive : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.from_scoping()
        >>> op.inputs.inclusive.connect(my_inclusive)
        >>> #or
        >>> op.inputs.inclusive(my_inclusive)

        """
        return self._inclusive

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.from_scoping()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsFromScoping(_Outputs):
    """Intermediate class used to get outputs from from_scoping operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.from_scoping()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh = op.outputs.mesh()
    """
    def __init__(self, op: Operator):
        super().__init__(from_scoping._spec().outputs, op)
        self._mesh = Output(from_scoping._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mesh)

    @property
    def mesh(self):
        """Allows to get mesh output of the operator


        Returns
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.from_scoping()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh() 
        """
        return self._mesh

