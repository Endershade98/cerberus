# tests/unit/domain/member/test_member_rules.py

import pytest

from domain.member.rules import MemberRules
from domain.member.status import MemberStatus
from domain.member.value_objects import MemberRole
from domain.shared.exceptions import BusinessRuleViolation


def test_can_activate_validated():
    MemberRules.assert_can_activate(MemberStatus.VALIDATED)


def test_cannot_activate_non_validated():
    with pytest.raises(BusinessRuleViolation):
        MemberRules.assert_can_activate(MemberStatus.PENDING)


def test_can_suspend_active():
    MemberRules.assert_can_suspend(MemberStatus.ACTIVE)


def test_cannot_suspend_non_active():
    with pytest.raises(BusinessRuleViolation):
        MemberRules.assert_can_suspend(MemberStatus.VALIDATED)


def test_can_change_role_only_active():
    MemberRules.assert_can_change_role(MemberStatus.ACTIVE)


def test_cannot_change_role_if_not_active():
    with pytest.raises(BusinessRuleViolation):
        MemberRules.assert_can_change_role(MemberStatus.PENDING)