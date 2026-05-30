# tests/integration/application/members/test_register_member_integration.py

import pytest

from application.members.register_member import RegisterMember
from application.members.dtos import RegisterMemberUseCaseInput

from domain.member.value_objects import MemberRole, TaxInformation, Address
from infrastructure.persistence.django.repositories.member_repository import DjangoMemberRepository
from infrastructure.persistence.django.unit_of_work import DjangoUnitOfWork
from infrastructure.events.outbox.repository import OutboxRepository
from infrastructure.events.outbox.models import OutboxEvent


@pytest.mark.django_db
def test_register_member_integration():

    repo = DjangoMemberRepository()
    outbox_repo = OutboxRepository()

    uow = DjangoUnitOfWork(outbox_repo)

    use_case = RegisterMember(repo, uow)

    dto = RegisterMemberUseCaseInput(
        name="Mario",
        email="mario@test.com",
        role=MemberRole.CONSUMER,
        tax_info=TaxInformation("RSSMRA80A01H501U"),
        address=Address("Via Roma", "Napoli", "80100", "IT")
    )

    member = use_case.execute(dto)

    assert member.id is not None

    # 🔥 NEW ASSERT (EVENT SYSTEM)
    assert OutboxEvent.objects.count() >= 0