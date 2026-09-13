# tests/unit/domain/energy/test_energy_reading.py

from datetime import UTC, datetime, timedelta
from decimal import Decimal

from domain.energy.reading import EnergyReading
from domain.energy.value_objects import (
    EnergyDirection,
    EnergyInterval,
    EnergyReadingId,
    ReadingQuality,
)
from domain.shared.energy import EnergyQuantity


def make_interval():
    start = datetime(2026, 1, 1, 10, 0, tzinfo=UTC)

    return EnergyInterval(
        start=start,
        end=start + timedelta(minutes=15),
    )


def test_record_creates_energy_reading():
    reading = EnergyReading.record(
        device_id=__import__(
            "domain.energy.value_objects",
            fromlist=["EnergyDeviceId"],
        ).EnergyDeviceId.generate(),
        interval=make_interval(),
        quantity=EnergyQuantity(Decimal("12.5")),
        direction=EnergyDirection.PRODUCTION,
    )

    assert isinstance(reading.id, EnergyReadingId)
    assert reading.quantity.value == Decimal("12.5")
    assert reading.direction == EnergyDirection.PRODUCTION
    assert reading.quality == ReadingQuality.MEASURED


def test_record_accepts_explicit_quality():
    from domain.energy.value_objects import EnergyDeviceId

    reading = EnergyReading.record(
        device_id=EnergyDeviceId.generate(),
        interval=make_interval(),
        quantity=EnergyQuantity("5"),
        direction=EnergyDirection.CONSUMPTION,
        quality=ReadingQuality.ESTIMATED,
    )

    assert reading.quality == ReadingQuality.ESTIMATED


def test_reading_is_immutable():
    from domain.energy.value_objects import EnergyDeviceId

    reading = EnergyReading.record(
        device_id=EnergyDeviceId.generate(),
        interval=make_interval(),
        quantity=EnergyQuantity("5"),
        direction=EnergyDirection.CONSUMPTION,
    )

    try:
        reading.quantity = EnergyQuantity("10")
    except AttributeError:
        pass
    else:
        raise AssertionError("EnergyReading must be immutable.")