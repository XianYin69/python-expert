from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Iterable, Callable, TypeVar
T, R = TypeVar("T"), TypeVar("R")

def run(items: Iterable[T], fn: Callable[[T], R], workers: int = 4) -> list[R]:
    """CPU-bound: processes bypass the GIL. I/O-bound: use ThreadPoolExecutor."""
    with ProcessPoolExecutor(max_workers=workers) as ex:
        return [f.result() for f in as_completed([ex.submit(fn, i) for i in items])]
