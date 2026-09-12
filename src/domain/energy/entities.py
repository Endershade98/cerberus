# domain/energy/entities.py

from dataclasses import dataclass
from datetime import datetime

from src.domain.energy.value_objects import (
    EnergyQuantity,
    FlowDirection,
)
from src.domain.shared.aggregate_root import AggregateRoot
from src.domain.shared.id_provider import IdProvider
from src.domain.shared.time_provider import TimeProvider


id_provider = IdProvider()
time_provider = TimeProvider()


@dataclass
class EnergyRecord(AggregateRoot):

    id: str
    asset_id: str
    timestamp: datetime
    quantity: EnergyQuantity
    direction: FlowDirection


    @staticmethod
    def create(
        asset_id: str,
        timestamp: datetime,
        production: EnergyQuantity,
        consumption: EnergyQuantity,
    ):

        if production.value > 0:

            return EnergyRecord(
                id=id_provider.generate(),
                asset_id=asset_id,
                timestamp=timestamp,
                quantity=production,
                direction=FlowDirection.PRODUCTION,
            )

        return EnergyRecord(
            id=id_provider.generate(),
            asset_id=asset_id,
            timestamp=timestamp,
            quantity=consumption,
            direction=FlowDirection.CONSUMPTION,
        )