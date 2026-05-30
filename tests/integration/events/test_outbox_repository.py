# tests/integration/events/test_outbox_repository.py

import uuid
from datetime import datetime
import pytest

from infrastructure.events.outbox.repository import OutboxRepository
from infrastructure.events.outbox.models import OutboxEvent


class DummyEvent:
    def __init__(self):
        self.id = uuid.uuid4()
        self.occurred_on = datetime.utcnow()

    def to_dict(self):
        return {"foo": "bar"}


@pytest.mark.django_db
def test_save_outbox_event():

    repo = OutboxRepository()
    event = DummyEvent()

    repo.save(event)

    assert OutboxEvent.objects.count() == 1

    saved = OutboxEvent.objects.first()

    assert saved.payload == {"foo": "bar"}
    assert saved.processed is False