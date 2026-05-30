# application/members/validate_member.py

from domain.member.exceptions import MemberDomainError


class ValidateMember:

    def __init__(self, uow):
        self.uow = uow

    def execute(self, member_id):

        with self.uow:
            member = self.uow.member_repository.get(member_id)

            if not member:
                raise MemberDomainError("Member not found")

            member.validate()

            self.uow.member_repository.save(member)

            self.uow.commit()

        return member