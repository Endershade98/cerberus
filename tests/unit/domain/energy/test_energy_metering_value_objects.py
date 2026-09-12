# tests/unit/domain/energy/test_energy_metering_value_objects.py

from datetime import datetime, UTC

import pytest

from domain.energy.value_objects import (
    MeterReading,
    TimeWindow,
    AggregationPeriod,
)


def test_meter_reading_creation():

    reading = MeterReading(
        value=100.5,
        unit="kWh",
    )

    assert reading.value == 100.5


def test_meter_reading_cannot_be_negative():

    with pytest.raises(ValueError):
        MeterReading(
            value=-1,
            unit="kWh",
        )


def test_time_window_requires_order():

    start = datetime(2026, 1, 1, tzinfo=UTC)
    end = datetime(2026, 1, 2, tzinfo=UTC)

    window = TimeWindow(
        start=start,
        end=end,
    )

    assert window.start == start


def test_time_window_invalid_range():

    start = datetime(2026, 1, 2, tzinfo=UTC)
    end = datetime(2026, 1, 1, tzinfo=UTC)

    with pytest.raises(ValueError):
        TimeWindow(
            start=start,
            end=end,
        )


def test_aggregation_period():

    period = AggregationPeriod.HOUR

    assert period.value == "HOUR"