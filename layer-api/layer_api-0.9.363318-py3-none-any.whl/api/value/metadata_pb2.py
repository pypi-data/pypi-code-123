# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/value/metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61pi/value/metadata.proto\x12\x03\x61pi\"a\n\x08Metadata\x12\'\n\x05value\x18\x01 \x03(\x0b\x32\x18.api.Metadata.ValueEntry\x1a,\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_METADATA = DESCRIPTOR.message_types_by_name['Metadata']
_METADATA_VALUEENTRY = _METADATA.nested_types_by_name['ValueEntry']
Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {

  'ValueEntry' : _reflection.GeneratedProtocolMessageType('ValueEntry', (_message.Message,), {
    'DESCRIPTOR' : _METADATA_VALUEENTRY,
    '__module__' : 'api.value.metadata_pb2'
    # @@protoc_insertion_point(class_scope:api.Metadata.ValueEntry)
    })
  ,
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'api.value.metadata_pb2'
  # @@protoc_insertion_point(class_scope:api.Metadata)
  })
_sym_db.RegisterMessage(Metadata)
_sym_db.RegisterMessage(Metadata.ValueEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _METADATA_VALUEENTRY._options = None
  _METADATA_VALUEENTRY._serialized_options = b'8\001'
  _METADATA._serialized_start=33
  _METADATA._serialized_end=130
  _METADATA_VALUEENTRY._serialized_start=86
  _METADATA_VALUEENTRY._serialized_end=130
# @@protoc_insertion_point(module_scope)
