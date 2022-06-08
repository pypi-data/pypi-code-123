# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resource.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from . import provider_pb2 as provider__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eresource.proto\x12\tpulumirpc\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0eprovider.proto\"$\n\x16SupportsFeatureRequest\x12\n\n\x02id\x18\x01 \x01(\t\"-\n\x17SupportsFeatureResponse\x12\x12\n\nhasSupport\x18\x01 \x01(\x08\"\xb0\x02\n\x13ReadResourceRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12+\n\nproperties\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x14\n\x0c\x64\x65pendencies\x18\x06 \x03(\t\x12\x10\n\x08provider\x18\x07 \x01(\t\x12\x0f\n\x07version\x18\x08 \x01(\t\x12\x15\n\racceptSecrets\x18\t \x01(\x08\x12\x1f\n\x17\x61\x64\x64itionalSecretOutputs\x18\n \x03(\t\x12\x0f\n\x07\x61liases\x18\x0b \x03(\t\x12\x17\n\x0f\x61\x63\x63\x65ptResources\x18\x0c \x01(\x08\x12\x19\n\x11pluginDownloadURL\x18\r \x01(\t\"P\n\x14ReadResourceResponse\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x8d\x08\n\x17RegisterResourceRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06parent\x18\x03 \x01(\t\x12\x0e\n\x06\x63ustom\x18\x04 \x01(\x08\x12\'\n\x06object\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07protect\x18\x06 \x01(\x08\x12\x14\n\x0c\x64\x65pendencies\x18\x07 \x03(\t\x12\x10\n\x08provider\x18\x08 \x01(\t\x12Z\n\x14propertyDependencies\x18\t \x03(\x0b\x32<.pulumirpc.RegisterResourceRequest.PropertyDependenciesEntry\x12\x1b\n\x13\x64\x65leteBeforeReplace\x18\n \x01(\x08\x12\x0f\n\x07version\x18\x0b \x01(\t\x12\x15\n\rignoreChanges\x18\x0c \x03(\t\x12\x15\n\racceptSecrets\x18\r \x01(\x08\x12\x1f\n\x17\x61\x64\x64itionalSecretOutputs\x18\x0e \x03(\t\x12\x0f\n\x07\x61liases\x18\x0f \x03(\t\x12\x10\n\x08importId\x18\x10 \x01(\t\x12I\n\x0e\x63ustomTimeouts\x18\x11 \x01(\x0b\x32\x31.pulumirpc.RegisterResourceRequest.CustomTimeouts\x12\"\n\x1a\x64\x65leteBeforeReplaceDefined\x18\x12 \x01(\x08\x12\x1d\n\x15supportsPartialValues\x18\x13 \x01(\x08\x12\x0e\n\x06remote\x18\x14 \x01(\x08\x12\x17\n\x0f\x61\x63\x63\x65ptResources\x18\x15 \x01(\x08\x12\x44\n\tproviders\x18\x16 \x03(\x0b\x32\x31.pulumirpc.RegisterResourceRequest.ProvidersEntry\x12\x18\n\x10replaceOnChanges\x18\x17 \x03(\t\x12\x19\n\x11pluginDownloadURL\x18\x18 \x01(\t\x12\x16\n\x0eretainOnDelete\x18\x19 \x01(\x08\x1a$\n\x14PropertyDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1a@\n\x0e\x43ustomTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06update\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x03 \x01(\t\x1at\n\x19PropertyDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x37.pulumirpc.RegisterResourceRequest.PropertyDependencies:\x02\x38\x01\x1a\x30\n\x0eProvidersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf7\x02\n\x18RegisterResourceResponse\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\'\n\x06object\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06stable\x18\x04 \x01(\x08\x12\x0f\n\x07stables\x18\x05 \x03(\t\x12[\n\x14propertyDependencies\x18\x06 \x03(\x0b\x32=.pulumirpc.RegisterResourceResponse.PropertyDependenciesEntry\x1a$\n\x14PropertyDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1au\n\x19PropertyDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x38.pulumirpc.RegisterResourceResponse.PropertyDependencies:\x02\x38\x01\"W\n\x1eRegisterResourceOutputsRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12(\n\x07outputs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xa2\x01\n\x15ResourceInvokeRequest\x12\x0b\n\x03tok\x18\x01 \x01(\t\x12%\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ptResources\x18\x05 \x01(\x08\x12\x19\n\x11pluginDownloadURL\x18\x06 \x01(\t2\xd4\x04\n\x0fResourceMonitor\x12Z\n\x0fSupportsFeature\x12!.pulumirpc.SupportsFeatureRequest\x1a\".pulumirpc.SupportsFeatureResponse\"\x00\x12G\n\x06Invoke\x12 .pulumirpc.ResourceInvokeRequest\x1a\x19.pulumirpc.InvokeResponse\"\x00\x12O\n\x0cStreamInvoke\x12 .pulumirpc.ResourceInvokeRequest\x1a\x19.pulumirpc.InvokeResponse\"\x00\x30\x01\x12\x39\n\x04\x43\x61ll\x12\x16.pulumirpc.CallRequest\x1a\x17.pulumirpc.CallResponse\"\x00\x12Q\n\x0cReadResource\x12\x1e.pulumirpc.ReadResourceRequest\x1a\x1f.pulumirpc.ReadResourceResponse\"\x00\x12]\n\x10RegisterResource\x12\".pulumirpc.RegisterResourceRequest\x1a#.pulumirpc.RegisterResourceResponse\"\x00\x12^\n\x17RegisterResourceOutputs\x12).pulumirpc.RegisterResourceOutputsRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')



_SUPPORTSFEATUREREQUEST = DESCRIPTOR.message_types_by_name['SupportsFeatureRequest']
_SUPPORTSFEATURERESPONSE = DESCRIPTOR.message_types_by_name['SupportsFeatureResponse']
_READRESOURCEREQUEST = DESCRIPTOR.message_types_by_name['ReadResourceRequest']
_READRESOURCERESPONSE = DESCRIPTOR.message_types_by_name['ReadResourceResponse']
_REGISTERRESOURCEREQUEST = DESCRIPTOR.message_types_by_name['RegisterResourceRequest']
_REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIES = _REGISTERRESOURCEREQUEST.nested_types_by_name['PropertyDependencies']
_REGISTERRESOURCEREQUEST_CUSTOMTIMEOUTS = _REGISTERRESOURCEREQUEST.nested_types_by_name['CustomTimeouts']
_REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY = _REGISTERRESOURCEREQUEST.nested_types_by_name['PropertyDependenciesEntry']
_REGISTERRESOURCEREQUEST_PROVIDERSENTRY = _REGISTERRESOURCEREQUEST.nested_types_by_name['ProvidersEntry']
_REGISTERRESOURCERESPONSE = DESCRIPTOR.message_types_by_name['RegisterResourceResponse']
_REGISTERRESOURCERESPONSE_PROPERTYDEPENDENCIES = _REGISTERRESOURCERESPONSE.nested_types_by_name['PropertyDependencies']
_REGISTERRESOURCERESPONSE_PROPERTYDEPENDENCIESENTRY = _REGISTERRESOURCERESPONSE.nested_types_by_name['PropertyDependenciesEntry']
_REGISTERRESOURCEOUTPUTSREQUEST = DESCRIPTOR.message_types_by_name['RegisterResourceOutputsRequest']
_RESOURCEINVOKEREQUEST = DESCRIPTOR.message_types_by_name['ResourceInvokeRequest']
SupportsFeatureRequest = _reflection.GeneratedProtocolMessageType('SupportsFeatureRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTSFEATUREREQUEST,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.SupportsFeatureRequest)
  })
_sym_db.RegisterMessage(SupportsFeatureRequest)

SupportsFeatureResponse = _reflection.GeneratedProtocolMessageType('SupportsFeatureResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTSFEATURERESPONSE,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.SupportsFeatureResponse)
  })
_sym_db.RegisterMessage(SupportsFeatureResponse)

ReadResourceRequest = _reflection.GeneratedProtocolMessageType('ReadResourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _READRESOURCEREQUEST,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ReadResourceRequest)
  })
_sym_db.RegisterMessage(ReadResourceRequest)

ReadResourceResponse = _reflection.GeneratedProtocolMessageType('ReadResourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _READRESOURCERESPONSE,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ReadResourceResponse)
  })
_sym_db.RegisterMessage(ReadResourceResponse)

RegisterResourceRequest = _reflection.GeneratedProtocolMessageType('RegisterResourceRequest', (_message.Message,), {

  'PropertyDependencies' : _reflection.GeneratedProtocolMessageType('PropertyDependencies', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIES,
    '__module__' : 'resource_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceRequest.PropertyDependencies)
    })
  ,

  'CustomTimeouts' : _reflection.GeneratedProtocolMessageType('CustomTimeouts', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERRESOURCEREQUEST_CUSTOMTIMEOUTS,
    '__module__' : 'resource_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceRequest.CustomTimeouts)
    })
  ,

  'PropertyDependenciesEntry' : _reflection.GeneratedProtocolMessageType('PropertyDependenciesEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY,
    '__module__' : 'resource_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceRequest.PropertyDependenciesEntry)
    })
  ,

  'ProvidersEntry' : _reflection.GeneratedProtocolMessageType('ProvidersEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERRESOURCEREQUEST_PROVIDERSENTRY,
    '__module__' : 'resource_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceRequest.ProvidersEntry)
    })
  ,
  'DESCRIPTOR' : _REGISTERRESOURCEREQUEST,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceRequest)
  })
_sym_db.RegisterMessage(RegisterResourceRequest)
_sym_db.RegisterMessage(RegisterResourceRequest.PropertyDependencies)
_sym_db.RegisterMessage(RegisterResourceRequest.CustomTimeouts)
_sym_db.RegisterMessage(RegisterResourceRequest.PropertyDependenciesEntry)
_sym_db.RegisterMessage(RegisterResourceRequest.ProvidersEntry)

RegisterResourceResponse = _reflection.GeneratedProtocolMessageType('RegisterResourceResponse', (_message.Message,), {

  'PropertyDependencies' : _reflection.GeneratedProtocolMessageType('PropertyDependencies', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERRESOURCERESPONSE_PROPERTYDEPENDENCIES,
    '__module__' : 'resource_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceResponse.PropertyDependencies)
    })
  ,

  'PropertyDependenciesEntry' : _reflection.GeneratedProtocolMessageType('PropertyDependenciesEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERRESOURCERESPONSE_PROPERTYDEPENDENCIESENTRY,
    '__module__' : 'resource_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceResponse.PropertyDependenciesEntry)
    })
  ,
  'DESCRIPTOR' : _REGISTERRESOURCERESPONSE,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceResponse)
  })
_sym_db.RegisterMessage(RegisterResourceResponse)
_sym_db.RegisterMessage(RegisterResourceResponse.PropertyDependencies)
_sym_db.RegisterMessage(RegisterResourceResponse.PropertyDependenciesEntry)

RegisterResourceOutputsRequest = _reflection.GeneratedProtocolMessageType('RegisterResourceOutputsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESOURCEOUTPUTSREQUEST,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceOutputsRequest)
  })
_sym_db.RegisterMessage(RegisterResourceOutputsRequest)

ResourceInvokeRequest = _reflection.GeneratedProtocolMessageType('ResourceInvokeRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEINVOKEREQUEST,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ResourceInvokeRequest)
  })
_sym_db.RegisterMessage(ResourceInvokeRequest)

_RESOURCEMONITOR = DESCRIPTOR.services_by_name['ResourceMonitor']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY._options = None
  _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY._serialized_options = b'8\001'
  _REGISTERRESOURCEREQUEST_PROVIDERSENTRY._options = None
  _REGISTERRESOURCEREQUEST_PROVIDERSENTRY._serialized_options = b'8\001'
  _REGISTERRESOURCERESPONSE_PROPERTYDEPENDENCIESENTRY._options = None
  _REGISTERRESOURCERESPONSE_PROPERTYDEPENDENCIESENTRY._serialized_options = b'8\001'
  _SUPPORTSFEATUREREQUEST._serialized_start=104
  _SUPPORTSFEATUREREQUEST._serialized_end=140
  _SUPPORTSFEATURERESPONSE._serialized_start=142
  _SUPPORTSFEATURERESPONSE._serialized_end=187
  _READRESOURCEREQUEST._serialized_start=190
  _READRESOURCEREQUEST._serialized_end=494
  _READRESOURCERESPONSE._serialized_start=496
  _READRESOURCERESPONSE._serialized_end=576
  _REGISTERRESOURCEREQUEST._serialized_start=579
  _REGISTERRESOURCEREQUEST._serialized_end=1616
  _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIES._serialized_start=1346
  _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIES._serialized_end=1382
  _REGISTERRESOURCEREQUEST_CUSTOMTIMEOUTS._serialized_start=1384
  _REGISTERRESOURCEREQUEST_CUSTOMTIMEOUTS._serialized_end=1448
  _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY._serialized_start=1450
  _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY._serialized_end=1566
  _REGISTERRESOURCEREQUEST_PROVIDERSENTRY._serialized_start=1568
  _REGISTERRESOURCEREQUEST_PROVIDERSENTRY._serialized_end=1616
  _REGISTERRESOURCERESPONSE._serialized_start=1619
  _REGISTERRESOURCERESPONSE._serialized_end=1994
  _REGISTERRESOURCERESPONSE_PROPERTYDEPENDENCIES._serialized_start=1346
  _REGISTERRESOURCERESPONSE_PROPERTYDEPENDENCIES._serialized_end=1382
  _REGISTERRESOURCERESPONSE_PROPERTYDEPENDENCIESENTRY._serialized_start=1877
  _REGISTERRESOURCERESPONSE_PROPERTYDEPENDENCIESENTRY._serialized_end=1994
  _REGISTERRESOURCEOUTPUTSREQUEST._serialized_start=1996
  _REGISTERRESOURCEOUTPUTSREQUEST._serialized_end=2083
  _RESOURCEINVOKEREQUEST._serialized_start=2086
  _RESOURCEINVOKEREQUEST._serialized_end=2248
  _RESOURCEMONITOR._serialized_start=2251
  _RESOURCEMONITOR._serialized_end=2847
# @@protoc_insertion_point(module_scope)
