# src/domain/incentive/incentive.py

from dataclasses import dataclass

from domain.community.value_objects import CerId
from domain.incentive.events import IncentiveCalculated
from domain.incentive.value_objects import IncentiveId, IncentiveRate
from domain.membership.value_objects import MemberId
from domain.shared.aggregate_root import AggregateRoot
from domain.shared.energy import EnergyQuantity
from domain.shared.money import MoneyAmount
from domain.shared_energy.value_objects import (
    CalculationPeriod,
    SharedEnergyId,
)


@dataclass(frozen=True)
class SharedEnergyReference:
    shared_energy_id: SharedEnergyId


@dataclass
class Incentive(AggregateRoot):
    id: IncentiveId
    cer_id: CerId
    member_id: MemberId
    reference_period: CalculationPeriod
    shared_energy_reference: SharedEnergyReference
    eligible_energy: EnergyQuantity
    rate: IncentiveRate
    amount: MoneyAmount

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

    @classmethod
    def calculate(
        cls,
        *,
        cer_id: CerId,
        member_id: MemberId,
        reference_period: CalculationPeriod,
        shared_energy_reference: SharedEnergyReference,
        eligible_energy: EnergyQuantity,
        rate: IncentiveRate,
        incentive_id: IncentiveId | None = None,
    ) -> "Incentive":
        amount = rate.calculate(eligible_energy)

        aggregate = cls(
            id=incentive_id or IncentiveId.generate(),
            cer_id=cer_id,
            member_id=member_id,
            reference_period=reference_period,
            shared_energy_reference=shared_energy_reference,
            eligible_energy=eligible_energy,
            rate=rate,
            amount=amount,
        )

        aggregate.add_event(
            IncentiveCalculated(
                incentive_id=aggregate.id,
                cer_id=aggregate.cer_id,
                member_id=aggregate.member_id,
                eligible_energy=aggregate.eligible_energy,
                rate=aggregate.rate,
                amount=aggregate.amount,
            )
        )

        return aggregate