# tests/integration/members/test_member_repository.py

import pytest
from uuid import uuid4

from domain.member.entities import Member
from domain.member.status import MemberStatus
from domain.member.value_objects import MemberRole
from infrastructure.persistence.repositories.member_repository import DjangoMemberRepository


@pytest.mark.django_db
def test_add_and_get_member():
    repo = DjangoMemberRepository()

    member = Member(
        name="Alice",
        email="alice@example.com",
        role=MemberRole.CONSUMER,
        status=MemberStatus.PENDING,
    )

    repo.add(member)
    retrieved = repo.get_by_id(member.id)

    assert retrieved.id == member.id
    assert retrieved.name == "Alice"
    assert retrieved.email == "alice@example.com"
    assert retrieved.role == member.role
    assert retrieved.status == member.status


@pytest.mark.django_db
def test_get_by_id_raises_when_not_found():
    # Arrange
    repo = DjangoMemberRepository()
    non_existent_id = uuid4()

    # Act + Assert
    with pytest.raises(Exception):  # oppure MemberModel.DoesNotExist
        repo.get_by_id(non_existent_id)