# domain/energy/entities.py
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass
class EnergyRecord:
    member_id: int
    timestamp: datetime
    value_kwh: Decimal