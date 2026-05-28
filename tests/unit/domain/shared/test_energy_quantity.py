# tests/unit/domain/shared/test_energy_quantity.py

from decimal import Decimal

from domain.shared.value_objects import EnergyQuantity


def test_should_sum_energy_quantities():

    q1 = EnergyQuantity(Decimal("10"))
    q2 = EnergyQuantity(Decimal("5"))

    result = q1 + q2

    assert result.value == Decimal("15")