# domain/shared/events.py

from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import UUID, uuid4


# =========================
# Marker base event
# =========================
class DomainEvent:
    """
    Base marker for domain events (no metadata here).
    """


# =========================
# Metadata (infrastructure-safe)
# =========================
@dataclass(frozen=True)
class EventMetadata:
    event_id: UUID = field(default_factory=uuid4)
    occurred_on: datetime = field(default_factory=lambda: datetime.now(UTC))


# =========================
# Envelope (B OPTION CORE)
# =========================
@dataclass(frozen=True)
class EventEnvelope:
    metadata: EventMetadata
    payload: DomainEvent