# domain/shared/domain_event.py

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class DomainEvent:
    """
    Base class for all domain events.
    """

    event_id: UUID = field(default_factory=uuid4)
    occurred_on: datetime = field(default_factory=datetime.utcnow)