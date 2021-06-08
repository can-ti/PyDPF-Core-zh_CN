"""
Operator Config
===============
"""

import functools
import grpc
from ansys import dpf
from ansys.grpc.dpf import base_pb2, operator_config_pb2, operator_config_pb2_grpc
from ansys.dpf.core.errors import protect_grpc


class Config:
    """A class used to represent an operator's configuration.
        With configurations the user can optionally choose how the operator will run.
        This is an advanced feature used for deep customization. 
        The different options can change the way loops are done, 
        it can change whether the operator needs to make check on the input or not...
    """
    def __init__(self,operator_name=None, config=None, server=None):
        if server is None:
            server = dpf.core._global_server()

        self._server = server

        self._stub = self._connect()
        
        if config:
            self._message = config
        else:
            self.__send_init_request(operator_name)
        
        if hasattr(self._message, "spec"):
            self._config_help=self._message.spec
        
        opt = self.options
        for name in opt : 
            bound_method = self.config_option_value.__get__(self, self.__class__)
            method2 = functools.partial(bound_method,
                                        config_name=name)
            setattr(self, "get_"+name+"_option", method2)
            
            bound_method = self.__set_config_option__.__get__(self, self.__class__)
            method2 = functools.partial(bound_method,
                                        config_name=name)
            setattr(self, "set_"+name+"_option", method2)
        
    def _connect(self):
        """Connect to the grpc service"""
        return operator_config_pb2_grpc.OperatorConfigServiceStub(self._server.channel)


    @protect_grpc
    def __send_init_request(self, operator_name=None):
        request = operator_config_pb2.CreateRequest()
        if operator_name:
            request.operator_name.operator_name = operator_name
        self._message = self._stub.Create(request)
    
    @property
    def options(self):
        """Returns a list of the different config options and their values"""
        tmp= self._stub.List(self._message)
        out ={}
        for opt in tmp.options:
            out[opt.option_name]=opt.value_str
        return out
    
    
    
    def __set_config_option__(self,config_value, config_name):
        """Change the value of a config option

        Parameters
        ----------
        config_name : str
            Name of the config option to change

        config_value : bool, int, float
            The value to give to this config option
        """
        request = operator_config_pb2.UpdateRequest()
        request.config.CopyFrom(self._message)
        option_request = operator_config_pb2.ConfigOption()
        option_request.option_name = config_name
        if isinstance(config_value, bool):
            option_request.bool = config_value
        elif isinstance(config_value, int):
            option_request.int = config_value
        elif isinstance(config_value, float):
            option_request.double = config_value
        else:
            raise TypeError("str, int, float are the accepted type for config options")            
        
        request.options.extend([option_request])
        self._stub.Update(request)
        
        
    def set_config_option(self, config_name, config_value):
        """Change the value of a config option

        Parameters
        ----------
        config_name : str
            Name of the config option to change

        config_value : bool, int, float
            The value to give to this config option
        """
        return self.__set_config_option__(config_value, config_name)
        
        
    def config_option_value(self, config_name):
        """Description of the given config_name and how it impacts the operator
        
        Parameters
        ----------
        config_name : str
            Name of the config option to change
            
        Returns
        ----------
        value : str
        """
        opt = self.options
        if config_name in opt:
            return opt[config_name]
        else:
            raise KeyError(f"{config_name} option doesn't exist")
            
        
    def __try_get_option__(self,config_name):
        if self._config_help:
            for option in self._config_help.config_options_spec:
                if option.name==config_name:
                    return option
        return None
    
    
    def config_option_documentation(self, config_name):
        """Description of the given config_name and how it impacts the operator
        
        Parameters
        ----------
        config_name : str
            Name of the config option to change
            
        Returns
        ----------
        documentation : str
        """
        option =self.__try_get_option__(config_name)
        if option:
            return option.document
        return ""
    
    
    def config_option_accepted_types(self, config_name):
        """Description of the given config_name and how it impacts the operator
        
        Parameters
        ----------
        config_name : str
            Name of the config option to change
            
        Returns
        ----------
        types : list str
        """
        if self._config_help:
            for option in self._config_help.config_options_spec:
                if option.name==config_name:
                    return option.type_names
        return ""
    
    def config_option_default_value(self, config_name):
        """Description of the given config_name and how it impacts the operator
        
        Parameters
        ----------
        config_name : str
            Name of the config option to change
            
        Returns
        ----------
        default value : str
        """
        if self._config_help:
            for option in self._config_help.config_options_spec:
                if option.name==config_name:
                    return option.default_value_str
        return ""
    
    
    @property
    def available_config_options(self):
        """Returns the list of available config options for this operator
        
        Returns
        ----------
        types : list str
        """
        tmp= self._stub.List(self._message)
        out =[]
        for opt in tmp.options:
            out.append(opt.option_name)
        return out

    def __str__(self):
        """describe the entity
        
        Returns
        -------
        description : str
        """
        from ansys.dpf.core.core import _description
        return _description(self._message, self._server)
    