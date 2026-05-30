# infrastructure/persistence/django/models/energy.py

from django.db import models


class EnergyModel(models.Model):
    member_id = models.UUIDField()
    recorded_at = models.DateTimeField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "energy_records"