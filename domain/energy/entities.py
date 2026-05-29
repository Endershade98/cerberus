# domain/energy/entities.py

from dataclasses import dataclass
from uuid import UUID, uuid4

from domain.shared.value_objects import EnergyQuantity



@dataclass
class EnergyRecord:
    id: UUID
    member_id: UUID
    value_kwh: EnergyQuantity

    @staticmethod
    def create(member_id: UUID, kwh: float):
        return EnergyRecord(
            id=uuid4(),
            member_id=member_id,
            value_kwh=EnergyQuantity(kwh),
        )