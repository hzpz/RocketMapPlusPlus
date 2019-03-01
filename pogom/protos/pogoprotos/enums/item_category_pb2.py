# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/item_category.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/item_category.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$pogoprotos/enums/item_category.proto\x12\x10pogoprotos.enums*\xba\x04\n\x0cItemCategory\x12\x16\n\x12ITEM_CATEGORY_NONE\x10\x00\x12\x1a\n\x16ITEM_CATEGORY_POKEBALL\x10\x01\x12\x16\n\x12ITEM_CATEGORY_FOOD\x10\x02\x12\x1a\n\x16ITEM_CATEGORY_MEDICINE\x10\x03\x12\x17\n\x13ITEM_CATEGORY_BOOST\x10\x04\x12\x1a\n\x16ITEM_CATEGORY_UTILITES\x10\x05\x12\x18\n\x14ITEM_CATEGORY_CAMERA\x10\x06\x12\x16\n\x12ITEM_CATEGORY_DISK\x10\x07\x12\x1b\n\x17ITEM_CATEGORY_INCUBATOR\x10\x08\x12\x19\n\x15ITEM_CATEGORY_INCENSE\x10\t\x12\x1a\n\x16ITEM_CATEGORY_XP_BOOST\x10\n\x12#\n\x1fITEM_CATEGORY_INVENTORY_UPGRADE\x10\x0b\x12\'\n#ITEM_CATEGORY_EVOLUTION_REQUIREMENT\x10\x0c\x12\x1d\n\x19ITEM_CATEGORY_MOVE_REROLL\x10\r\x12\x17\n\x13ITEM_CATEGORY_CANDY\x10\x0e\x12\x1d\n\x19ITEM_CATEGORY_RAID_TICKET\x10\x0f\x12 \n\x1cITEM_CATEGORY_STARDUST_BOOST\x10\x10\x12!\n\x1dITEM_CATEGORY_FRIEND_GIFT_BOX\x10\x11\x12\x1d\n\x19ITEM_CATEGORY_TEAM_CHANGE\x10\x12\x62\x06proto3')
)

_ITEMCATEGORY = _descriptor.EnumDescriptor(
  name='ItemCategory',
  full_name='pogoprotos.enums.ItemCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_POKEBALL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_FOOD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_MEDICINE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_BOOST', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_UTILITES', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_CAMERA', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_DISK', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_INCUBATOR', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_INCENSE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_XP_BOOST', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_INVENTORY_UPGRADE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_EVOLUTION_REQUIREMENT', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_MOVE_REROLL', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_CANDY', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_RAID_TICKET', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_STARDUST_BOOST', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_FRIEND_GIFT_BOX', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_CATEGORY_TEAM_CHANGE', index=18, number=18,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=59,
  serialized_end=629,
)
_sym_db.RegisterEnumDescriptor(_ITEMCATEGORY)

ItemCategory = enum_type_wrapper.EnumTypeWrapper(_ITEMCATEGORY)
ITEM_CATEGORY_NONE = 0
ITEM_CATEGORY_POKEBALL = 1
ITEM_CATEGORY_FOOD = 2
ITEM_CATEGORY_MEDICINE = 3
ITEM_CATEGORY_BOOST = 4
ITEM_CATEGORY_UTILITES = 5
ITEM_CATEGORY_CAMERA = 6
ITEM_CATEGORY_DISK = 7
ITEM_CATEGORY_INCUBATOR = 8
ITEM_CATEGORY_INCENSE = 9
ITEM_CATEGORY_XP_BOOST = 10
ITEM_CATEGORY_INVENTORY_UPGRADE = 11
ITEM_CATEGORY_EVOLUTION_REQUIREMENT = 12
ITEM_CATEGORY_MOVE_REROLL = 13
ITEM_CATEGORY_CANDY = 14
ITEM_CATEGORY_RAID_TICKET = 15
ITEM_CATEGORY_STARDUST_BOOST = 16
ITEM_CATEGORY_FRIEND_GIFT_BOX = 17
ITEM_CATEGORY_TEAM_CHANGE = 18


DESCRIPTOR.enum_types_by_name['ItemCategory'] = _ITEMCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
