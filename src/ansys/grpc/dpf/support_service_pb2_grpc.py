# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ansys.grpc.dpf.support_pb2 as support__pb2
import ansys.grpc.dpf.support_service_pb2 as support__service__pb2


class SupportServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSupport = channel.unary_unary(
                '/ansys.api.dpf.support_service.v0.SupportService/GetSupport',
                request_serializer=support__pb2.Support.SerializeToString,
                response_deserializer=support__service__pb2.SupportResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/ansys.api.dpf.support_service.v0.SupportService/List',
                request_serializer=support__service__pb2.ListRequest.SerializeToString,
                response_deserializer=support__service__pb2.ListResponse.FromString,
                )


class SupportServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSupport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SupportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSupport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSupport,
                    request_deserializer=support__pb2.Support.FromString,
                    response_serializer=support__service__pb2.SupportResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=support__service__pb2.ListRequest.FromString,
                    response_serializer=support__service__pb2.ListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ansys.api.dpf.support_service.v0.SupportService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SupportService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSupport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.support_service.v0.SupportService/GetSupport',
            support__pb2.Support.SerializeToString,
            support__service__pb2.SupportResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.support_service.v0.SupportService/List',
            support__service__pb2.ListRequest.SerializeToString,
            support__service__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)