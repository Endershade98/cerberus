# tests/unit/application/energy/test_record_energy.py

from unittest.mock import Mock
from application.energy.record_energy import RecordEnergyUseCase


def test_record_energy():

    repo = Mock()
    use_case = RecordEnergyUseCase(repo)

    result = use_case.execute(member_id=1, kwh=10.5)

    repo.save.assert_called_once()

    assert result.member_id.value == 1
    assert result.quantity.value == 10.5