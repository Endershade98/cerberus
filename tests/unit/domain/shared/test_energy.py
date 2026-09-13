# tests/unit/domain/shared/test_energy.py

from decimal import Decimal

import pytest

from domain.shared.energy import EnergyQuantity


def test_energy_quantity_normalizes_decimal():
    quantity = EnergyQuantity("10.50")

    assert quantity.value == Decimal("10.50")


def test_energy_quantity_rejects_negative_value():
    with pytest.raises(ValueError, match="cannot be negative"):
        EnergyQuantity("-1")


def test_zero_returns_zero_quantity():
    quantity = EnergyQuantity.zero()

    assert quantity.value == Decimal("0")


def test_add_returns_sum():
    first = EnergyQuantity("10")
    second = EnergyQuantity("2.5")

    result = first.add(second)

    assert result.value == Decimal("12.5")


def test_subtract_returns_difference():
    first = EnergyQuantity("10")
    second = EnergyQuantity("2.5")

    result = first.subtract(second)

    assert result.value == Decimal("7.5")


def test_subtract_rejects_negative_result():
    with pytest.raises(ValueError, match="cannot become negative"):
        EnergyQuantity("2").subtract(EnergyQuantity("3"))


def test_min_returns_lower_quantity():
    first = EnergyQuantity("10")
    second = EnergyQuantity("7")

    result = first.min(second)

    assert result.value == Decimal("7")