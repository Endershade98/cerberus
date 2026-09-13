# tests/unit/domain/incentive/test_incentive.py

from datetime import UTC, datetime, timedelta
from decimal import Decimal

import pytest

from domain.community.value_objects import CerId
from domain.incentive.events import IncentiveCalculated
from domain.incentive.incentive import Incentive, SharedEnergyReference
from domain.incentive.value_objects import IncentiveId, IncentiveRate
from domain.membership.value_objects import MemberId
from domain.shared.energy import EnergyQuantity
from domain.shared.money import MoneyAmount
from domain.shared_energy.value_objects import (
    CalculationPeriod,
    SharedEnergyId,
)


def make_period():
    start = datetime(2026, 1, 1, tzinfo=UTC)

    return CalculationPeriod(
        start=start,
        end=start + timedelta(days=31),
    )


def make_incentive():
    return Incentive.calculate(
        cer_id=CerId.generate(),
        member_id=MemberId.generate(),
        reference_period=make_period(),
        shared_energy_reference=SharedEnergyReference(
            shared_energy_id=SharedEnergyId.generate(),
        ),
        eligible_energy=EnergyQuantity("100"),
        rate=IncentiveRate(Decimal("0.15")),
    )


def test_calculate_creates_incentive():
    incentive = make_incentive()

    assert isinstance(incentive.id, IncentiveId)
    assert incentive.eligible_energy.value == Decimal("100")
    assert incentive.rate.value == Decimal("0.15")
    assert incentive.amount.value == Decimal("15.00")


def test_calculate_emits_incentive_calculated_event():
    incentive = make_incentive()

    events = incentive.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], IncentiveCalculated)
    assert events[0].incentive_id == incentive.id
    assert events[0].cer_id == incentive.cer_id
    assert events[0].member_id == incentive.member_id
    assert events[0].eligible_energy == incentive.eligible_energy
    assert events[0].rate == incentive.rate
    assert events[0].amount == incentive.amount


def test_incentive_amount_is_calculated_from_energy_and_rate():
    incentive = Incentive.calculate(
        cer_id=CerId.generate(),
        member_id=MemberId.generate(),
        reference_period=make_period(),
        shared_energy_reference=SharedEnergyReference(
            shared_energy_id=SharedEnergyId.generate(),
        ),
        eligible_energy=EnergyQuantity("250"),
        rate=IncentiveRate(Decimal("0.20")),
    )

    assert incentive.amount == MoneyAmount("50.00")


def test_incentive_keeps_shared_energy_reference():
    reference = SharedEnergyReference(
        shared_energy_id=SharedEnergyId.generate(),
    )

    incentive = Incentive.calculate(
        cer_id=CerId.generate(),
        member_id=MemberId.generate(),
        reference_period=make_period(),
        shared_energy_reference=reference,
        eligible_energy=EnergyQuantity("100"),
        rate=IncentiveRate(Decimal("0.15")),
    )

    assert incentive.shared_energy_reference == reference


def test_incentive_rate_rejects_negative_value():
    with pytest.raises(ValueError, match="cannot be negative"):
        IncentiveRate(Decimal("-0.01"))


def test_incentive_rate_calculates_money_amount():
    rate = IncentiveRate(Decimal("0.15"))

    amount = rate.calculate(EnergyQuantity("100"))

    assert amount.value == Decimal("15.00")
    assert amount.currency.code == "EUR"