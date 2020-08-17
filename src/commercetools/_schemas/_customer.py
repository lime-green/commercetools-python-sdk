# DO NOT EDIT! This file is automatically generated
import marshmallow
import marshmallow_enum

from commercetools import helpers, types
from commercetools._schemas._common import (
    BaseResourceSchema,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from commercetools._schemas._type import FieldContainerField

__all__ = [
    "CustomerAddAddressActionSchema",
    "CustomerAddBillingAddressIdActionSchema",
    "CustomerAddShippingAddressIdActionSchema",
    "CustomerAddStoreActionSchema",
    "CustomerChangeAddressActionSchema",
    "CustomerChangeEmailActionSchema",
    "CustomerChangePasswordSchema",
    "CustomerCreateEmailTokenSchema",
    "CustomerCreatePasswordResetTokenSchema",
    "CustomerDraftSchema",
    "CustomerEmailVerifySchema",
    "CustomerPagedQueryResponseSchema",
    "CustomerReferenceSchema",
    "CustomerRemoveAddressActionSchema",
    "CustomerRemoveBillingAddressIdActionSchema",
    "CustomerRemoveShippingAddressIdActionSchema",
    "CustomerRemoveStoreActionSchema",
    "CustomerResetPasswordSchema",
    "CustomerResourceIdentifierSchema",
    "CustomerSchema",
    "CustomerSetCompanyNameActionSchema",
    "CustomerSetCustomFieldActionSchema",
    "CustomerSetCustomTypeActionSchema",
    "CustomerSetCustomerGroupActionSchema",
    "CustomerSetCustomerNumberActionSchema",
    "CustomerSetDateOfBirthActionSchema",
    "CustomerSetDefaultBillingAddressActionSchema",
    "CustomerSetDefaultShippingAddressActionSchema",
    "CustomerSetExternalIdActionSchema",
    "CustomerSetFirstNameActionSchema",
    "CustomerSetKeyActionSchema",
    "CustomerSetLastNameActionSchema",
    "CustomerSetLocaleActionSchema",
    "CustomerSetMiddleNameActionSchema",
    "CustomerSetSalutationActionSchema",
    "CustomerSetStoresActionSchema",
    "CustomerSetTitleActionSchema",
    "CustomerSetVatIdActionSchema",
    "CustomerSignInResultSchema",
    "CustomerSigninSchema",
    "CustomerTokenSchema",
    "CustomerUpdateActionSchema",
    "CustomerUpdateSchema",
]


class CustomerChangePasswordSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerChangePassword`."""

    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    current_password = marshmallow.fields.String(
        allow_none=True, data_key="currentPassword"
    )
    new_password = marshmallow.fields.String(allow_none=True, data_key="newPassword")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerChangePassword(**data)


class CustomerCreateEmailTokenSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerCreateEmailToken`."""

    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    ttl_minutes = marshmallow.fields.Integer(allow_none=True, data_key="ttlMinutes")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerCreateEmailToken(**data)


class CustomerCreatePasswordResetTokenSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerCreatePasswordResetToken`."""

    email = marshmallow.fields.String(allow_none=True)
    ttl_minutes = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="ttlMinutes"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerCreatePasswordResetToken(**data)


class CustomerDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerDraft`."""

    customer_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerNumber"
    )
    email = marshmallow.fields.String(allow_none=True)
    password = marshmallow.fields.String(allow_none=True)
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )
    title = marshmallow.fields.String(allow_none=True, missing=None)
    anonymous_cart_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousCartId"
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")
    addresses = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )
    default_shipping_address = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="defaultShippingAddress"
    )
    shipping_addresses = marshmallow.fields.List(
        marshmallow.fields.Integer(allow_none=True),
        missing=None,
        data_key="shippingAddresses",
    )
    default_billing_address = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="defaultBillingAddress"
    )
    billing_addresses = marshmallow.fields.List(
        marshmallow.fields.Integer(allow_none=True),
        missing=None,
        data_key="billingAddresses",
    )
    is_email_verified = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="isEmailVerified"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    customer_group = helpers.LazyNestedField(
        nested="commercetools._schemas._customer_group.CustomerGroupResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="customerGroup",
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    salutation = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    stores = helpers.LazyNestedField(
        nested="commercetools._schemas._store.StoreResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerDraft(**data)


class CustomerEmailVerifySchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerEmailVerify`."""

    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    token_value = marshmallow.fields.String(allow_none=True, data_key="tokenValue")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerEmailVerify(**data)


class CustomerPagedQueryResponseSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerPagedQueryResponse`."""

    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = helpers.LazyNestedField(
        nested="commercetools._schemas._customer.CustomerSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerPagedQueryResponse(**data)


class CustomerReferenceSchema(ReferenceSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerReference`."""

    obj = helpers.LazyNestedField(
        nested="commercetools._schemas._customer.CustomerSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.CustomerReference(**data)


class CustomerResetPasswordSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerResetPassword`."""

    token_value = marshmallow.fields.String(allow_none=True, data_key="tokenValue")
    new_password = marshmallow.fields.String(allow_none=True, data_key="newPassword")
    version = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerResetPassword(**data)


class CustomerResourceIdentifierSchema(ResourceIdentifierSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerResourceIdentifier`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.CustomerResourceIdentifier(**data)


class CustomerSchema(BaseResourceSchema):
    """Marshmallow schema for :class:`commercetools.types.Customer`."""

    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, data_key="lastModifiedAt"
    )
    last_modified_by = helpers.LazyNestedField(
        nested="commercetools._schemas._common.LastModifiedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested="commercetools._schemas._common.CreatedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="createdBy",
    )
    customer_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerNumber"
    )
    email = marshmallow.fields.String(allow_none=True)
    password = marshmallow.fields.String(allow_none=True)
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )
    title = marshmallow.fields.String(allow_none=True, missing=None)
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")
    addresses = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    default_shipping_address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="defaultShippingAddressId"
    )
    shipping_address_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        missing=None,
        data_key="shippingAddressIds",
    )
    default_billing_address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="defaultBillingAddressId"
    )
    billing_address_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        missing=None,
        data_key="billingAddressIds",
    )
    is_email_verified = marshmallow.fields.Bool(
        allow_none=True, data_key="isEmailVerified"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    customer_group = helpers.LazyNestedField(
        nested="commercetools._schemas._customer_group.CustomerGroupReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="customerGroup",
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    salutation = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    stores = helpers.LazyNestedField(
        nested="commercetools._schemas._store.StoreKeyReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Customer(**data)


class CustomerSignInResultSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSignInResult`."""

    customer = helpers.LazyNestedField(
        nested="commercetools._schemas._customer.CustomerSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    cart = marshmallow.fields.Dict(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerSignInResult(**data)


class CustomerSigninSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSignin`."""

    email = marshmallow.fields.String(allow_none=True)
    password = marshmallow.fields.String(allow_none=True)
    anonymous_cart_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousCartId"
    )
    anonymous_cart_sign_in_mode = marshmallow_enum.EnumField(
        types.AnonymousCartSignInMode,
        by_value=True,
        missing=None,
        data_key="anonymousCartSignInMode",
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )
    update_product_data = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="updateProductData"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerSignin(**data)


class CustomerTokenSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerToken`."""

    id = marshmallow.fields.String(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="lastModifiedAt"
    )
    customer_id = marshmallow.fields.String(allow_none=True, data_key="customerId")
    expires_at = marshmallow.fields.DateTime(allow_none=True, data_key="expiresAt")
    value = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerToken(**data)


class CustomerUpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerUpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerUpdateAction(**data)


class CustomerUpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerUpdate`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addAddress": "commercetools._schemas._customer.CustomerAddAddressActionSchema",
                "addBillingAddressId": "commercetools._schemas._customer.CustomerAddBillingAddressIdActionSchema",
                "addShippingAddressId": "commercetools._schemas._customer.CustomerAddShippingAddressIdActionSchema",
                "addStore": "commercetools._schemas._customer.CustomerAddStoreActionSchema",
                "changeAddress": "commercetools._schemas._customer.CustomerChangeAddressActionSchema",
                "changeEmail": "commercetools._schemas._customer.CustomerChangeEmailActionSchema",
                "removeAddress": "commercetools._schemas._customer.CustomerRemoveAddressActionSchema",
                "removeBillingAddressId": "commercetools._schemas._customer.CustomerRemoveBillingAddressIdActionSchema",
                "removeShippingAddressId": "commercetools._schemas._customer.CustomerRemoveShippingAddressIdActionSchema",
                "removeStore": "commercetools._schemas._customer.CustomerRemoveStoreActionSchema",
                "setCompanyName": "commercetools._schemas._customer.CustomerSetCompanyNameActionSchema",
                "setCustomField": "commercetools._schemas._customer.CustomerSetCustomFieldActionSchema",
                "setCustomType": "commercetools._schemas._customer.CustomerSetCustomTypeActionSchema",
                "setCustomerGroup": "commercetools._schemas._customer.CustomerSetCustomerGroupActionSchema",
                "setCustomerNumber": "commercetools._schemas._customer.CustomerSetCustomerNumberActionSchema",
                "setDateOfBirth": "commercetools._schemas._customer.CustomerSetDateOfBirthActionSchema",
                "setDefaultBillingAddress": "commercetools._schemas._customer.CustomerSetDefaultBillingAddressActionSchema",
                "setDefaultShippingAddress": "commercetools._schemas._customer.CustomerSetDefaultShippingAddressActionSchema",
                "setExternalId": "commercetools._schemas._customer.CustomerSetExternalIdActionSchema",
                "setFirstName": "commercetools._schemas._customer.CustomerSetFirstNameActionSchema",
                "setKey": "commercetools._schemas._customer.CustomerSetKeyActionSchema",
                "setLastName": "commercetools._schemas._customer.CustomerSetLastNameActionSchema",
                "setLocale": "commercetools._schemas._customer.CustomerSetLocaleActionSchema",
                "setMiddleName": "commercetools._schemas._customer.CustomerSetMiddleNameActionSchema",
                "setSalutation": "commercetools._schemas._customer.CustomerSetSalutationActionSchema",
                "setStores": "commercetools._schemas._customer.CustomerSetStoresActionSchema",
                "setTitle": "commercetools._schemas._customer.CustomerSetTitleActionSchema",
                "setVatId": "commercetools._schemas._customer.CustomerSetVatIdActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerUpdate(**data)


class CustomerAddAddressActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerAddAddressAction`."""

    address = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerAddAddressAction(**data)


class CustomerAddBillingAddressIdActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerAddBillingAddressIdAction`."""

    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerAddBillingAddressIdAction(**data)


class CustomerAddShippingAddressIdActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerAddShippingAddressIdAction`."""

    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerAddShippingAddressIdAction(**data)


class CustomerAddStoreActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerAddStoreAction`."""

    store = helpers.LazyNestedField(
        nested="commercetools._schemas._store.StoreResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerAddStoreAction(**data)


class CustomerChangeAddressActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerChangeAddressAction`."""

    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )
    address = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerChangeAddressAction(**data)


class CustomerChangeEmailActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerChangeEmailAction`."""

    email = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerChangeEmailAction(**data)


class CustomerRemoveAddressActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerRemoveAddressAction`."""

    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerRemoveAddressAction(**data)


class CustomerRemoveBillingAddressIdActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerRemoveBillingAddressIdAction`."""

    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerRemoveBillingAddressIdAction(**data)


class CustomerRemoveShippingAddressIdActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerRemoveShippingAddressIdAction`."""

    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerRemoveShippingAddressIdAction(**data)


class CustomerRemoveStoreActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerRemoveStoreAction`."""

    store = helpers.LazyNestedField(
        nested="commercetools._schemas._store.StoreResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerRemoveStoreAction(**data)


class CustomerSetCompanyNameActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetCompanyNameAction`."""

    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetCompanyNameAction(**data)


class CustomerSetCustomFieldActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetCustomFieldAction`."""

    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetCustomFieldAction(**data)


class CustomerSetCustomTypeActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetCustomTypeAction`."""

    type = helpers.LazyNestedField(
        nested="commercetools._schemas._type.TypeResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetCustomTypeAction(**data)


class CustomerSetCustomerGroupActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetCustomerGroupAction`."""

    customer_group = helpers.LazyNestedField(
        nested="commercetools._schemas._customer_group.CustomerGroupResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="customerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetCustomerGroupAction(**data)


class CustomerSetCustomerNumberActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetCustomerNumberAction`."""

    customer_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerNumber"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetCustomerNumberAction(**data)


class CustomerSetDateOfBirthActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetDateOfBirthAction`."""

    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetDateOfBirthAction(**data)


class CustomerSetDefaultBillingAddressActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetDefaultBillingAddressAction`."""

    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetDefaultBillingAddressAction(**data)


class CustomerSetDefaultShippingAddressActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetDefaultShippingAddressAction`."""

    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetDefaultShippingAddressAction(**data)


class CustomerSetExternalIdActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetExternalIdAction`."""

    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetExternalIdAction(**data)


class CustomerSetFirstNameActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetFirstNameAction`."""

    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetFirstNameAction(**data)


class CustomerSetKeyActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetKeyAction`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetKeyAction(**data)


class CustomerSetLastNameActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetLastNameAction`."""

    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetLastNameAction(**data)


class CustomerSetLocaleActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetLocaleAction`."""

    locale = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetLocaleAction(**data)


class CustomerSetMiddleNameActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetMiddleNameAction`."""

    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetMiddleNameAction(**data)


class CustomerSetSalutationActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetSalutationAction`."""

    salutation = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetSalutationAction(**data)


class CustomerSetStoresActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetStoresAction`."""

    stores = helpers.LazyNestedField(
        nested="commercetools._schemas._store.StoreResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetStoresAction(**data)


class CustomerSetTitleActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetTitleAction`."""

    title = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetTitleAction(**data)


class CustomerSetVatIdActionSchema(CustomerUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerSetVatIdAction`."""

    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerSetVatIdAction(**data)