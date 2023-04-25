# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\x12\x05users\"\xbb\x01\n\x07request\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x01\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x12\n\npackage_id\x18\x06 \x01(\t\x12\r\n\x05token\x18\x07 \x01(\t\x12\x18\n\x10verificationCode\x18\x08 \x01(\t\x12\x11\n\tdebugInfo\x18\t \x01(\t\x12\x0c\n\x04\x63\x64ma\x18\n \x01(\t\"\xf4\x01\n\x08response\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x01\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x1d\n\x06status\x18\x06 \x01(\x0e\x32\r.users.Status\x12\r\n\x05token\x18\x07 \x01(\t\x12\x1b\n\x05\x65rror\x18\x08 \x01(\x0b\x32\x0c.users.Error\x12\x19\n\x04info\x18\t \x01(\x0b\x32\x0b.users.Info\x12\x1f\n\x07success\x18\n \x01(\x0b\x32\x0e.users.Success\x12\r\n\x05\x61lias\x18\x0b \x01(\t\"?\n\x05\x45rror\x12\x1c\n\x14localizedDescription\x18\x01 \x01(\t\x12\x18\n\x10\x64\x65\x62ugDescription\x18\x02 \x01(\t\"A\n\x07Success\x12\x1c\n\x14localizedDescription\x18\x01 \x01(\t\x12\x18\n\x10\x64\x65\x62ugDescription\x18\x02 \x01(\t\"\x1b\n\x04Info\x12\x13\n\x0binformation\x18\x01 \x01(\t*=\n\x06Status\x12\x0f\n\x0bINFORMATION\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x32\xd3\x01\n\x0buserService\x12\x37\n\x14SendVerificationCode\x12\x0e.users.request\x1a\x0f.users.response\x12+\n\x08Register\x12\x0e.users.request\x1a\x0f.users.response\x12-\n\nGetBalance\x12\x0e.users.request\x1a\x0f.users.response\x12/\n\x0cRegisterCDMA\x12\x0e.users.request\x1a\x0f.users.responseB$Z\"momariserver/services/users/userpbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\"momariserver/services/users/userpb'
  _STATUS._serialized_start=620
  _STATUS._serialized_end=681
  _REQUEST._serialized_start=23
  _REQUEST._serialized_end=210
  _RESPONSE._serialized_start=213
  _RESPONSE._serialized_end=457
  _ERROR._serialized_start=459
  _ERROR._serialized_end=522
  _SUCCESS._serialized_start=524
  _SUCCESS._serialized_end=589
  _INFO._serialized_start=591
  _INFO._serialized_end=618
  _USERSERVICE._serialized_start=684
  _USERSERVICE._serialized_end=895
# @@protoc_insertion_point(module_scope)
