# application/energy/record_energy.py

from domain.energy.entities import EnergyRecord
from application.common.use_case import UseCase


class RecordEnergyUseCase(UseCase):

    def _execute(self, member_id: str, kwh: float):

        record = EnergyRecord.create(
            member_id=member_id,
            kwh=kwh
        )

        self.uow.energy_repository.save(record)

        return record