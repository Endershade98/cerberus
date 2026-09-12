# tests/unit/domain/energy/test_energy_entity.py

from src.domain.energy.entities import EnergyRecord


def test_create_energy_record():
    record = EnergyRecord.create("1", 10.5)

    assert record.member_id == "1"
    assert record.quantity.value == 10.5