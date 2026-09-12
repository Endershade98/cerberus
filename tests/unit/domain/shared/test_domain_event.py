# tests/unit/domain/shared/test_domain_event.py

from src.domain.shared.domain_event import DomainEvent


def test_event_has_id_and_timestamp():
    e = DomainEvent()

    assert e.event_id is not None
    assert e.occurred_on is not None