# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/entity/docker_environment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.api.value import docker_context_pb2 as api_dot_value_dot_docker__context__pb2
from layerapi.api.value import dockerfile_pb2 as api_dot_value_dot_dockerfile__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/entity/docker_environment.proto\x12\x03\x61pi\x1a\x1e\x61pi/value/docker_context.proto\x1a\x1a\x61pi/value/dockerfile.proto\"d\n\x11\x44ockerEnvironment\x12#\n\ndockerfile\x18\x01 \x01(\x0b\x32\x0f.api.Dockerfile\x12*\n\x0e\x64ocker_context\x18\x02 \x01(\x0b\x32\x12.api.DockerContextB\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_DOCKERENVIRONMENT = DESCRIPTOR.message_types_by_name['DockerEnvironment']
DockerEnvironment = _reflection.GeneratedProtocolMessageType('DockerEnvironment', (_message.Message,), {
  'DESCRIPTOR' : _DOCKERENVIRONMENT,
  '__module__' : 'api.entity.docker_environment_pb2'
  # @@protoc_insertion_point(class_scope:api.DockerEnvironment)
  })
_sym_db.RegisterMessage(DockerEnvironment)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _DOCKERENVIRONMENT._serialized_start=104
  _DOCKERENVIRONMENT._serialized_end=204
# @@protoc_insertion_point(module_scope)
