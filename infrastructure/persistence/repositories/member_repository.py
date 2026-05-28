# infrastructure/persistence/repositories/member_repository.py

from domain.member.entities import Member
from domain.member.repository import MemberRepository
from domain.member.value_objects import (
    MemberId,
    TaxInformation,
    Address,
)

from infrastructure.persistence.django_models.member_model import MemberModel

from domain.member.status import MemberStatus
from domain.member.value_objects import MemberRole


class DjangoMemberRepository(MemberRepository):

    def save(self, member: Member):

        MemberModel.objects.update_or_create(
            id=str(member.id.value),
            defaults={
                "name": member.name,
                "email": member.email,
                "role": member.role.value,
                "status": member.status.value,
                "fiscal_code": member.tax_info.fiscal_code,
                "street": member.address.street,
                "city": member.address.city,
                "postal_code": member.address.postal_code,
                "country": member.address.country,
            }
        )

    def get(self, member_id: MemberId) -> Member:

        obj = MemberModel.objects.get(id=str(member_id.value))

        return Member(
            id=MemberId(obj.id),
            name=obj.name,
            email=obj.email,
            role=MemberRole(obj.role),
            status=MemberStatus(obj.status),
            tax_info=TaxInformation(
                fiscal_code=obj.fiscal_code
            ),
            address=Address(
                street=obj.street,
                city=obj.city,
                postal_code=obj.postal_code,
                country=obj.country,
            ),
        )

    def find_by_email(self, email: str):

        obj = MemberModel.objects.filter(email=email).first()

        if not obj:
            return None

        return Member(
            id=MemberId(obj.id),
            name=obj.name,
            email=obj.email,
            role=MemberRole(obj.role),
            status=MemberStatus(obj.status),
            tax_info=TaxInformation(
                fiscal_code=obj.fiscal_code
            ),
            address=Address(
                street=obj.street,
                city=obj.city,
                postal_code=obj.postal_code,
                country=obj.country,
            ),
        )