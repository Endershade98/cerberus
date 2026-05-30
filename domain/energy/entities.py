# domain/energy/entities.py

from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from domain.energy.value_objects import EnergyQuantity


@dataclass
class EnergyRecord:

    id: str
    member_id: str
    quantity: EnergyQuantity
    recorded_at: datetime

    @staticmethod
    def create(member_id: str, kwh: float) -> "EnergyRecord":

        return EnergyRecord(
            id=str(uuid4()),
            member_id=member_id,
            quantity=EnergyQuantity(kwh),
            recorded_at=datetime.utcnow(),
        )