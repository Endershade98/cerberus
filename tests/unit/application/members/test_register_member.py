# tests/unit/application/members/test_register_member.py


from unittest.mock import Mock

from application.members.register_member import RegisterMember
from application.members.dtos import RegisterMemberUseCaseInput
from domain.member.value_objects import MemberRole, TaxInformation, Address


def test_register_member_success():

    uow = Mock()
    repo = Mock()
    uow.member_repository = repo

    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    use_case = RegisterMember(uow)

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