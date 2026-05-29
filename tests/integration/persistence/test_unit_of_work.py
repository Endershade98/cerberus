# tests/integration/persistence/test_unit_of_work.py

import pytest
from infrastructure.persistence.django.unit_of_work import DjangoUnitOfWork
from infrastructure.persistence.django.repositories.member_repository import DjangoMemberRepository
from domain.member.value_objects import MemberId


@pytest.mark.django_db
def test_unit_of_work_commit_and_rollback():
    uow = DjangoUnitOfWork()

    with uow:
        member = uow.members.create_dummy_member()
        uow.commit()

    repo = DjangoMemberRepository()
    fetched = repo.get(MemberId(member.id.value))

    assert fetched is not None