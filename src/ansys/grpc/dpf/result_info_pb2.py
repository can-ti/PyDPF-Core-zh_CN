# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: result_info.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.available_result_pb2 as available__result__pb2
import ansys.grpc.dpf.cyclic_support_pb2 as cyclic__support__pb2
import ansys.grpc.dpf.support_pb2 as support__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11result_info.proto\x12\x1c\x61nsys.api.dpf.result_info.v0\x1a\nbase.proto\x1a\x16\x61vailable_result.proto\x1a\x14\x63yclic_support.proto\x1a\rsupport.proto\"A\n\nResultInfo\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\"\xc9\x03\n\x12ResultInfoResponse\x12\x41\n\ranalysis_type\x18\x01 \x01(\x0e\x32*.ansys.api.dpf.result_info.v0.AnalysisType\x12?\n\x0cphysics_type\x18\x02 \x01(\x0e\x32).ansys.api.dpf.result_info.v0.PhysicsType\x12\x13\n\x0bunit_system\x18\x03 \x01(\x05\x12\x0f\n\x07nresult\x18\x04 \x01(\x05\x12\x18\n\x10unit_system_name\x18\x05 \x01(\t\x12\x1c\n\x14solver_major_version\x18\x06 \x01(\x05\x12\x1c\n\x14solver_minor_version\x18\x07 \x01(\x05\x12\x13\n\x0bsolver_date\x18\x08 \x01(\x05\x12\x13\n\x0bsolver_time\x18\t \x01(\x05\x12\x11\n\tuser_name\x18\n \x01(\t\x12\x10\n\x08job_name\x18\x0b \x01(\t\x12\x14\n\x0cproduct_name\x18\x0c \x01(\t\x12\x12\n\nmain_title\x18\r \x01(\t\x12:\n\x08\x63yc_info\x18\x0e \x01(\x0b\x32(.ansys.api.dpf.result_info.v0.CyclicInfo\"g\n\x16\x41vailableResultRequest\x12=\n\x0bresult_info\x18\x01 \x01(\x0b\x32(.ansys.api.dpf.result_info.v0.ResultInfo\x12\x0e\n\x06numres\x18\x02 \x01(\x05\"z\n\nCyclicInfo\x12\x12\n\nhas_cyclic\x18\x01 \x01(\x08\x12\x13\n\x0b\x63yclic_type\x18\x02 \x01(\t\x12\x43\n\x0b\x63yc_support\x18\x03 \x01(\x0b\x32..ansys.api.dpf.cyclic_support.v0.CyclicSupport\"s\n\x1aGetStringPropertiesRequest\x12=\n\x0bresult_info\x18\x01 \x01(\x0b\x32(.ansys.api.dpf.result_info.v0.ResultInfo\x12\x16\n\x0eproperty_names\x18\x02 \x03(\t\"\xaf\x01\n\x1bGetStringPropertiesResponse\x12]\n\nproperties\x18\x05 \x03(\x0b\x32I.ansys.api.dpf.result_info.v0.GetStringPropertiesResponse.PropertiesEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe4\x01\n\x1cListQualifiersLabelsResponse\x12i\n\x10qualifier_labels\x18\x01 \x03(\x0b\x32O.ansys.api.dpf.result_info.v0.ListQualifiersLabelsResponse.QualifierLabelsEntry\x1aY\n\x14QualifierLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.ansys.api.dpf.support.v0.Support:\x02\x38\x01\"\\\n\x1bListQualifiersLabelsRequest\x12=\n\x0bresult_info\x18\x01 \x01(\x0b\x32(.ansys.api.dpf.result_info.v0.ResultInfo*\x96\x01\n\x0c\x41nalysisType\x12\n\n\x06STATIC\x10\x00\x12\x0c\n\x08\x42UCKLING\x10\x01\x12\t\n\x05MODAL\x10\x02\x12\x0c\n\x08HARMONIC\x10\x03\x12\x07\n\x03\x43MS\x10\x04\x12\r\n\tTRANSIENT\x10\x05\x12\x08\n\x04MSUP\x10\x06\x12\r\n\tSUBSTRUCT\x10\x07\x12\x0c\n\x08SPECTRUM\x10\x08\x12\x14\n\x10UNKNOWN_ANALYSIS\x10\t*X\n\x0bPhysicsType\x12\x0b\n\x07MECANIC\x10\x00\x12\x0b\n\x07THERMAL\x10\x01\x12\x0c\n\x08MAGNETIC\x10\x02\x12\x0c\n\x08\x45LECTRIC\x10\x03\x12\x13\n\x0fUNKNOWN_PHYSICS\x10\x04\x32\xe6\x04\n\x11ResultInfoService\x12\x62\n\x04List\x12(.ansys.api.dpf.result_info.v0.ResultInfo\x1a\x30.ansys.api.dpf.result_info.v0.ResultInfoResponse\x12\x8d\x01\n\x14ListQualifiersLabels\x12\x39.ansys.api.dpf.result_info.v0.ListQualifiersLabelsRequest\x1a:.ansys.api.dpf.result_info.v0.ListQualifiersLabelsResponse\x12\x8a\x01\n\x13GetStringProperties\x12\x38.ansys.api.dpf.result_info.v0.GetStringPropertiesRequest\x1a\x39.ansys.api.dpf.result_info.v0.GetStringPropertiesResponse\x12~\n\nListResult\x12\x34.ansys.api.dpf.result_info.v0.AvailableResultRequest\x1a:.ansys.api.dpf.available_result.v0.AvailableResultResponse\x12P\n\x06\x44\x65lete\x12(.ansys.api.dpf.result_info.v0.ResultInfo\x1a\x1c.ansys.api.dpf.base.v0.EmptyB\x1e\xaa\x02\x1b\x41nsys.Api.Dpf.ResultInfo.V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'result_info_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\033Ansys.Api.Dpf.ResultInfo.V0'
  _globals['_GETSTRINGPROPERTIESRESPONSE_PROPERTIESENTRY']._options = None
  _globals['_GETSTRINGPROPERTIESRESPONSE_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_LISTQUALIFIERSLABELSRESPONSE_QUALIFIERLABELSENTRY']._options = None
  _globals['_LISTQUALIFIERSLABELSRESPONSE_QUALIFIERLABELSENTRY']._serialized_options = b'8\001'
  _globals['_ANALYSISTYPE']._serialized_start=1501
  _globals['_ANALYSISTYPE']._serialized_end=1651
  _globals['_PHYSICSTYPE']._serialized_start=1653
  _globals['_PHYSICSTYPE']._serialized_end=1741
  _globals['_RESULTINFO']._serialized_start=124
  _globals['_RESULTINFO']._serialized_end=189
  _globals['_RESULTINFORESPONSE']._serialized_start=192
  _globals['_RESULTINFORESPONSE']._serialized_end=649
  _globals['_AVAILABLERESULTREQUEST']._serialized_start=651
  _globals['_AVAILABLERESULTREQUEST']._serialized_end=754
  _globals['_CYCLICINFO']._serialized_start=756
  _globals['_CYCLICINFO']._serialized_end=878
  _globals['_GETSTRINGPROPERTIESREQUEST']._serialized_start=880
  _globals['_GETSTRINGPROPERTIESREQUEST']._serialized_end=995
  _globals['_GETSTRINGPROPERTIESRESPONSE']._serialized_start=998
  _globals['_GETSTRINGPROPERTIESRESPONSE']._serialized_end=1173
  _globals['_GETSTRINGPROPERTIESRESPONSE_PROPERTIESENTRY']._serialized_start=1124
  _globals['_GETSTRINGPROPERTIESRESPONSE_PROPERTIESENTRY']._serialized_end=1173
  _globals['_LISTQUALIFIERSLABELSRESPONSE']._serialized_start=1176
  _globals['_LISTQUALIFIERSLABELSRESPONSE']._serialized_end=1404
  _globals['_LISTQUALIFIERSLABELSRESPONSE_QUALIFIERLABELSENTRY']._serialized_start=1315
  _globals['_LISTQUALIFIERSLABELSRESPONSE_QUALIFIERLABELSENTRY']._serialized_end=1404
  _globals['_LISTQUALIFIERSLABELSREQUEST']._serialized_start=1406
  _globals['_LISTQUALIFIERSLABELSREQUEST']._serialized_end=1498
  _globals['_RESULTINFOSERVICE']._serialized_start=1744
  _globals['_RESULTINFOSERVICE']._serialized_end=2358
# @@protoc_insertion_point(module_scope)
