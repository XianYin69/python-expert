from typing import Protocol, runtime_checkable

@runtime_checkable
class Store(Protocol):
    def get(self, key: str) -> str | None: ...
    def set(self, key: str, value: str) -> None: ...

def use(s: Store) -> str | None:
    return s.get("k")
