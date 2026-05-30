# infrastructure/events/outbox/dispatcher.py

from django.db import transaction


class OutboxDispatcher:
    """
    Dispatches persisted outbox events
    """

    def __init__(self, repo, bus):
        self.repo = repo
        self.bus = bus

    def dispatch_pending(self):
        events = list(self.repo.get_unprocessed())

        for outbox_event in events:
            with transaction.atomic():
                self.bus.publish(outbox_event.payload)
                self.repo.mark_processed(outbox_event.id)