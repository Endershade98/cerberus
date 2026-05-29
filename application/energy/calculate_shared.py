# application/energy/calculate_shared.py

from domain.energy.services import EnergyDomainService


class CalculateSharedEnergyUseCase:

    def __init__(self, repository):
        self.repository = repository

    def execute(self):

        records = self.repository.get_all()

        total = EnergyDomainService.calculate_total(records)

        return total