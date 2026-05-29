# infrastructure/events/publisher.py

class EventPublisher:
    """
    Publishes domain events via dispatcher
    """

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def publish(self, events):
        for event in events:
            self.dispatcher.dispatch(event)