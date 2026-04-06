# infrastructure/persistence/models/energy.py
from django.db import models

class EnergyProcessingStep(models.Model):
    job_id = models.UUIDField()
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    error = models.TextField(null=True)

    class Meta:
        db_table = "energy_processing_steps"


class EnergyModel(models.Model):
    member_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    value_kwh = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "energy_records"