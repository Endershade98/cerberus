# domain/energy/services.py

from domain.energy.entities import EnergyRecord
from domain.shared.value_objects import EnergyQuantity
from functools import reduce



class EnergyDomainService:

    @staticmethod
    def calculate_total(records):
        return reduce(
            lambda acc, r: acc + EnergyQuantity(r.value_kwh),
            records,
            EnergyQuantity(0)
        )