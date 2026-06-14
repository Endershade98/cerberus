# infrastructure/django_app/outbox/repository.py

from infrastructure.persistence.django.models import OutboxEvent


class OutboxRepository:

    def save(self, event):
        OutboxEvent.objects.create(
            id=event.event_id,
            event_type=type(event).__name__,
            payload=self._serialize(event),
            occurred_on=event.occurred_on,
            processed=False,
        )

    def get_unprocessed(self):
        return OutboxEvent.objects.filter(processed=False)

    def mark_processed(self, event_id):
        OutboxEvent.objects.filter(id=event_id).update(processed=True)

    def _serialize(self, event):
        return {
            k: self._safe(v)
            for k, v in event.__dict__.items()
            if not k.startswith("_")
        }

    def _safe(self, v):
        if hasattr(v, "value"):
            return str(v.value)
        return str(v)