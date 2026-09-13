# domain/member/value_objects.py

from dataclasses import dataclass
from enum import StrEnum
from uuid import UUID, uuid4


@dataclass(frozen=True)
class MemberId:
    value: UUID

    @classmethod
    def generate(cls) -> "MemberId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class EmailAddress:
    value: str

    def __post_init__(self) -> None:
        value = self.value.strip().lower()

        if not value or "@" not in value:
            raise ValueError("Invalid email address.")

        local, domain = value.rsplit("@", 1)

        if not local or not domain or "." not in domain:
            raise ValueError("Invalid email address.")

        object.__setattr__(self, "value", value)

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class TaxInformation:
    fiscal_code: str

    def __post_init__(self) -> None:
        normalized = self.fiscal_code.strip().upper()

        if len(normalized) != 16:
            raise ValueError("Fiscal code must contain 16 characters.")

        object.__setattr__(self, "fiscal_code", normalized)


@dataclass(frozen=True)
class Address:
    street: str
    city: str
    postal_code: str
    country: str

    def __post_init__(self) -> None:
        if not all(
            value.strip()
            for value in (
                self.street,
                self.city,
                self.postal_code,
                self.country,
            )
        ):
            raise ValueError("Address fields cannot be empty.")

    @property
    def full_address(self) -> str:
        return (
            f"{self.street}, "
            f"{self.postal_code} {self.city}, "
            f"{self.country}"
        )


class MemberRole(StrEnum):
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