# domain/shared/value_objects.py

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class MoneyAmount:
    value: Decimal

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("Money cannot be negative")


@dataclass(frozen=True)
class EnergyQuantity:
    value: Decimal

    def __add__(self, other):
        return EnergyQuantity(self.value + other.value)