# tests/unit/application/energy/test_record_energy.py

from unittest.mock import Mock
from application.energy.record_energy import RecordEnergyUseCase


def test_record_energy():

    uow = Mock()
    repo = Mock()
    uow.energy_repository = repo

    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    use_case = RecordEnergyUseCase(uow)

    result = use_case.execute(member_id=1, kwh=10.5)

    repo.add.assert_called_once()
    uow.commit.assert_called_once()

    assert result.member_id == 1
    assert result.quantity.value == 10.5