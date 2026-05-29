# tests/integration/events/test_outbox_repository.py

import uuid
from infrastructure.events.outbox.repository import OutboxRepository
from infrastructure.events.outbox.models import OutboxEvent


class DummyEvent:
    def __init__(self):
        self.id = uuid.uuid4()
        self.occurred_on = "2025-01-01T00:00:00"
    
    def to_dict(self):
        return {"foo": "bar"}


def test_save_outbox_event(db):

    repo = OutboxRepository()

    event = DummyEvent()

    repo.save(event)

    assert OutboxEvent.objects.count() == 1