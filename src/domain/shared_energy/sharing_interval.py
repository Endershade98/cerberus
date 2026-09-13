# src/domain/shared_energy/sharing_interval.py

from dataclasses import dataclass

from domain.energy.value_objects import EnergyInterval
from domain.membership.value_objects import MemberId
from domain.shared.energy import EnergyQuantity
from domain.shared.exceptions import BusinessRuleViolation


@dataclass(frozen=True)
class MemberSharingInterval:
    member_id: MemberId
    interval: EnergyInterval
    eligible_production: EnergyQuantity
    eligible_consumption: EnergyQuantity
    shared_energy: EnergyQuantity

    def __post_init__(self) -> None:
        if self.shared_energy.value > self.eligible_production.value:
            raise BusinessRuleViolation(
                "Shared energy cannot exceed eligible production."
            )

        if self.shared_energy.value > self.eligible_consumption.value:
            raise BusinessRuleViolation(
                "Shared energy cannot exceed eligible consumption."
            )