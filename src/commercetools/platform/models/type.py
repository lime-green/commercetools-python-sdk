# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, LocalizedString, ReferenceTypeId

__all__ = [
    "CustomFieldBooleanType",
    "CustomFieldDateTimeType",
    "CustomFieldDateType",
    "CustomFieldEnumType",
    "CustomFieldEnumValue",
    "CustomFieldLocalizedEnumType",
    "CustomFieldLocalizedEnumValue",
    "CustomFieldLocalizedStringType",
    "CustomFieldMoneyType",
    "CustomFieldNumberType",
    "CustomFieldReferenceType",
    "CustomFieldSetType",
    "CustomFieldStringType",
    "CustomFieldTimeType",
    "CustomFields",
    "CustomFieldsDraft",
    "FieldContainer",
    "FieldDefinition",
    "FieldType",
    "ResourceTypeId",
    "Type",
    "TypeAddEnumValueAction",
    "TypeAddFieldDefinitionAction",
    "TypeAddLocalizedEnumValueAction",
    "TypeChangeEnumValueLabelAction",
    "TypeChangeEnumValueOrderAction",
    "TypeChangeFieldDefinitionLabelAction",
    "TypeChangeFieldDefinitionOrderAction",
    "TypeChangeInputHintAction",
    "TypeChangeKeyAction",
    "TypeChangeLabelAction",
    "TypeChangeLocalizedEnumValueLabelAction",
    "TypeChangeLocalizedEnumValueOrderAction",
    "TypeChangeNameAction",
    "TypeDraft",
    "TypePagedQueryResponse",
    "TypeReference",
    "TypeRemoveFieldDefinitionAction",
    "TypeResourceIdentifier",
    "TypeSetDescriptionAction",
    "TypeTextInputHint",
    "TypeUpdate",
    "TypeUpdateAction",
]


class CustomFieldEnumValue(_BaseType):
    key: str
    label: str

    def __init__(self, *, key: str, label: str):
        self.key = key
        self.label = label
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldEnumValue":
        from ._schemas.type import CustomFieldEnumValueSchema

        return CustomFieldEnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldEnumValueSchema

        return CustomFieldEnumValueSchema().dump(self)


class CustomFieldLocalizedEnumValue(_BaseType):
    key: str
    label: "LocalizedString"

    def __init__(self, *, key: str, label: "LocalizedString"):
        self.key = key
        self.label = label
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldLocalizedEnumValue":
        from ._schemas.type import CustomFieldLocalizedEnumValueSchema

        return CustomFieldLocalizedEnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldLocalizedEnumValueSchema

        return CustomFieldLocalizedEnumValueSchema().dump(self)


class CustomFields(_BaseType):
    type: "TypeReference"
    #: A valid JSON object, based on FieldDefinition.
    fields: "FieldContainer"

    def __init__(self, *, type: "TypeReference", fields: "FieldContainer"):
        self.type = type
        self.fields = fields
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFields":
        from ._schemas.type import CustomFieldsSchema

        return CustomFieldsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldsSchema

        return CustomFieldsSchema().dump(self)


class CustomFieldsDraft(_BaseType):
    #: The `id` or the `key` of the type to use.
    type: "TypeResourceIdentifier"
    #: A valid JSON object, based on the FieldDefinitions of the Type.
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: "TypeResourceIdentifier",
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldsDraft":
        from ._schemas.type import CustomFieldsDraftSchema

        return CustomFieldsDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldsDraftSchema

        return CustomFieldsDraftSchema().dump(self)


class FieldContainer(typing.Dict[str, str]):
    pass


class FieldDefinition(_BaseType):
    #: Describes the type of the field.
    type: "FieldType"
    #: The name of the field.
    #: The name must be between two and 36 characters long and can contain the ASCII letters A to Z in lowercase or uppercase, digits, underscores (`_`) and the hyphen-minus (`-`).
    #: The name must be unique for a given resource type ID.
    #: In case there is a field with the same name in another type it has to have the same FieldType also.
    name: str
    #: A human-readable label for the field.
    label: "LocalizedString"
    #: Whether the field is required to have a value.
    required: bool
    #: Provides a visual representation type for this field.
    #: It is only relevant for string-based field types like StringType and LocalizedStringType.
    input_hint: typing.Optional["TypeTextInputHint"]

    def __init__(
        self,
        *,
        type: "FieldType",
        name: str,
        label: "LocalizedString",
        required: bool,
        input_hint: typing.Optional["TypeTextInputHint"] = None
    ):
        self.type = type
        self.name = name
        self.label = label
        self.required = required
        self.input_hint = input_hint
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "FieldDefinition":
        from ._schemas.type import FieldDefinitionSchema

        return FieldDefinitionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import FieldDefinitionSchema

        return FieldDefinitionSchema().dump(self)


class FieldType(_BaseType):
    name: str

    def __init__(self, *, name: str):
        self.name = name
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "FieldType":
        if data["name"] == "Boolean":
            from ._schemas.type import CustomFieldBooleanTypeSchema

            return CustomFieldBooleanTypeSchema().load(data)
        if data["name"] == "DateTime":
            from ._schemas.type import CustomFieldDateTimeTypeSchema

            return CustomFieldDateTimeTypeSchema().load(data)
        if data["name"] == "Date":
            from ._schemas.type import CustomFieldDateTypeSchema

            return CustomFieldDateTypeSchema().load(data)
        if data["name"] == "Enum":
            from ._schemas.type import CustomFieldEnumTypeSchema

            return CustomFieldEnumTypeSchema().load(data)
        if data["name"] == "LocalizedEnum":
            from ._schemas.type import CustomFieldLocalizedEnumTypeSchema

            return CustomFieldLocalizedEnumTypeSchema().load(data)
        if data["name"] == "LocalizedString":
            from ._schemas.type import CustomFieldLocalizedStringTypeSchema

            return CustomFieldLocalizedStringTypeSchema().load(data)
        if data["name"] == "Money":
            from ._schemas.type import CustomFieldMoneyTypeSchema

            return CustomFieldMoneyTypeSchema().load(data)
        if data["name"] == "Number":
            from ._schemas.type import CustomFieldNumberTypeSchema

            return CustomFieldNumberTypeSchema().load(data)
        if data["name"] == "Reference":
            from ._schemas.type import CustomFieldReferenceTypeSchema

            return CustomFieldReferenceTypeSchema().load(data)
        if data["name"] == "Set":
            from ._schemas.type import CustomFieldSetTypeSchema

            return CustomFieldSetTypeSchema().load(data)
        if data["name"] == "String":
            from ._schemas.type import CustomFieldStringTypeSchema

            return CustomFieldStringTypeSchema().load(data)
        if data["name"] == "Time":
            from ._schemas.type import CustomFieldTimeTypeSchema

            return CustomFieldTimeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import FieldTypeSchema

        return FieldTypeSchema().dump(self)


class CustomFieldBooleanType(FieldType):
    def __init__(self):

        super().__init__(name="Boolean")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldBooleanType":
        from ._schemas.type import CustomFieldBooleanTypeSchema

        return CustomFieldBooleanTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldBooleanTypeSchema

        return CustomFieldBooleanTypeSchema().dump(self)


class CustomFieldDateTimeType(FieldType):
    def __init__(self):

        super().__init__(name="DateTime")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldDateTimeType":
        from ._schemas.type import CustomFieldDateTimeTypeSchema

        return CustomFieldDateTimeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldDateTimeTypeSchema

        return CustomFieldDateTimeTypeSchema().dump(self)


class CustomFieldDateType(FieldType):
    def __init__(self):

        super().__init__(name="Date")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldDateType":
        from ._schemas.type import CustomFieldDateTypeSchema

        return CustomFieldDateTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldDateTypeSchema

        return CustomFieldDateTypeSchema().dump(self)


class CustomFieldEnumType(FieldType):
    values: typing.List["CustomFieldEnumValue"]

    def __init__(self, *, values: typing.List["CustomFieldEnumValue"]):
        self.values = values
        super().__init__(name="Enum")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldEnumType":
        from ._schemas.type import CustomFieldEnumTypeSchema

        return CustomFieldEnumTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldEnumTypeSchema

        return CustomFieldEnumTypeSchema().dump(self)


class CustomFieldLocalizedEnumType(FieldType):
    values: typing.List["CustomFieldLocalizedEnumValue"]

    def __init__(self, *, values: typing.List["CustomFieldLocalizedEnumValue"]):
        self.values = values
        super().__init__(name="LocalizedEnum")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldLocalizedEnumType":
        from ._schemas.type import CustomFieldLocalizedEnumTypeSchema

        return CustomFieldLocalizedEnumTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldLocalizedEnumTypeSchema

        return CustomFieldLocalizedEnumTypeSchema().dump(self)


class CustomFieldLocalizedStringType(FieldType):
    def __init__(self):

        super().__init__(name="LocalizedString")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldLocalizedStringType":
        from ._schemas.type import CustomFieldLocalizedStringTypeSchema

        return CustomFieldLocalizedStringTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldLocalizedStringTypeSchema

        return CustomFieldLocalizedStringTypeSchema().dump(self)


class CustomFieldMoneyType(FieldType):
    def __init__(self):

        super().__init__(name="Money")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldMoneyType":
        from ._schemas.type import CustomFieldMoneyTypeSchema

        return CustomFieldMoneyTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldMoneyTypeSchema

        return CustomFieldMoneyTypeSchema().dump(self)


class CustomFieldNumberType(FieldType):
    def __init__(self):

        super().__init__(name="Number")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldNumberType":
        from ._schemas.type import CustomFieldNumberTypeSchema

        return CustomFieldNumberTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldNumberTypeSchema

        return CustomFieldNumberTypeSchema().dump(self)


class CustomFieldReferenceType(FieldType):
    reference_type_id: "ReferenceTypeId"

    def __init__(self, *, reference_type_id: "ReferenceTypeId"):
        self.reference_type_id = reference_type_id
        super().__init__(name="Reference")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldReferenceType":
        from ._schemas.type import CustomFieldReferenceTypeSchema

        return CustomFieldReferenceTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldReferenceTypeSchema

        return CustomFieldReferenceTypeSchema().dump(self)


class CustomFieldSetType(FieldType):
    element_type: "FieldType"

    def __init__(self, *, element_type: "FieldType"):
        self.element_type = element_type
        super().__init__(name="Set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldSetType":
        from ._schemas.type import CustomFieldSetTypeSchema

        return CustomFieldSetTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldSetTypeSchema

        return CustomFieldSetTypeSchema().dump(self)


class CustomFieldStringType(FieldType):
    def __init__(self):

        super().__init__(name="String")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldStringType":
        from ._schemas.type import CustomFieldStringTypeSchema

        return CustomFieldStringTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldStringTypeSchema

        return CustomFieldStringTypeSchema().dump(self)


class CustomFieldTimeType(FieldType):
    def __init__(self):

        super().__init__(name="Time")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldTimeType":
        from ._schemas.type import CustomFieldTimeTypeSchema

        return CustomFieldTimeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import CustomFieldTimeTypeSchema

        return CustomFieldTimeTypeSchema().dump(self)


class ResourceTypeId(enum.Enum):
    ASSET = "asset"
    CATEGORY = "category"
    CHANNEL = "channel"
    CUSTOMER = "customer"
    ORDER = "order"
    ORDER_EDIT = "order-edit"
    INVENTORY_ENTRY = "inventory-entry"
    LINE_ITEM = "line-item"
    CUSTOM_LINE_ITEM = "custom-line-item"
    PRODUCT_PRICE = "product-price"
    PAYMENT = "payment"
    PAYMENT_INTERFACE_INTERACTION = "payment-interface-interaction"
    REVIEW = "review"
    SHOPPING_LIST = "shopping-list"
    SHOPPING_LIST_TEXT_LINE_ITEM = "shopping-list-text-line-item"
    DISCOUNT_CODE = "discount-code"
    CART_DISCOUNT = "cart-discount"
    CUSTOMER_GROUP = "customer-group"


class Type(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: Identifier for the type (max.
    #: 256 characters).
    key: str
    name: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    #: Defines for which resource(s) the type is valid.
    resource_type_ids: typing.List["ResourceTypeId"]
    field_definitions: typing.List["FieldDefinition"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: str,
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        resource_type_ids: typing.List["ResourceTypeId"],
        field_definitions: typing.List["FieldDefinition"]
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.description = description
        self.resource_type_ids = resource_type_ids
        self.field_definitions = field_definitions
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Type":
        from ._schemas.type import TypeSchema

        return TypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeSchema

        return TypeSchema().dump(self)


class TypeDraft(_BaseType):
    key: str
    name: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    #: The IDs of the resources that can be customized with this type.
    resource_type_ids: typing.List["ResourceTypeId"]
    field_definitions: typing.Optional[typing.List["FieldDefinition"]]

    def __init__(
        self,
        *,
        key: str,
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        resource_type_ids: typing.List["ResourceTypeId"],
        field_definitions: typing.Optional[typing.List["FieldDefinition"]] = None
    ):
        self.key = key
        self.name = name
        self.description = description
        self.resource_type_ids = resource_type_ids
        self.field_definitions = field_definitions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeDraft":
        from ._schemas.type import TypeDraftSchema

        return TypeDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeDraftSchema

        return TypeDraftSchema().dump(self)


class TypePagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Type"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Type"]
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypePagedQueryResponse":
        from ._schemas.type import TypePagedQueryResponseSchema

        return TypePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypePagedQueryResponseSchema

        return TypePagedQueryResponseSchema().dump(self)


class TypeReference(Reference):
    obj: typing.Optional["Type"]

    def __init__(self, *, id: str, obj: typing.Optional["Type"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.TYPE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeReference":
        from ._schemas.type import TypeReferenceSchema

        return TypeReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeReferenceSchema

        return TypeReferenceSchema().dump(self)


class TypeResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.TYPE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeResourceIdentifier":
        from ._schemas.type import TypeResourceIdentifierSchema

        return TypeResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeResourceIdentifierSchema

        return TypeResourceIdentifierSchema().dump(self)


class TypeTextInputHint(enum.Enum):
    SINGLE_LINE = "SingleLine"
    MULTI_LINE = "MultiLine"


class TypeUpdate(_BaseType):
    version: int
    actions: typing.List["TypeUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["TypeUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeUpdate":
        from ._schemas.type import TypeUpdateSchema

        return TypeUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeUpdateSchema

        return TypeUpdateSchema().dump(self)


class TypeUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeUpdateAction":
        if data["action"] == "addEnumValue":
            from ._schemas.type import TypeAddEnumValueActionSchema

            return TypeAddEnumValueActionSchema().load(data)
        if data["action"] == "addFieldDefinition":
            from ._schemas.type import TypeAddFieldDefinitionActionSchema

            return TypeAddFieldDefinitionActionSchema().load(data)
        if data["action"] == "addLocalizedEnumValue":
            from ._schemas.type import TypeAddLocalizedEnumValueActionSchema

            return TypeAddLocalizedEnumValueActionSchema().load(data)
        if data["action"] == "changeEnumValueLabel":
            from ._schemas.type import TypeChangeEnumValueLabelActionSchema

            return TypeChangeEnumValueLabelActionSchema().load(data)
        if data["action"] == "changeEnumValueOrder":
            from ._schemas.type import TypeChangeEnumValueOrderActionSchema

            return TypeChangeEnumValueOrderActionSchema().load(data)
        if data["action"] == "changeFieldDefinitionLabel":
            from ._schemas.type import TypeChangeFieldDefinitionLabelActionSchema

            return TypeChangeFieldDefinitionLabelActionSchema().load(data)
        if data["action"] == "changeFieldDefinitionOrder":
            from ._schemas.type import TypeChangeFieldDefinitionOrderActionSchema

            return TypeChangeFieldDefinitionOrderActionSchema().load(data)
        if data["action"] == "changeInputHint":
            from ._schemas.type import TypeChangeInputHintActionSchema

            return TypeChangeInputHintActionSchema().load(data)
        if data["action"] == "changeKey":
            from ._schemas.type import TypeChangeKeyActionSchema

            return TypeChangeKeyActionSchema().load(data)
        if data["action"] == "changeLabel":
            from ._schemas.type import TypeChangeLabelActionSchema

            return TypeChangeLabelActionSchema().load(data)
        if data["action"] == "changeLocalizedEnumValueLabel":
            from ._schemas.type import TypeChangeLocalizedEnumValueLabelActionSchema

            return TypeChangeLocalizedEnumValueLabelActionSchema().load(data)
        if data["action"] == "changeLocalizedEnumValueOrder":
            from ._schemas.type import TypeChangeLocalizedEnumValueOrderActionSchema

            return TypeChangeLocalizedEnumValueOrderActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.type import TypeChangeNameActionSchema

            return TypeChangeNameActionSchema().load(data)
        if data["action"] == "removeFieldDefinition":
            from ._schemas.type import TypeRemoveFieldDefinitionActionSchema

            return TypeRemoveFieldDefinitionActionSchema().load(data)
        if data["action"] == "setDescription":
            from ._schemas.type import TypeSetDescriptionActionSchema

            return TypeSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeUpdateActionSchema

        return TypeUpdateActionSchema().dump(self)


class TypeAddEnumValueAction(TypeUpdateAction):
    field_name: str
    value: "CustomFieldEnumValue"

    def __init__(self, *, field_name: str, value: "CustomFieldEnumValue"):
        self.field_name = field_name
        self.value = value
        super().__init__(action="addEnumValue")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeAddEnumValueAction":
        from ._schemas.type import TypeAddEnumValueActionSchema

        return TypeAddEnumValueActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeAddEnumValueActionSchema

        return TypeAddEnumValueActionSchema().dump(self)


class TypeAddFieldDefinitionAction(TypeUpdateAction):
    field_definition: "FieldDefinition"

    def __init__(self, *, field_definition: "FieldDefinition"):
        self.field_definition = field_definition
        super().__init__(action="addFieldDefinition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeAddFieldDefinitionAction":
        from ._schemas.type import TypeAddFieldDefinitionActionSchema

        return TypeAddFieldDefinitionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeAddFieldDefinitionActionSchema

        return TypeAddFieldDefinitionActionSchema().dump(self)


class TypeAddLocalizedEnumValueAction(TypeUpdateAction):
    field_name: str
    value: "CustomFieldLocalizedEnumValue"

    def __init__(self, *, field_name: str, value: "CustomFieldLocalizedEnumValue"):
        self.field_name = field_name
        self.value = value
        super().__init__(action="addLocalizedEnumValue")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeAddLocalizedEnumValueAction":
        from ._schemas.type import TypeAddLocalizedEnumValueActionSchema

        return TypeAddLocalizedEnumValueActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeAddLocalizedEnumValueActionSchema

        return TypeAddLocalizedEnumValueActionSchema().dump(self)


class TypeChangeEnumValueLabelAction(TypeUpdateAction):
    field_name: str
    value: "CustomFieldEnumValue"

    def __init__(self, *, field_name: str, value: "CustomFieldEnumValue"):
        self.field_name = field_name
        self.value = value
        super().__init__(action="changeEnumValueLabel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeChangeEnumValueLabelAction":
        from ._schemas.type import TypeChangeEnumValueLabelActionSchema

        return TypeChangeEnumValueLabelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeChangeEnumValueLabelActionSchema

        return TypeChangeEnumValueLabelActionSchema().dump(self)


class TypeChangeEnumValueOrderAction(TypeUpdateAction):
    field_name: str
    keys: typing.List["str"]

    def __init__(self, *, field_name: str, keys: typing.List["str"]):
        self.field_name = field_name
        self.keys = keys
        super().__init__(action="changeEnumValueOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeChangeEnumValueOrderAction":
        from ._schemas.type import TypeChangeEnumValueOrderActionSchema

        return TypeChangeEnumValueOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeChangeEnumValueOrderActionSchema

        return TypeChangeEnumValueOrderActionSchema().dump(self)


class TypeChangeFieldDefinitionLabelAction(TypeUpdateAction):
    field_name: str
    label: "LocalizedString"

    def __init__(self, *, field_name: str, label: "LocalizedString"):
        self.field_name = field_name
        self.label = label
        super().__init__(action="changeFieldDefinitionLabel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeChangeFieldDefinitionLabelAction":
        from ._schemas.type import TypeChangeFieldDefinitionLabelActionSchema

        return TypeChangeFieldDefinitionLabelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeChangeFieldDefinitionLabelActionSchema

        return TypeChangeFieldDefinitionLabelActionSchema().dump(self)


class TypeChangeFieldDefinitionOrderAction(TypeUpdateAction):
    field_names: typing.List["str"]

    def __init__(self, *, field_names: typing.List["str"]):
        self.field_names = field_names
        super().__init__(action="changeFieldDefinitionOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeChangeFieldDefinitionOrderAction":
        from ._schemas.type import TypeChangeFieldDefinitionOrderActionSchema

        return TypeChangeFieldDefinitionOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeChangeFieldDefinitionOrderActionSchema

        return TypeChangeFieldDefinitionOrderActionSchema().dump(self)


class TypeChangeInputHintAction(TypeUpdateAction):
    field_name: str
    input_hint: "TypeTextInputHint"

    def __init__(self, *, field_name: str, input_hint: "TypeTextInputHint"):
        self.field_name = field_name
        self.input_hint = input_hint
        super().__init__(action="changeInputHint")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeChangeInputHintAction":
        from ._schemas.type import TypeChangeInputHintActionSchema

        return TypeChangeInputHintActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeChangeInputHintActionSchema

        return TypeChangeInputHintActionSchema().dump(self)


class TypeChangeKeyAction(TypeUpdateAction):
    key: str

    def __init__(self, *, key: str):
        self.key = key
        super().__init__(action="changeKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeChangeKeyAction":
        from ._schemas.type import TypeChangeKeyActionSchema

        return TypeChangeKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeChangeKeyActionSchema

        return TypeChangeKeyActionSchema().dump(self)


class TypeChangeLabelAction(TypeUpdateAction):
    field_name: str
    label: "LocalizedString"

    def __init__(self, *, field_name: str, label: "LocalizedString"):
        self.field_name = field_name
        self.label = label
        super().__init__(action="changeLabel")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeChangeLabelAction":
        from ._schemas.type import TypeChangeLabelActionSchema

        return TypeChangeLabelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeChangeLabelActionSchema

        return TypeChangeLabelActionSchema().dump(self)


class TypeChangeLocalizedEnumValueLabelAction(TypeUpdateAction):
    field_name: str
    value: "CustomFieldLocalizedEnumValue"

    def __init__(self, *, field_name: str, value: "CustomFieldLocalizedEnumValue"):
        self.field_name = field_name
        self.value = value
        super().__init__(action="changeLocalizedEnumValueLabel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeChangeLocalizedEnumValueLabelAction":
        from ._schemas.type import TypeChangeLocalizedEnumValueLabelActionSchema

        return TypeChangeLocalizedEnumValueLabelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeChangeLocalizedEnumValueLabelActionSchema

        return TypeChangeLocalizedEnumValueLabelActionSchema().dump(self)


class TypeChangeLocalizedEnumValueOrderAction(TypeUpdateAction):
    field_name: str
    keys: typing.List["str"]

    def __init__(self, *, field_name: str, keys: typing.List["str"]):
        self.field_name = field_name
        self.keys = keys
        super().__init__(action="changeLocalizedEnumValueOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeChangeLocalizedEnumValueOrderAction":
        from ._schemas.type import TypeChangeLocalizedEnumValueOrderActionSchema

        return TypeChangeLocalizedEnumValueOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeChangeLocalizedEnumValueOrderActionSchema

        return TypeChangeLocalizedEnumValueOrderActionSchema().dump(self)


class TypeChangeNameAction(TypeUpdateAction):
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeChangeNameAction":
        from ._schemas.type import TypeChangeNameActionSchema

        return TypeChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeChangeNameActionSchema

        return TypeChangeNameActionSchema().dump(self)


class TypeRemoveFieldDefinitionAction(TypeUpdateAction):
    field_name: str

    def __init__(self, *, field_name: str):
        self.field_name = field_name
        super().__init__(action="removeFieldDefinition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeRemoveFieldDefinitionAction":
        from ._schemas.type import TypeRemoveFieldDefinitionActionSchema

        return TypeRemoveFieldDefinitionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeRemoveFieldDefinitionActionSchema

        return TypeRemoveFieldDefinitionActionSchema().dump(self)


class TypeSetDescriptionAction(TypeUpdateAction):
    description: typing.Optional["LocalizedString"]

    def __init__(self, *, description: typing.Optional["LocalizedString"] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TypeSetDescriptionAction":
        from ._schemas.type import TypeSetDescriptionActionSchema

        return TypeSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.type import TypeSetDescriptionActionSchema

        return TypeSetDescriptionActionSchema().dump(self)
