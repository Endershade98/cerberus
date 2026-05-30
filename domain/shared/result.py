# domain/shared/result.py

from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar("T")
E = TypeVar("E")


@dataclass(frozen=True)
class Result(Generic[T, E]):
    value: Optional[T] = None
    error: Optional[E] = None

    @staticmethod
    def ok(value: T) -> "Result[T, E]":
        return Result(value=value)

    @staticmethod
    def fail(error: E) -> "Result[T, E]":
        return Result(error=error)

    def is_ok(self) -> bool:
        return self.error is None

    def is_fail(self) -> bool:
        return self.error is not None