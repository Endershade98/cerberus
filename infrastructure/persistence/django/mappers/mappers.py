# infrastructure/persistence/mappers.py

from domain.member.entities import Member
from domain.member.value_objects import MemberId


def to_domain(member_model):
    return Member(
        id=MemberId(member_model.member_id),
        name=member_model.name,
        email=member_model.email,
        role=member_model.role,
        status=member_model.status,
    )


def to_orm(member: Member):
    return {
        "member_id": str(member.id.value),
        "name": member.name,
        "email": member.email,
        "role": member.role.value,
        "status": member.status.value,
    }