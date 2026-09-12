# application/energy/record_energy.py

from src.application.energy.dtos import RecordEnergyRequest

from src.domain.energy.entities import EnergyRecord
from src.domain.energy.events import EnergyRecorded
from src.domain.energy.value_objects import EnergyQuantity



class RecordEnergyUseCase:


    def __init__(
        self,
        repository,
        uow,
        publisher,
    ):

        self.repository = repository
        self.uow = uow
        self.publisher = publisher



    def execute(
        self,
        request: RecordEnergyRequest,
    ):

        record = EnergyRecord.create(
            asset_id=request.asset_id,
            timestamp=request.timestamp,
            production=EnergyQuantity(
                float(request.production_kwh)
            ),
            consumption=EnergyQuantity(
                float(request.consumption_kwh)
            ),
        )


        with self.uow:

            self.repository.save(record)


            self.publisher.publish(
                [
                    EnergyRecorded(
                        record.id,
                        record.asset_id
                    )
                ]
            )


        return record