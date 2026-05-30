# application/members/register_member.py

from domain.member.entities import Member
from application.members.dtos import RegisterMemberUseCaseInput


class RegisterMember:

    def __init__(self, uow):
        self.uow = uow

    def execute(self, input_dto: RegisterMemberUseCaseInput):

        with self.uow:
            member = Member.register(
                name=input_dto.name,
                email=input_dto.email,
                role=input_dto.role,
                tax_info=input_dto.tax_info,
                address=input_dto.address,
            )

            self.uow.member_repository.save(member)
            self.uow.commit()

        return member