# tests/unit/domain/member/test_member_entity.py

import pytest

from domain.member.entities import Member
from domain.member.status import MemberStatus
from domain.member.value_objects import (
    MemberRole,
    TaxInformation,
    Address,
)

from domain.shared.exceptions import (
    BusinessRuleViolation,
    InvalidStateTransition,
)

from domain.member.exceptions import (
    InvalidMemberStateError,
)


def create_tax_info():
    return TaxInformation(
        fiscal_code="RSSMRA85T10A562S"
    )


def create_address():
    return Address(
        street="Via Roma 1",
        city="Napoli",
        postal_code="80100",
        country="IT"
    )


def create_member():
    return Member.register(
        name="John",
        email="john@test.com",
        tax_info=create_tax_info(),
        address=create_address(),
    )


def activate_member(member: Member):
    member.validate()
    member.activate()


def test_should_register_member_as_pending():

    member = create_member()

    assert member.status == MemberStatus.PENDING


def test_should_validate_member():

    member = create_member()

    member.validate()

    assert member.status == MemberStatus.VALIDATED


def test_should_activate_member():

    member = create_member()

    activate_member(member)

    assert member.status == MemberStatus.ACTIVE


def test_should_suspend_member():

    member = create_member()

    activate_member(member)

    member.suspend()

    assert member.status == MemberStatus.SUSPENDED


def test_should_reactivate_suspended_member():

    member = create_member()

    activate_member(member)

    member.suspend()

    member.reactivate()

    assert member.status == MemberStatus.ACTIVE


def test_should_reject_member():

    member = create_member()

    member.reject()

    assert member.status == MemberStatus.REJECTED


def test_should_exit_member():

    member = create_member()

    activate_member(member)

    member.exit()

    assert member.status == MemberStatus.EXITED


def test_should_change_role_if_active():

    member = create_member()

    activate_member(member)

    member.change_role(MemberRole.PRODUCER)

    assert member.role == MemberRole.PRODUCER


def test_should_not_change_role_if_not_active():

    member = create_member()

    with pytest.raises(BusinessRuleViolation):
        member.change_role(MemberRole.PRODUCER)


def test_should_not_activate_non_validated_member():

    member = create_member()

    with pytest.raises(InvalidMemberStateError):
        member.activate()


def test_should_not_suspend_non_active_member():

    member = create_member()

    with pytest.raises(InvalidMemberStateError):
        member.suspend()


def test_should_block_invalid_transition():

    member = create_member()

    with pytest.raises(InvalidStateTransition):
        member.exit()