# domain/shared/aggregate_root.py

from dataclasses import dataclass, field
from typing import List, Any
from uuid import UUID, uuid4


class DomainEvent:
    """Base class for all domain events."""
    pass


@dataclass
class AggregateRoot:
    """
    Base class for all Aggregate Roots.

    Responsibilities:
    - Identity
    - Domain events tracking
    """

    id: UUID = field(default_factory=uuid4, init=False)
    _events: List[DomainEvent] = field(default_factory=list, init=False, repr=False)

    def add_event(self, event: DomainEvent):
        self._events.append(event)

    def pull_events(self) -> List[DomainEvent]:
        events = self._events[:]
        self._events.clear()
        return events