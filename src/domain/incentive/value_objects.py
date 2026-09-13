# src/domain/incentive/value_objects.py

from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID, uuid4

from domain.shared.energy import EnergyQuantity
from domain.shared.money import Currency, EUR, MoneyAmount


@dataclass(frozen=True)
class IncentiveId:
    value: UUID

    @classmethod
    def generate(cls) -> "IncentiveId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class IncentiveRate:
    value: Decimal
    currency: Currency = EUR

    def __post_init__(self) -> None:
        value = Decimal(str(self.value))

        if value < Decimal("0"):
            raise ValueError("Incentive rate cannot be negative.")

        object.__setattr__(self, "value", value)

    def calculate(
        self,
        energy: EnergyQuantity,
    ) -> MoneyAmount:
        return MoneyAmount(
            energy.value * self.value,
            self.currency,
        )