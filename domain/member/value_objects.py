# domain/member/value_objects.py

from dataclasses import dataclass
from uuid import UUID, uuid4
from enum import Enum


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

        if self.fiscal_code is None:
            raise ValueError("Fiscal code is required")

        normalized = self.fiscal_code.strip().upper()

        # FIX: tolleriamo input sporco nei test + validazione reale separata
        if len(normalized) != 16:
            raise ValueError(
                f"Invalid fiscal code length: expected 16, got {len(normalized)}"
            )

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