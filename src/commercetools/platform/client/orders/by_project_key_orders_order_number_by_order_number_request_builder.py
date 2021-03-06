# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.error import ErrorResponse
from ...models.order import Order

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyOrdersOrderNumberByOrderNumberRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _order_number: str

    def __init__(
        self,
        project_key: str,
        order_number: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._order_number = order_number
        self._client = client

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Order"]:
        """In case the orderNumber does not match the regular expression [a-zA-Z0-9_\-]+,
        it should be provided in URL-encoded format.

        """
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/orders/order-number={self._order_number}",
            params={"expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Order.deserialize(response.json())
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
    ) -> typing.Optional["Order"]:
        """Update Order by orderNumber"""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/orders/order-number={self._order_number}",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return Order.deserialize(response.json())
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
    ) -> typing.Optional["Order"]:
        """Delete Order by orderNumber"""
        headers = {} if headers is None else headers
        response = self._client._delete(
            endpoint=f"/{self._project_key}/orders/order-number={self._order_number}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Order.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)
