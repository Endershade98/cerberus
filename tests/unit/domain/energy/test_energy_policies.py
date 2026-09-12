# tests/unit/domain/energy/test_energy_policies.py

from datetime import datetime, UTC

from domain.energy.policies import (
    DuplicateReadingPolicy,
    TemporalAlignmentPolicy,
)


def test_duplicate_policy_detects_duplicate():

    ts = datetime.now(UTC)

    records = [
        ("member-1", ts),
    ]

    assert DuplicateReadingPolicy.is_duplicate(
        records,
        "member-1",
        ts,
    )


def test_duplicate_policy_accepts_new_record():

    ts = datetime.now(UTC)

    records = []

    assert not DuplicateReadingPolicy.is_duplicate(
        records,
        "member-1",
        ts,
    )


def test_temporal_alignment_valid():

    ts = datetime(
        2026,
        1,
        1,
        10,
        0,
        0,
        tzinfo=UTC,
    )

    assert TemporalAlignmentPolicy.is_aligned(ts)


def test_temporal_alignment_invalid():

    ts = datetime(
        2026,
        1,
        1,
        10,
        12,
        0,
        tzinfo=UTC,
    )

    assert not TemporalAlignmentPolicy.is_aligned(ts)