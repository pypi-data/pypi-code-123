# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/value/dataset_stats.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/value/dataset_stats.proto\x12\x03\x61pi\"\xd8\x05\n\x0c\x44\x61tasetStats\x12\x11\n\trow_count\x18\x01 \x01(\x03\x12/\n\nhistograms\x18\x02 \x03(\x0b\x32\x1b.api.DatasetStats.Histogram\x12\x15\n\rsize_in_bytes\x18\x03 \x01(\x03\x12)\n\x07\x63olumns\x18\x04 \x03(\x0b\x32\x18.api.DatasetStats.Column\x1a\xea\x01\n\tHistogram\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x33\n\x07\x62uckets\x18\x02 \x03(\x0b\x32\".api.DatasetStats.Histogram.Bucket\x12<\n\x0bpercentiles\x18\x03 \x01(\x0b\x32\'.api.DatasetStats.Histogram.Percentiles\x1a&\n\x06\x42ucket\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x1a\x34\n\x0bPercentiles\x12\x0b\n\x03p25\x18\x19 \x01(\x03\x12\x0b\n\x03p50\x18\x32 \x01(\x03\x12\x0b\n\x03p75\x18K \x01(\x03\x1a\xd4\x02\n\x06\x43olumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nnull_count\x18\x02 \x01(\x03\x12\x16\n\x0enot_null_count\x18\x03 \x01(\x03\x12+\n\x03min\x18\x04 \x01(\x0b\x32\x1e.api.DatasetStats.Column.Value\x12+\n\x03max\x18\x05 \x01(\x0b\x32\x1e.api.DatasetStats.Column.Value\x12,\n\x04mean\x18\x06 \x01(\x0b\x32\x1e.api.DatasetStats.Column.Value\x12+\n\x03std\x18\x07 \x01(\x0b\x32\x1e.api.DatasetStats.Column.Value\x12\x1b\n\x13unique_count_approx\x18\x08 \x01(\x03\x1a>\n\x05Value\x12\x14\n\nlong_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x02 \x01(\x01H\x00\x42\x07\n\x05valueB\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_DATASETSTATS = DESCRIPTOR.message_types_by_name['DatasetStats']
_DATASETSTATS_HISTOGRAM = _DATASETSTATS.nested_types_by_name['Histogram']
_DATASETSTATS_HISTOGRAM_BUCKET = _DATASETSTATS_HISTOGRAM.nested_types_by_name['Bucket']
_DATASETSTATS_HISTOGRAM_PERCENTILES = _DATASETSTATS_HISTOGRAM.nested_types_by_name['Percentiles']
_DATASETSTATS_COLUMN = _DATASETSTATS.nested_types_by_name['Column']
_DATASETSTATS_COLUMN_VALUE = _DATASETSTATS_COLUMN.nested_types_by_name['Value']
DatasetStats = _reflection.GeneratedProtocolMessageType('DatasetStats', (_message.Message,), {

  'Histogram' : _reflection.GeneratedProtocolMessageType('Histogram', (_message.Message,), {

    'Bucket' : _reflection.GeneratedProtocolMessageType('Bucket', (_message.Message,), {
      'DESCRIPTOR' : _DATASETSTATS_HISTOGRAM_BUCKET,
      '__module__' : 'api.value.dataset_stats_pb2'
      # @@protoc_insertion_point(class_scope:api.DatasetStats.Histogram.Bucket)
      })
    ,

    'Percentiles' : _reflection.GeneratedProtocolMessageType('Percentiles', (_message.Message,), {
      'DESCRIPTOR' : _DATASETSTATS_HISTOGRAM_PERCENTILES,
      '__module__' : 'api.value.dataset_stats_pb2'
      # @@protoc_insertion_point(class_scope:api.DatasetStats.Histogram.Percentiles)
      })
    ,
    'DESCRIPTOR' : _DATASETSTATS_HISTOGRAM,
    '__module__' : 'api.value.dataset_stats_pb2'
    # @@protoc_insertion_point(class_scope:api.DatasetStats.Histogram)
    })
  ,

  'Column' : _reflection.GeneratedProtocolMessageType('Column', (_message.Message,), {

    'Value' : _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
      'DESCRIPTOR' : _DATASETSTATS_COLUMN_VALUE,
      '__module__' : 'api.value.dataset_stats_pb2'
      # @@protoc_insertion_point(class_scope:api.DatasetStats.Column.Value)
      })
    ,
    'DESCRIPTOR' : _DATASETSTATS_COLUMN,
    '__module__' : 'api.value.dataset_stats_pb2'
    # @@protoc_insertion_point(class_scope:api.DatasetStats.Column)
    })
  ,
  'DESCRIPTOR' : _DATASETSTATS,
  '__module__' : 'api.value.dataset_stats_pb2'
  # @@protoc_insertion_point(class_scope:api.DatasetStats)
  })
_sym_db.RegisterMessage(DatasetStats)
_sym_db.RegisterMessage(DatasetStats.Histogram)
_sym_db.RegisterMessage(DatasetStats.Histogram.Bucket)
_sym_db.RegisterMessage(DatasetStats.Histogram.Percentiles)
_sym_db.RegisterMessage(DatasetStats.Column)
_sym_db.RegisterMessage(DatasetStats.Column.Value)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _DATASETSTATS._serialized_start=39
  _DATASETSTATS._serialized_end=767
  _DATASETSTATS_HISTOGRAM._serialized_start=190
  _DATASETSTATS_HISTOGRAM._serialized_end=424
  _DATASETSTATS_HISTOGRAM_BUCKET._serialized_start=332
  _DATASETSTATS_HISTOGRAM_BUCKET._serialized_end=370
  _DATASETSTATS_HISTOGRAM_PERCENTILES._serialized_start=372
  _DATASETSTATS_HISTOGRAM_PERCENTILES._serialized_end=424
  _DATASETSTATS_COLUMN._serialized_start=427
  _DATASETSTATS_COLUMN._serialized_end=767
  _DATASETSTATS_COLUMN_VALUE._serialized_start=705
  _DATASETSTATS_COLUMN_VALUE._serialized_end=767
# @@protoc_insertion_point(module_scope)
