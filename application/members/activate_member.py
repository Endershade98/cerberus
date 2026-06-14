# application/members/activate_member.py

from domain.member.exceptions import MemberDomainError
from application.common.use_case import UseCase


class ActivateMember(UseCase):

    def _execute(self, member_id):

        member = self.uow.member_repository.get(member_id)

        if not member:
            raise MemberDomainError("Member not found")

        member.activate()

        # FIX: eventi raccolti qui
        events = member.pull_events()

        self.uow.member_repository.save(member)

        self.uow.collect(events)

        return member