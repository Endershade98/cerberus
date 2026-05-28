# tests/e2e/test_member_full_lifecycle.py

from domain.member.entities import Member
from domain.member.status import MemberStatus
from domain.member.value_objects import (
    TaxInformation,
    Address,
)


def create_member():

    return Member.register(
        name="Mario Rossi",
        email="mario@test.com",
        tax_info=TaxInformation(
            fiscal_code="RSSMRA85T10A562S"
        ),
        address=Address(
            street="Via Roma",
            city="Napoli",
            postal_code="80100",
            country="IT",
        ),
    )


def test_full_member_lifecycle():

    member = create_member()

    assert member.status == MemberStatus.REGISTERED

    member.submit_for_validation()

    assert member.status == MemberStatus.PENDING

    member.validate()

    assert member.status == MemberStatus.VALIDATED

    member.activate()

    assert member.status == MemberStatus.ACTIVE

    member.suspend()

    assert member.status == MemberStatus.SUSPENDED

    member.reactivate()

    assert member.status == MemberStatus.ACTIVE

    member.exit()

    assert member.status == MemberStatus.EXITED