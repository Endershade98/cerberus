# domain/energy/services.py

from domain.energy.value_objects import EnergyQuantity


class EnergyDomainService:

    @staticmethod
    def calculate_total(records) -> EnergyQuantity:
        return EnergyQuantity(
            sum(r.quantity.value for r in records)
        )