# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: facestyle.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='facestyle.proto',
  package='tutorial',
  serialized_pb='\n\x0f\x66\x61\x63\x65style.proto\x12\x08tutorial\"\x19\n\tFaceStyle\x12\x0c\n\x04name\x18\x01 \x02(\tB\x11\n\x0f\x63om.learn.proto')




_FACESTYLE = _descriptor.Descriptor(
  name='FaceStyle',
  full_name='tutorial.FaceStyle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tutorial.FaceStyle.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=29,
  serialized_end=54,
)

DESCRIPTOR.message_types_by_name['FaceStyle'] = _FACESTYLE

class FaceStyle(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FACESTYLE

  # @@protoc_insertion_point(class_scope:tutorial.FaceStyle)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\017com.learn.proto')
# @@protoc_insertion_point(module_scope)
