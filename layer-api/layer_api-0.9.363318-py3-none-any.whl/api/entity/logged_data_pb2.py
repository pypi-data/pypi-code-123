# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/entity/logged_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.api.value import logged_data_type_pb2 as api_dot_value_dot_logged__data__type__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/entity/logged_data.proto\x12\x03\x61pi\x1a api/value/logged_data_type.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xba\x02\n\nLoggedData\x12\x12\n\nunique_tag\x18\x01 \x01(\t\x12!\n\x04type\x18\x02 \x01(\x0e\x32\x13.api.LoggedDataType\x12\x30\n\x0c\x63reated_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0cupdated_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x04text\x18\x03 \x01(\tH\x00\x12\r\n\x03url\x18\x04 \x01(\tH\x00\x12\x36\n\x0c\x65poched_data\x18\x07 \x03(\x0b\x32 .api.LoggedData.EpochedDataEntry\x1a\x32\n\x10\x45pochedDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x06\n\x04\x64\x61taB\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_LOGGEDDATA = DESCRIPTOR.message_types_by_name['LoggedData']
_LOGGEDDATA_EPOCHEDDATAENTRY = _LOGGEDDATA.nested_types_by_name['EpochedDataEntry']
LoggedData = _reflection.GeneratedProtocolMessageType('LoggedData', (_message.Message,), {

  'EpochedDataEntry' : _reflection.GeneratedProtocolMessageType('EpochedDataEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOGGEDDATA_EPOCHEDDATAENTRY,
    '__module__' : 'api.entity.logged_data_pb2'
    # @@protoc_insertion_point(class_scope:api.LoggedData.EpochedDataEntry)
    })
  ,
  'DESCRIPTOR' : _LOGGEDDATA,
  '__module__' : 'api.entity.logged_data_pb2'
  # @@protoc_insertion_point(class_scope:api.LoggedData)
  })
_sym_db.RegisterMessage(LoggedData)
_sym_db.RegisterMessage(LoggedData.EpochedDataEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _LOGGEDDATA_EPOCHEDDATAENTRY._options = None
  _LOGGEDDATA_EPOCHEDDATAENTRY._serialized_options = b'8\001'
  _LOGGEDDATA._serialized_start=105
  _LOGGEDDATA._serialized_end=419
  _LOGGEDDATA_EPOCHEDDATAENTRY._serialized_start=361
  _LOGGEDDATA_EPOCHEDDATAENTRY._serialized_end=411
# @@protoc_insertion_point(module_scope)
