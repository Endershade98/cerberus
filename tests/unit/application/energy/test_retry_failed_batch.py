# tests/unit/application/energy/test_retry_failed_batch.py

from src.application.energy.retry_failed_batch import (
    RetryFailedBatchUseCase,
)

from tests.support.fake_uow import FakeUnitOfWork


def test_retry_failed_batch():

    uow = FakeUnitOfWork()

    use_case = RetryFailedBatchUseCase(
        uow=uow
    )

    result = use_case.execute()

    assert result is True