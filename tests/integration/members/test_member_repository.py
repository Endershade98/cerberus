# tests/integration/members/test_member_repository.py
import pytest
from domain.member.entities import Member
from domain.member.value_objects import MemberRole
from infrastructure.persistence.repositories.member_repository import DjangoMemberRepository

@pytest.mark.django_db
def test_add_and_get_member():
    repo = DjangoMemberRepository()
    member = Member(name="Alice", email="alice@example.com", role=MemberRole.CONSUMER)
    repo.add(member)

    retrieved = repo.get_by_id(member.id)
    assert retrieved is not None
    assert retrieved.name == "Alice"