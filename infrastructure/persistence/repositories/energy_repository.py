# infrastructure/persistence/repositories/energy_repository.py
from infrastructure.persistence.models.energy import EnergyModel
from domain.energy.entities import EnergyRecord
from datetime import datetime
from decimal import Decimal

class EnergyRepository:
    def save(self, record: EnergyRecord):
        EnergyModel.objects.create(
            member_id=record.member_id,
            timestamp=record.timestamp,
            value_kwh=record.value_kwh
        )

    def get_all(self) -> list[EnergyRecord]:
        return [
            EnergyRecord(member_id=e.member_id, timestamp=e.timestamp, value_kwh=e.value_kwh)
            for e in EnergyModel.objects.all()
        ]