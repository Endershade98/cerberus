# infrastructure/events/outbox/dispatcher.py

class OutboxDispatcher:

    def __init__(self, repo, bus):
        self.repo = repo
        self.bus = bus

    def dispatch_pending(self):
        events = self.repo.get_unprocessed()

        for outbox_event in events:
            self.bus.publish(outbox_event.payload)

            outbox_event.processed = True
            outbox_event.save()