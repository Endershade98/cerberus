# tests/integration/infrastructure/persistence/django/test_member_repository.py

import pytest
from uuid import uuid4

from src.domain.member.entities import Member
from src.domain.member.value_objects import MemberId, TaxInformation, Address, MemberRole
from src.domain.member.status import MemberStatus
from src.infrastructure.django_app.persistence.django.repositories.member_repository import DjangoMemberRepository



@pytest.mark.django_db
def test_member_repository_save_and_get():

    repo = DjangoMemberRepository()

    member = Member(
        id=MemberId(uuid4()),
        name="Mario",
        email="mario@test.com",
        role=MemberRole.CONSUMER,
        status=MemberStatus.PENDING,
        tax_info=TaxInformation("RSSMRA80A01F205X"),
        address=Address("Via Roma", "Napoli", "80100", "IT"),
    )

    repo.save(member)

    fetched = repo.get(member.id)

    assert fetched is not None
    assert fetched.email == "mario@test.com"
    assert fetched.tax_info.fiscal_code == "RSSMRA80A01F205X"