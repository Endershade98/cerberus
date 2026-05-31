# tests/unit/domain/shared/test_aggregate_root.py

from domain.shared.aggregate_root import AggregateRoot
from domain.shared.domain_event import DomainEvent


class FakeEvent(DomainEvent):
    pass


def test_should_collect_events():
    agg = AggregateRoot()
    agg.add_event(FakeEvent())

    assert len(agg.pull_events()) == 1


def test_should_clear_events():
    agg = AggregateRoot()
    agg.add_event(FakeEvent())

    agg.pull_events()

    assert agg.pull_events() == []