# tests/unit/member/test_member_entity.py

import pytest

from domain.member.entities import Member
from domain.member.status import MemberStatus
from domain.member.value_objects import MemberRole
from domain.shared.exceptions import BusinessRuleViolation


def test_should_activate_member():

    member = Member()

    member.activate()

    assert member.status == MemberStatus.ACTIVE


def test_should_suspend_member():

    member = Member(status=MemberStatus.ACTIVE)

    member.suspend()

    assert member.status == MemberStatus.SUSPENDED


def test_should_change_role_if_active():

    member = Member(status=MemberStatus.ACTIVE)

    member.change_role(MemberRole.PROSUMER)

    assert member.role == MemberRole.PROSUMER


def test_should_not_change_role_if_not_active():

    member = Member(status=MemberStatus.PENDING)

    with pytest.raises(BusinessRuleViolation):
        member.change_role(MemberRole.PRODUCER)