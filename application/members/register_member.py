# application/members/register_member.py

from application.common.use_case import UseCase
from domain.member.entities import Member


class RegisterMember(UseCase):

    def _execute(self, input_dto):

        member = self.uow.member_repository.find_by_email(
            input_dto.email
        )

        if member:
            raise ValueError(
                "Member already exists"
            )

        member = Member.create(
            name=input_dto.name,
            email=input_dto.email,
            role=input_dto.role,
            tax_info=input_dto.tax_info,
            address=input_dto.address,
        )

        self.uow.member_repository.save(member)

        return member