# src/domain/energy/events.py

from dataclasses import dataclass

from domain.energy.value_objects import (
    EnergyBatchId,
    EnergyReadingId,
)
from domain.shared.domain_event import DomainEvent


@dataclass(frozen=True, kw_only=True)
class EnergyReadingRecorded(DomainEvent):
    reading_id: EnergyReadingId  # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class EnergyBatchReceived(DomainEvent):
    batch_id: EnergyBatchId  # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class EnergyBatchValidated(DomainEvent):
    batch_id: EnergyBatchId  # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class EnergyBatchRejected(DomainEvent):
    batch_id: EnergyBatchId # type: ignore[assignment]