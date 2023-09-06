# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: field.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.scoping_pb2 as scoping__pb2
import ansys.grpc.dpf.field_definition_pb2 as field__definition__pb2
import ansys.grpc.dpf.support_pb2 as support__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x66ield.proto\x12\x16\x61nsys.api.dpf.field.v0\x1a\nbase.proto\x1a\rscoping.proto\x1a\x16\x66ield_definition.proto\x1a\rsupport.proto\"P\n\x14\x43ustomTypeDefinition\x12\x18\n\x10unitary_datatype\x18\x01 \x01(\t\x12\x1e\n\x16num_bytes_unitary_data\x18\x02 \x01(\x05\"\x95\x01\n\x05\x46ield\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\x12\x10\n\x08\x64\x61tatype\x18\x02 \x01(\t\x12\x45\n\x0f\x63ustom_type_def\x18\x03 \x01(\x0b\x32,.ansys.api.dpf.field.v0.CustomTypeDefinition\"\xc5\x02\n\x0c\x46ieldRequest\x12-\n\x06nature\x18\x01 \x01(\x0e\x32\x1d.ansys.api.dpf.base.v0.Nature\x12\x31\n\x08location\x18\x02 \x01(\x0b\x32\x1f.ansys.api.dpf.base.v0.Location\x12/\n\x04size\x18\x03 \x01(\x0b\x32!.ansys.api.dpf.field.v0.FieldSize\x12\x10\n\x08\x64\x61tatype\x18\x04 \x01(\t\x12I\n\x0e\x64imensionality\x18\x05 \x01(\x0b\x32\x31.ansys.api.dpf.field_definition.v0.Dimensionality\x12\x45\n\x0f\x63ustom_type_def\x18\x06 \x01(\x0b\x32,.ansys.api.dpf.field.v0.CustomTypeDefinition\"\x8d\x01\n\x0e\x41\x64\x64\x44\x61taRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12M\n\x13\x65lemdata_containers\x18\x02 \x01(\x0b\x32\x30.ansys.api.dpf.field.v0.ElementaryDataContainers\"x\n\x14UpdateScopingRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12\x32\n\x07scoping\x18\x02 \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.Scoping\"\x93\x01\n\x1cUpdateFieldDefinitionRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12\x45\n\tfield_def\x18\x02 \x01(\x0b\x32\x32.ansys.api.dpf.field_definition.v0.FieldDefinition\"\x9a\x01\n\x1bUpdateElementaryDataRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12M\n\x13\x65lemdata_containers\x18\x02 \x01(\x0b\x32\x30.ansys.api.dpf.field.v0.ElementaryDataContainers\"r\n\x11UpdateSizeRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12/\n\x04size\x18\x02 \x01(\x0b\x32!.ansys.api.dpf.field.v0.FieldSize\"4\n\tFieldSize\x12\x14\n\x0cscoping_size\x18\x01 \x01(\x05\x12\x11\n\tdata_size\x18\x02 \x01(\x05\"\xae\x02\n\x04\x44\x61ta\x12\x39\n\ndatadouble\x18\x02 \x01(\x0b\x32#.ansys.api.dpf.base.v0.DoubleVectorH\x00\x12\x33\n\x07\x64\x61taint\x18\x03 \x01(\x0b\x32 .ansys.api.dpf.base.v0.IntVectorH\x00\x12\x37\n\tdatafloat\x18\x04 \x01(\x0b\x32\".ansys.api.dpf.base.v0.FloatVectorH\x00\x12\x39\n\ndatastring\x18\x01 \x01(\x0b\x32#.ansys.api.dpf.base.v0.StringVectorH\x00\x12\x35\n\x08\x64\x61tabyte\x18\x05 \x01(\x0b\x32!.ansys.api.dpf.base.v0.ByteVectorH\x00\x42\x0b\n\tdatatypes\"q\n\x18\x45lementaryDataContainers\x12\x12\n\nscoping_id\x18\x01 \x01(\x05\x12*\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1c.ansys.api.dpf.field.v0.Data\x12\x15\n\rscoping_index\x18\x03 \x01(\x05\";\n\x0bListRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\":\n\nGetRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\"s\n\x18GetElementaryDataRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12\x0f\n\x05index\x18\x02 \x01(\x05H\x00\x12\x0c\n\x02id\x18\x03 \x01(\x05H\x00\x42\n\n\x08index_id\"\x1d\n\x0cListResponse\x12\r\n\x05\x61rray\x18\x01 \x01(\x0c\"j\n\x19GetElementaryDataResponse\x12M\n\x13\x65lemdata_containers\x18\x01 \x01(\x0b\x32\x30.ansys.api.dpf.field.v0.ElementaryDataContainers\"H\n\x12GetScopingResponse\x12\x32\n\x07scoping\x18\x01 \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.Scoping\"x\n\x1aGetFieldDefinitionResponse\x12L\n\x10\x66ield_definition\x18\x01 \x01(\x0b\x32\x32.ansys.api.dpf.field_definition.v0.FieldDefinition\x12\x0c\n\x04name\x18\x02 \x01(\t\"p\n\x0c\x43ountRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12\x32\n\x06\x65ntity\x18\x02 \x01(\x0e\x32\".ansys.api.dpf.base.v0.CountEntity\"i\n\x0eSupportRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.ansys.api.dpf.base.v0.Type\"u\n\x11SetSupportRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12\x32\n\x07support\x18\x02 \x01(\x0b\x32!.ansys.api.dpf.support.v0.Support\"P\n\x11UpdateDataRequest\x12,\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12\r\n\x05\x61rray\x18\x02 \x01(\x0c\x32\xba\x0c\n\x0c\x46ieldService\x12M\n\x06\x43reate\x12$.ansys.api.dpf.field.v0.FieldRequest\x1a\x1d.ansys.api.dpf.field.v0.Field\x12O\n\x07\x41\x64\x64\x44\x61ta\x12&.ansys.api.dpf.field.v0.AddDataRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12W\n\nUpdateData\x12).ansys.api.dpf.field.v0.UpdateDataRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty(\x01\x12^\n\x11UpdateDataPointer\x12).ansys.api.dpf.field.v0.UpdateDataRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty(\x01\x12[\n\rUpdateScoping\x12,.ansys.api.dpf.field.v0.UpdateScopingRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12U\n\nUpdateSize\x12).ansys.api.dpf.field.v0.UpdateSizeRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12k\n\x15UpdateFieldDefinition\x12\x34.ansys.api.dpf.field.v0.UpdateFieldDefinitionRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12i\n\x14UpdateElementaryData\x12\x33.ansys.api.dpf.field.v0.UpdateElementaryDataRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12S\n\x04List\x12#.ansys.api.dpf.field.v0.ListRequest\x1a$.ansys.api.dpf.field.v0.ListResponse0\x01\x12^\n\x0fListDataPointer\x12#.ansys.api.dpf.field.v0.ListRequest\x1a$.ansys.api.dpf.field.v0.ListResponse0\x01\x12\\\n\nGetScoping\x12\".ansys.api.dpf.field.v0.GetRequest\x1a*.ansys.api.dpf.field.v0.GetScopingResponse\x12W\n\nGetSupport\x12&.ansys.api.dpf.field.v0.SupportRequest\x1a!.ansys.api.dpf.support.v0.Support\x12U\n\nSetSupport\x12).ansys.api.dpf.field.v0.SetSupportRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12l\n\x12GetFieldDefinition\x12\".ansys.api.dpf.field.v0.GetRequest\x1a\x32.ansys.api.dpf.field.v0.GetFieldDefinitionResponse\x12x\n\x11GetElementaryData\x12\x30.ansys.api.dpf.field.v0.GetElementaryDataRequest\x1a\x31.ansys.api.dpf.field.v0.GetElementaryDataResponse\x12S\n\x05\x43ount\x12$.ansys.api.dpf.field.v0.CountRequest\x1a$.ansys.api.dpf.base.v0.CountResponse\x12\x45\n\x06\x44\x65lete\x12\x1d.ansys.api.dpf.field.v0.Field\x1a\x1c.ansys.api.dpf.base.v0.EmptyB\x19\xaa\x02\x16\x41nsys.Api.Dpf.Field.V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'field_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\026Ansys.Api.Dpf.Field.V0'
  _globals['_CUSTOMTYPEDEFINITION']._serialized_start=105
  _globals['_CUSTOMTYPEDEFINITION']._serialized_end=185
  _globals['_FIELD']._serialized_start=188
  _globals['_FIELD']._serialized_end=337
  _globals['_FIELDREQUEST']._serialized_start=340
  _globals['_FIELDREQUEST']._serialized_end=665
  _globals['_ADDDATAREQUEST']._serialized_start=668
  _globals['_ADDDATAREQUEST']._serialized_end=809
  _globals['_UPDATESCOPINGREQUEST']._serialized_start=811
  _globals['_UPDATESCOPINGREQUEST']._serialized_end=931
  _globals['_UPDATEFIELDDEFINITIONREQUEST']._serialized_start=934
  _globals['_UPDATEFIELDDEFINITIONREQUEST']._serialized_end=1081
  _globals['_UPDATEELEMENTARYDATAREQUEST']._serialized_start=1084
  _globals['_UPDATEELEMENTARYDATAREQUEST']._serialized_end=1238
  _globals['_UPDATESIZEREQUEST']._serialized_start=1240
  _globals['_UPDATESIZEREQUEST']._serialized_end=1354
  _globals['_FIELDSIZE']._serialized_start=1356
  _globals['_FIELDSIZE']._serialized_end=1408
  _globals['_DATA']._serialized_start=1411
  _globals['_DATA']._serialized_end=1713
  _globals['_ELEMENTARYDATACONTAINERS']._serialized_start=1715
  _globals['_ELEMENTARYDATACONTAINERS']._serialized_end=1828
  _globals['_LISTREQUEST']._serialized_start=1830
  _globals['_LISTREQUEST']._serialized_end=1889
  _globals['_GETREQUEST']._serialized_start=1891
  _globals['_GETREQUEST']._serialized_end=1949
  _globals['_GETELEMENTARYDATAREQUEST']._serialized_start=1951
  _globals['_GETELEMENTARYDATAREQUEST']._serialized_end=2066
  _globals['_LISTRESPONSE']._serialized_start=2068
  _globals['_LISTRESPONSE']._serialized_end=2097
  _globals['_GETELEMENTARYDATARESPONSE']._serialized_start=2099
  _globals['_GETELEMENTARYDATARESPONSE']._serialized_end=2205
  _globals['_GETSCOPINGRESPONSE']._serialized_start=2207
  _globals['_GETSCOPINGRESPONSE']._serialized_end=2279
  _globals['_GETFIELDDEFINITIONRESPONSE']._serialized_start=2281
  _globals['_GETFIELDDEFINITIONRESPONSE']._serialized_end=2401
  _globals['_COUNTREQUEST']._serialized_start=2403
  _globals['_COUNTREQUEST']._serialized_end=2515
  _globals['_SUPPORTREQUEST']._serialized_start=2517
  _globals['_SUPPORTREQUEST']._serialized_end=2622
  _globals['_SETSUPPORTREQUEST']._serialized_start=2624
  _globals['_SETSUPPORTREQUEST']._serialized_end=2741
  _globals['_UPDATEDATAREQUEST']._serialized_start=2743
  _globals['_UPDATEDATAREQUEST']._serialized_end=2823
  _globals['_FIELDSERVICE']._serialized_start=2826
  _globals['_FIELDSERVICE']._serialized_end=4420
# @@protoc_insertion_point(module_scope)
