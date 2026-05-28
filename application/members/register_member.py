# application/members/register_member.py

from domain.member.entities import Member
from domain.member.value_objects import MemberRole
from application.members.dtos import RegisterMemberUseCaseInput


class RegisterMember:
    """
    Clean Use Case: no business logic outside domain.
    """

    def __init__(self, repository, uow):
        self.repository = repository
        self.uow = uow

    def execute(self, input_dto: RegisterMemberUseCaseInput) -> Member:

        if not isinstance(input_dto.role, MemberRole):
            raise ValueError("Invalid role")

        member = Member(
            name=input_dto.name,
            email=input_dto.email,
            role=input_dto.role,
            tax_info=input_dto.tax_info,
            address=input_dto.address,
        )

        self.repository.save(member)
        self.uow.commit()

        return member