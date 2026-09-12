# tests/integration/infrastructure/events/test_event_dispatcher.py

from src.infrastructure.django_app.events.dispatcher import EventDispatcher


class FakeBus:
    def __init__(self):
        self.published = []

    def publish(self, event):
        self.published.append(event)


class DummyEvent:
    pass


def test_event_dispatcher():

    bus = FakeBus()
    dispatcher = EventDispatcher(bus)

    event = DummyEvent()

    dispatcher.dispatch(event)

    assert bus.published == [event]