# domain/energy/events.py

from dataclasses import dataclass

from src.domain.shared.domain_event import DomainEvent


@dataclass(frozen=True)
class EnergyRecorded(DomainEvent):

    record_id: str
    asset_id: str



@dataclass(frozen=True)
class EnergyValidated(DomainEvent):

    record_id: str



@dataclass(frozen=True)
class EnergyAggregationCompleted(DomainEvent):

    batch_id: str