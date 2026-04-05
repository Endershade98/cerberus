# application/members/register_member.py
from domain.member.entities import Member, RegisterMemberUseCaseInput
from domain.member.value_objects import MemberRole


class RegisterMemberUseCase:
    """
    Use case for registering a new member in the system.
    This use case handles the creation of a new member with a specified role,
    and sets the initial status to PENDING. It validates the input role and ensures that only valid roles are accepted. 
    The new member is then saved to the repository, and the member's ID is returned.
    """

    def __init__(self, member_repository):
        self.member_repository = member_repository

    def execute(self, input_dto: RegisterMemberUseCaseInput) -> str:
        if not isinstance(input_dto.role, MemberRole):
            raise ValueError("Invalid role")

        member = Member(role=input_dto.role)

        self.member_repository.save(member)

        return member.id