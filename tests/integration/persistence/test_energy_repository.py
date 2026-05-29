# tests/integration/persistence/test_energy_repository.py

import pytest
from domain.energy.entities import EnergyRecord
from domain.shared.value_objects import EnergyQuantity
from infrastructure.persistence.django.repositories.energy_repository import DjangoEnergyRepository


@pytest.mark.django_db
def test_save_and_get_energy_record():

    repo = DjangoEnergyRepository()

    record = EnergyRecord(
        member_id="123e4567-e89b-12d3-a456-426614174000",
        quantity=EnergyQuantity(10.5),
        timestamp=None,
    )

    repo.save(record)

    all_records = repo.get_all()

    assert len(all_records) == 1
    assert float(all_records[0].quantity.value) == 10.5