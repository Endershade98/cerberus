# tests/unit/domain/incentive/test_incentive_calculator.py

from decimal import Decimal

from domain.incentive.calculator import IncentiveCalculator
from domain.incentive.value_objects import IncentiveRate
from domain.shared.energy import EnergyQuantity


def test_calculate_incentive_amount():
    result = IncentiveCalculator().calculate(
        eligible_energy=EnergyQuantity("100"),
        rate=IncentiveRate(Decimal("0.15")),
    )

    assert result.value == Decimal("15.00")
    assert result.currency.code == "EUR"


def test_calculate_zero_energy_returns_zero():
    result = IncentiveCalculator().calculate(
        eligible_energy=EnergyQuantity.zero(),
        rate=IncentiveRate(Decimal("0.15")),
    )

    assert result.value == Decimal("0.00")