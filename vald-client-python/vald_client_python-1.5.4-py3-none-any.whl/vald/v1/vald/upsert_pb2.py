# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/vald/upsert.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19vald/v1/vald/upsert.proto\x12\x07vald.v1\x1a\x1dvald/v1/payload/payload.proto\x1a\x1cgoogle/api/annotations.proto2\x9f\x02\n\x06Upsert\x12U\n\x06Upsert\x12\x1a.payload.v1.Upsert.Request\x1a\x1b.payload.v1.Object.Location\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/upsert:\x01*\x12S\n\x0cStreamUpsert\x12\x1a.payload.v1.Upsert.Request\x1a!.payload.v1.Object.StreamLocation\"\x00(\x01\x30\x01\x12i\n\x0bMultiUpsert\x12\x1f.payload.v1.Upsert.MultiRequest\x1a\x1c.payload.v1.Object.Locations\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/upsert/multiple:\x01*BS\n\x1aorg.vdaas.vald.api.v1.valdB\nValdUpsertP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/valdb\x06proto3')



_UPSERT = DESCRIPTOR.services_by_name['Upsert']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032org.vdaas.vald.api.v1.valdB\nValdUpsertP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald'
  _UPSERT.methods_by_name['Upsert']._options = None
  _UPSERT.methods_by_name['Upsert']._serialized_options = b'\202\323\344\223\002\014\"\007/upsert:\001*'
  _UPSERT.methods_by_name['MultiUpsert']._options = None
  _UPSERT.methods_by_name['MultiUpsert']._serialized_options = b'\202\323\344\223\002\025\"\020/upsert/multiple:\001*'
  _UPSERT._serialized_start=100
  _UPSERT._serialized_end=387
# @@protoc_insertion_point(module_scope)
