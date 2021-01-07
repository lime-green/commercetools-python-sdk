# Generated file, please do not change!!!
import typing

from ...models.me import MyShoppingListDraft
from ...models.shopping_list import MyShoppingList, ShoppingListPagedQueryResponse
from .by_project_key_me_shopping_lists_by_id_request_builder import (
    ByProjectKeyMeShoppingListsByIDRequestBuilder,
)
from .by_project_key_me_shopping_lists_key_by_key_request_builder import (
    ByProjectKeyMeShoppingListsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMeShoppingListsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_id(self, id: str) -> ByProjectKeyMeShoppingListsByIDRequestBuilder:
        return ByProjectKeyMeShoppingListsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def with_key(self, key: str) -> ByProjectKeyMeShoppingListsKeyByKeyRequestBuilder:
        return ByProjectKeyMeShoppingListsKeyByKeyRequestBuilder(
            key=key,
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
    ) -> "ShoppingListPagedQueryResponse":
        """Query shopping-lists"""
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
            endpoint=f"/{self._project_key}/me/shopping-lists",
            params=params,
            response_class=ShoppingListPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "MyShoppingListDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "MyShoppingList":
        """Create MyShoppingList"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/me/shopping-lists",
            params={"expand": expand},
            data_object=body,
            response_class=MyShoppingList,
            headers={"Content-Type": "application/json", **headers},
        )