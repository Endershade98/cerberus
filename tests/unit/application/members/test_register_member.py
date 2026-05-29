# tests/unit/application/members/test_register_member.py

import pytest
from unittest.mock import Mock

from application.members.register_member import RegisterMember
from application.members.dtos import RegisterMemberUseCaseInput
from domain.member.value_objects import MemberRole, TaxInformation, Address


def test_register_member_success():

    repo = Mock()
    uow = Mock()

    use_case = RegisterMember(repo, uow)

    dto = RegisterMemberUseCaseInput(
        name="Mario",
        email="mario@test.com",
        role=MemberRole.CONSUMER,
        tax_info=TaxInformation("RSSMRA80A01H501U"),
        address=Address("Via Roma", "Napoli", "80100", "IT")
    )

    member = use_case.execute(dto)

    assert member.name == "Mario"
    repo.save.assert_called_once()
    uow.commit.assert_called_once()