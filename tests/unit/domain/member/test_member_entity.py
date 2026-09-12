# tests/unit/domain/member/test_member_entity.py

import pytest

from src.domain.member.entities import Member
from src.domain.member.status import MemberStatus
from src.domain.member.value_objects import MemberRole, TaxInformation, Address
from src.domain.shared.exceptions import InvalidStateTransition


def create_member():
    return Member.create(
        name="Mario",
        email="mario@test.com",
        role=MemberRole.CONSUMER,
        tax_info=TaxInformation("RSSMRA85T10A562S"),
        address=Address("Via Roma", "Napoli", "80100", "IT"),
    )


def test_should_create_member_in_registered_state():
    member = create_member()
    assert member.status == MemberStatus.PENDING


def test_should_validate_member():
    member = create_member()
    member.validate()

    assert member.status == MemberStatus.VALIDATED


def test_should_activate_member():
    member = create_member()

    member.validate()
    member.activate()

    assert member.status == MemberStatus.ACTIVE


def test_should_fail_activation_if_not_validated():

    member = create_member()

    with pytest.raises(InvalidStateTransition):
        member.activate()


def test_should_suspend_active_member():
    member = create_member()

    member.validate()
    member.activate()
    member.suspend()

    assert member.status == MemberStatus.SUSPENDED


def test_should_reject_member():
    member = create_member()
    member.reject()

    assert member.status == MemberStatus.REJECTED


def test_should_exit_member():

    member = create_member()

    member.validate()
    member.activate()
    member.exit()

    assert member.status == MemberStatus.EXITED


def test_should_change_role_only_if_active():
    member = create_member()

    member.validate()
    member.activate()

    member.change_role(MemberRole.PRODUCER)

    assert member.role == MemberRole.PRODUCER