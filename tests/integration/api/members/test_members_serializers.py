# tests/integration/api/members/test_members_serializers.py

import pytest
from interfaces.api.members.serializers import (
    RegisterMemberSerializer,
    ActivateMemberSerializer
)


def test_register_member_serializer_valid():
    serializer = RegisterMemberSerializer(data={
        "role": "PRODUCER"
    })

    assert serializer.is_valid()


def test_register_member_serializer_invalid_role():
    serializer = RegisterMemberSerializer(data={
        "role": "INVALID_ROLE"
    })

    assert not serializer.is_valid()


def test_activate_member_serializer_valid_uuid():
    serializer = ActivateMemberSerializer(data={
        "member_id": "123e4567-e89b-12d3-a456-426614174000"
    })

    assert serializer.is_valid()