# tests/unit/application/energy/test_validate_energy_batch.py

from application.energy.validate_energy_batch import (
    ValidateEnergyBatchUseCase,
)

from tests.support.fake_uow import FakeUnitOfWork


def test_validate_energy_batch():

    uow = FakeUnitOfWork()

    use_case = ValidateEnergyBatchUseCase(
        uow=uow
    )

    result = use_case.execute()

    assert result is True