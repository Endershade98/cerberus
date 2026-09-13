# src/domain/energy/value_objects.py

from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from uuid import UUID, uuid4


@dataclass(frozen=True)
class EnergyAssetId:
    value: UUID

    @classmethod
    def generate(cls) -> "EnergyAssetId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class EnergyDeviceId:
    value: UUID

    @classmethod
    def generate(cls) -> "EnergyDeviceId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class EnergyReadingId:
    value: UUID

    @classmethod
    def generate(cls) -> "EnergyReadingId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class EnergyBatchId:
    value: UUID

    @classmethod
    def generate(cls) -> "EnergyBatchId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class PodCode:
    value: str

    def __post_init__(self) -> None:
        value = self.value.strip().upper()

        if len(value) < 5:
            raise ValueError("POD code is too short.")

        object.__setattr__(self, "value", value)

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class EnergyInterval:
    start: datetime
    end: datetime

    def __post_init__(self) -> None:
        if self.start.tzinfo is None or self.end.tzinfo is None:
            raise ValueError("Energy interval must use timezone-aware datetimes.")

        if self.start >= self.end:
            raise ValueError("Energy interval start must precede end.")

    def contains(self, timestamp: datetime) -> bool:
        return self.start <= timestamp < self.end


class EnergyDirection(StrEnum):
    PRODUCTION = "PRODUCTION"
    CONSUMPTION = "CONSUMPTION"


class ReadingQuality(StrEnum):
    MEASURED = "MEASURED"
    ESTIMATED = "ESTIMATED"
    CORRECTED = "CORRECTED"


class EnergyAssetType(StrEnum):
    PRODUCTION = "PRODUCTION"
    CONSUMPTION = "CONSUMPTION"
    PROSUMER = "PROSUMER"


class EnergyAssetStatus(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class EnergyDeviceStatus(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"