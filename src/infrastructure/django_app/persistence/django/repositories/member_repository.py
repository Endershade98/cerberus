# infrastructure/django_app/persistence/django/repositories/member_repository.py

from domain.membership.entities import Member
from domain.membership.repositories import MemberRepository
from domain.membership.value_objects import MemberId, TaxInformation, Address, MemberRole
from domain.membership.status import MemberStatus
from src.infrastructure.persistence.django.models import MemberModel


class DjangoMemberRepository(MemberRepository):

    def save(self, member: Member) -> None:
        MemberModel.objects.update_or_create(
            member_id=member.id.value,
            defaults={
                "name": member.name,
                "email": member.email,
                "role": member.role.value,
                "status": member.status.value,
                "fiscal_code": member.tax_info.fiscal_code if member.tax_info else None,
                "street": member.address.street if member.address else None,
                "city": member.address.city if member.address else None,
                "postal_code": member.address.postal_code if member.address else None,
                "country": member.address.country if member.address else None,
                "created_at": member.created_at,
            },
        )

    def get(self, member_id: MemberId) -> Member | None:
        try:
            obj = MemberModel.objects.get(member_id=member_id.value)
        except MemberModel.DoesNotExist:
            return None

        return self._to_domain(obj)

    def find_by_email(self, email: str) -> Member | None:
        obj = MemberModel.objects.filter(email=email).first()
        return self._to_domain(obj) if obj else None

    def _to_domain(self, obj: MemberModel) -> Member:
        return Member(
            id=MemberId(obj.member_id),
            name=obj.name,
            email=obj.email,
            role=MemberRole(obj.role),
            status=MemberStatus(obj.status),
            tax_info=TaxInformation(obj.fiscal_code) if obj.fiscal_code else None,
            address=Address(
                street=obj.street,
                city=obj.city,
                postal_code=obj.postal_code,
                country=obj.country,
            ) if obj.street else None,
            created_at=obj.created_at,
        )