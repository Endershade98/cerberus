# tests/integration/persistence/test_member_repository.py

import pytest
from domain.member.entities import Member
from domain.member.value_objects import MemberId, TaxInformation, Address, MemberRole
from domain.member.status import MemberStatus
from infrastructure.persistence.django.repositories.member_repository import DjangoMemberRepository


@pytest.mark.django_db
def test_save_and_load_member():

    repo = DjangoMemberRepository()

    member = Member(
        id=MemberId("123e4567-e89b-12d3-a456-426614174000"),
        name="Mario",
        email="mario@test.com",
        role=MemberRole.PRODUCER,
        status=MemberStatus.ACTIVE,
        tax_info=TaxInformation("ABC"),
        address=Address("Street", "City", "12345", "IT"),
    )

    repo.save(member)

    loaded = repo.get_by_id(member.id)

    assert loaded.email == "mario@test.com"
    assert loaded.status == MemberStatus.ACTIVE