# tests/integration/infrastructure/persistence/django/test_energy_repository.py

import pytest
from uuid import uuid4

from domain.energy.entities import EnergyRecord
from infrastructure.django_app.persistence.django.repositories.energy_repository import DjangoEnergyRepository


@pytest.mark.django_db
def test_energy_repository_persistence():

    repo = DjangoEnergyRepository()

    member_id = str(uuid4())

    record = EnergyRecord.create(
        member_id=member_id,
        kwh=10.5,
    )

    # FIX: usare save invece di add
    repo.save(record)

    results = repo.get_all()

    assert len(results) == 1

    saved = results[0]

    assert str(saved.member_id) == member_id
    assert float(saved.quantity.value) == 10.5