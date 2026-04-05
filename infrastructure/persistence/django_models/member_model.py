# infrastructure/persistence/django_models/member_model.py
from django.db import models

class MemberModel(models.Model):
    member_id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "infrastructure"