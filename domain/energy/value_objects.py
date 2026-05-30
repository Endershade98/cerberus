# domain/energy/value_objects.py

from dataclasses import dataclass


@dataclass(frozen=True)
class EnergyQuantity:
    value: float

    def __post_init__(self):
        if self.value <= 0:
            raise ValueError("Energy quantity must be positive")

    def __add__(self, other: "EnergyQuantity") -> "EnergyQuantity":
        return EnergyQuantity(self.value + other.value)