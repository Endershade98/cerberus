# tests/unit/application/energy/test_aggregate_energy_data.py

from src.application.energy.aggregate_energy_data import (
    AggregateEnergyDataUseCase,
)

from tests.support.fake_uow import FakeUnitOfWork


def test_aggregate_energy_data():

    uow = FakeUnitOfWork()

    use_case = AggregateEnergyDataUseCase(
        uow=uow
    )

    result = use_case.execute()

    assert result is not None