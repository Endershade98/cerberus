# domain/shared/value_objects.py

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class MoneyAmount:
    value: Decimal

    def __post_init__(self):

        if self.value < 0:
            raise ValueError(
                "Money amount cannot be negative"
            )

    def __add__(self, other: "MoneyAmount") -> "MoneyAmount":
        return MoneyAmount(self.value + other.value)

@dataclass(frozen=True)
class EnergyQuantity:
    amount: float

    def __float__(self):
        return float(self.amount)

    def __add__(self, other):
        if isinstance(other, EnergyQuantity):
            return EnergyQuantity(self.amount + other.amount)
        return EnergyQuantity(self.amount + float(other))