# tests/unit/application/energy/test_calculate_shared.py

from unittest.mock import Mock
from application.energy.calculate_shared import CalculateSharedEnergyUseCase
from domain.energy.entities import EnergyRecord


def test_calculate_shared_energy_returns_total():

    uow = Mock()
    repo = Mock()

    uow.energy_repository = repo
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    repo.get_all.return_value = [
        EnergyRecord.create("1", 10.0),
        EnergyRecord.create("2", 20.0),
    ]

    use_case = CalculateSharedEnergyUseCase(uow)

    result = use_case.execute()

    assert result.value == 30.0