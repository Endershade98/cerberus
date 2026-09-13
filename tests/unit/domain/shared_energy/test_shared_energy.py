# tests/unit/domain/shared_energy/test_shared_energy.py

from datetime import UTC, datetime, timedelta
from decimal import Decimal

import pytest

from domain.community.value_objects import CerId
from domain.membership.value_objects import MemberId
from domain.shared.energy import EnergyQuantity
from domain.shared.exceptions import BusinessRuleViolation
from domain.shared_energy.events import SharedEnergyCalculated
from domain.shared_energy.shared_energy import SharedEnergy
from domain.shared_energy.value_objects import (
    CalculationPeriod,
    SharedEnergyId,
)


def make_period():
    start = datetime(2026, 1, 1, tzinfo=UTC)

    return CalculationPeriod(
        start=start,
        end=start + timedelta(hours=1),
    )


def test_calculate_uses_minimum_of_production_and_consumption():
    shared_energy = SharedEnergy.calculate(
        cer_id=CerId.generate(),
        member_id=MemberId.generate(),
        calculation_period=make_period(),
        eligible_production=EnergyQuantity("10"),
        eligible_consumption=EnergyQuantity("6"),
    )

    assert shared_energy.shared_energy.value == Decimal("6")


def test_calculate_preserves_business_inputs():
    cer_id = CerId.generate()
    member_id = MemberId.generate()
    period = make_period()

    shared_energy = SharedEnergy.calculate(
        cer_id=cer_id,
        member_id=member_id,
        calculation_period=period,
        eligible_production=EnergyQuantity("10"),
        eligible_consumption=EnergyQuantity("6"),
    )

    assert shared_energy.cer_id == cer_id
    assert shared_energy.member_id == member_id
    assert shared_energy.calculation_period == period
    assert shared_energy.eligible_production.value == Decimal("10")
    assert shared_energy.eligible_consumption.value == Decimal("6")


def test_calculate_generates_identifier():
    shared_energy = SharedEnergy.calculate(
        cer_id=CerId.generate(),
        member_id=MemberId.generate(),
        calculation_period=make_period(),
        eligible_production=EnergyQuantity("10"),
        eligible_consumption=EnergyQuantity("6"),
    )

    assert isinstance(shared_energy.id, SharedEnergyId)


def test_calculate_emits_event():
    shared_energy = SharedEnergy.calculate(
        cer_id=CerId.generate(),
        member_id=MemberId.generate(),
        calculation_period=make_period(),
        eligible_production=EnergyQuantity("10"),
        eligible_consumption=EnergyQuantity("6"),
    )

    events = shared_energy.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], SharedEnergyCalculated)
    assert events[0].shared_energy_id == shared_energy.id
    assert events[0].cer_id == shared_energy.cer_id
    assert events[0].member_id == shared_energy.member_id
    assert events[0].shared_energy == shared_energy.shared_energy


def test_shared_energy_cannot_exceed_production():
    with pytest.raises(
        BusinessRuleViolation,
        match="cannot exceed eligible production",
    ):
        SharedEnergy(
            id=SharedEnergyId.generate(),
            cer_id=CerId.generate(),
            member_id=MemberId.generate(),
            calculation_period=make_period(),
            eligible_production=EnergyQuantity("5"),
            eligible_consumption=EnergyQuantity("10"),
            shared_energy=EnergyQuantity("6"),
        )


def test_shared_energy_cannot_exceed_consumption():
    with pytest.raises(
        BusinessRuleViolation,
        match="cannot exceed eligible consumption",
    ):
        SharedEnergy(
            id=SharedEnergyId.generate(),
            cer_id=CerId.generate(),
            member_id=MemberId.generate(),
            calculation_period=make_period(),
            eligible_production=EnergyQuantity("10"),
            eligible_consumption=EnergyQuantity("5"),
            shared_energy=EnergyQuantity("6"),
        )