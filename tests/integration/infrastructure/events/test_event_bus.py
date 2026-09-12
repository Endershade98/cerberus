# tests/integration/infrastructure/events/test_event_bus.py

from src.infrastructure.django_app.events.bus import EventBus


class DummyEvent:
    pass


def test_event_bus_dispatch():

    bus = EventBus()

    called = []

    def handler(event):
        called.append(event)

    bus.register(DummyEvent, handler)

    event = DummyEvent()

    bus.publish(event)

    assert len(called) == 1
    assert called[0] == event