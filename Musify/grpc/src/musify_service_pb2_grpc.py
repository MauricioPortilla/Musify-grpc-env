# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import musify_service_pb2 as musify__service__pb2


class MusifyServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.upload = channel.stream_unary(
                '/MusifyService/upload',
                request_serializer=musify__service__pb2.SongChunk.SerializeToString,
                response_deserializer=musify__service__pb2.SongStored.FromString,
                )
        self.download = channel.unary_stream(
                '/MusifyService/download',
                request_serializer=musify__service__pb2.SongRequest.SerializeToString,
                response_deserializer=musify__service__pb2.SongChunk.FromString,
                )


class MusifyServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def upload(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def download(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MusifyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'upload': grpc.stream_unary_rpc_method_handler(
                    servicer.upload,
                    request_deserializer=musify__service__pb2.SongChunk.FromString,
                    response_serializer=musify__service__pb2.SongStored.SerializeToString,
            ),
            'download': grpc.unary_stream_rpc_method_handler(
                    servicer.download,
                    request_deserializer=musify__service__pb2.SongRequest.FromString,
                    response_serializer=musify__service__pb2.SongChunk.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MusifyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MusifyService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def upload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/MusifyService/upload',
            musify__service__pb2.SongChunk.SerializeToString,
            musify__service__pb2.SongStored.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def download(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/MusifyService/download',
            musify__service__pb2.SongRequest.SerializeToString,
            musify__service__pb2.SongChunk.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
