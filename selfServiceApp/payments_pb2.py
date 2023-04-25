# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: payments.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epayments.proto\x12\x08payments\"?\n\x07\x44\x65tails\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x12\n\npurchaseId\x18\x03 \x01(\t\"\xcb\x01\n\x07Payment\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\'\n\x06status\x18\x04 \x01(\x0e\x32\x17.payments.PaymentStatus\x12\'\n\x06method\x18\x05 \x01(\x0e\x32\x17.payments.PaymentMethod\x12\x14\n\x0btransaction\x18\xe6\x07 \x01(\t\x12\x10\n\x07\x63reated\x18\xe7\x07 \x01(\t\x12\x14\n\x0bpaymentType\x18\xe8\x07 \x01(\t\"=\n\x07request\x12\"\n\x07payment\x18\x01 \x01(\x0b\x32\x11.payments.Payment\x12\x0e\n\x06object\x18\x02 \x01(\t\"U\n\x08transfer\x12!\n\x06source\x18\x01 \x01(\x0b\x32\x11.payments.Payment\x12&\n\x0b\x64\x65stination\x18\x02 \x01(\x0b\x32\x11.payments.Payment\"K\n\x04Gift\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x01\"\x82\x01\n\x0binformation\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x04 \x01(\t\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x01\x12\r\n\x05\x65mail\x18\x06 \x01(\t\x12\r\n\x05\x63ount\x18\x07 \x01(\x03\"\x1a\n\x08response\x12\x0e\n\x06result\x18\x01 \x01(\t\"b\n\x07product\x12\x13\n\x0bpackageName\x18\x01 \x01(\t\x12\x11\n\tproductId\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x0e\n\x06\x64omain\x18\x05 \x01(\t\"\x1e\n\x08verified\x12\x12\n\nisVerified\x18\x01 \x01(\x08\"\xe1\x01\n\x08requests\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x01\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x12\n\npackage_id\x18\x06 \x01(\t\x12\r\n\x05token\x18\x07 \x01(\t\x12\x10\n\x08receiver\x18\x08 \x01(\t\x12\x0e\n\x06\x61mount\x18\t \x01(\x01\x12\x12\n\nvoucherPin\x18\n \x01(\t\x12\x11\n\tdebugInfo\x18\x0b \x01(\t\x12\x15\n\rtransactionId\x18\x0c \x01(\t\"\xee\x01\n\x05reply\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x01\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12 \n\x06status\x18\x06 \x01(\x0e\x32\x10.payments.Status\x12\r\n\x05token\x18\x07 \x01(\t\x12\x1e\n\x05\x65rror\x18\x08 \x01(\x0b\x32\x0f.payments.Error\x12\x1c\n\x04info\x18\t \x01(\x0b\x32\x0e.payments.Info\x12\"\n\x07success\x18\n \x01(\x0b\x32\x11.payments.Success\"?\n\x05\x45rror\x12\x1c\n\x14localizedDescription\x18\x01 \x01(\t\x12\x18\n\x10\x64\x65\x62ugDescription\x18\x02 \x01(\t\"A\n\x07Success\x12\x1c\n\x14localizedDescription\x18\x01 \x01(\t\x12\x18\n\x10\x64\x65\x62ugDescription\x18\x02 \x01(\t\"\x1b\n\x04Info\x12\x13\n\x0binformation\x18\x01 \x01(\t*C\n\rPaymentStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0c\n\x08\x44ISPUTED\x10\x03*@\n\rPaymentMethod\x12\n\n\x06PAYPAL\x10\x00\x12\n\n\x06PAYNOW\x10\x01\x12\x0b\n\x07VOUCHER\x10\x02\x12\n\n\x06STRIPE\x10\x03*A\n\x06Status\x12\x0f\n\x0bINFORMATION\x10\x00\x12\x0e\n\nSUCCESSFUL\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x0b\n\x07\x46\x41ILURE\x10\x03\x32\x82\x01\n\x0fpaymentsService\x12\x39\n\x10MasweraseiPayNow\x12\x11.payments.Payment\x1a\x12.payments.response\x12\x34\n\rRedeemVoucher\x12\x12.payments.requests\x1a\x0f.payments.replyB+Z)momariserver/services/payments/paymentspbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'payments_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)momariserver/services/payments/paymentspb'
  _PAYMENTSTATUS._serialized_start=1449
  _PAYMENTSTATUS._serialized_end=1516
  _PAYMENTMETHOD._serialized_start=1518
  _PAYMENTMETHOD._serialized_end=1582
  _STATUS._serialized_start=1584
  _STATUS._serialized_end=1649
  _DETAILS._serialized_start=28
  _DETAILS._serialized_end=91
  _PAYMENT._serialized_start=94
  _PAYMENT._serialized_end=297
  _REQUEST._serialized_start=299
  _REQUEST._serialized_end=360
  _TRANSFER._serialized_start=362
  _TRANSFER._serialized_end=447
  _GIFT._serialized_start=449
  _GIFT._serialized_end=524
  _INFORMATION._serialized_start=527
  _INFORMATION._serialized_end=657
  _RESPONSE._serialized_start=659
  _RESPONSE._serialized_end=685
  _PRODUCT._serialized_start=687
  _PRODUCT._serialized_end=785
  _VERIFIED._serialized_start=787
  _VERIFIED._serialized_end=817
  _REQUESTS._serialized_start=820
  _REQUESTS._serialized_end=1045
  _REPLY._serialized_start=1048
  _REPLY._serialized_end=1286
  _ERROR._serialized_start=1288
  _ERROR._serialized_end=1351
  _SUCCESS._serialized_start=1353
  _SUCCESS._serialized_end=1418
  _INFO._serialized_start=1420
  _INFO._serialized_end=1447
  _PAYMENTSSERVICE._serialized_start=1652
  _PAYMENTSSERVICE._serialized_end=1782
# @@protoc_insertion_point(module_scope)
