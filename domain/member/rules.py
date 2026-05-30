# domain/member/rules.py

from domain.member.status import MemberStatus
from domain.member.value_objects import MemberRole
from domain.shared.exceptions import BusinessRuleViolation


class MemberRules:

    @staticmethod
    def assert_can_activate(status: MemberStatus):
        if status != MemberStatus.VALIDATED:
            raise BusinessRuleViolation(
                "Member must be VALIDATED before activation"
            )

    @staticmethod
    def assert_can_suspend(status: MemberStatus):
        if status != MemberStatus.ACTIVE:
            raise BusinessRuleViolation(
                "Only ACTIVE members can be suspended"
            )

    @staticmethod
    def assert_can_change_role(status: MemberStatus):
        if status != MemberStatus.ACTIVE:
            raise BusinessRuleViolation(
                "Only ACTIVE members can change role"
            )

    @staticmethod
    def assert_valid_role_change(role: MemberRole):
        if role not in MemberRole:
            raise BusinessRuleViolation("Invalid role")