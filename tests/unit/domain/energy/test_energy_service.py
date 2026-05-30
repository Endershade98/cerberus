# tests/unit/domain/energy/test_energy_service.py

from domain.energy.entities import EnergyRecord


def test_should_calculate_total_energy():

    records = [
        EnergyRecord.create(member_id="1", kwh=10.0),
        EnergyRecord.create(member_id="2", kwh=20.0),
    ]

    assert sum(r.quantity.value for r in records) == 30.0