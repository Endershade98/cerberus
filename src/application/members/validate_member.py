# application/members/validate_member.py

from domain.membership.exceptions import MemberDomainError
from src.application.common.use_case import UseCase


class ValidateMember(UseCase):

    def _execute(self, member_id):

        member = self.uow.member_repository.get(member_id)

        if not member:
            raise MemberDomainError(
                "Member not found"
            )

        member.validate()

        self.uow.member_repository.save(member)

        return member