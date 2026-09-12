# application/energy/validate_energy_batch.py

from src.application.energy.dtos import ValidateEnergyBatchRequest


class ValidateEnergyBatch:


    def __init__(
        self,
        batch_repository,
        policy
    ):
        self.batch_repository = batch_repository
        self.policy = policy


    def execute(
        self,
        request
    ):

        batch = self.batch_repository.get(
            request.batch_id
        )


        self.policy.validate(batch)


        batch.validate()


        self.batch_repository.save(batch)


        return batch