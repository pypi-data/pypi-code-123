# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.tick.v1 import tick_book_pb2 as systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__book__pb2


class TickBookServiceStub(object):
    """Called to request tick by tick normalized book data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TickBook = channel.unary_stream(
                '/systemathics.apis.services.tick.v1.TickBookService/TickBook',
                request_serializer=systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__book__pb2.TickBookRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__book__pb2.TickBookResponse.FromString,
                )


class TickBookServiceServicer(object):
    """Called to request tick by tick normalized book data.
    """

    def TickBook(self, request, context):
        """Get tick by tick normalized historical book 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TickBookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TickBook': grpc.unary_stream_rpc_method_handler(
                    servicer.TickBook,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__book__pb2.TickBookRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__book__pb2.TickBookResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.tick.v1.TickBookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TickBookService(object):
    """Called to request tick by tick normalized book data.
    """

    @staticmethod
    def TickBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/systemathics.apis.services.tick.v1.TickBookService/TickBook',
            systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__book__pb2.TickBookRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__book__pb2.TickBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
