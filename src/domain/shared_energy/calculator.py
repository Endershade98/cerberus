# src/domain/shared_energy/calculator.py

from domain.shared.energy import EnergyQuantity
from domain.shared.exceptions import BusinessRuleViolation
from domain.shared_energy.sharing_interval import MemberSharingInterval


class SharedEnergyCalculator:
    """
    Calculates shared energy for a single member and interval.

    Shared energy is limited by both eligible production
    and eligible consumption.
    """

    def calculate_interval(
        self,
        *,
        member_id,
        interval,
        eligible_production: EnergyQuantity,
        eligible_consumption: EnergyQuantity,
    ) -> MemberSharingInterval:
        if eligible_production.value < 0:
            raise BusinessRuleViolation(
                "Eligible production cannot be negative."
            )

        if eligible_consumption.value < 0:
            raise BusinessRuleViolation(
                "Eligible consumption cannot be negative."
            )

        shared = eligible_production.min(
            eligible_consumption
        )

        return MemberSharingInterval(
            member_id=member_id,
            interval=interval,
            eligible_production=eligible_production,
            eligible_consumption=eligible_consumption,
            shared_energy=shared,
        )

    def aggregate(
        self,
        intervals: list[MemberSharingInterval],
    ) -> EnergyQuantity:
        total = EnergyQuantity.zero()

        for interval in intervals:
            total = total.add(interval.shared_energy)

        return total