# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/type/shared/v1/book.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from systemathics.apis.type.shared.v1 import limit_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_limit__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+systemathics/apis/type/shared/v1/book.proto\x12 systemathics.apis.type.shared.v1\x1a,systemathics/apis/type/shared/v1/limit.proto\"r\n\x04\x42ook\x12\x34\n\x03\x62id\x18\x01 \x03(\x0b\x32\'.systemathics.apis.type.shared.v1.Limit\x12\x34\n\x03\x61sk\x18\x02 \x03(\x0b\x32\'.systemathics.apis.type.shared.v1.Limitb\x06proto3')



_BOOK = DESCRIPTOR.message_types_by_name['Book']
Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'systemathics.apis.type.shared.v1.book_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.type.shared.v1.Book)
  })
_sym_db.RegisterMessage(Book)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=127
  _BOOK._serialized_end=241
# @@protoc_insertion_point(module_scope)
