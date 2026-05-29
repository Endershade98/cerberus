# domain/energy/services.py

from functools import reduce
from domain.shared.value_objects import EnergyQuantity


class EnergyDomainService:

    @staticmethod
    def calculate_total(records):

        return reduce(
            lambda acc, r: acc + EnergyQuantity(r.value_kwh),
            records,
            EnergyQuantity(0)
        )