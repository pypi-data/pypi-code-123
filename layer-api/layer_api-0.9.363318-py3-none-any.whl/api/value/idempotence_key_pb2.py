# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/value/idempotence_key.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61pi/value/idempotence_key.proto\x12\x03\x61pi\x1a\x17validate/validate.proto\"+\n\x0eIdempotenceKey\x12\x19\n\x05value\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\x80\x01\x42\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_IDEMPOTENCEKEY = DESCRIPTOR.message_types_by_name['IdempotenceKey']
IdempotenceKey = _reflection.GeneratedProtocolMessageType('IdempotenceKey', (_message.Message,), {
  'DESCRIPTOR' : _IDEMPOTENCEKEY,
  '__module__' : 'api.value.idempotence_key_pb2'
  # @@protoc_insertion_point(class_scope:api.IdempotenceKey)
  })
_sym_db.RegisterMessage(IdempotenceKey)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _IDEMPOTENCEKEY.fields_by_name['value']._options = None
  _IDEMPOTENCEKEY.fields_by_name['value']._serialized_options = b'\372B\007r\005\020\001\030\200\001'
  _IDEMPOTENCEKEY._serialized_start=65
  _IDEMPOTENCEKEY._serialized_end=108
# @@protoc_insertion_point(module_scope)
