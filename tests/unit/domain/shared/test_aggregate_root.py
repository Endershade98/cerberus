# tests/unit/domain/shared/test_aggregate_root.py

from dataclasses import dataclass

from domain.shared.aggregate_root import AggregateRoot
from domain.shared.domain_event import DomainEvent


@dataclass(frozen=True)
class DummyEvent(DomainEvent):
    pass


@dataclass
class DummyAggregate(AggregateRoot):
    pass


def test_aggregate_starts_without_events():
    aggregate = DummyAggregate()

    assert aggregate.pull_events() == []


def test_add_event_stores_event():
    aggregate = DummyAggregate()
    event = DummyEvent()

    aggregate.add_event(event)

    assert aggregate.pull_events() == [event]


def test_pull_events_clears_event_queue():
    aggregate = DummyAggregate()
    event = DummyEvent()

    aggregate.add_event(event)

    assert aggregate.pull_events() == [event]
    assert aggregate.pull_events() == []