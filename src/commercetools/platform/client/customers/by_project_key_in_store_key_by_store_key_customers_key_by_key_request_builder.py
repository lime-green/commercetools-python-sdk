# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.customer import Customer
from ...models.error import ErrorResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCustomersKeyByKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._key = key
        self._client = client

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Customer"]:
        """Returns a customer by its Key from a specific Store. The {storeKey} path parameter maps to a Store's key.
        It also considers customers that do not have the stores field.
        If the customer exists in the commercetools project but the stores field references different stores,
        this method returns a ResourceNotFound error.

        """
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/key={self._key}",
            params={"expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Customer.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)

    def post(
        self,
        body: "Update",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Customer"]:
        """If the customer exists in the commercetools project but the stores field references a different store,
        this method returns a ResourceNotFound error.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/key={self._key}",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return Customer.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)

    def delete(
        self,
        *,
        data_erasure: bool = None,
        version: int,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Customer"]:
        """Delete Customer by key"""
        headers = {} if headers is None else headers
        response = self._client._delete(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/key={self._key}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Customer.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)
