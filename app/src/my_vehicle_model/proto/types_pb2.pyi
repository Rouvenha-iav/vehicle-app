"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
I added V1 as in databroker. Is this good practice?"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DataType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DataTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DataType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DATA_TYPE_UNSPECIFIED: _DataType.ValueType  # 0
    DATA_TYPE_STRING: _DataType.ValueType  # 1
    DATA_TYPE_BOOLEAN: _DataType.ValueType  # 2
    DATA_TYPE_INT8: _DataType.ValueType  # 3
    DATA_TYPE_INT16: _DataType.ValueType  # 4
    DATA_TYPE_INT32: _DataType.ValueType  # 5
    DATA_TYPE_INT64: _DataType.ValueType  # 6
    DATA_TYPE_UINT8: _DataType.ValueType  # 7
    DATA_TYPE_UINT16: _DataType.ValueType  # 8
    DATA_TYPE_UINT32: _DataType.ValueType  # 9
    DATA_TYPE_UINT64: _DataType.ValueType  # 10
    DATA_TYPE_FLOAT: _DataType.ValueType  # 11
    DATA_TYPE_DOUBLE: _DataType.ValueType  # 12
    DATA_TYPE_TIMESTAMP: _DataType.ValueType  # 13
    DATA_TYPE_STRING_ARRAY: _DataType.ValueType  # 20
    DATA_TYPE_BOOLEAN_ARRAY: _DataType.ValueType  # 21
    DATA_TYPE_INT8_ARRAY: _DataType.ValueType  # 22
    DATA_TYPE_INT16_ARRAY: _DataType.ValueType  # 23
    DATA_TYPE_INT32_ARRAY: _DataType.ValueType  # 24
    DATA_TYPE_INT64_ARRAY: _DataType.ValueType  # 25
    DATA_TYPE_UINT8_ARRAY: _DataType.ValueType  # 26
    DATA_TYPE_UINT16_ARRAY: _DataType.ValueType  # 27
    DATA_TYPE_UINT32_ARRAY: _DataType.ValueType  # 28
    DATA_TYPE_UINT64_ARRAY: _DataType.ValueType  # 29
    DATA_TYPE_FLOAT_ARRAY: _DataType.ValueType  # 30
    DATA_TYPE_DOUBLE_ARRAY: _DataType.ValueType  # 31
    DATA_TYPE_TIMESTAMP_ARRAY: _DataType.ValueType  # 32

class DataType(_DataType, metaclass=_DataTypeEnumTypeWrapper):
    """VSS Data type of a signal

    Protobuf doesn't support int8, int16, uint8 or uint16.
    These are mapped to int32 and uint32 respectively.
    """

DATA_TYPE_UNSPECIFIED: DataType.ValueType  # 0
DATA_TYPE_STRING: DataType.ValueType  # 1
DATA_TYPE_BOOLEAN: DataType.ValueType  # 2
DATA_TYPE_INT8: DataType.ValueType  # 3
DATA_TYPE_INT16: DataType.ValueType  # 4
DATA_TYPE_INT32: DataType.ValueType  # 5
DATA_TYPE_INT64: DataType.ValueType  # 6
DATA_TYPE_UINT8: DataType.ValueType  # 7
DATA_TYPE_UINT16: DataType.ValueType  # 8
DATA_TYPE_UINT32: DataType.ValueType  # 9
DATA_TYPE_UINT64: DataType.ValueType  # 10
DATA_TYPE_FLOAT: DataType.ValueType  # 11
DATA_TYPE_DOUBLE: DataType.ValueType  # 12
DATA_TYPE_TIMESTAMP: DataType.ValueType  # 13
DATA_TYPE_STRING_ARRAY: DataType.ValueType  # 20
DATA_TYPE_BOOLEAN_ARRAY: DataType.ValueType  # 21
DATA_TYPE_INT8_ARRAY: DataType.ValueType  # 22
DATA_TYPE_INT16_ARRAY: DataType.ValueType  # 23
DATA_TYPE_INT32_ARRAY: DataType.ValueType  # 24
DATA_TYPE_INT64_ARRAY: DataType.ValueType  # 25
DATA_TYPE_UINT8_ARRAY: DataType.ValueType  # 26
DATA_TYPE_UINT16_ARRAY: DataType.ValueType  # 27
DATA_TYPE_UINT32_ARRAY: DataType.ValueType  # 28
DATA_TYPE_UINT64_ARRAY: DataType.ValueType  # 29
DATA_TYPE_FLOAT_ARRAY: DataType.ValueType  # 30
DATA_TYPE_DOUBLE_ARRAY: DataType.ValueType  # 31
DATA_TYPE_TIMESTAMP_ARRAY: DataType.ValueType  # 32
global___DataType = DataType

class _EntryType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EntryTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EntryType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ENTRY_TYPE_UNSPECIFIED: _EntryType.ValueType  # 0
    ENTRY_TYPE_ATTRIBUTE: _EntryType.ValueType  # 1
    ENTRY_TYPE_SENSOR: _EntryType.ValueType  # 2
    ENTRY_TYPE_ACTUATOR: _EntryType.ValueType  # 3

class EntryType(_EntryType, metaclass=_EntryTypeEnumTypeWrapper):
    """Entry type"""

ENTRY_TYPE_UNSPECIFIED: EntryType.ValueType  # 0
ENTRY_TYPE_ATTRIBUTE: EntryType.ValueType  # 1
ENTRY_TYPE_SENSOR: EntryType.ValueType  # 2
ENTRY_TYPE_ACTUATOR: EntryType.ValueType  # 3
global___EntryType = EntryType

class _View:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ViewEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_View.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VIEW_UNSPECIFIED: _View.ValueType  # 0
    """Unspecified. Equivalent to VIEW_CURRENT_VALUE unless `fields` are explicitly set."""
    VIEW_CURRENT_VALUE: _View.ValueType  # 1
    """Populate DataEntry with value."""
    VIEW_TARGET_VALUE: _View.ValueType  # 2
    """Populate DataEntry with actuator target."""
    VIEW_METADATA: _View.ValueType  # 3
    """Populate DataEntry with metadata."""
    VIEW_FIELDS: _View.ValueType  # 10
    """Populate DataEntry only with requested fields."""
    VIEW_ALL: _View.ValueType  # 20
    """Populate DataEntry with everything."""

class View(_View, metaclass=_ViewEnumTypeWrapper):
    """A `View` specifies a set of fields which should
    be populated in a `DataEntry` (in a response message)
    """

VIEW_UNSPECIFIED: View.ValueType  # 0
"""Unspecified. Equivalent to VIEW_CURRENT_VALUE unless `fields` are explicitly set."""
VIEW_CURRENT_VALUE: View.ValueType  # 1
"""Populate DataEntry with value."""
VIEW_TARGET_VALUE: View.ValueType  # 2
"""Populate DataEntry with actuator target."""
VIEW_METADATA: View.ValueType  # 3
"""Populate DataEntry with metadata."""
VIEW_FIELDS: View.ValueType  # 10
"""Populate DataEntry only with requested fields."""
VIEW_ALL: View.ValueType  # 20
"""Populate DataEntry with everything."""
global___View = View

class _Field:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Field.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FIELD_UNSPECIFIED: _Field.ValueType  # 0
    """"*" i.e. everything"""
    FIELD_PATH: _Field.ValueType  # 1
    """path"""
    FIELD_VALUE: _Field.ValueType  # 2
    """value"""
    FIELD_ACTUATOR_TARGET: _Field.ValueType  # 3
    """actuator_target"""
    FIELD_METADATA: _Field.ValueType  # 10
    """metadata.*"""
    FIELD_METADATA_DATA_TYPE: _Field.ValueType  # 11
    """metadata.data_type"""
    FIELD_METADATA_DESCRIPTION: _Field.ValueType  # 12
    """metadata.description"""
    FIELD_METADATA_ENTRY_TYPE: _Field.ValueType  # 13
    """metadata.entry_type"""
    FIELD_METADATA_COMMENT: _Field.ValueType  # 14
    """metadata.comment"""
    FIELD_METADATA_DEPRECATION: _Field.ValueType  # 15
    """metadata.deprecation"""
    FIELD_METADATA_UNIT: _Field.ValueType  # 16
    """metadata.unit"""
    FIELD_METADATA_VALUE_RESTRICTION: _Field.ValueType  # 17
    """metadata.value_restriction.*"""
    FIELD_METADATA_ACTUATOR: _Field.ValueType  # 20
    """metadata.actuator.*"""
    FIELD_METADATA_SENSOR: _Field.ValueType  # 30
    """metadata.sensor.*"""
    FIELD_METADATA_ATTRIBUTE: _Field.ValueType  # 40
    """metadata.attribute.*"""

class Field(_Field, metaclass=_FieldEnumTypeWrapper):
    """A `Field` corresponds to a specific field of a `DataEntry`.

    It can be used to:
      * populate only specific fields of a `DataEntry` response.
      * specify which fields of a `DataEntry` should be set as
        part of a `Set` request.
      * subscribe to only specific fields of a data entry.
      * convey which fields of an updated `DataEntry` have changed.
    """

FIELD_UNSPECIFIED: Field.ValueType  # 0
""""*" i.e. everything"""
FIELD_PATH: Field.ValueType  # 1
"""path"""
FIELD_VALUE: Field.ValueType  # 2
"""value"""
FIELD_ACTUATOR_TARGET: Field.ValueType  # 3
"""actuator_target"""
FIELD_METADATA: Field.ValueType  # 10
"""metadata.*"""
FIELD_METADATA_DATA_TYPE: Field.ValueType  # 11
"""metadata.data_type"""
FIELD_METADATA_DESCRIPTION: Field.ValueType  # 12
"""metadata.description"""
FIELD_METADATA_ENTRY_TYPE: Field.ValueType  # 13
"""metadata.entry_type"""
FIELD_METADATA_COMMENT: Field.ValueType  # 14
"""metadata.comment"""
FIELD_METADATA_DEPRECATION: Field.ValueType  # 15
"""metadata.deprecation"""
FIELD_METADATA_UNIT: Field.ValueType  # 16
"""metadata.unit"""
FIELD_METADATA_VALUE_RESTRICTION: Field.ValueType  # 17
"""metadata.value_restriction.*"""
FIELD_METADATA_ACTUATOR: Field.ValueType  # 20
"""metadata.actuator.*"""
FIELD_METADATA_SENSOR: Field.ValueType  # 30
"""metadata.sensor.*"""
FIELD_METADATA_ATTRIBUTE: Field.ValueType  # 40
"""metadata.attribute.*"""
global___Field = Field

class DataEntry(google.protobuf.message.Message):
    """Describes a VSS entry
    When requesting an entry, the amount of information returned can
    be controlled by specifying either a `View` or a set of `Field`s.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    ACTUATOR_TARGET_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    path: builtins.str
    """Defines the full VSS path of the entry.
    [field: FIELD_PATH]
    """
    @property
    def value(self) -> global___Datapoint:
        """The value (datapoint)
        [field: FIELD_VALUE]
        """
    @property
    def actuator_target(self) -> global___Datapoint:
        """Actuator target (only used if the entry is an actuator)
        [field: FIELD_ACTUATOR_TARGET]
        """
    @property
    def metadata(self) -> global___Metadata:
        """Metadata for this entry
        [field: FIELD_METADATA]
        """
    def __init__(
        self,
        *,
        path: builtins.str = ...,
        value: global___Datapoint | None = ...,
        actuator_target: global___Datapoint | None = ...,
        metadata: global___Metadata | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["actuator_target", b"actuator_target", "metadata", b"metadata", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["actuator_target", b"actuator_target", "metadata", b"metadata", "path", b"path", "value", b"value"]) -> None: ...

global___DataEntry = DataEntry

class Datapoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    BOOL_FIELD_NUMBER: builtins.int
    INT32_FIELD_NUMBER: builtins.int
    INT64_FIELD_NUMBER: builtins.int
    UINT32_FIELD_NUMBER: builtins.int
    UINT64_FIELD_NUMBER: builtins.int
    FLOAT_FIELD_NUMBER: builtins.int
    DOUBLE_FIELD_NUMBER: builtins.int
    STRING_ARRAY_FIELD_NUMBER: builtins.int
    BOOL_ARRAY_FIELD_NUMBER: builtins.int
    INT32_ARRAY_FIELD_NUMBER: builtins.int
    INT64_ARRAY_FIELD_NUMBER: builtins.int
    UINT32_ARRAY_FIELD_NUMBER: builtins.int
    UINT64_ARRAY_FIELD_NUMBER: builtins.int
    FLOAT_ARRAY_FIELD_NUMBER: builtins.int
    DOUBLE_ARRAY_FIELD_NUMBER: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    string: builtins.str
    bool: builtins.bool
    int32: builtins.int
    int64: builtins.int
    uint32: builtins.int
    uint64: builtins.int
    float: builtins.float
    double: builtins.float
    @property
    def string_array(self) -> global___StringArray: ...
    @property
    def bool_array(self) -> global___BoolArray: ...
    @property
    def int32_array(self) -> global___Int32Array: ...
    @property
    def int64_array(self) -> global___Int64Array: ...
    @property
    def uint32_array(self) -> global___Uint32Array: ...
    @property
    def uint64_array(self) -> global___Uint64Array: ...
    @property
    def float_array(self) -> global___FloatArray: ...
    @property
    def double_array(self) -> global___DoubleArray: ...
    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        string: builtins.str = ...,
        bool: builtins.bool = ...,
        int32: builtins.int = ...,
        int64: builtins.int = ...,
        uint32: builtins.int = ...,
        uint64: builtins.int = ...,
        float: builtins.float = ...,
        double: builtins.float = ...,
        string_array: global___StringArray | None = ...,
        bool_array: global___BoolArray | None = ...,
        int32_array: global___Int32Array | None = ...,
        int64_array: global___Int64Array | None = ...,
        uint32_array: global___Uint32Array | None = ...,
        uint64_array: global___Uint64Array | None = ...,
        float_array: global___FloatArray | None = ...,
        double_array: global___DoubleArray | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bool", b"bool", "bool_array", b"bool_array", "double", b"double", "double_array", b"double_array", "float", b"float", "float_array", b"float_array", "int32", b"int32", "int32_array", b"int32_array", "int64", b"int64", "int64_array", b"int64_array", "string", b"string", "string_array", b"string_array", "timestamp", b"timestamp", "uint32", b"uint32", "uint32_array", b"uint32_array", "uint64", b"uint64", "uint64_array", b"uint64_array", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bool", b"bool", "bool_array", b"bool_array", "double", b"double", "double_array", b"double_array", "float", b"float", "float_array", b"float_array", "int32", b"int32", "int32_array", b"int32_array", "int64", b"int64", "int64_array", b"int64_array", "string", b"string", "string_array", b"string_array", "timestamp", b"timestamp", "uint32", b"uint32", "uint32_array", b"uint32_array", "uint64", b"uint64", "uint64_array", b"uint64_array", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value", b"value"]) -> typing_extensions.Literal["string", "bool", "int32", "int64", "uint32", "uint64", "float", "double", "string_array", "bool_array", "int32_array", "int64_array", "uint32_array", "uint64_array", "float_array", "double_array"] | None: ...

global___Datapoint = Datapoint

class Metadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_TYPE_FIELD_NUMBER: builtins.int
    ENTRY_TYPE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    COMMENT_FIELD_NUMBER: builtins.int
    DEPRECATION_FIELD_NUMBER: builtins.int
    UNIT_FIELD_NUMBER: builtins.int
    VALUE_RESTRICTION_FIELD_NUMBER: builtins.int
    ACTUATOR_FIELD_NUMBER: builtins.int
    SENSOR_FIELD_NUMBER: builtins.int
    ATTRIBUTE_FIELD_NUMBER: builtins.int
    data_type: global___DataType.ValueType
    """Data type
    The VSS data type of the entry (i.e. the value, min, max etc).

    NOTE: protobuf doesn't have int8, int16, uint8 or uint16 which means
    that these values must be serialized as int32 and uint32 respectively.
    [field: FIELD_METADATA_DATA_TYPE]
    """
    entry_type: global___EntryType.ValueType
    """Entry type
    [field: FIELD_METADATA_ENTRY_TYPE]
    """
    description: builtins.str
    """Description
    Describes the meaning and content of the entry.
    [field: FIELD_METADATA_DESCRIPTION]
    """
    comment: builtins.str
    """Comment [optional]
    A comment can be used to provide additional informal information
    on a entry.
    [field: FIELD_METADATA_COMMENT]
    """
    deprecation: builtins.str
    """Deprecation [optional]
    Whether this entry is deprecated. Can contain recommendations of what
    to use instead.
    [field: FIELD_METADATA_DEPRECATION]
    """
    unit: builtins.str
    """Unit [optional]
    The unit of measurement
    [field: FIELD_METADATA_UNIT]
    """
    @property
    def value_restriction(self) -> global___ValueRestriction:
        """Value restrictions [optional]
        Restrict which values are allowed.
        Only restrictions matching the DataType {datatype} above are valid.
        [field: FIELD_METADATA_VALUE_RESTRICTION]
        """
    @property
    def actuator(self) -> global___Actuator:
        """[field: FIELD_METADATA_ACTUATOR]"""
    @property
    def sensor(self) -> global___Sensor:
        """[field: FIELD_METADATA_SENSOR]"""
    @property
    def attribute(self) -> global___Attribute:
        """[field: FIELD_METADATA_ATTRIBUTE]"""
    def __init__(
        self,
        *,
        data_type: global___DataType.ValueType = ...,
        entry_type: global___EntryType.ValueType = ...,
        description: builtins.str | None = ...,
        comment: builtins.str | None = ...,
        deprecation: builtins.str | None = ...,
        unit: builtins.str | None = ...,
        value_restriction: global___ValueRestriction | None = ...,
        actuator: global___Actuator | None = ...,
        sensor: global___Sensor | None = ...,
        attribute: global___Attribute | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_comment", b"_comment", "_deprecation", b"_deprecation", "_description", b"_description", "_unit", b"_unit", "actuator", b"actuator", "attribute", b"attribute", "comment", b"comment", "deprecation", b"deprecation", "description", b"description", "entry_specific", b"entry_specific", "sensor", b"sensor", "unit", b"unit", "value_restriction", b"value_restriction"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_comment", b"_comment", "_deprecation", b"_deprecation", "_description", b"_description", "_unit", b"_unit", "actuator", b"actuator", "attribute", b"attribute", "comment", b"comment", "data_type", b"data_type", "deprecation", b"deprecation", "description", b"description", "entry_specific", b"entry_specific", "entry_type", b"entry_type", "sensor", b"sensor", "unit", b"unit", "value_restriction", b"value_restriction"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_comment", b"_comment"]) -> typing_extensions.Literal["comment"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_deprecation", b"_deprecation"]) -> typing_extensions.Literal["deprecation"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_description", b"_description"]) -> typing_extensions.Literal["description"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_unit", b"_unit"]) -> typing_extensions.Literal["unit"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["entry_specific", b"entry_specific"]) -> typing_extensions.Literal["actuator", "sensor", "attribute"] | None: ...

global___Metadata = Metadata

class Actuator(google.protobuf.message.Message):
    """/////////////////////
    Actuator specific fields
    Nothing for now
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Actuator = Actuator

class Sensor(google.protobuf.message.Message):
    """//////////////////////
    Sensor specific
    Nothing for now
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Sensor = Sensor

class Attribute(google.protobuf.message.Message):
    """//////////////////////
    Attribute specific
    Nothing for now.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Attribute = Attribute

class ValueRestriction(google.protobuf.message.Message):
    """Value restriction

    One ValueRestriction{type} for each type, since
    they don't make sense unless the types match
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STRING_FIELD_NUMBER: builtins.int
    SIGNED_FIELD_NUMBER: builtins.int
    UNSIGNED_FIELD_NUMBER: builtins.int
    FLOATING_POINT_FIELD_NUMBER: builtins.int
    @property
    def string(self) -> global___ValueRestrictionString: ...
    @property
    def signed(self) -> global___ValueRestrictionInt:
        """For signed VSS integers"""
    @property
    def unsigned(self) -> global___ValueRestrictionUint:
        """For unsigned VSS integers"""
    @property
    def floating_point(self) -> global___ValueRestrictionFloat:
        """For floating point VSS values (float and double)"""
    def __init__(
        self,
        *,
        string: global___ValueRestrictionString | None = ...,
        signed: global___ValueRestrictionInt | None = ...,
        unsigned: global___ValueRestrictionUint | None = ...,
        floating_point: global___ValueRestrictionFloat | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["floating_point", b"floating_point", "signed", b"signed", "string", b"string", "type", b"type", "unsigned", b"unsigned"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["floating_point", b"floating_point", "signed", b"signed", "string", b"string", "type", b"type", "unsigned", b"unsigned"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["string", "signed", "unsigned", "floating_point"] | None: ...

global___ValueRestriction = ValueRestriction

class ValueRestrictionInt(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MIN_FIELD_NUMBER: builtins.int
    MAX_FIELD_NUMBER: builtins.int
    ALLOWED_VALUES_FIELD_NUMBER: builtins.int
    min: builtins.int
    max: builtins.int
    @property
    def allowed_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        min: builtins.int | None = ...,
        max: builtins.int | None = ...,
        allowed_values: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_max", b"_max", "_min", b"_min", "max", b"max", "min", b"min"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_max", b"_max", "_min", b"_min", "allowed_values", b"allowed_values", "max", b"max", "min", b"min"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_max", b"_max"]) -> typing_extensions.Literal["max"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_min", b"_min"]) -> typing_extensions.Literal["min"] | None: ...

global___ValueRestrictionInt = ValueRestrictionInt

class ValueRestrictionUint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MIN_FIELD_NUMBER: builtins.int
    MAX_FIELD_NUMBER: builtins.int
    ALLOWED_VALUES_FIELD_NUMBER: builtins.int
    min: builtins.int
    max: builtins.int
    @property
    def allowed_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        min: builtins.int | None = ...,
        max: builtins.int | None = ...,
        allowed_values: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_max", b"_max", "_min", b"_min", "max", b"max", "min", b"min"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_max", b"_max", "_min", b"_min", "allowed_values", b"allowed_values", "max", b"max", "min", b"min"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_max", b"_max"]) -> typing_extensions.Literal["max"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_min", b"_min"]) -> typing_extensions.Literal["min"] | None: ...

global___ValueRestrictionUint = ValueRestrictionUint

class ValueRestrictionFloat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MIN_FIELD_NUMBER: builtins.int
    MAX_FIELD_NUMBER: builtins.int
    ALLOWED_VALUES_FIELD_NUMBER: builtins.int
    min: builtins.float
    max: builtins.float
    @property
    def allowed_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """allowed for doubles/floats not recommended"""
    def __init__(
        self,
        *,
        min: builtins.float | None = ...,
        max: builtins.float | None = ...,
        allowed_values: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_max", b"_max", "_min", b"_min", "max", b"max", "min", b"min"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_max", b"_max", "_min", b"_min", "allowed_values", b"allowed_values", "max", b"max", "min", b"min"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_max", b"_max"]) -> typing_extensions.Literal["max"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_min", b"_min"]) -> typing_extensions.Literal["min"] | None: ...

global___ValueRestrictionFloat = ValueRestrictionFloat

class ValueRestrictionString(google.protobuf.message.Message):
    """min, max doesn't make much sense for a string"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALLOWED_VALUES_FIELD_NUMBER: builtins.int
    @property
    def allowed_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        allowed_values: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allowed_values", b"allowed_values"]) -> None: ...

global___ValueRestrictionString = ValueRestrictionString

class Error(google.protobuf.message.Message):
    """Error response shall be an HTTP-like code.
    Should follow https://www.w3.org/TR/viss2-transport/#status-codes.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    code: builtins.int
    reason: builtins.str
    message: builtins.str
    def __init__(
        self,
        *,
        code: builtins.int = ...,
        reason: builtins.str = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "message", b"message", "reason", b"reason"]) -> None: ...

global___Error = Error

class DataEntryError(google.protobuf.message.Message):
    """Used in get/set requests to report errors for specific entries"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    path: builtins.str
    """vss path"""
    @property
    def error(self) -> global___Error: ...
    def __init__(
        self,
        *,
        path: builtins.str = ...,
        error: global___Error | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error", b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error", b"error", "path", b"path"]) -> None: ...

global___DataEntryError = DataEntryError

class StringArray(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values", b"values"]) -> None: ...

global___StringArray = StringArray

class BoolArray(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bool]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[builtins.bool] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values", b"values"]) -> None: ...

global___BoolArray = BoolArray

class Int32Array(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values", b"values"]) -> None: ...

global___Int32Array = Int32Array

class Int64Array(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values", b"values"]) -> None: ...

global___Int64Array = Int64Array

class Uint32Array(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values", b"values"]) -> None: ...

global___Uint32Array = Uint32Array

class Uint64Array(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values", b"values"]) -> None: ...

global___Uint64Array = Uint64Array

class FloatArray(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values", b"values"]) -> None: ...

global___FloatArray = FloatArray

class DoubleArray(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values", b"values"]) -> None: ...

global___DoubleArray = DoubleArray
