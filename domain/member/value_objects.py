# domain/member/value_objects.py

from enum import Enum
from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class MemberId:
    value: UUID

    @staticmethod
    def generate() -> "MemberId":
        return MemberId(uuid4())


@dataclass(frozen=True)
class TaxInformation:
    fiscal_code: str

    def __post_init__(self):

        normalized = self.fiscal_code.strip().upper()

        if len(normalized) != 16:
            raise ValueError("Fiscal code must be 16 chars")

        object.__setattr__(self, "fiscal_code", normalized)


@dataclass(frozen=True)
class Address:
    street: str
    city: str
    postal_code: str
    country: str

    def full_address(self) -> str:
        return (
            f"{self.street}, "
            f"{self.postal_code} "
            f"{self.city}, "
            f"{self.country}"
        )


class MemberRole(str, Enum):
    CONSUMER = "CONSUMER"
    PRODUCER = "PRODUCER"
    PROSUMER = "PROSUMER"

    def can_produce(self) -> bool:
        return self in {
            MemberRole.PRODUCER,
            MemberRole.PROSUMER,
        }

    def can_consume(self) -> bool:
        return self in {
            MemberRole.CONSUMER,
            MemberRole.PROSUMER,
        }