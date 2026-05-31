# domain/energy/entities.py

from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from domain.energy.value_objects import EnergyQuantity
from domain.shared.time_provider import TimeProvider
from domain.shared.id_provider import IdProvider

time_provider = TimeProvider()
id_provider = IdProvider()

@dataclass
class EnergyRecord:

    id: str
    member_id: str
    quantity: EnergyQuantity
    recorded_at: datetime

    @staticmethod
    def create(member_id: str, kwh: float) -> "EnergyRecord":

        return EnergyRecord(
            id=id_provider.generate(),
            member_id=str(member_id),
            quantity=EnergyQuantity(kwh),
            recorded_at=time_provider.now()
        )