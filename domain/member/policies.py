# domain/member/policies.py

from domain.member.status import MemberStatus
from domain.member.exceptions import InvalidMemberStateError


class ActivationPolicy:

    @staticmethod
    def validate(member):

        if member.status != MemberStatus.VALIDATED:
            raise InvalidMemberStateError(
                "Member must be VALIDATED before activation"
            )

        if not member.tax_info:
            raise InvalidMemberStateError(
                "Tax information required"
            )

        if not member.address:
            raise InvalidMemberStateError(
                "Address required"
            )


class SuspensionPolicy:

    @staticmethod
    def validate(member):

        if member.status != MemberStatus.ACTIVE:
            raise InvalidMemberStateError(
                "Only ACTIVE members can be suspended"
            )