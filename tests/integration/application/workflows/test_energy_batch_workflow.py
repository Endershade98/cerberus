# tests/integration/application/workflows/test_energy_batch_workflow.py

from application.energy.validate_energy_batch import (
    ValidateEnergyBatchUseCase,
)

from application.energy.aggregate_energy_data import (
    AggregateEnergyDataUseCase,
)

from tests.support.fake_uow import FakeUnitOfWork


def test_energy_batch_workflow():

    uow = FakeUnitOfWork()

    ValidateEnergyBatchUseCase(
        uow=uow
    ).execute()

    result = AggregateEnergyDataUseCase(
        uow=uow
    ).execute()

    assert result is not None