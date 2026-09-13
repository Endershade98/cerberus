# tests/unit/domain/shared_energy/test_sharing_interval.py

from datetime import UTC, datetime, timedelta
from decimal import Decimal

import pytest

from domain.energy.value_objects import EnergyInterval
from domain.membership.value_objects import MemberId
from domain.shared.energy import EnergyQuantity
from domain.shared.exceptions import BusinessRuleViolation
from domain.shared_energy.calculator import SharedEnergyCalculator
from domain.shared_energy.sharing_interval import MemberSharingInterval


def make_interval():
    start = datetime(2026, 1, 1, 10, 0, tzinfo=UTC)

    return EnergyInterval(
        start=start,
        end=start + timedelta(minutes=15),
    )


def test_calculate_interval_uses_minimum():
    member_id = MemberId.generate()

    result = SharedEnergyCalculator().calculate_interval(
        member_id=member_id,
        interval=make_interval(),
        eligible_production=EnergyQuantity("10"),
        eligible_consumption=EnergyQuantity("6"),
    )

    assert isinstance(result, MemberSharingInterval)
    assert result.member_id == member_id
    assert result.shared_energy.value == Decimal("6")


def test_zero_production_produces_zero_shared_energy():
    result = SharedEnergyCalculator().calculate_interval(
        member_id=MemberId.generate(),
        interval=make_interval(),
        eligible_production=EnergyQuantity.zero(),
        eligible_consumption=EnergyQuantity("6"),
    )

    assert result.shared_energy.value == Decimal("0")


def test_zero_consumption_produces_zero_shared_energy():
    result = SharedEnergyCalculator().calculate_interval(
        member_id=MemberId.generate(),
        interval=make_interval(),
        eligible_production=EnergyQuantity("6"),
        eligible_consumption=EnergyQuantity.zero(),
    )

    assert result.shared_energy.value == Decimal("0")


def test_aggregate_sums_shared_energy():
    calculator = SharedEnergyCalculator()

    first = calculator.calculate_interval(
        member_id=MemberId.generate(),
        interval=make_interval(),
        eligible_production=EnergyQuantity("10"),
        eligible_consumption=EnergyQuantity("6"),
    )

    second = calculator.calculate_interval(
        member_id=MemberId.generate(),
        interval=make_interval(),
        eligible_production=EnergyQuantity("4"),
        eligible_consumption=EnergyQuantity("3"),
    )

    result = calculator.aggregate([first, second])

    assert result.value == Decimal("9")


def test_sharing_interval_rejects_shared_energy_above_production():
    with pytest.raises(
        BusinessRuleViolation,
        match="cannot exceed eligible production",
    ):
        MemberSharingInterval(
            member_id=MemberId.generate(),
            interval=make_interval(),
            eligible_production=EnergyQuantity("5"),
            eligible_consumption=EnergyQuantity("10"),
            shared_energy=EnergyQuantity("6"),
        )


def test_sharing_interval_rejects_shared_energy_above_consumption():
    with pytest.raises(
        BusinessRuleViolation,
        match="cannot exceed eligible consumption",
    ):
        MemberSharingInterval(
            member_id=MemberId.generate(),
            interval=make_interval(),
            eligible_production=EnergyQuantity("10"),
            eligible_consumption=EnergyQuantity("5"),
            shared_energy=EnergyQuantity("6"),
        )