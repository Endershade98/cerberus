# tests/unit/member/test_member_entity.py
import pytest
from domain.member.entities import Member
from domain.member.status import MemberStatus
from domain.member.value_objects import MemberRole


def test_member_activation():
    member = Member()

    member.activate()

    assert member.status == MemberStatus.ACTIVE


def test_member_cannot_exit_from_pending():
    member = Member()

    with pytest.raises(ValueError):
        member.exit()


def test_change_role_only_if_active():
    member = Member()

    with pytest.raises(ValueError):
        member.change_role(MemberRole.PRODUCER)


def test_change_role_when_active():
    member = Member()
    member.activate()

    member.change_role(MemberRole.PRODUCER)

    assert member.role == MemberRole.PRODUCER