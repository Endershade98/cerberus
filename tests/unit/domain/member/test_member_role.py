# tests/unit/member/test_member_role.py

from domain.member.value_objects import MemberRole


def test_consumer_can_consume():
    assert MemberRole.CONSUMER.can_consume() is True


def test_consumer_cannot_produce():
    assert MemberRole.CONSUMER.can_produce() is False


def test_prosumer_can_do_both():
    assert MemberRole.PROSUMER.can_consume() is True
    assert MemberRole.PROSUMER.can_produce() is True