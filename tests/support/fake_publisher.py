# tests/support/fake_publisher.py

from domain.shared.event_publisher import EventPublisher


class FakePublisher(EventPublisher):

    def __init__(self):
        self.events = []

    def publish(self, events):
        self.events.extend(events)