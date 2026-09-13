# application/energy/calculate_shared.py

from src.application.energy.dtos import (
    CalculateSharedEnergyRequest,
)

from domain.energy.aggregation_service import (
    EnergyAggregationService,
)



class CalculateSharedEnergyUseCase:


    def __init__(
        self,
        repository,
        service=None,
    ):

        self.repository = repository

        self.service = (
            service
            or EnergyAggregationService()
        )



    def execute(
        self,
        request: CalculateSharedEnergyRequest,
    ):


        records = self.repository.get_window(
            request.start,
            request.end
        )


        return self.service.shared_energy(
            records
        )