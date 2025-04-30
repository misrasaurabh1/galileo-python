from functools import cache
from importlib.util import find_spec


def is_dependency_available(name: str) -> bool:
    return _cached_find_spec(name)


# Cache the results of dependency availability checks
@cache
def _cached_find_spec(name: str) -> bool:
    return find_spec(name) is not None


is_langchain_available = is_dependency_available("langchain_core")
