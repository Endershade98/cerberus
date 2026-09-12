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