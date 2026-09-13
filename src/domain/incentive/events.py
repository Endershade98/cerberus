# src/domain/incentive/events.py

from dataclasses import dataclass

from domain.community.value_objects import CerId
from domain.incentive.value_objects import IncentiveId, IncentiveRate
from domain.membership.value_objects import MemberId
from domain.shared.domain_event import DomainEvent
from domain.shared.energy import EnergyQuantity
from domain.shared.money import MoneyAmount


@dataclass(frozen=True, kw_only=True)
class IncentiveCalculated(DomainEvent):
    incentive_id: IncentiveId # type: ignore[assignment]
    cer_id: CerId # type: ignore[assignment]
    member_id: MemberId # type: ignore[assignment]
    eligible_energy: EnergyQuantity # type: ignore[assignment]
    rate: IncentiveRate # type: ignore[assignment]
    amount: MoneyAmount # type: ignore[assignment]