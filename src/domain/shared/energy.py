# src/domain/shared/energy.py

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class EnergyQuantity:
    value: Decimal

    def __post_init__(self) -> None:
        value = Decimal(str(self.value))

        if value < Decimal("0"):
            raise ValueError("Energy quantity cannot be negative.")

        object.__setattr__(self, "value", value)

    @classmethod
    def zero(cls) -> "EnergyQuantity":
        return cls(Decimal("0"))

    def add(self, other: "EnergyQuantity") -> "EnergyQuantity":
        return EnergyQuantity(self.value + other.value)

    def subtract(self, other: "EnergyQuantity") -> "EnergyQuantity":
        result = self.value - other.value

        if result < Decimal("0"):
            raise ValueError("Energy quantity cannot become negative.")

        return EnergyQuantity(result)

    def min(self, other: "EnergyQuantity") -> "EnergyQuantity":
        return EnergyQuantity(min(self.value, other.value))