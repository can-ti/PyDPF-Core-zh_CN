# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.support_pb2 as support__pb2
import ansys.grpc.dpf.time_freq_support_pb2 as time__freq__support__pb2
import ansys.grpc.dpf.scoping_pb2 as scoping__pb2
import ansys.grpc.dpf.label_space_pb2 as label__space__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63ollection.proto\x12\x1b\x61nsys.api.dpf.collection.v0\x1a\x19google/protobuf/any.proto\x1a\nbase.proto\x1a\rsupport.proto\x1a\x17time_freq_support.proto\x1a\rscoping.proto\x1a\x11label_space.proto\"l\n\nCollection\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.ansys.api.dpf.base.v0.Type\">\n\x11\x43ollectionRequest\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.ansys.api.dpf.base.v0.Type\"%\n\x0c\x44\x65\x66\x61ultValue\x12\x15\n\rdefault_value\x18\x01 \x01(\x05\"[\n\x08NewLabel\x12\r\n\x05label\x18\x01 \x01(\t\x12@\n\rdefault_value\x18\x02 \x01(\x0b\x32).ansys.api.dpf.collection.v0.DefaultValue\"\xa2\x01\n\x13UpdateLabelsRequest\x12;\n\ncollection\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.Collection\x12\x35\n\x06labels\x18\x02 \x03(\x0b\x32%.ansys.api.dpf.collection.v0.NewLabel\x12\x17\n\x0foverride_others\x18\x03 \x01(\x08\"\xdd\x01\n\rUpdateRequest\x12;\n\ncollection\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.Collection\x12\x31\n\x05\x65ntry\x18\x02 \x01(\x0b\x32\".ansys.api.dpf.collection.v0.Entry\x12?\n\x0blabel_space\x18\x03 \x01(\x0b\x32(.ansys.api.dpf.label_space.v0.LabelSpaceH\x00\x12\x0f\n\x05index\x18\x04 \x01(\x05H\x00\x42\n\n\x08location\"\xa9\x01\n\x0c\x45ntryRequest\x12;\n\ncollection\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.Collection\x12?\n\x0blabel_space\x18\x03 \x01(\x0b\x32(.ansys.api.dpf.label_space.v0.LabelSpaceH\x00\x12\x0f\n\x05index\x18\x04 \x01(\x05H\x00\x42\n\n\x08location\"\xbb\x01\n\x05\x45ntry\x12(\n\x08\x64pf_type\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x12\n\x08int_type\x18\x02 \x01(\x05H\x00\x12\x15\n\x0b\x64ouble_type\x18\x03 \x01(\x01H\x00\x12\x15\n\x0bstring_type\x18\x04 \x01(\tH\x00\x12=\n\x0blabel_space\x18\x05 \x01(\x0b\x32(.ansys.api.dpf.label_space.v0.LabelSpaceB\x07\n\x05\x65ntry\"I\n\x12GetEntriesResponse\x12\x33\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\".ansys.api.dpf.collection.v0.Entry\"\x18\n\x06Labels\x12\x0e\n\x06labels\x18\x01 \x03(\t\"Z\n\x0cListResponse\x12\x33\n\x06labels\x18\x01 \x01(\x0b\x32#.ansys.api.dpf.collection.v0.Labels\x12\x15\n\rcount_entries\x18\x02 \x01(\x05\"a\n\x13LabelScopingRequest\x12;\n\ncollection\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.Collection\x12\r\n\x05label\x18\x02 \x01(\t\"P\n\x14LabelScopingResponse\x12\x38\n\rlabel_scoping\x18\x01 \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.Scoping\"\x87\x01\n\x0eSupportRequest\x12;\n\ncollection\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.Collection\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.ansys.api.dpf.base.v0.Type\x12\r\n\x05label\x18\x03 \x01(\t\"\xfa\x01\n\x14UpdateSupportRequest\x12;\n\ncollection\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.Collection\x12\r\n\x05label\x18\x02 \x01(\t\x12P\n\x11time_freq_support\x18\x03 \x01(\x0b\x32\x33.ansys.api.dpf.time_freq_support.v0.TimeFreqSupportH\x00\x12\x34\n\x07support\x18\x04 \x01(\x0b\x32!.ansys.api.dpf.support.v0.SupportH\x00\x42\x0e\n\x0csupport_type\"P\n\x11GetAllDataRequest\x12;\n\ncollection\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.Collection\"b\n\x14UpdateAllDataRequest\x12;\n\ncollection\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.Collection\x12\r\n\x05\x61rray\x18\x02 \x01(\x0c\x32\x9d\t\n\x11\x43ollectionService\x12\x61\n\x06\x43reate\x12..ansys.api.dpf.collection.v0.CollectionRequest\x1a\'.ansys.api.dpf.collection.v0.Collection\x12^\n\x0cUpdateLabels\x12\x30.ansys.api.dpf.collection.v0.UpdateLabelsRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12W\n\x0bUpdateEntry\x12*.ansys.api.dpf.collection.v0.UpdateRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12Z\n\x04List\x12\'.ansys.api.dpf.collection.v0.Collection\x1a).ansys.api.dpf.collection.v0.ListResponse\x12h\n\nGetEntries\x12).ansys.api.dpf.collection.v0.EntryRequest\x1a/.ansys.api.dpf.collection.v0.GetEntriesResponse\x12\\\n\nGetSupport\x12+.ansys.api.dpf.collection.v0.SupportRequest\x1a!.ansys.api.dpf.support.v0.Support\x12v\n\x0fGetLabelScoping\x12\x30.ansys.api.dpf.collection.v0.LabelScopingRequest\x1a\x31.ansys.api.dpf.collection.v0.LabelScopingResponse\x12`\n\rUpdateSupport\x12\x31.ansys.api.dpf.collection.v0.UpdateSupportRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12\\\n\nGetAllData\x12..ansys.api.dpf.collection.v0.GetAllDataRequest\x1a\x1c.ansys.api.dpf.base.v0.Array0\x01\x12\x62\n\rUpdateAllData\x12\x31.ansys.api.dpf.collection.v0.UpdateAllDataRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty(\x01\x12[\n\x08\x44\x65scribe\x12&.ansys.api.dpf.base.v0.DescribeRequest\x1a\'.ansys.api.dpf.base.v0.DescribeResponse\x12O\n\x06\x44\x65lete\x12\'.ansys.api.dpf.collection.v0.Collection\x1a\x1c.ansys.api.dpf.base.v0.EmptyB\x1e\xaa\x02\x1b\x41nsys.Api.Dpf.Collection.v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'collection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\033Ansys.Api.Dpf.Collection.v0'
  _globals['_COLLECTION']._serialized_start=162
  _globals['_COLLECTION']._serialized_end=270
  _globals['_COLLECTIONREQUEST']._serialized_start=272
  _globals['_COLLECTIONREQUEST']._serialized_end=334
  _globals['_DEFAULTVALUE']._serialized_start=336
  _globals['_DEFAULTVALUE']._serialized_end=373
  _globals['_NEWLABEL']._serialized_start=375
  _globals['_NEWLABEL']._serialized_end=466
  _globals['_UPDATELABELSREQUEST']._serialized_start=469
  _globals['_UPDATELABELSREQUEST']._serialized_end=631
  _globals['_UPDATEREQUEST']._serialized_start=634
  _globals['_UPDATEREQUEST']._serialized_end=855
  _globals['_ENTRYREQUEST']._serialized_start=858
  _globals['_ENTRYREQUEST']._serialized_end=1027
  _globals['_ENTRY']._serialized_start=1030
  _globals['_ENTRY']._serialized_end=1217
  _globals['_GETENTRIESRESPONSE']._serialized_start=1219
  _globals['_GETENTRIESRESPONSE']._serialized_end=1292
  _globals['_LABELS']._serialized_start=1294
  _globals['_LABELS']._serialized_end=1318
  _globals['_LISTRESPONSE']._serialized_start=1320
  _globals['_LISTRESPONSE']._serialized_end=1410
  _globals['_LABELSCOPINGREQUEST']._serialized_start=1412
  _globals['_LABELSCOPINGREQUEST']._serialized_end=1509
  _globals['_LABELSCOPINGRESPONSE']._serialized_start=1511
  _globals['_LABELSCOPINGRESPONSE']._serialized_end=1591
  _globals['_SUPPORTREQUEST']._serialized_start=1594
  _globals['_SUPPORTREQUEST']._serialized_end=1729
  _globals['_UPDATESUPPORTREQUEST']._serialized_start=1732
  _globals['_UPDATESUPPORTREQUEST']._serialized_end=1982
  _globals['_GETALLDATAREQUEST']._serialized_start=1984
  _globals['_GETALLDATAREQUEST']._serialized_end=2064
  _globals['_UPDATEALLDATAREQUEST']._serialized_start=2066
  _globals['_UPDATEALLDATAREQUEST']._serialized_end=2164
  _globals['_COLLECTIONSERVICE']._serialized_start=2167
  _globals['_COLLECTIONSERVICE']._serialized_end=3348
# @@protoc_insertion_point(module_scope)
