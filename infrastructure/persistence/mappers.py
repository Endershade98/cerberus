# infrastructure/persistence/mappers.py

from domain.member.entities import Member
from infrastructure.persistence.django_models.member_model import MemberModel

def to_orm(member: Member) -> MemberModel:
    return MemberModel(
        id=member.id,
        name=member.name,
        email=member.email,
        status=member.status.value,
    )

def to_domain(member_model: MemberModel) -> Member:
    return Member(
        id=member_model.id,
        name=member_model.name,
        email=member_model.email,
        status=member_model.status,
    )