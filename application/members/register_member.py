# application/members/register_member.py
from domain.member.entities import Member, RegisterMemberInput
from domain.member.value_objects import MemberRole


class RegisterMember:
    """
    Use case for registering a new member. It creates a member with the provided role and saves it to the repository.
    The member is created with a default status of PENDING. The use case also validates the input role to ensure it's a valid MemberRole before creating the member.
    """

    def __init__(self, member_repository):
        self.member_repository = member_repository

    def execute(self, input_dto: RegisterMemberInput) -> str:
        if not isinstance(input_dto.role, MemberRole):
            raise ValueError("Invalid role")

        member = Member(role=input_dto.role)

        self.member_repository.save(member)

        return member.id