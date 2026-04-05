# application/members/register_member.py
from domain.member.entities import Member
from domain.member.value_objects import MemberRole


class RegisterMember:

    def __init__(self, member_repository):
        self.member_repository = member_repository

    def execute(self, input_dto):
        if not isinstance(input_dto.role, MemberRole):
            raise ValueError("Invalid role")

        member = Member(role=input_dto.role)

        self.member_repository.save(member)

        return member.id