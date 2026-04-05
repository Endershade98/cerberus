from domain.member.repository import MemberRepository
from domain.member.entities import Member
from infrastructure.persistence.mappers import to_orm, to_domain
from infrastructure.persistence.django_models.member_model import MemberModel

class DjangoMemberRepository(MemberRepository):

    def add(self, member: Member) -> None:
        orm_member = to_orm(member)
        orm_member.save()

    def get_by_id(self, member_id: str) -> Member | None:
        try:
            orm_member = MemberModel.objects.get(id=member_id)
            return to_domain(orm_member)
        except MemberModel.DoesNotExist:
            return None