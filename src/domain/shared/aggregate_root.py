# src/domain/shared/aggregate_root.py

from domain.shared.domain_event import DomainEvent


class AggregateRoot:
    """
    Base class for domain aggregates.

    Business identity belongs to the concrete aggregate.
    This class only manages domain events.
    """

    def __init__(self) -> None:
        self._events: list[DomainEvent] = []

    def add_event(self, event: DomainEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> list[DomainEvent]:
        events = self._events.copy()
        self._events.clear()
        return events