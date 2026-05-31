# tests/unit/application/energy/test_record_energy.py

from unittest.mock import Mock
from application.energy.record_energy import RecordEnergyUseCase


def test_record_energy_persists_record():

    uow = Mock()
    repo = Mock()

    uow.energy_repository = repo
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    use_case = RecordEnergyUseCase(uow)

    record = use_case.execute(member_id="1", kwh=10.5)

    repo.save.assert_called_once()
    assert record.member_id == "1"
    assert record.quantity.value == 10.5