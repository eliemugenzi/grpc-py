# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\x12\x04user\"E\n\x08UserData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"\x11\n\x0fGetUsersRequest\"1\n\x10GetUsersResponse\x12\x1d\n\x05users\x18\x01 \x03(\x0b\x32\x0e.user.UserData\" \n\x12GetUserByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"3\n\x13GetUserByIdResponse\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.user.UserData\"1\n\x11\x43reateUserRequest\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.user.UserData\"2\n\x12\x43reateUserResponse\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.user.UserData\"1\n\x11UpdateUserRequest\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.user.UserData\"2\n\x12UpdateUserResponse\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.user.UserData\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"2\n\x12\x44\x65leteUserResponse\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.user.UserData2\xd2\x02\n\x04User\x12;\n\x08GetUsers\x12\x15.user.GetUsersRequest\x1a\x16.user.GetUsersResponse\"\x00\x12\x44\n\x0bGetUserById\x12\x18.user.GetUserByIdRequest\x1a\x19.user.GetUserByIdResponse\"\x00\x12\x41\n\nCreateUser\x12\x17.user.CreateUserRequest\x1a\x18.user.CreateUserResponse\"\x00\x12\x41\n\nUpdateUser\x12\x17.user.UpdateUserRequest\x1a\x18.user.UpdateUserResponse\"\x00\x12\x41\n\nDeleteUser\x12\x17.user.DeleteUserRequest\x1a\x18.user.DeleteUserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USERDATA']._serialized_start=21
  _globals['_USERDATA']._serialized_end=90
  _globals['_GETUSERSREQUEST']._serialized_start=92
  _globals['_GETUSERSREQUEST']._serialized_end=109
  _globals['_GETUSERSRESPONSE']._serialized_start=111
  _globals['_GETUSERSRESPONSE']._serialized_end=160
  _globals['_GETUSERBYIDREQUEST']._serialized_start=162
  _globals['_GETUSERBYIDREQUEST']._serialized_end=194
  _globals['_GETUSERBYIDRESPONSE']._serialized_start=196
  _globals['_GETUSERBYIDRESPONSE']._serialized_end=247
  _globals['_CREATEUSERREQUEST']._serialized_start=249
  _globals['_CREATEUSERREQUEST']._serialized_end=298
  _globals['_CREATEUSERRESPONSE']._serialized_start=300
  _globals['_CREATEUSERRESPONSE']._serialized_end=350
  _globals['_UPDATEUSERREQUEST']._serialized_start=352
  _globals['_UPDATEUSERREQUEST']._serialized_end=401
  _globals['_UPDATEUSERRESPONSE']._serialized_start=403
  _globals['_UPDATEUSERRESPONSE']._serialized_end=453
  _globals['_DELETEUSERREQUEST']._serialized_start=455
  _globals['_DELETEUSERREQUEST']._serialized_end=486
  _globals['_DELETEUSERRESPONSE']._serialized_start=488
  _globals['_DELETEUSERRESPONSE']._serialized_end=538
  _globals['_USER']._serialized_start=541
  _globals['_USER']._serialized_end=879
# @@protoc_insertion_point(module_scope)
