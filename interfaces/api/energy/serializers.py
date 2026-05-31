# interfaces/api/energy/serializers.py

from rest_framework import serializers


class EnergyRecordSerializer(serializers.Serializer):
    member_id = serializers.UUIDField()
    kwh = serializers.FloatField(min_value=0.0)