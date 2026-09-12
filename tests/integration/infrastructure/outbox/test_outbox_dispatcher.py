# tests/integration/infrastructure/outbox/test_outbox_dispatcher.py

import pytest
from dataclasses import dataclass

from infrastructure.django_app.outbox.dispatcher import OutboxDispatcher


@dataclass
class DummyEvent:
    x: int


class FakeRegistry:

    def get(self, name):
        return DummyEvent


class FakeRepo:

    def __init__(self):
        self.events = []
        self.marked = []

    def get_unprocessed(self):
        return self.events

    def mark_processed(self, event_id):
        self.marked.append(event_id)


class FakeBus:

    def __init__(self):
        self.published = []

    def publish(self, event):
        self.published.append(event)


@pytest.mark.django_db
def test_outbox_dispatcher_flow():

    repo = FakeRepo()
    bus = FakeBus()

    dispatcher = OutboxDispatcher(
        repo,
        bus,
        FakeRegistry(),
    )

    class OutboxDummy:

        id = "1"
        event_type = "DummyEvent"
        payload = {
            "x": 1
        }

    repo.events = [
        OutboxDummy()
    ]

    dispatcher.dispatch_pending()

    assert len(bus.published) == 1

    assert isinstance(
        bus.published[0],
        DummyEvent
    )

    assert bus.published[0].x == 1

    assert repo.marked == [
        "1"
    ]