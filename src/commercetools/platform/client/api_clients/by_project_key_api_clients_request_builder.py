# Generated file, please do not change!!!
import typing

from ...models.api_client import ApiClient, ApiClientDraft, ApiClientPagedQueryResponse
from .by_project_key_api_clients_by_id_request_builder import (
    ByProjectKeyApiClientsByIDRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyApiClientsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_id(self, id: str) -> ByProjectKeyApiClientsByIDRequestBuilder:
        return ByProjectKeyApiClientsByIDRequestBuilder(
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
    ) -> "ApiClientPagedQueryResponse":
        """Query api-clients"""
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
            endpoint=f"/{self._project_key}/api-clients",
            params=params,
            response_class=ApiClientPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ApiClientDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ApiClient":
        """Create ApiClient"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/api-clients",
            params={"expand": expand},
            data_object=body,
            response_class=ApiClient,
            headers={"Content-Type": "application/json", **headers},
        )