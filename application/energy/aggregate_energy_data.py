# application/energy/aggregate_energy_data.py

from dataclasses import dataclass

from application.common.use_case import UseCase

from domain.energy.aggregation_service import (
    EnergyAggregationService,
)


@dataclass(frozen=True)
class AggregateEnergyDataRequest:

    batch_id: str



@dataclass(frozen=True)
class AggregateEnergyDataResponse:

    total_energy: object



class AggregateEnergyDataUseCase(
    UseCase[
        AggregateEnergyDataRequest,
        AggregateEnergyDataResponse,
    ]
):


    def __init__(
        self,
        uow,
        aggregation_service,
    ):

        super().__init__(uow)

        self.service = aggregation_service



    def _execute(
        self,
        request,
    ):

        records = (
            self.uow.energy_repository
            .get_batch_records(
                request.batch_id
            )
        )


        total = (
            self.service.total(records)
        )


        return AggregateEnergyDataResponse(
            total
        )