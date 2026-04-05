# interfaces/api/members/serializers.py
from rest_framework import serializers
from domain.member.value_objects import MemberRole

# Serializer per POST /register/
class RegisterMemberSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=[(role.value, role.name) for role in MemberRole])

# Serializer per POST /activate/
class ActivateMemberSerializer(serializers.Serializer):
    member_id = serializers.UUIDField()