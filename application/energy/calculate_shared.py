# application/energy/calculate_shared.py

from domain.energy.services import EnergyDomainService


class CalculateSharedEnergyUseCase:

    def __init__(self, uow):
        self.uow = uow

    def execute(self):

        with self.uow:
            records = self.uow.energy_repository.get_all()
            total = EnergyDomainService.calculate_total(records)

        return total