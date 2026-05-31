# application/energy/calculate_shared.py

from domain.energy.services import EnergyDomainService
from application.common.use_case import UseCase


class CalculateSharedEnergyUseCase(UseCase):

    def _execute(self):

        records = self.uow.energy_repository.get_all()

        return EnergyDomainService.calculate_total(records)