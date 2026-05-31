# tests/unit/domain/member/test_member_events.py

from domain.member.entities import Member
from domain.member.events import (
    MemberRegistered,
    MemberValidated,
    MemberActivated,
    MemberSuspended,
    MemberRejected,
    MemberExited,
)
from domain.member.value_objects import MemberRole, TaxInformation, Address


def create_member():
    return Member.create(
        name="Mario",
        email="mario@test.com",
        role=MemberRole.CONSUMER,
        tax_info=TaxInformation("RSSMRA85T10A562S"),
        address=Address("Via Roma", "Napoli", "80100", "IT"),
    )


def test_should_emit_registration_event():
    member = create_member()

    events = member.pull_events()
    assert isinstance(events[0], MemberRegistered)


def test_should_emit_validation_event():
    member = create_member()
    member.validate()

    events = member.pull_events()

    assert any(isinstance(e, MemberValidated) for e in events)


def test_should_emit_activation_event():
    member = create_member()

    member.validate()
    member.activate()

    events = member.pull_events()
    assert isinstance(events[-1], MemberActivated)


def test_should_emit_suspension_event():
    member = create_member()

    member.validate()
    member.activate()
    member.suspend()

    events = member.pull_events()
    assert isinstance(events[-1], MemberSuspended)


def test_should_emit_reject_event():
    member = create_member()

    member.reject()

    events = member.pull_events()
    assert isinstance(events[-1], MemberRejected)


def test_should_emit_exit_event():
    member = create_member()

    member.exit()

    events = member.pull_events()
    assert isinstance(events[-1], MemberExited)