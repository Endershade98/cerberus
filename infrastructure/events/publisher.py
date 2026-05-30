# infrastructure/events/publisher.py

class EventPublisher:

    def __init__(self, uow, dispatcher=None):
        self.uow = uow
        self.dispatcher = dispatcher

    def publish(self, events):
        if not events:
            return

        self.uow.collect(events)

        if self.dispatcher:
            for event in events:
                # FIX: usare dispatch o publish coerentemente
                self.dispatcher.dispatch(event)