# application/energy/retry_failed_batch.py

from src.application.energy.dtos import RetryFailedBatchRequest


class RetryFailedBatch:


    def __init__(
        self,
        repository
    ):
        self.repository = repository


    def execute(
        self,
        request: RetryFailedBatchRequest
    ):

        batch = self.repository.get(
            request.batch_id
        )


        batch.retry()


        self.repository.save(batch)


        return batch