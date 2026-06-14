# tests/integration/infrastructure/outbox/test_outbox_repository.py

import pytest
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timezone

from domain.shared.domain_event import DomainEvent
from infrastructure.django_app.outbox.repository import OutboxRepository


@dataclass(frozen=True)
class FakeEvent(DomainEvent):
    test: str = "value"

    def to_dict(self):
        return {"test": self.test}


@pytest.mark.django_db
def test_outbox_save_and_fetch():

    repo = OutboxRepository()

    event = FakeEvent()

    repo.save(event)

    pending = repo.get_unprocessed()

    assert pending.count() == 1

    stored = pending.first()

    assert stored.event_type == "FakeEvent"

    # FIX: payload include solo to_dict() oppure fallback serialize
    assert stored.payload["test"] == "value"