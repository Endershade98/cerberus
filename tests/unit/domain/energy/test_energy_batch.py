# tests/unit/domain/energy/test_energy_batch.py

from datetime import UTC, datetime, timedelta

import pytest

from domain.energy.batch import EnergyBatch
from domain.energy.status import EnergyBatchStatus
from domain.energy.value_objects import EnergyBatchId
from domain.shared.exceptions import InvalidStateTransition


def make_batch():
    start = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
    end = start + timedelta(hours=1)

    return EnergyBatch.receive(
        source="GSE",
        period_start=start,
        period_end=end,
        received_at=end,
    )


def test_receive_creates_received_batch():
    batch = make_batch()

    assert isinstance(batch.id, EnergyBatchId)
    assert batch.status == EnergyBatchStatus.RECEIVED
    assert batch.source == "GSE"


def test_source_is_normalized():
    start = datetime(2026, 1, 1, tzinfo=UTC)
    end = start + timedelta(hours=1)

    batch = EnergyBatch.receive(
        source="  GSE  ",
        period_start=start,
        period_end=end,
        received_at=end,
    )

    assert batch.source == "GSE"


def test_invalid_period_is_rejected():
    start = datetime(2026, 1, 1, 1, 0, tzinfo=UTC)
    end = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)

    with pytest.raises(ValueError, match="Batch period is invalid"):
        EnergyBatch.receive(
            source="GSE",
            period_start=start,
            period_end=end,
            received_at=end,
        )


def test_blank_source_is_rejected():
    start = datetime(2026, 1, 1, tzinfo=UTC)
    end = start + timedelta(hours=1)

    with pytest.raises(ValueError, match="Batch source is required"):
        EnergyBatch.receive(
            source="   ",
            period_start=start,
            period_end=end,
            received_at=end,
        )


def test_validate_changes_status():
    batch = make_batch()

    batch.validate()

    assert batch.status == EnergyBatchStatus.VALIDATED


def test_reject_changes_status():
    batch = make_batch()

    batch.reject()

    assert batch.status == EnergyBatchStatus.REJECTED


@pytest.mark.parametrize(
    "operation",
    [
        "validate",
        "reject",
    ],
)
def test_terminal_batch_cannot_transition_again(operation):
    batch = make_batch()

    getattr(batch, operation)()

    second_operation = (
        "reject" if operation == "validate" else "validate"
    )

    with pytest.raises(InvalidStateTransition):
        getattr(batch, second_operation)()