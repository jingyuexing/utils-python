from typing import Any, Callable, Dict, Optional, TypeVar
from time import time
from functools import wraps

T = TypeVar("T")


def pipeline_callback(*funs: Callable) -> Callable[[T], T]:
    def pipeline(args):
        result = args
        for fn in funs:
            result = fn(result)
        return result

    return pipeline


def debounce_callback(
    callback: Callable[..., Any], interval: float
) -> Callable[..., Any]:
    last_invocation = 0

    def debounced(*args: Any, **kwargs: Any) -> Optional[Any]:
        nonlocal last_invocation
        current_time = time()

        if current_time - last_invocation > interval:
            last_invocation = current_time
            return callback(*args, **kwargs)
        return None

    return debounced


def debounce(interval: float) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        last_invocation = 0

        def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
            nonlocal last_invocation
            current_time = time()

            if current_time - last_invocation > interval:
                last_invocation = current_time
                return func(*args, **kwargs)

            return None

        return wrapper

    return decorator


def pipeline(*funs: Callable[[T], T]) -> Callable[[Callable[[T], T]], Callable[[T], T]]:
    def decorator(func: Callable[[T], T]) -> Callable[[T], T]:
        def wrapper(args: T) -> T:
            result = args
            for fn in funs:
                result = fn(result)
            return func(result)

        return wrapper

    return decorator


def compose(
    *functions: Callable[[T], T]
) -> Callable[[Callable[[T], T]], Callable[[T], T]]:
    def decorator(func: Callable[[T], T]) -> Callable[[T], T]:
        def wrapper(arg: T) -> T:
            result = arg
            for fn in reversed(functions):
                result = fn(result)
            return func(result)

        return wrapper

    return decorator


def compose_callback(*functions: Callable[[T], T]) -> Callable[[T], T]:
    def composed(arg: T) -> T:
        result = arg
        for func in reversed(functions):
            result = func(result)
        return result

    return composed


def times_callback(callback: Callable[..., Any], limit: int) -> Callable[..., Any]:
    count = 0

    def limited(*args: Any, **kwargs: Any) -> Any:
        nonlocal count
        if count < limit:
            count += 1
            return callback(*args, **kwargs)
        return None

    return limited


def times(limit: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        count = 0

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal count
            if count < limit:
                count += 1
                return func(*args, **kwargs)
            return None

        return wrapper

    return decorator


def memo(func: Callable[..., Any]) -> Callable[..., Any]:
    cache: Dict = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = args + tuple(kwargs.items())
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

class Limit:
    """docstring for Limit"""
    callback:Callable[...,bool]
    def __init__(self, callback:Callable[...,bool]):
        self.callback = callback
    def __call__(self,func):
        def wapper(*args, **kw):
            if self.callback():
               return func(*args,**kw)
            else:
                return func
        return wapper


def Reactive(
    getter: Optional[Callable[[Any, str], bool]] = None,
    setter: Optional[Callable[[Any, str, Any], bool]] = None
):
    def wrapper(cls):
        def __setter__(self, key, value):
            if setter:
                result = setter(cls, key, value)
                if result:
                    super(cls, self).__setattr__(key, value)
        def __getter__(self, key):
            if getter:
                result = getter(cls, key)
                if result:
                    return super(cls, self).__getattribute__(key)
        setattr(cls, "__setattr__", __setter__)
        setattr(cls, "__getattribute__", __getter__)
        return cls
    return wrapper
