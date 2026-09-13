# tests/unit/domain/shared/test_domain_event.py

from datetime import UTC, datetime
from uuid import UUID

from domain.shared.domain_event import DomainEvent


def test_domain_event_generates_unique_id():
    first = DomainEvent()
    second = DomainEvent()

    assert isinstance(first.event_id, UUID)
    assert isinstance(second.event_id, UUID)
    assert first.event_id != second.event_id


def test_domain_event_has_utc_timestamp():
    event = DomainEvent()

    assert isinstance(event.occurred_on, datetime)
    assert event.occurred_on.tzinfo == UTC


def test_domain_event_is_immutable():
    event = DomainEvent()

    try:
        event.event_id = UUID(int=0)
    except AttributeError:
        pass
    else:
        raise AssertionError("DomainEvent must be immutable.")