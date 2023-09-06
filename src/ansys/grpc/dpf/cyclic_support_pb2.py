# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cyclic_support.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.scoping_pb2 as scoping__pb2
import ansys.grpc.dpf.field_pb2 as field__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63yclic_support.proto\x12\x1f\x61nsys.api.dpf.cyclic_support.v0\x1a\nbase.proto\x1a\rscoping.proto\x1a\x0b\x66ield.proto\"D\n\rCyclicSupport\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\"\xdc\x01\n\x15GetExpandedIdsRequest\x12?\n\x07support\x18\x01 \x01(\x0b\x32..ansys.api.dpf.cyclic_support.v0.CyclicSupport\x12\x11\n\x07node_id\x18\x02 \x01(\x05H\x00\x12\x14\n\nelement_id\x18\x03 \x01(\x05H\x00\x12<\n\x11sectors_to_expand\x18\x04 \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.Scoping\x12\x11\n\tstage_num\x18\x05 \x01(\x05\x42\x08\n\x06\x65ntity\"Q\n\x16GetExpandedIdsResponse\x12\x37\n\x0c\x65xpanded_ids\x18\x01 \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.Scoping\"O\n\x0cGetCSRequest\x12?\n\x07support\x18\x01 \x01(\x0b\x32..ansys.api.dpf.cyclic_support.v0.CyclicSupport\":\n\rGetCSResponse\x12)\n\x02\x63s\x18\x01 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\"c\n\x0cListResponse\x12\x12\n\nnum_stages\x18\x01 \x01(\x05\x12?\n\x0bstage_infos\x18\x02 \x03(\x0b\x32*.ansys.api.dpf.cyclic_support.v0.StageList\"\xcd\x02\n\tStageList\x12\x13\n\x0bnum_sectors\x18\x01 \x01(\x05\x12@\n\x15\x62\x61se_elements_scoping\x18\x02 \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.Scoping\x12=\n\x12\x62\x61se_nodes_scoping\x18\x03 \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.Scoping\x12@\n\x15sectors_for_expansion\x18\x04 \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.Scoping\x12\x33\n\x0chigh_low_map\x18\x05 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12\x33\n\x0clow_high_map\x18\x06 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field2\xc1\x03\n\x14\x43yclicSupportService\x12\x65\n\x04List\x12..ansys.api.dpf.cyclic_support.v0.CyclicSupport\x1a-.ansys.api.dpf.cyclic_support.v0.ListResponse\x12\x81\x01\n\x0eGetExpandedIds\x12\x36.ansys.api.dpf.cyclic_support.v0.GetExpandedIdsRequest\x1a\x37.ansys.api.dpf.cyclic_support.v0.GetExpandedIdsResponse\x12\x66\n\x05GetCS\x12-.ansys.api.dpf.cyclic_support.v0.GetCSRequest\x1a..ansys.api.dpf.cyclic_support.v0.GetCSResponse\x12V\n\x06\x44\x65lete\x12..ansys.api.dpf.cyclic_support.v0.CyclicSupport\x1a\x1c.ansys.api.dpf.base.v0.EmptyB!\xaa\x02\x1e\x41nsys.Api.Dpf.CyclicSupport.V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cyclic_support_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\036Ansys.Api.Dpf.CyclicSupport.V0'
  _globals['_CYCLICSUPPORT']._serialized_start=97
  _globals['_CYCLICSUPPORT']._serialized_end=165
  _globals['_GETEXPANDEDIDSREQUEST']._serialized_start=168
  _globals['_GETEXPANDEDIDSREQUEST']._serialized_end=388
  _globals['_GETEXPANDEDIDSRESPONSE']._serialized_start=390
  _globals['_GETEXPANDEDIDSRESPONSE']._serialized_end=471
  _globals['_GETCSREQUEST']._serialized_start=473
  _globals['_GETCSREQUEST']._serialized_end=552
  _globals['_GETCSRESPONSE']._serialized_start=554
  _globals['_GETCSRESPONSE']._serialized_end=612
  _globals['_LISTRESPONSE']._serialized_start=614
  _globals['_LISTRESPONSE']._serialized_end=713
  _globals['_STAGELIST']._serialized_start=716
  _globals['_STAGELIST']._serialized_end=1049
  _globals['_CYCLICSUPPORTSERVICE']._serialized_start=1052
  _globals['_CYCLICSUPPORTSERVICE']._serialized_end=1501
# @@protoc_insertion_point(module_scope)
