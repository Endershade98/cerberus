# tests/unit/application/energy/test_calculate_shared.py

from unittest.mock import Mock
from application.energy.calculate_shared import CalculateSharedEnergyUseCase


def test_calculate_shared_energy():

    repo = Mock()
    repo.get_all = Mock(return_value=[
        Mock(value_kwh=10),
        Mock(value_kwh=15),
    ])

    use_case = CalculateSharedEnergyUseCase(repo)

    result = use_case.execute()

    assert result.value == 25