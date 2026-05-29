# application/energy/record_energy.py

from domain.energy.entities import EnergyRecord


class RecordEnergy:

    def __init__(self, uow):
        self.uow = uow

    def execute(self, member_id: str, kwh: float):

        record = EnergyRecord.create(
            member_id=member_id,
            kwh=kwh
        )

        with self.uow:
            self.uow.energy_repository.add(record)
            self.uow.commit()

        return record