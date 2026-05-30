# infrastructure/persistence/django/repositories/member_repository.py

from domain.member.entities import Member
from domain.member.repository import MemberRepository
from domain.member.value_objects import MemberId, TaxInformation, Address, MemberRole
from domain.member.status import MemberStatus

from infrastructure.persistence.django.models.member import MemberModel


class DjangoMemberRepository(MemberRepository):

    def save(self, member: Member) -> None:

        MemberModel.objects.update_or_create(
            member_id=str(member.id.value),
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
            },
        )

    def get(self, member_id: MemberId) -> Member | None:
        try:
            obj = MemberModel.objects.get(member_id=str(member_id.value))
        except MemberModel.DoesNotExist:
            return None

        return self._to_domain(obj)

    def find_by_email(self, email: str) -> Member | None:
        obj = MemberModel.objects.filter(email=email).first()
        return self._to_domain(obj) if obj else None

    # -------------------------
    # DOMAIN MAPPER
    # -------------------------
    def _to_domain(self, obj: MemberModel) -> Member:
        return Member(
            id=MemberId(obj.member_id),
            name=obj.name,
            email=obj.email,
            role=MemberRole(obj.role),
            status=MemberStatus(obj.status),
            tax_info=TaxInformation(obj.fiscal_code),
            address=Address(
                street=obj.street,
                city=obj.city,
                postal_code=obj.postal_code,
                country=obj.country,
            ),
        )