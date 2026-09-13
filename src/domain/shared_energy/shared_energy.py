# src/domain/shared_energy/shared_energy.py

from dataclasses import dataclass

from domain.community.value_objects import CerId
from domain.membership.value_objects import MemberId
from domain.shared.aggregate_root import AggregateRoot
from domain.shared.energy import EnergyQuantity
from domain.shared.exceptions import BusinessRuleViolation
from domain.shared_energy.events import SharedEnergyCalculated
from domain.shared_energy.value_objects import (
    CalculationPeriod,
    SharedEnergyId,
)


@dataclass
class SharedEnergy(AggregateRoot):
    id: SharedEnergyId
    cer_id: CerId
    member_id: MemberId
    calculation_period: CalculationPeriod
    eligible_production: EnergyQuantity
    eligible_consumption: EnergyQuantity
    shared_energy: EnergyQuantity

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)
        self._validate_invariants()

    @classmethod
    def calculate(
        cls,
        *,
        cer_id: CerId,
        member_id: MemberId,
        calculation_period: CalculationPeriod,
        eligible_production: EnergyQuantity,
        eligible_consumption: EnergyQuantity,
        shared_energy_id: SharedEnergyId | None = None,
    ) -> "SharedEnergy":
        shared_energy = eligible_production.min(
            eligible_consumption
        )

        aggregate = cls(
            id=shared_energy_id or SharedEnergyId.generate(),
            cer_id=cer_id,
            member_id=member_id,
            calculation_period=calculation_period,
            eligible_production=eligible_production,
            eligible_consumption=eligible_consumption,
            shared_energy=shared_energy,
        )

        aggregate.add_event(
            SharedEnergyCalculated(
                shared_energy_id=aggregate.id,
                cer_id=aggregate.cer_id,
                member_id=aggregate.member_id,
                calculation_period=aggregate.calculation_period,
                shared_energy=aggregate.shared_energy,
                eligible_production=aggregate.eligible_production,
                eligible_consumption=aggregate.eligible_consumption,
            )
        )

        return aggregate

    def _validate_invariants(self) -> None:
        if self.shared_energy.value > self.eligible_production.value:
            raise BusinessRuleViolation(
                "Shared energy cannot exceed eligible production."
            )

        if self.shared_energy.value > self.eligible_consumption.value:
            raise BusinessRuleViolation(
                "Shared energy cannot exceed eligible consumption."
            )