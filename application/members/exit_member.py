# application/members/exit_member.py

from domain.member.repository import MemberRepository
from domain.shared.unit_of_work import UnitOfWork


class ExitMember:

    def __init__(
        self,
        repository: MemberRepository,
        uow: UnitOfWork,
    ):
        self.repository = repository
        self.uow = uow

    def execute(self, member_id):

        member = self.repository.get(member_id)

        member.exit()

        self.repository.save(member)

        self.uow.commit()

        return member