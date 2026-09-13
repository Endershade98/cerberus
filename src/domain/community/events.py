# src/domain/community/events.py

from dataclasses import dataclass

from domain.community.value_objects import CerId
from domain.shared.domain_event import DomainEvent


@dataclass(frozen=True, kw_only=True)
class CerCreated(DomainEvent):
    cer_id: CerId  # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class CerActivated(DomainEvent):
    cer_id: CerId  # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class CerSuspended(DomainEvent):
    cer_id: CerId  # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class CerClosed(DomainEvent):
    cer_id: CerId  # type: ignore[assignment]