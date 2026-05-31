# domain/shared/aggregate_root.py

from dataclasses import dataclass, field
from typing import List
from uuid import UUID, uuid4

from domain.shared.domain_event import DomainEvent


@dataclass
class AggregateRoot:

    internal_id: UUID = field(default_factory=uuid4, init=False)

    _events: List[DomainEvent] = field(default_factory=list, init=False, repr=False)

    def add_event(self, event: DomainEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> list[DomainEvent]:
        events = list(self._events)
        self._events.clear()
        return events