# tests/integration/persistence/test_unit_of_work.py

import pytest

from infrastructure.events.outbox.models import OutboxEvent
from infrastructure.persistence.django.unit_of_work import DjangoUnitOfWork
from infrastructure.persistence.django.repositories.member_repository import DjangoMemberRepository
from infrastructure.events.outbox.repository import OutboxRepository
from domain.member.entities import Member
from domain.member.value_objects import MemberId, MemberRole, TaxInformation, Address
from domain.member.status import MemberStatus


@pytest.mark.django_db
def test_unit_of_work_commit_and_persistence():

    repo = DjangoMemberRepository()
    outbox_repo = OutboxRepository()

    uow = DjangoUnitOfWork(outbox_repo)

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

    uow.commit(member)

    # persistence check
    fetched = repo.get(member.id)
    assert fetched is not None

    # event system check
    assert OutboxEvent.objects.count() == 1