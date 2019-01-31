import typing

from commercetools import types


class Paginator:
    """This paginator uses the offset kwarg for retrieving the pages

    Example::

        paginator = Paginator(client.products.query, sort=["id asc"])
        for product in paginator:
            print(product)

        paginator = Paginator(client.products.query, sort=["id asc"])
        for product in paginator[:-20]:
            print(product)

    """

    def __init__(self, operation: typing.Callable, **kwargs: typing.Dict[str, typing.Any]):
        if not callable(operation):
            raise ValueError("Expected a callable as first argument")

        if "offset" in kwargs or "limit" in kwargs:
            raise ValueError(
                "It is not possible to supply either the offset or limit "
                "keyword arguments when using the paginator."
            )

        self.page_size = 20
        self._operation = operation
        self._kwargs = kwargs
        self._offset = 0
        self._limit = None

    def __iter__(self) -> typing.Generator[types.Resource, None, None]:

        offset = self._offset or 0
        limit = self._limit
        num = 0
        while True:
            response = self._operation(**self._kwargs, offset=offset, limit=self.page_size)

            if limit is not None and limit < 0:
                limit = (response.total + limit) - offset

            for item in response.results:
                yield item

                if limit is not None:
                    num += 1
                    if num >= limit:
                        raise StopIteration()

            offset += response.count
            if offset >= response.total:
                break

    def _clone(self):
        clone = self.__class__(operation=self._operation, **self._kwargs)
        clone.page_size = self.page_size
        return clone

    def __getitem__(self, item):
        if isinstance(item, slice):
            clone = self._clone()
            clone._offset = item.start
            clone._limit = item.stop
            return clone
        raise IndexError
