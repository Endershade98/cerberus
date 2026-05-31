# tests/unit/domain/energy/test_energy_value_objects.py

import pytest

from domain.energy.value_objects import EnergyQuantity


def test_should_create_quantity():
    q = EnergyQuantity(10)
    assert q.value == 10


def test_should_not_allow_negative():
    with pytest.raises(ValueError):
        EnergyQuantity(-1)


def test_should_sum_quantities():
    assert (EnergyQuantity(10) + EnergyQuantity(5)).value == 15


def test_should_zero():
    assert EnergyQuantity.zero().value == 0