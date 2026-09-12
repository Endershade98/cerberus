# infrastructure/django_app/outbox/dispatcher.py

from django.db import transaction


class OutboxDispatcher:

    def __init__(self, repo, bus, registry=None):
        self.repo = repo
        self.bus = bus
        self.registry = registry or {}

    def dispatch_pending(self):
        events = list(self.repo.get_unprocessed())

        for outbox_event in events:
            with transaction.atomic():

                event_class = self.registry.get(outbox_event.event_type)

                if not event_class:
                    raise ValueError(
                        f"Unknown event type: {outbox_event.event_type}"
                    )

                event = event_class(**outbox_event.payload)

                self.bus.publish(event)

                self.repo.mark_processed(outbox_event.id)