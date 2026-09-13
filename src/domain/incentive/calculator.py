# src/domain/incentive/calculator.py

from domain.incentive.value_objects import IncentiveRate
from domain.shared.energy import EnergyQuantity
from domain.shared.money import MoneyAmount


class IncentiveCalculator:

    def calculate(
        self,
        *,
        eligible_energy: EnergyQuantity,
        rate: IncentiveRate,
    ) -> MoneyAmount:
        return rate.calculate(eligible_energy)