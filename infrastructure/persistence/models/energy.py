from django.db import models

class EnergyProcessingStep(models.Model):
    job_id = models.UUIDField()
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    error = models.TextField(null=True)