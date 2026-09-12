# tests/unit/domain/energy/test_energy_events.py

from domain.energy.events import (
    EnergyRecorded,
    EnergyValidated,
    EnergyAggregationStarted,
    EnergyAggregationCompleted,
)


def test_energy_recorded_event():

    event = EnergyRecorded(
        record_id="r1",
        member_id="m1",
    )

    assert event.record_id == "r1"


def test_energy_validated_event():

    event = EnergyValidated(
        batch_id="b1",
    )

    assert event.batch_id == "b1"


def test_energy_aggregation_started_event():

    event = EnergyAggregationStarted(
        batch_id="b1",
    )

    assert event.batch_id == "b1"


def test_energy_aggregation_completed_event():

    event = EnergyAggregationCompleted(
        batch_id="b1",
        total_kwh=100,
    )

    assert event.total_kwh == 100