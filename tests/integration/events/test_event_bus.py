# tests/integration/events/test_event_bus.py

class FakeBus:
    def __init__(self):
        self.events = []

    def publish(self, event):
        self.events.append(event)


def test_event_dispatch():

    from infrastructure.events.dispatcher import EventDispatcher

    bus = FakeBus()
    dispatcher = EventDispatcher(bus)

    dispatcher.dispatch({"type": "TEST"})

    assert len(bus.events) == 1