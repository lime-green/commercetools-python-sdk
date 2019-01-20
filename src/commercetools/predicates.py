import json
from collections.abc import Collection
from decimal import Decimal
from functools import reduce


class QueryPredicate:
    AND = "AND"
    OR = "OR"

    _operators = {
        "exact": "=",
        "gte": ">=",
        "lte": "=<",
        "lt": "<",
        "gt": ">",
        "is_defined": ("is defined", "is not defined"),
        "contains_all": "contains all",
        "contains_any": "contains any",
    }

    def __init__(self, **filters: str):
        self._connector = filters.pop("_connector", self.AND)
        self._filters = filters

    def __str__(self):
        result = []

        for key, value in self._filters.items():
            fields = key.split("__")
            operator = fields.pop()
            if operator not in self._operators:
                fields.append(operator)
                operator = "exact"

            lhs = fields.pop()
            val = self._clause(lhs, operator, value)
            fields.append(val)
            result.append(reduce(lambda x, y: f"{y}({x})", fields[::-1]))

        if self._connector == self.OR:
            return " OR ".join(result)
        return " AND ".join(result)

    def __or__(self, other):
        data = {}
        data.update(self._filters)
        data.update(other._filters)
        return self.__class__(**data, _connector=self.OR)

    def __and__(self, other):
        data = {}
        data.update(self._filters)
        data.update(other._filters)
        return self.__class__(**data, _connector=self.AND)

    def _clause(self, lhs, operator, rhs):
        assert operator in self._operators

        if isinstance(rhs, dict):
            rhs = self.__class__(**rhs)
            return "%s(%s)" % (lhs, rhs)

        if isinstance(rhs, self.__class__):
            return "%s(%s)" % (lhs, rhs)

        op = self._operators[operator]
        if isinstance(op, tuple):
            return " ".join((lhs, op[0 if rhs else 1]))
        else:
            rhs = self._escape_value(rhs)
            return " ".join((lhs, op, rhs))

    def _escape_value(self, value):
        if isinstance(value, self.__class__):
            return "(%s)" % value
        if isinstance(value, Decimal):
            return str(value)
        if not isinstance(value, str) and isinstance(value, Collection):
            return "(%s)" % (", ".join(self._escape_value(v) for v in value))
        return json.dumps(value)
