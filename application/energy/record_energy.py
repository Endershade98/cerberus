# application/energy/record_energy.py

from datetime import datetime
from domain.energy.entities import EnergyRecord
from domain.energy.services import EnergyProcessor

class RecordEnergyUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, member_id: int, kwh: float):
        record = EnergyRecord(member_id=member_id, timestamp=datetime.now(), value_kwh=kwh)
        self.repository.save(record)
        return record