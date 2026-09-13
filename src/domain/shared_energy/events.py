# src/domain/shared_energy/events.py

from dataclasses import dataclass

from domain.community.value_objects import CerId
from domain.membership.value_objects import MemberId
from domain.shared.domain_event import DomainEvent
from domain.shared.energy import EnergyQuantity
from domain.shared_energy.value_objects import (
    CalculationPeriod,
    SharedEnergyId,
)


@dataclass(frozen=True, kw_only=True)
class SharedEnergyCalculated(DomainEvent):
    shared_energy_id: SharedEnergyId # type: ignore[assignment]
    cer_id: CerId # type: ignore[assignment]
    member_id: MemberId # type: ignore[assignment]
    calculation_period: CalculationPeriod  # type: ignore[assignment]
    shared_energy: EnergyQuantity # type: ignore[assignment]
    eligible_production: EnergyQuantity  # type: ignore[assignment]
    eligible_consumption: EnergyQuantity # type: ignore[assignment]