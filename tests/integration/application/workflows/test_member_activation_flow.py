# tests/integration/application/workflows/test_member_activation_flow.py

import pytest

from application.members.activate_member import ActivateMember

from domain.member.entities import Member
from domain.member.status import MemberStatus
from domain.member.value_objects import (
    TaxInformation,
    Address,
    MemberRole,
)


@pytest.mark.django_db
def test_activation_flow(uow):

    member = Member.create(
        name="Mario Rossi",
        email="mario@test.it",
        role=MemberRole.CONSUMER,
        tax_info=TaxInformation("RSSMRA80A01H501Z"),
        address=Address(
            street="Via Roma 1",
            city="Roma",
            postal_code="00100",
            country="IT",
        ),
    )

    member.validate()

    uow.member_repository.save(member)

    use_case = ActivateMember(uow)

    activated = use_case.execute(member.id)

    assert activated.status == MemberStatus.ACTIVE