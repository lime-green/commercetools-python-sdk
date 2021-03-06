# Generated file, please do not change!!!
import typing

from ...models.error import ErrorResponse
from ...models.product import ProductProjectionPagedSearchResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductProjectionsSearchRequestBuilder:

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
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional[None]:
        """Search Product Projection"""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/product-projections/search",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        elif response.status_code == 200:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)

    def get(
        self,
        *,
        fuzzy: bool = None,
        fuzzy_level: float = None,
        mark_matching_variants: bool,
        staged: bool = None,
        filter: typing.List["str"] = None,
        filter_facets: typing.List["str"] = None,
        filter_query: typing.List["str"] = None,
        facet: typing.List["str"] = None,
        text: typing.Dict[str, typing.List["str"]] = None,
        sort: typing.List["str"] = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: str = None,
        store_projection: str = None,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ProductProjectionPagedSearchResponse"]:
        """Search Product Projection"""
        params = {
            "fuzzy": fuzzy,
            "fuzzyLevel": fuzzy_level,
            "markMatchingVariants": mark_matching_variants,
            "staged": staged,
            "filter": filter,
            "filter.facets": filter_facets,
            "filter.query": filter_query,
            "facet": facet,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "priceCurrency": price_currency,
            "priceCountry": price_country,
            "priceCustomerGroup": price_customer_group,
            "priceChannel": price_channel,
            "localeProjection": locale_projection,
            "storeProjection": store_projection,
            "expand": expand,
        }
        text and params.update({f"text.{k}": v for k, v in text.items()})
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/product-projections/search",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ProductProjectionPagedSearchResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)
