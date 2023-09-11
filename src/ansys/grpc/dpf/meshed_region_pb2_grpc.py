# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.field_pb2 as field__pb2
import ansys.grpc.dpf.meshed_region_pb2 as meshed__region__pb2
import ansys.grpc.dpf.scoping_pb2 as scoping__pb2


class MeshedRegionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/Create',
                request_serializer=meshed__region__pb2.CreateRequest.SerializeToString,
                response_deserializer=meshed__region__pb2.MeshedRegion.FromString,
                )
        self.Add = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/Add',
                request_serializer=meshed__region__pb2.AddRequest.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )
        self.GetScoping = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/GetScoping',
                request_serializer=meshed__region__pb2.GetScopingRequest.SerializeToString,
                response_deserializer=scoping__pb2.Scoping.FromString,
                )
        self.SetNamedSelection = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/SetNamedSelection',
                request_serializer=meshed__region__pb2.SetNamedSelectionRequest.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )
        self.SetField = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/SetField',
                request_serializer=meshed__region__pb2.SetFieldRequest.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )
        self.GetElementalProperty = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/GetElementalProperty',
                request_serializer=meshed__region__pb2.ElementalPropertyRequest.SerializeToString,
                response_deserializer=meshed__region__pb2.ElementalPropertyResponse.FromString,
                )
        self.UpdateRequest = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/UpdateRequest',
                request_serializer=meshed__region__pb2.UpdateMeshedRegionRequest.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )
        self.ListProperty = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/ListProperty',
                request_serializer=meshed__region__pb2.ListPropertyRequest.SerializeToString,
                response_deserializer=field__pb2.Field.FromString,
                )
        self.List = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/List',
                request_serializer=meshed__region__pb2.MeshedRegion.SerializeToString,
                response_deserializer=meshed__region__pb2.ListResponse.FromString,
                )
        self.ListNamedSelections = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/ListNamedSelections',
                request_serializer=meshed__region__pb2.ListNamedSelectionsRequest.SerializeToString,
                response_deserializer=meshed__region__pb2.ListNamedSelectionsResponse.FromString,
                )
        self.GetNode = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/GetNode',
                request_serializer=meshed__region__pb2.GetRequest.SerializeToString,
                response_deserializer=meshed__region__pb2.Node.FromString,
                )
        self.GetElement = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/GetElement',
                request_serializer=meshed__region__pb2.GetRequest.SerializeToString,
                response_deserializer=meshed__region__pb2.Element.FromString,
                )
        self.Delete = channel.unary_unary(
                '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/Delete',
                request_serializer=meshed__region__pb2.MeshedRegion.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )


class MeshedRegionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetScoping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetNamedSelection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetField(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetElementalProperty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProperty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNamedSelections(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetElement(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeshedRegionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=meshed__region__pb2.CreateRequest.FromString,
                    response_serializer=meshed__region__pb2.MeshedRegion.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=meshed__region__pb2.AddRequest.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
            'GetScoping': grpc.unary_unary_rpc_method_handler(
                    servicer.GetScoping,
                    request_deserializer=meshed__region__pb2.GetScopingRequest.FromString,
                    response_serializer=scoping__pb2.Scoping.SerializeToString,
            ),
            'SetNamedSelection': grpc.unary_unary_rpc_method_handler(
                    servicer.SetNamedSelection,
                    request_deserializer=meshed__region__pb2.SetNamedSelectionRequest.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
            'SetField': grpc.unary_unary_rpc_method_handler(
                    servicer.SetField,
                    request_deserializer=meshed__region__pb2.SetFieldRequest.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
            'GetElementalProperty': grpc.unary_unary_rpc_method_handler(
                    servicer.GetElementalProperty,
                    request_deserializer=meshed__region__pb2.ElementalPropertyRequest.FromString,
                    response_serializer=meshed__region__pb2.ElementalPropertyResponse.SerializeToString,
            ),
            'UpdateRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRequest,
                    request_deserializer=meshed__region__pb2.UpdateMeshedRegionRequest.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
            'ListProperty': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProperty,
                    request_deserializer=meshed__region__pb2.ListPropertyRequest.FromString,
                    response_serializer=field__pb2.Field.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=meshed__region__pb2.MeshedRegion.FromString,
                    response_serializer=meshed__region__pb2.ListResponse.SerializeToString,
            ),
            'ListNamedSelections': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNamedSelections,
                    request_deserializer=meshed__region__pb2.ListNamedSelectionsRequest.FromString,
                    response_serializer=meshed__region__pb2.ListNamedSelectionsResponse.SerializeToString,
            ),
            'GetNode': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNode,
                    request_deserializer=meshed__region__pb2.GetRequest.FromString,
                    response_serializer=meshed__region__pb2.Node.SerializeToString,
            ),
            'GetElement': grpc.unary_unary_rpc_method_handler(
                    servicer.GetElement,
                    request_deserializer=meshed__region__pb2.GetRequest.FromString,
                    response_serializer=meshed__region__pb2.Element.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=meshed__region__pb2.MeshedRegion.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ansys.api.dpf.meshed_region.v0.MeshedRegionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeshedRegionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/Create',
            meshed__region__pb2.CreateRequest.SerializeToString,
            meshed__region__pb2.MeshedRegion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/Add',
            meshed__region__pb2.AddRequest.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetScoping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/GetScoping',
            meshed__region__pb2.GetScopingRequest.SerializeToString,
            scoping__pb2.Scoping.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetNamedSelection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/SetNamedSelection',
            meshed__region__pb2.SetNamedSelectionRequest.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/SetField',
            meshed__region__pb2.SetFieldRequest.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetElementalProperty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/GetElementalProperty',
            meshed__region__pb2.ElementalPropertyRequest.SerializeToString,
            meshed__region__pb2.ElementalPropertyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/UpdateRequest',
            meshed__region__pb2.UpdateMeshedRegionRequest.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListProperty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/ListProperty',
            meshed__region__pb2.ListPropertyRequest.SerializeToString,
            field__pb2.Field.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/List',
            meshed__region__pb2.MeshedRegion.SerializeToString,
            meshed__region__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNamedSelections(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/ListNamedSelections',
            meshed__region__pb2.ListNamedSelectionsRequest.SerializeToString,
            meshed__region__pb2.ListNamedSelectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/GetNode',
            meshed__region__pb2.GetRequest.SerializeToString,
            meshed__region__pb2.Node.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetElement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/GetElement',
            meshed__region__pb2.GetRequest.SerializeToString,
            meshed__region__pb2.Element.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.meshed_region.v0.MeshedRegionService/Delete',
            meshed__region__pb2.MeshedRegion.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)