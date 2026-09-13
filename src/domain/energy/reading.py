# src/domain/energy/reading.py

from dataclasses import dataclass

from domain.energy.value_objects import (
    EnergyDeviceId,
    EnergyDirection,
    EnergyInterval,
    EnergyReadingId,
    ReadingQuality,
)
from domain.shared.energy import EnergyQuantity
from domain.shared.exceptions import BusinessRuleViolation


@dataclass(frozen=True)
class EnergyReading:
    id: EnergyReadingId
    device_id: EnergyDeviceId
    interval: EnergyInterval
    quantity: EnergyQuantity
    direction: EnergyDirection
    quality: ReadingQuality = ReadingQuality.MEASURED

    @classmethod
    def record(
        cls,
        *,
        device_id: EnergyDeviceId,
        interval: EnergyInterval,
        quantity: EnergyQuantity,
        direction: EnergyDirection,
        quality: ReadingQuality = ReadingQuality.MEASURED,
        reading_id: EnergyReadingId | None = None,
    ) -> "EnergyReading":
        if quantity.value < 0:
            raise BusinessRuleViolation(
                "Energy reading quantity cannot be negative."
            )

        return cls(
            id=reading_id or EnergyReadingId.generate(),
            device_id=device_id,
            interval=interval,
            quantity=quantity,
            direction=direction,
            quality=quality,
        )