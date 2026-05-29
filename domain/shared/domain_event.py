# domain/shared/domain_event.py

from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import UUID, uuid4


@dataclass(frozen=True)
class DomainEvent:
    """
    Base immutable domain event.
    """

    event_id: UUID = field(
        default_factory=uuid4,
        init=False,
    )

    occurred_on: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        init=False,
    )