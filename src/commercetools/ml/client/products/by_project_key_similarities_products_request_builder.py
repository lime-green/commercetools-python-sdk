# Generated file, please do not change!!!
import typing

from ...models.common import TaskToken
from ...models.similar_products import SimilarProductSearchRequest
from ..status.by_project_key_similarities_products_status_request_builder import (
    ByProjectKeySimilaritiesProductsStatusRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeySimilaritiesProductsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def status(self) -> ByProjectKeySimilaritiesProductsStatusRequestBuilder:
        return ByProjectKeySimilaritiesProductsStatusRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def post(
        self,
        body: "SimilarProductSearchRequest",
        *,
        headers: typing.Dict[str, str] = None,
    ) -> "TaskToken":
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/similarities/products",
            params={},
            data_object=body,
            response_class=TaskToken,
            headers={"Content-Type": "application/json", **headers},
        )