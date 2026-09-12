# tests/unit/application/members/test_register_member.py

from unittest.mock import Mock

from src.application.members.register_member import RegisterMember
from src.application.members.dtos import RegisterMemberUseCaseInput
from src.domain.member.value_objects import MemberRole, TaxInformation, Address


def test_register_member_executes_use_case_and_saves_member():

    uow = Mock()
    repo = Mock()

    uow.member_repository = repo
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    repo.find_by_email.return_value = None  # FIX CRITICO

    use_case = RegisterMember(uow)

    dto = RegisterMemberUseCaseInput(
        name="Mario",
        email="mario@test.com",
        role=MemberRole.CONSUMER,
        tax_info=TaxInformation("RSSMRA85T10A562S"),
        address=Address("Via Roma", "Napoli", "80100", "IT"),
    )

    member = use_case.execute(dto)

    repo.save.assert_called_once()
    assert member.email == "mario@test.com"