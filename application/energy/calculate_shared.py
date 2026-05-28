# application/energy/calculate_shared.py

from domain.energy.services import EnergyProcessor

class CalculateSharedEnergyUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        records = self.repository.get_all()
        total_kwh = EnergyProcessor.calculate_total(records)
        return total_kwh