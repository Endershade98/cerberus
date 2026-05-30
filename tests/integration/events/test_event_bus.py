# tests/integration/events/test_event_bus.py

from infrastructure.events.dispatcher import EventDispatcher


class TestEvent:
    pass


class FakeBus:
    def __init__(self):
        self.events = []

    def publish(self, event):
        self.events.append(event)


def test_event_dispatch():

    bus = FakeBus()
    dispatcher = EventDispatcher(bus)

    event = TestEvent()

    dispatcher.dispatch(event)

    assert len(bus.events) == 1
    assert isinstance(bus.events[0], TestEvent)