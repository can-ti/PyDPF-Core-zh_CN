# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dpf_any.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.dpf_any_message_pb2 as dpf__any__message__pb2
import ansys.grpc.dpf.collection_pb2 as collection__pb2
import ansys.grpc.dpf.field_pb2 as field__pb2
import ansys.grpc.dpf.scoping_pb2 as scoping__pb2
import ansys.grpc.dpf.data_sources_pb2 as data__sources__pb2
import ansys.grpc.dpf.meshed_region_pb2 as meshed__region__pb2
import ansys.grpc.dpf.time_freq_support_pb2 as time__freq__support__pb2
import ansys.grpc.dpf.cyclic_support_pb2 as cyclic__support__pb2
import ansys.grpc.dpf.workflow_message_pb2 as workflow__message__pb2
import ansys.grpc.dpf.result_info_pb2 as result__info__pb2
import ansys.grpc.dpf.operator_pb2 as operator__pb2
import ansys.grpc.dpf.generic_data_container_pb2 as generic__data__container__pb2
import ansys.grpc.dpf.data_tree_pb2 as data__tree__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rdpf_any.proto\x12\x18\x61nsys.api.dpf.dpf_any.v0\x1a\nbase.proto\x1a\x15\x64pf_any_message.proto\x1a\x10\x63ollection.proto\x1a\x0b\x66ield.proto\x1a\rscoping.proto\x1a\x12\x64\x61ta_sources.proto\x1a\x13meshed_region.proto\x1a\x17time_freq_support.proto\x1a\x14\x63yclic_support.proto\x1a\x16workflow_message.proto\x1a\x11result_info.proto\x1a\x0eoperator.proto\x1a\x1cgeneric_data_container.proto\x1a\x0f\x64\x61ta_tree.proto\"$\n\x0cListResponse\x12\x14\n\x0cwrapped_type\x18\x01 \x01(\t\"\\\n\x0bTypeRequest\x12\x35\n\x03\x61ny\x18\x01 \x01(\x0b\x32(.ansys.api.dpf.dpf_any_message.v0.DpfAny\x12\x16\n\x0erequested_type\x18\x02 \x01(\t\"\"\n\x0cTypeResponse\x12\x12\n\nis_type_of\x18\x01 \x01(\x08\"\x9e\x01\n\x0cGetAsRequest\x12\x35\n\x03\x61ny\x18\x01 \x01(\x0b\x32(.ansys.api.dpf.dpf_any_message.v0.DpfAny\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.ansys.api.dpf.base.v0.Type\x12,\n\x07subtype\x18\x03 \x01(\x0e\x32\x1b.ansys.api.dpf.base.v0.Type\"\xf1\x06\n\rGetAsResponse\x12.\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.FieldH\x00\x12=\n\ncollection\x18\x02 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.CollectionH\x00\x12\x34\n\x07scoping\x18\x03 \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.ScopingH\x00\x12\x42\n\x0c\x64\x61ta_sources\x18\x04 \x01(\x0b\x32*.ansys.api.dpf.data_sources.v0.DataSourcesH\x00\x12<\n\x04mesh\x18\x05 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegionH\x00\x12\x45\n\x0b\x63yc_support\x18\x06 \x01(\x0b\x32..ansys.api.dpf.cyclic_support.v0.CyclicSupportH\x00\x12P\n\x11time_freq_support\x18\x07 \x01(\x0b\x32\x33.ansys.api.dpf.time_freq_support.v0.TimeFreqSupportH\x00\x12?\n\x08workflow\x18\x08 \x01(\x0b\x32+.ansys.api.dpf.workflow_message.v0.WorkflowH\x00\x12;\n\x08operator\x18\t \x01(\x0b\x32\'.ansys.api.dpf.dpf_operator.v0.OperatorH\x00\x12?\n\x0bresult_info\x18\n \x01(\x0b\x32(.ansys.api.dpf.result_info.v0.ResultInfoH\x00\x12_\n\x16generic_data_container\x18\x0b \x01(\x0b\x32=.ansys.api.dpf.generic_data_container.v0.GenericDataContainerH\x00\x12\x39\n\tdata_tree\x18\x0f \x01(\x0b\x32$.ansys.api.dpf.data_tree.v0.DataTreeH\x00\x12\x11\n\x07int_val\x18\x0c \x01(\x05H\x00\x12\x14\n\nstring_val\x18\r \x01(\tH\x00\x12\x14\n\ndouble_val\x18\x0e \x01(\x01H\x00\x42\x06\n\x04\x64\x61ta\"\xb8\x01\n\rCreateRequest\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.ansys.api.dpf.base.v0.Type\x12\x35\n\x02id\x18\x02 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifierH\x00\x12\x11\n\x07int_val\x18\x03 \x01(\x05H\x00\x12\x14\n\nstring_val\x18\x04 \x01(\tH\x00\x12\x14\n\ndouble_val\x18\x05 \x01(\x01H\x00\x42\x06\n\x04\x64\x61ta2\xf9\x02\n\rDpfAnyService\x12[\n\x06\x43reate\x12\'.ansys.api.dpf.dpf_any.v0.CreateRequest\x1a(.ansys.api.dpf.dpf_any_message.v0.DpfAny\x12X\n\x04List\x12(.ansys.api.dpf.dpf_any_message.v0.DpfAny\x1a&.ansys.api.dpf.dpf_any.v0.ListResponse\x12W\n\x06IsType\x12%.ansys.api.dpf.dpf_any.v0.TypeRequest\x1a&.ansys.api.dpf.dpf_any.v0.TypeResponse\x12X\n\x05GetAs\x12&.ansys.api.dpf.dpf_any.v0.GetAsRequest\x1a\'.ansys.api.dpf.dpf_any.v0.GetAsResponseB\x1a\xaa\x02\x17\x41nsys.Api.Dpf.DpfAny.V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dpf_any_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\027Ansys.Api.Dpf.DpfAny.V0'
  _globals['_LISTRESPONSE']._serialized_start=318
  _globals['_LISTRESPONSE']._serialized_end=354
  _globals['_TYPEREQUEST']._serialized_start=356
  _globals['_TYPEREQUEST']._serialized_end=448
  _globals['_TYPERESPONSE']._serialized_start=450
  _globals['_TYPERESPONSE']._serialized_end=484
  _globals['_GETASREQUEST']._serialized_start=487
  _globals['_GETASREQUEST']._serialized_end=645
  _globals['_GETASRESPONSE']._serialized_start=648
  _globals['_GETASRESPONSE']._serialized_end=1529
  _globals['_CREATEREQUEST']._serialized_start=1532
  _globals['_CREATEREQUEST']._serialized_end=1716
  _globals['_DPFANYSERVICE']._serialized_start=1719
  _globals['_DPFANYSERVICE']._serialized_end=2096
# @@protoc_insertion_point(module_scope)
