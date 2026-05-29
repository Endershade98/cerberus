# infrastructure/persistence/django/models/member.py

from django.db import models


class MemberModel(models.Model):
    member_id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    fiscal_code = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "members"