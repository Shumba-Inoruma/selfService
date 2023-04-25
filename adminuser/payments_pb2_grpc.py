# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import payments_pb2 as payments__pb2


class paymentsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MasweraseiPayNow = channel.unary_unary(
                '/payments.paymentsService/MasweraseiPayNow',
                request_serializer=payments__pb2.Payment.SerializeToString,
                response_deserializer=payments__pb2.response.FromString,
                )


class paymentsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MasweraseiPayNow(self, request, context):
        """
        ****** Topup Account ********
        confirm and authorise taura user account topup payment

        RETURNS response.result:
        onSuccess: "success"
        onFailed: "failed" || "payment unsuccessful"(failed to validate payment) || ERROR (+reason)

        FOR MASWERASEI PAYNOW (Endpoind for maswerasei api to retail)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_paymentsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MasweraseiPayNow': grpc.unary_unary_rpc_method_handler(
                    servicer.MasweraseiPayNow,
                    request_deserializer=payments__pb2.Payment.FromString,
                    response_serializer=payments__pb2.response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'payments.paymentsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class paymentsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MasweraseiPayNow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/payments.paymentsService/MasweraseiPayNow',
            payments__pb2.Payment.SerializeToString,
            payments__pb2.response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
