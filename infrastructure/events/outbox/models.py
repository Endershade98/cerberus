# infrastructure/events/outbox/models.py

from django.db import models
import uuid


class OutboxEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(max_length=255)
    payload = models.JSONField()
    occurred_on = models.DateTimeField()
    processed = models.BooleanField(default=False)

    class Meta:
        db_table = "outbox_events"