# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generic_support.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.field_pb2 as field__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15generic_support.proto\x12 ansys.api.dpf.generic_support.v0\x1a\nbase.proto\x1a\x0b\x66ield.proto\"E\n\x0eGenericSupport\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\"!\n\rCreateRequest\x12\x10\n\x08location\x18\x01 \x01(\t\"\x83\x02\n\rUpdateRequest\x12\x41\n\x07support\x18\x01 \x01(\x0b\x32\x30.ansys.api.dpf.generic_support.v0.GenericSupport\x12Z\n\x0e\x66ield_supports\x18\x02 \x03(\x0b\x32\x42.ansys.api.dpf.generic_support.v0.UpdateRequest.FieldSupportsEntry\x1aS\n\x12\x46ieldSupportsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field:\x02\x38\x01\x32\xdd\x01\n\x15GenericSupportService\x12k\n\x06\x43reate\x12/.ansys.api.dpf.generic_support.v0.CreateRequest\x1a\x30.ansys.api.dpf.generic_support.v0.GenericSupport\x12W\n\x06Update\x12/.ansys.api.dpf.generic_support.v0.UpdateRequest\x1a\x1c.ansys.api.dpf.base.v0.EmptyB\"\xaa\x02\x1f\x41nsys.Api.Dpf.GenericSupport.v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generic_support_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\037Ansys.Api.Dpf.GenericSupport.v0'
  _globals['_UPDATEREQUEST_FIELDSUPPORTSENTRY']._options = None
  _globals['_UPDATEREQUEST_FIELDSUPPORTSENTRY']._serialized_options = b'8\001'
  _globals['_GENERICSUPPORT']._serialized_start=84
  _globals['_GENERICSUPPORT']._serialized_end=153
  _globals['_CREATEREQUEST']._serialized_start=155
  _globals['_CREATEREQUEST']._serialized_end=188
  _globals['_UPDATEREQUEST']._serialized_start=191
  _globals['_UPDATEREQUEST']._serialized_end=450
  _globals['_UPDATEREQUEST_FIELDSUPPORTSENTRY']._serialized_start=367
  _globals['_UPDATEREQUEST_FIELDSUPPORTSENTRY']._serialized_end=450
  _globals['_GENERICSUPPORTSERVICE']._serialized_start=453
  _globals['_GENERICSUPPORTSERVICE']._serialized_end=674
# @@protoc_insertion_point(module_scope)
