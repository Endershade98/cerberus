# infrastructure/persistence/repositories/member_repository.py
from domain.member.entities import Member
from domain.member.value_objects import MemberRole
from infrastructure.persistence.django_models.member_model import MemberModel
from domain.member.status import MemberStatus

class DjangoMemberRepository:
    def add(self, member: Member):
        MemberModel.objects.create(
            member_id=member.id,
            name=member.name,
            email=member.email,
            role=member.role.value,
            status=member.status.value,
        )

    def get_by_id(self, member_id) -> Member:
        m = MemberModel.objects.get(member_id=member_id)
        return Member(
            id=m.member_id,
            name=m.name,
            email=m.email,
            role=MemberRole(m.role),
            status=MemberStatus(m.status),
            created_at=m.created_at,
        )