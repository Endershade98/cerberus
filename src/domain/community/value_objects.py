# src/domain/community/value_objects.py

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class CerId:
    value: UUID

    @classmethod
    def generate(cls) -> "CerId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class CommunityId:
    value: UUID

    @classmethod
    def generate(cls) -> "CommunityId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)