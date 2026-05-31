# domain/shared/value_objects_extra.py

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Percentage:
    value: Decimal

    def __post_init__(self):
        if self.value < 0 or self.value > 100:
            raise ValueError("Percentage must be between 0 and 100")


@dataclass(frozen=True)
class PodCode:
    value: str

    def __post_init__(self):
        if not self.value or len(self.value) < 5:
            raise ValueError("Invalid POD code")


@dataclass(frozen=True)
class IncentiveAmount:
    value: Decimal

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("Incentive cannot be negative")


@dataclass(frozen=True)
class TimeSlot:
    start: str
    end: str