# src/domain/shared_energy/value_objects.py

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True)
class SharedEnergyId:
    value: UUID

    @classmethod
    def generate(cls) -> "SharedEnergyId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class CalculationPeriod:
    start: datetime
    end: datetime

    def __post_init__(self) -> None:
        if self.start.tzinfo is None or self.end.tzinfo is None:
            raise ValueError(
                "Calculation period must use timezone-aware datetimes."
            )

        if self.start >= self.end:
            raise ValueError(
                "Calculation period start must precede end."
            )