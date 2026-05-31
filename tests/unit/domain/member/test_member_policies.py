# tests/unit/domain/member/test_member_policies.py

import pytest

from domain.member.entities import Member
from domain.member.policies import ActivationPolicy
from domain.member.status import MemberStatus
from domain.member.value_objects import TaxInformation, Address
from domain.member.exceptions import InvalidMemberStateError


def create_member():
    return Member(
        name="Mario",
        email="mario@test.com",
        tax_info=TaxInformation("RSSMRA85T10A562S"),
        address=Address("Via Roma", "Napoli", "80100", "IT"),
    )


def test_activation_policy_requires_validated():
    member = create_member()
    member.status = MemberStatus.ACTIVE

    with pytest.raises(InvalidMemberStateError):
        ActivationPolicy.validate(member)


def test_activation_policy_requires_tax_info():
    member = Member(name="Mario", email="m@x.com")
    member.status = MemberStatus.VALIDATED

    with pytest.raises(InvalidMemberStateError):
        ActivationPolicy.validate(member)


def test_activation_policy_requires_address():
    member = Member(
        name="Mario",
        email="m@x.com",
        tax_info=TaxInformation("RSSMRA85T10A562S"),
    )
    member.status = MemberStatus.VALIDATED

    with pytest.raises(InvalidMemberStateError):
        ActivationPolicy.validate(member)