# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: val.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2 as types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tval.proto\x12\x0ckuksa.val.v1\x1a\x0btypes.proto\"c\n\x0c\x45ntryRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12 \n\x04view\x18\x02 \x01(\x0e\x32\x12.kuksa.val.v1.View\x12#\n\x06\x66ields\x18\x03 \x03(\x0e\x32\x13.kuksa.val.v1.Field\"9\n\nGetRequest\x12+\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1a.kuksa.val.v1.EntryRequest\"\x89\x01\n\x0bGetResponse\x12(\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x17.kuksa.val.v1.DataEntry\x12,\n\x06\x65rrors\x18\x02 \x03(\x0b\x32\x1c.kuksa.val.v1.DataEntryError\x12\"\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x13.kuksa.val.v1.Error\"Z\n\x0b\x45ntryUpdate\x12&\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x17.kuksa.val.v1.DataEntry\x12#\n\x06\x66ields\x18\x02 \x03(\x0e\x32\x13.kuksa.val.v1.Field\"8\n\nSetRequest\x12*\n\x07updates\x18\x01 \x03(\x0b\x32\x19.kuksa.val.v1.EntryUpdate\"_\n\x0bSetResponse\x12\"\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x13.kuksa.val.v1.Error\x12,\n\x06\x65rrors\x18\x02 \x03(\x0b\x32\x1c.kuksa.val.v1.DataEntryError\"e\n\x0eSubscribeEntry\x12\x0c\n\x04path\x18\x01 \x01(\t\x12 \n\x04view\x18\x02 \x01(\x0e\x32\x12.kuksa.val.v1.View\x12#\n\x06\x66ields\x18\x03 \x03(\x0e\x32\x13.kuksa.val.v1.Field\"A\n\x10SubscribeRequest\x12-\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1c.kuksa.val.v1.SubscribeEntry\"?\n\x11SubscribeResponse\x12*\n\x07updates\x18\x01 \x03(\x0b\x32\x19.kuksa.val.v1.EntryUpdate\"\x16\n\x14GetServerInfoRequest\"6\n\x15GetServerInfoResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t2\xa7\x02\n\x03VAL\x12:\n\x03Get\x12\x18.kuksa.val.v1.GetRequest\x1a\x19.kuksa.val.v1.GetResponse\x12:\n\x03Set\x12\x18.kuksa.val.v1.SetRequest\x1a\x19.kuksa.val.v1.SetResponse\x12N\n\tSubscribe\x12\x1e.kuksa.val.v1.SubscribeRequest\x1a\x1f.kuksa.val.v1.SubscribeResponse0\x01\x12X\n\rGetServerInfo\x12\".kuksa.val.v1.GetServerInfoRequest\x1a#.kuksa.val.v1.GetServerInfoResponseB\x13Z\x11/kuksa_grpc_protob\x06proto3')



_ENTRYREQUEST = DESCRIPTOR.message_types_by_name['EntryRequest']
_GETREQUEST = DESCRIPTOR.message_types_by_name['GetRequest']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
_ENTRYUPDATE = DESCRIPTOR.message_types_by_name['EntryUpdate']
_SETREQUEST = DESCRIPTOR.message_types_by_name['SetRequest']
_SETRESPONSE = DESCRIPTOR.message_types_by_name['SetResponse']
_SUBSCRIBEENTRY = DESCRIPTOR.message_types_by_name['SubscribeEntry']
_SUBSCRIBEREQUEST = DESCRIPTOR.message_types_by_name['SubscribeRequest']
_SUBSCRIBERESPONSE = DESCRIPTOR.message_types_by_name['SubscribeResponse']
_GETSERVERINFOREQUEST = DESCRIPTOR.message_types_by_name['GetServerInfoRequest']
_GETSERVERINFORESPONSE = DESCRIPTOR.message_types_by_name['GetServerInfoResponse']
EntryRequest = _reflection.GeneratedProtocolMessageType('EntryRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENTRYREQUEST,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.EntryRequest)
  })
_sym_db.RegisterMessage(EntryRequest)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

EntryUpdate = _reflection.GeneratedProtocolMessageType('EntryUpdate', (_message.Message,), {
  'DESCRIPTOR' : _ENTRYUPDATE,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.EntryUpdate)
  })
_sym_db.RegisterMessage(EntryUpdate)

SetRequest = _reflection.GeneratedProtocolMessageType('SetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETREQUEST,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.SetRequest)
  })
_sym_db.RegisterMessage(SetRequest)

SetResponse = _reflection.GeneratedProtocolMessageType('SetResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETRESPONSE,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.SetResponse)
  })
_sym_db.RegisterMessage(SetResponse)

SubscribeEntry = _reflection.GeneratedProtocolMessageType('SubscribeEntry', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEENTRY,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.SubscribeEntry)
  })
_sym_db.RegisterMessage(SubscribeEntry)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

SubscribeResponse = _reflection.GeneratedProtocolMessageType('SubscribeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBERESPONSE,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.SubscribeResponse)
  })
_sym_db.RegisterMessage(SubscribeResponse)

GetServerInfoRequest = _reflection.GeneratedProtocolMessageType('GetServerInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERINFOREQUEST,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.GetServerInfoRequest)
  })
_sym_db.RegisterMessage(GetServerInfoRequest)

GetServerInfoResponse = _reflection.GeneratedProtocolMessageType('GetServerInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERINFORESPONSE,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:kuksa.val.v1.GetServerInfoResponse)
  })
_sym_db.RegisterMessage(GetServerInfoResponse)

_VAL = DESCRIPTOR.services_by_name['VAL']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\021/kuksa_grpc_proto'
  _ENTRYREQUEST._serialized_start=40
  _ENTRYREQUEST._serialized_end=139
  _GETREQUEST._serialized_start=141
  _GETREQUEST._serialized_end=198
  _GETRESPONSE._serialized_start=201
  _GETRESPONSE._serialized_end=338
  _ENTRYUPDATE._serialized_start=340
  _ENTRYUPDATE._serialized_end=430
  _SETREQUEST._serialized_start=432
  _SETREQUEST._serialized_end=488
  _SETRESPONSE._serialized_start=490
  _SETRESPONSE._serialized_end=585
  _SUBSCRIBEENTRY._serialized_start=587
  _SUBSCRIBEENTRY._serialized_end=688
  _SUBSCRIBEREQUEST._serialized_start=690
  _SUBSCRIBEREQUEST._serialized_end=755
  _SUBSCRIBERESPONSE._serialized_start=757
  _SUBSCRIBERESPONSE._serialized_end=820
  _GETSERVERINFOREQUEST._serialized_start=822
  _GETSERVERINFOREQUEST._serialized_end=844
  _GETSERVERINFORESPONSE._serialized_start=846
  _GETSERVERINFORESPONSE._serialized_end=900
  _VAL._serialized_start=903
  _VAL._serialized_end=1198
# @@protoc_insertion_point(module_scope)
