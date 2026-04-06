# domain/energy/services.py
from domain.energy.entities import EnergyRecord
from domain.energy.status import EnergyStatus
from decimal import Decimal

class EnergyProcessor:
    @staticmethod
    def calculate_total(records: list[EnergyRecord]) -> Decimal:
        return sum(r.value_kwh for r in records)
    
    @staticmethod
    def mark_processed(record: EnergyRecord) -> dict:
        return {"member_id": record.member_id, "status": EnergyStatus.PROCESSED}