# Generated file, please do not change!!!
import typing

from ...models.error import ErrorResponse
from ...models.graph_ql import GraphQLRequest, GraphQLResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyGraphqlRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def post(
        self,
        body: "GraphQLRequest",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["GraphQLResponse"]:
        """Execute a GraphQL query"""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/graphql",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/graphql", **headers},
            options=options,
        )
        if response.status_code == 200:
            return GraphQLResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)
