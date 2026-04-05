# tests/unit/member/test_member_role.py
import pytest
from domain.member.value_objects import MemberRole


def test_consumer_can_consume():
    role = MemberRole.CONSUMER
    assert role.can_consume() is True


def test_consumer_cannot_produce():
    role = MemberRole.CONSUMER
    assert role.can_produce() is False


def test_prosumer_can_do_both():
    role = MemberRole.PROSUMER
    assert role.can_consume() is True
    assert role.can_produce() is True