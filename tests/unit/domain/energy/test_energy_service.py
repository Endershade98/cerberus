# tests/unit/domain/energy/test_energy_service.py

from src.domain.energy.entities import EnergyRecord
from src.domain.energy.services import EnergyDomainService


def test_should_sum_energy_records():
    records = [
        EnergyRecord.create("1", 10),
        EnergyRecord.create("2", 20),
    ]

    result = EnergyDomainService.calculate_total(records)

    assert result.value == 30