# domain/energy/entities.py

from domain.shared.aggregate_root import AggregateRoot
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class EnergyRecord(AggregateRoot):
    member_id: int
    timestamp: datetime
    value_kwh: Decimal