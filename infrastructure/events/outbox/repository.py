# infrastructure/events/outbox/repository.py

from infrastructure.events.outbox.models import OutboxEvent


class OutboxRepository:

    def save(self, event):
        OutboxEvent.objects.create(
            id=event.id,
            event_type=event.__class__.__name__,
            payload=event.to_dict(),
            occurred_on=event.occurred_on,
            processed=False,
        )

    def get_unprocessed(self):
        return OutboxEvent.objects.filter(processed=False)