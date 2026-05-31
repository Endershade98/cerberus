# domain/member/policies.py

from domain.member.rules import MemberRules
from domain.member.status import MemberStatus
from domain.member.value_objects import MemberRole
from domain.member.exceptions import InvalidMemberStateError


class ActivationPolicy:

    @staticmethod
    def validate(member):
        try:
            MemberRules.assert_can_activate(member.status)
        except Exception as e:
            raise InvalidMemberStateError(str(e))

        if not member.tax_info:
            raise InvalidMemberStateError("Tax information required")

        if not member.address:
            raise InvalidMemberStateError("Address required")


class SuspensionPolicy:

    @staticmethod
    def validate(member):
        try:
            MemberRules.assert_can_suspend(member.status)
        except Exception as e:
            raise InvalidMemberStateError(str(e))