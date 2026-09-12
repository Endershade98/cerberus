# application/energy/dtos.py

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal



@dataclass(frozen=True)
class RecordEnergyRequest:

    asset_id: str
    timestamp: datetime
    production_kwh: Decimal
    consumption_kwh: Decimal



@dataclass(frozen=True)
class CalculateSharedEnergyRequest:

    start: datetime
    end: datetime



@dataclass(frozen=True)
class ValidateEnergyBatchRequest:

    batch_id: str