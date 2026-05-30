# tests/unit/application/energy/test_calculate_shared.py

from domain.energy.entities import EnergyRecord


def test_calculate_shared_energy():

    record = EnergyRecord.create(
        member_id=1,
        kwh=10.0
    )

    assert record.quantity.value == 10.0