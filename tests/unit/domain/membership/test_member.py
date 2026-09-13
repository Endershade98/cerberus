# tests/unit/domain/membership/test_member.py

import pytest

from domain.community.value_objects import CerId
from domain.membership.entities import Member
from domain.membership.events import (
    MemberActivated,
    MemberExited,
    MemberRejected,
    MemberRegistered,
    MemberRoleChanged,
    MemberSuspended,
    MemberValidated,
)
from domain.membership.exceptions import InvalidMemberRoleChange
from domain.membership.status import MemberStatus
from domain.membership.value_objects import (
    Address,
    EmailAddress,
    MemberId,
    MemberRole,
    TaxInformation,
)
from domain.shared.exceptions import BusinessRuleViolation, InvalidStateTransition


@pytest.fixture
def cer_id():
    return CerId.generate()


@pytest.fixture
def tax_info():
    return TaxInformation("ABCDEFGHIJKLMNOP")


@pytest.fixture
def address():
    return Address(
        street="Via Roma 10",
        city="Matera",
        postal_code="75100",
        country="Italy",
    )


def make_member(cer_id):
    return Member.create(
        cer_id=cer_id,
        name="Mario Rossi",
        email="Mario.Rossi@example.com",
        role=MemberRole.CONSUMER,
    )


def activate_member(member, tax_info, address):
    member.validate()
    member.activate()


def test_create_starts_in_pending(cer_id):
    member = make_member(cer_id)

    assert isinstance(member.id, MemberId)
    assert member.cer_id == cer_id
    assert member.status == MemberStatus.PENDING
    assert member.name == "Mario Rossi"
    assert member.email.value == "mario.rossi@example.com"


def test_create_emits_registered_event(cer_id):
    member = make_member(cer_id)

    events = member.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], MemberRegistered)
    assert events[0].member_id == member.id


def test_create_rejects_blank_name(cer_id):
    with pytest.raises(
        BusinessRuleViolation,
        match="Member name is required",
    ):
        Member.create(
            cer_id=cer_id,
            name="   ",
            email="user@example.com",
            role=MemberRole.CONSUMER,
        )


def test_validate_changes_status(cer_id):
    member = make_member(cer_id)
    member.pull_events()

    member.validate()

    assert member.status == MemberStatus.VALIDATED


def test_validate_emits_event(cer_id):
    member = make_member(cer_id)
    member.pull_events()

    member.validate()

    events = member.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], MemberValidated)
    assert events[0].member_id == member.id


def test_activate_requires_tax_information(cer_id, address):
    member = make_member(cer_id)
    member.validate()

    with pytest.raises(
        BusinessRuleViolation,
        match="Tax information is required",
    ):
        member.activate()


def test_activate_requires_address(cer_id, tax_info):
    member = Member.create(
        cer_id=cer_id,
        name="Mario Rossi",
        email="mario@example.com",
        role=MemberRole.CONSUMER,
        tax_info=tax_info,
    )
    member.validate()

    with pytest.raises(
        BusinessRuleViolation,
        match="Address is required",
    ):
        member.activate()


def test_activate_changes_status(cer_id, tax_info, address):
    member = Member.create(
        cer_id=cer_id,
        name="Mario Rossi",
        email="mario@example.com",
        role=MemberRole.CONSUMER,
        tax_info=tax_info,
        address=address,
    )
    member.pull_events()

    member.validate()
    member.pull_events()

    member.activate()

    assert member.status == MemberStatus.ACTIVE


def test_activate_emits_event(cer_id, tax_info, address):
    member = Member.create(
        cer_id=cer_id,
        name="Mario Rossi",
        email="mario@example.com",
        role=MemberRole.CONSUMER,
        tax_info=tax_info,
        address=address,
    )
    member.pull_events()

    member.validate()
    member.pull_events()
    member.activate()

    events = member.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], MemberActivated)
    assert events[0].member_id == member.id


def test_suspend_active_member(cer_id, tax_info, address):
    member = Member.create(
        cer_id=cer_id,
        name="Mario Rossi",
        email="mario@example.com",
        role=MemberRole.CONSUMER,
        tax_info=tax_info,
        address=address,
    )
    member.validate()
    member.activate()
    member.pull_events()

    member.suspend()

    assert member.status == MemberStatus.SUSPENDED

    events = member.pull_events()
    assert len(events) == 1
    assert isinstance(events[0], MemberSuspended)
    assert events[0].member_id == member.id


def test_suspended_member_can_be_reactivated(cer_id, tax_info, address):
    member = Member.create(
        cer_id=cer_id,
        name="Mario Rossi",
        email="mario@example.com",
        role=MemberRole.CONSUMER,
        tax_info=tax_info,
        address=address,
    )
    member.validate()
    member.activate()
    member.suspend()

    member.activate()

    assert member.status == MemberStatus.ACTIVE


def test_reject_pending_member(cer_id):
    member = make_member(cer_id)
    member.pull_events()

    member.reject()

    assert member.status == MemberStatus.REJECTED

    events = member.pull_events()
    assert len(events) == 1
    assert isinstance(events[0], MemberRejected)
    assert events[0].member_id == member.id


def test_exit_active_member(cer_id, tax_info, address):
    member = Member.create(
        cer_id=cer_id,
        name="Mario Rossi",
        email="mario@example.com",
        role=MemberRole.CONSUMER,
        tax_info=tax_info,
        address=address,
    )
    member.validate()
    member.activate()
    member.pull_events()

    member.exit()

    assert member.status == MemberStatus.EXITED

    events = member.pull_events()
    assert len(events) == 1
    assert isinstance(events[0], MemberExited)
    assert events[0].member_id == member.id


def test_role_can_change_only_when_active(
    cer_id,
    tax_info,
    address,
):
    member = Member.create(
        cer_id=cer_id,
        name="Mario Rossi",
        email="mario@example.com",
        role=MemberRole.CONSUMER,
        tax_info=tax_info,
        address=address,
    )

    with pytest.raises(InvalidMemberRoleChange):
        member.change_role(MemberRole.PROSUMER)


def test_active_member_can_change_role(
    cer_id,
    tax_info,
    address,
):
    member = Member.create(
        cer_id=cer_id,
        name="Mario Rossi",
        email="mario@example.com",
        role=MemberRole.CONSUMER,
        tax_info=tax_info,
        address=address,
    )
    member.validate()
    member.activate()
    member.pull_events()

    member.change_role(MemberRole.PROSUMER)

    assert member.role == MemberRole.PROSUMER

    events = member.pull_events()
    assert len(events) == 1
    assert isinstance(events[0], MemberRoleChanged)
    assert events[0].member_id == member.id


def test_changing_to_same_role_does_not_emit_event(
    cer_id,
    tax_info,
    address,
):
    member = Member.create(
        cer_id=cer_id,
        name="Mario Rossi",
        email="mario@example.com",
        role=MemberRole.CONSUMER,
        tax_info=tax_info,
        address=address,
    )
    member.validate()
    member.activate()
    member.pull_events()

    member.change_role(MemberRole.CONSUMER)

    assert member.role == MemberRole.CONSUMER
    assert member.pull_events() == []


@pytest.mark.parametrize(
    "operation",
    [
        "validate",
        "activate",
        "suspend",
        "reject",
        "exit",
    ],
)
def test_invalid_member_transition_does_not_apply(
    cer_id,
    operation,
):
    member = make_member(cer_id)

    if operation == "activate":
        member.validate()
        member.tax_info = TaxInformation("ABCDEFGHIJKLMNOP")
        member.address = Address(
            street="Via Roma 10",
            city="Matera",
            postal_code="75100",
            country="Italy",
        )
        member.activate()
        with pytest.raises(InvalidStateTransition):
            member.activate()
        return

    if operation == "suspend":
        with pytest.raises(InvalidStateTransition):
            member.suspend()
        return

    if operation == "exit":
        with pytest.raises(InvalidStateTransition):
            member.exit()
        return

    if operation == "reject":
        member.reject()
        with pytest.raises(InvalidStateTransition):
            member.reject()
        return

    member.validate()
    with pytest.raises(InvalidStateTransition):
        member.validate()