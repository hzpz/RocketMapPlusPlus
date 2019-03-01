# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/onboarding_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import onboarding_event_ids_pb2 as pogoprotos_dot_enums_dot_onboarding__event__ids__pb2
from pogoprotos.enums import onboarding_ar_status_pb2 as pogoprotos_dot_enums_dot_onboarding__ar__status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/onboarding_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n4pogoprotos/data/telemetry/onboarding_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a+pogoprotos/enums/onboarding_event_ids.proto\x1a+pogoprotos/enums/onboarding_ar_status.proto\"\xe8\x01\n\x13OnboardingTelemetry\x12<\n\x0fonboarding_path\x18\x01 \x01(\x0e\x32#.pogoprotos.enums.OnboardingPathIds\x12\x36\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32$.pogoprotos.enums.OnboardingEventIds\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x05\x12\x14\n\x0c\x63onversation\x18\x04 \x01(\t\x12\x37\n\tar_status\x18\x05 \x01(\x0e\x32$.pogoprotos.enums.OnboardingArStatusb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_onboarding__event__ids__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_onboarding__ar__status__pb2.DESCRIPTOR,])




_ONBOARDINGTELEMETRY = _descriptor.Descriptor(
  name='OnboardingTelemetry',
  full_name='pogoprotos.data.telemetry.OnboardingTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='onboarding_path', full_name='pogoprotos.data.telemetry.OnboardingTelemetry.onboarding_path', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='pogoprotos.data.telemetry.OnboardingTelemetry.event_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pogoprotos.data.telemetry.OnboardingTelemetry.data', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversation', full_name='pogoprotos.data.telemetry.OnboardingTelemetry.conversation', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ar_status', full_name='pogoprotos.data.telemetry.OnboardingTelemetry.ar_status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=406,
)

_ONBOARDINGTELEMETRY.fields_by_name['onboarding_path'].enum_type = pogoprotos_dot_enums_dot_onboarding__event__ids__pb2._ONBOARDINGPATHIDS
_ONBOARDINGTELEMETRY.fields_by_name['event_id'].enum_type = pogoprotos_dot_enums_dot_onboarding__event__ids__pb2._ONBOARDINGEVENTIDS
_ONBOARDINGTELEMETRY.fields_by_name['ar_status'].enum_type = pogoprotos_dot_enums_dot_onboarding__ar__status__pb2._ONBOARDINGARSTATUS
DESCRIPTOR.message_types_by_name['OnboardingTelemetry'] = _ONBOARDINGTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OnboardingTelemetry = _reflection.GeneratedProtocolMessageType('OnboardingTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _ONBOARDINGTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.onboarding_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.OnboardingTelemetry)
  ))
_sym_db.RegisterMessage(OnboardingTelemetry)


# @@protoc_insertion_point(module_scope)
