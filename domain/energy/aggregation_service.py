# domain/energy/aggregation_service.py

from domain.energy.value_objects import EnergyQuantity
from domain.energy.value_objects import FlowDirection


class EnergyAggregationService:


    @staticmethod
    def total(records):

        return EnergyQuantity(
            sum(
                r.quantity.value
                for r in records
            )
        )


    @staticmethod
    def shared_energy(records):

        production = sum(
            r.quantity.value
            for r in records
            if r.direction == FlowDirection.PRODUCTION
        )


        consumption = sum(
            r.quantity.value
            for r in records
            if r.direction == FlowDirection.CONSUMPTION
        )


        return EnergyQuantity(
            min(
                production,
                consumption
            )
        )