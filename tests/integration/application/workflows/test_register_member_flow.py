# tests/integration/application/workflows/test_register_member_flow.py

import pytest

from application.members.register_member import RegisterMember
from application.members.dtos import RegisterMemberUseCaseInput

from domain.member.value_objects import MemberRole, TaxInformation, Address


@pytest.mark.django_db
def test_register_member_flow(uow):

    use_case = RegisterMember(uow)

    input_dto = RegisterMemberUseCaseInput(
        name="Mario",
        email="mario@test.com",
        role=MemberRole.CONSUMER,
        tax_info=TaxInformation("RSSMRA80A01F205X"),
        address=Address("Via Roma", "Napoli", "80100", "IT"),
    )

    member = use_case.execute(input_dto)

    assert member.id is not None
    assert member.email == "mario@test.com"