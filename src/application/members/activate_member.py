# application/members/activate_member.py

from src.domain.member.exceptions import MemberDomainError
from src.application.common.use_case import UseCase


class ActivateMember(UseCase):

    def _execute(self, member_id):

        member = self.uow.member_repository.get(member_id)

        if not member:
            raise MemberDomainError(
                "Member not found"
            )

        member.activate()

        self.uow.member_repository.save(member)

        return member