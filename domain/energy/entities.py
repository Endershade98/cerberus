# domain/energy/entities.py

from dataclasses import dataclass
from datetime import datetime

from domain.shared.aggregate_root import AggregateRoot
from domain.shared.value_objects import EnergyQuantity
from domain.member.value_objects import MemberId


@dataclass
class EnergyRecord(AggregateRoot):

    member_id: MemberId
    timestamp: datetime
    quantity: EnergyQuantity

    def energy(self) -> EnergyQuantity:
        return self.quantity