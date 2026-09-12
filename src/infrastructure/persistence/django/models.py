# infrastructure/persistence/django/models.py


import uuid

from django.db import models


class MemberModel(models.Model):
    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    role = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    fiscal_code = models.CharField(max_length=50, null=True, blank=True)

    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField()

    class Meta:
        db_table = "members"


class EnergyModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member_id = models.UUIDField()
    recorded_at = models.DateTimeField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "energy_records"


class OutboxEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(max_length=255)
    payload = models.JSONField()
    occurred_on = models.DateTimeField()
    processed = models.BooleanField(default=False)

    class Meta:
        db_table = "outbox_events"