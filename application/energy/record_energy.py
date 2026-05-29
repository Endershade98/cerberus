# application/energy/record_energy.py

from datetime import datetime
from domain.energy.entities import EnergyRecord
from domain.shared.value_objects import EnergyQuantity
from domain.member.value_objects import MemberId


class RecordEnergyUseCase:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, member_id: int, kwh: float):

        record = EnergyRecord(
            member_id=MemberId(member_id),
            timestamp=datetime.now(),
            quantity=EnergyQuantity(kwh),
        )

        self.repository.save(record)
        return record