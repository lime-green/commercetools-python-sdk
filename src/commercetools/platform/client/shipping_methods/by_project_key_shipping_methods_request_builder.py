# Generated file, please do not change!!!
import typing

from ...models.shipping_method import (
    ShippingMethod,
    ShippingMethodDraft,
    ShippingMethodPagedQueryResponse,
)
from ..matching_cart.by_project_key_shipping_methods_matching_cart_request_builder import (
    ByProjectKeyShippingMethodsMatchingCartRequestBuilder,
)
from ..matching_location.by_project_key_shipping_methods_matching_location_request_builder import (
    ByProjectKeyShippingMethodsMatchingLocationRequestBuilder,
)
from ..matching_orderedit.by_project_key_shipping_methods_matching_orderedit_request_builder import (
    ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder,
)
from .by_project_key_shipping_methods_by_id_request_builder import (
    ByProjectKeyShippingMethodsByIDRequestBuilder,
)
from .by_project_key_shipping_methods_key_by_key_request_builder import (
    ByProjectKeyShippingMethodsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyShippingMethodsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyShippingMethodsKeyByKeyRequestBuilder:
        return ByProjectKeyShippingMethodsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def matching_cart(self) -> ByProjectKeyShippingMethodsMatchingCartRequestBuilder:
        """Get ShippingMethods for a cart"""
        return ByProjectKeyShippingMethodsMatchingCartRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def matching_orderedit(
        self,
    ) -> ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder:
        """Get ShippingMethods for an order edit"""
        return ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def matching_location(
        self,
    ) -> ByProjectKeyShippingMethodsMatchingLocationRequestBuilder:
        """Get ShippingMethods for a location"""
        return ByProjectKeyShippingMethodsMatchingLocationRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyShippingMethodsByIDRequestBuilder:
        return ByProjectKeyShippingMethodsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: str = None,
        predicate_var: typing.Dict[str, str] = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShippingMethodPagedQueryResponse":
        """Query shipping-methods"""
        params = {
            "expand": expand,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/shipping-methods",
            params=params,
            response_class=ShippingMethodPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ShippingMethodDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShippingMethod":
        """Create ShippingMethod"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/shipping-methods",
            params={"expand": expand},
            data_object=body,
            response_class=ShippingMethod,
            headers={"Content-Type": "application/json", **headers},
        )