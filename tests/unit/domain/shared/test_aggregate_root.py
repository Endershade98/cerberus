# tests/unit/domain/shared/test_aggregate_root.py

from domain.shared.aggregate_root import AggregateRoot, DomainEvent


class FakeEvent(DomainEvent):
    pass


def test_should_collect_domain_events():

    aggregate = AggregateRoot()

    event = FakeEvent()

    aggregate.add_event(event)

    events = aggregate.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], FakeEvent)


def test_should_clear_events_after_pull():

    aggregate = AggregateRoot()

    aggregate.add_event(FakeEvent())

    aggregate.pull_events()

    assert aggregate.pull_events() == []