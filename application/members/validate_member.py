# application/members/validate_member.py

from domain.member.repository import MemberRepository


class ValidateMember:

    def __init__(self, repo: MemberRepository):
        self.repo = repo

    def execute(self, member_id):
        member = self.repo.get_by_id(member_id)

        if not member:
            raise ValueError("Member not found")

        member.validate()

        self.repo.add(member)

        return member