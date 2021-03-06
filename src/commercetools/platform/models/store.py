# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import (
    BaseResource,
    KeyReference,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from .channel import ChannelReference, ChannelResourceIdentifier
    from .common import CreatedBy, LastModifiedBy, LocalizedString, ReferenceTypeId
    from .type import CustomFields, CustomFieldsDraft, TypeResourceIdentifier

__all__ = [
    "Store",
    "StoreAddDistributionChannelAction",
    "StoreAddSupplyChannelAction",
    "StoreDraft",
    "StoreKeyReference",
    "StorePagedQueryResponse",
    "StoreReference",
    "StoreRemoveDistributionChannelAction",
    "StoreRemoveSupplyChannelAction",
    "StoreResourceIdentifier",
    "StoreSetCustomFieldAction",
    "StoreSetCustomTypeAction",
    "StoreSetDistributionChannelsAction",
    "StoreSetLanguagesAction",
    "StoreSetNameAction",
    "StoreSetSupplyChannelsAction",
    "StoreUpdate",
    "StoreUpdateAction",
]


class Store(BaseResource):
    last_modified_by: typing.Optional["LastModifiedBy"]
    created_by: typing.Optional["CreatedBy"]
    #: User-specific unique identifier for the store.
    #: The `key` is mandatory and immutable.
    #: It is used to reference the store.
    key: str
    #: The name of the store
    name: typing.Optional["LocalizedString"]
    languages: typing.Optional[typing.List["str"]]
    #: Set of References to a Channel with `ProductDistribution` role
    distribution_channels: typing.List["ChannelReference"]
    #: Set of ResourceIdentifiers of Channels with `InventorySupply` role
    supply_channels: typing.Optional[typing.List["ChannelReference"]]
    custom: typing.Optional["CustomFields"]

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
        name: typing.Optional["LocalizedString"] = None,
        languages: typing.Optional[typing.List["str"]] = None,
        distribution_channels: typing.List["ChannelReference"],
        supply_channels: typing.Optional[typing.List["ChannelReference"]] = None,
        custom: typing.Optional["CustomFields"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.languages = languages
        self.distribution_channels = distribution_channels
        self.supply_channels = supply_channels
        self.custom = custom
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Store":
        from ._schemas.store import StoreSchema

        return StoreSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSchema

        return StoreSchema().dump(self)


class StoreDraft(_BaseType):
    #: User-specific unique identifier for the store.
    #: The `key` is mandatory and immutable.
    #: It is used to reference the store.
    key: str
    #: The name of the store
    name: "LocalizedString"
    languages: typing.Optional[typing.List["str"]]
    #: Set of ResourceIdentifiers to a Channel with `ProductDistribution` role
    distribution_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]
    #: Set of ResourceIdentifiers of Channels with `InventorySupply` role
    supply_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        key: str,
        name: "LocalizedString",
        languages: typing.Optional[typing.List["str"]] = None,
        distribution_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None,
        supply_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.key = key
        self.name = name
        self.languages = languages
        self.distribution_channels = distribution_channels
        self.supply_channels = supply_channels
        self.custom = custom
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreDraft":
        from ._schemas.store import StoreDraftSchema

        return StoreDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreDraftSchema

        return StoreDraftSchema().dump(self)


class StoreKeyReference(KeyReference):
    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceTypeId.STORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreKeyReference":
        from ._schemas.store import StoreKeyReferenceSchema

        return StoreKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreKeyReferenceSchema

        return StoreKeyReferenceSchema().dump(self)


class StorePagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Store"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Store"]
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
    ) -> "StorePagedQueryResponse":
        from ._schemas.store import StorePagedQueryResponseSchema

        return StorePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StorePagedQueryResponseSchema

        return StorePagedQueryResponseSchema().dump(self)


class StoreReference(Reference):
    obj: typing.Optional["Store"]

    def __init__(self, *, id: str, obj: typing.Optional["Store"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.STORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreReference":
        from ._schemas.store import StoreReferenceSchema

        return StoreReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreReferenceSchema

        return StoreReferenceSchema().dump(self)


class StoreResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.STORE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreResourceIdentifier":
        from ._schemas.store import StoreResourceIdentifierSchema

        return StoreResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreResourceIdentifierSchema

        return StoreResourceIdentifierSchema().dump(self)


class StoreUpdate(_BaseType):
    version: int
    actions: typing.List["StoreUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["StoreUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreUpdate":
        from ._schemas.store import StoreUpdateSchema

        return StoreUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreUpdateSchema

        return StoreUpdateSchema().dump(self)


class StoreUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreUpdateAction":
        if data["action"] == "addDistributionChannel":
            from ._schemas.store import StoreAddDistributionChannelActionSchema

            return StoreAddDistributionChannelActionSchema().load(data)
        if data["action"] == "addSupplyChannel":
            from ._schemas.store import StoreAddSupplyChannelActionSchema

            return StoreAddSupplyChannelActionSchema().load(data)
        if data["action"] == "removeDistributionChannel":
            from ._schemas.store import StoreRemoveDistributionChannelActionSchema

            return StoreRemoveDistributionChannelActionSchema().load(data)
        if data["action"] == "removeSupplyChannel":
            from ._schemas.store import StoreRemoveSupplyChannelActionSchema

            return StoreRemoveSupplyChannelActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.store import StoreSetCustomFieldActionSchema

            return StoreSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.store import StoreSetCustomTypeActionSchema

            return StoreSetCustomTypeActionSchema().load(data)
        if data["action"] == "setDistributionChannels":
            from ._schemas.store import StoreSetDistributionChannelsActionSchema

            return StoreSetDistributionChannelsActionSchema().load(data)
        if data["action"] == "setLanguages":
            from ._schemas.store import StoreSetLanguagesActionSchema

            return StoreSetLanguagesActionSchema().load(data)
        if data["action"] == "setName":
            from ._schemas.store import StoreSetNameActionSchema

            return StoreSetNameActionSchema().load(data)
        if data["action"] == "setSupplyChannels":
            from ._schemas.store import StoreSetSupplyChannelsActionSchema

            return StoreSetSupplyChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreUpdateActionSchema

        return StoreUpdateActionSchema().dump(self)


class StoreAddDistributionChannelAction(StoreUpdateAction):
    distribution_channel: "ChannelResourceIdentifier"

    def __init__(self, *, distribution_channel: "ChannelResourceIdentifier"):
        self.distribution_channel = distribution_channel
        super().__init__(action="addDistributionChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreAddDistributionChannelAction":
        from ._schemas.store import StoreAddDistributionChannelActionSchema

        return StoreAddDistributionChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreAddDistributionChannelActionSchema

        return StoreAddDistributionChannelActionSchema().dump(self)


class StoreAddSupplyChannelAction(StoreUpdateAction):
    supply_channel: "ChannelResourceIdentifier"

    def __init__(self, *, supply_channel: "ChannelResourceIdentifier"):
        self.supply_channel = supply_channel
        super().__init__(action="addSupplyChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreAddSupplyChannelAction":
        from ._schemas.store import StoreAddSupplyChannelActionSchema

        return StoreAddSupplyChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreAddSupplyChannelActionSchema

        return StoreAddSupplyChannelActionSchema().dump(self)


class StoreRemoveDistributionChannelAction(StoreUpdateAction):
    distribution_channel: "ChannelResourceIdentifier"

    def __init__(self, *, distribution_channel: "ChannelResourceIdentifier"):
        self.distribution_channel = distribution_channel
        super().__init__(action="removeDistributionChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreRemoveDistributionChannelAction":
        from ._schemas.store import StoreRemoveDistributionChannelActionSchema

        return StoreRemoveDistributionChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreRemoveDistributionChannelActionSchema

        return StoreRemoveDistributionChannelActionSchema().dump(self)


class StoreRemoveSupplyChannelAction(StoreUpdateAction):
    supply_channel: "ChannelResourceIdentifier"

    def __init__(self, *, supply_channel: "ChannelResourceIdentifier"):
        self.supply_channel = supply_channel
        super().__init__(action="removeSupplyChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreRemoveSupplyChannelAction":
        from ._schemas.store import StoreRemoveSupplyChannelActionSchema

        return StoreRemoveSupplyChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreRemoveSupplyChannelActionSchema

        return StoreRemoveSupplyChannelActionSchema().dump(self)


class StoreSetCustomFieldAction(StoreUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetCustomFieldAction":
        from ._schemas.store import StoreSetCustomFieldActionSchema

        return StoreSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetCustomFieldActionSchema

        return StoreSetCustomFieldActionSchema().dump(self)


class StoreSetCustomTypeAction(StoreUpdateAction):
    #: If set, the custom type is reset to this value.
    #: If absent, the custom type and any existing custom fields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: A valid JSON object, based on the FieldDefinitions of the Type
    #: Sets the custom field to this value.
    fields: typing.Optional[object]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional[object] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetCustomTypeAction":
        from ._schemas.store import StoreSetCustomTypeActionSchema

        return StoreSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetCustomTypeActionSchema

        return StoreSetCustomTypeActionSchema().dump(self)


class StoreSetDistributionChannelsAction(StoreUpdateAction):
    distribution_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]

    def __init__(
        self,
        *,
        distribution_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None
    ):
        self.distribution_channels = distribution_channels
        super().__init__(action="setDistributionChannels")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetDistributionChannelsAction":
        from ._schemas.store import StoreSetDistributionChannelsActionSchema

        return StoreSetDistributionChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetDistributionChannelsActionSchema

        return StoreSetDistributionChannelsActionSchema().dump(self)


class StoreSetLanguagesAction(StoreUpdateAction):
    languages: typing.Optional[typing.List["str"]]

    def __init__(self, *, languages: typing.Optional[typing.List["str"]] = None):
        self.languages = languages
        super().__init__(action="setLanguages")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetLanguagesAction":
        from ._schemas.store import StoreSetLanguagesActionSchema

        return StoreSetLanguagesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetLanguagesActionSchema

        return StoreSetLanguagesActionSchema().dump(self)


class StoreSetNameAction(StoreUpdateAction):
    #: The updated name of the store
    name: typing.Optional["LocalizedString"]

    def __init__(self, *, name: typing.Optional["LocalizedString"] = None):
        self.name = name
        super().__init__(action="setName")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreSetNameAction":
        from ._schemas.store import StoreSetNameActionSchema

        return StoreSetNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetNameActionSchema

        return StoreSetNameActionSchema().dump(self)


class StoreSetSupplyChannelsAction(StoreUpdateAction):
    supply_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]

    def __init__(
        self,
        *,
        supply_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None
    ):
        self.supply_channels = supply_channels
        super().__init__(action="setSupplyChannels")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetSupplyChannelsAction":
        from ._schemas.store import StoreSetSupplyChannelsActionSchema

        return StoreSetSupplyChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetSupplyChannelsActionSchema

        return StoreSetSupplyChannelsActionSchema().dump(self)
