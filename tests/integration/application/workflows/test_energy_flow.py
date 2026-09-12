# tests/integration/application/workflows/test_energy_flow.py

import pytest
from uuid import uuid4

from src.application.energy.record_energy import RecordEnergyUseCase
from src.application.energy.calculate_shared import (
    CalculateSharedEnergyUseCase,
)


@pytest.mark.django_db
def test_energy_flow(uow):

    record_uc = RecordEnergyUseCase(uow)

    record_uc.execute(str(uuid4()), 10)
    record_uc.execute(str(uuid4()), 20)

    calculate_uc = CalculateSharedEnergyUseCase(uow)

    total = calculate_uc.execute()

    assert total.value == 30