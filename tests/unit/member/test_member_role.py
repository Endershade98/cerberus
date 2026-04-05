# tests/unit/member/test_member_role.py
import pytest
from domain.member.value_objects import MemberRole

# CONSUMER
def test_consumer_can_consume():
    role = MemberRole.CONSUMER
    assert role.can_consume() is True

def test_consumer_cannot_produce():
    role = MemberRole.CONSUMER
    assert role.can_produce() is False

def test_invalid_role_raises_error():
    with pytest.raises(ValueError):
        MemberRole("invalid_role")

# PRODUCER
def test_producer_can_produce():
    role = MemberRole.PRODUCER
    assert role.can_produce() is True

def test_producer_cannot_consume():
    role = MemberRole.PRODUCER
    assert role.can_consume() is False

# PROSUMER
def test_prosumer_can_do_both():
    role = MemberRole.PROSUMER
    assert role.can_consume() is True
    assert role.can_produce() is True