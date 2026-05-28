# tests/unit/domain/member/test_member_events.py

from domain.member.entities import Member

from domain.member.events import (
    MemberRegistered,
    MemberValidated,
    MemberActivated,
)

from domain.member.value_objects import (
    TaxInformation,
    Address,
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
        name="Mario Rossi",
        email="mario@test.com",
        tax_info=create_tax_info(),
        address=create_address(),
    )


def test_member_registration_emits_event():

    member = create_member()

    events = member.pull_events()

    assert len(events) == 1

    assert isinstance(events[0], MemberRegistered)

    assert events[0].member_id == member.id


def test_member_validation_emits_event():

    member = create_member()

    member.pull_events()

    member.validate()

    events = member.pull_events()

    assert len(events) == 1

    assert isinstance(events[0], MemberValidated)

    assert events[0].member_id == member.id


def test_member_activation_emits_event():

    member = create_member()

    member.pull_events()

    member.validate()
    member.activate()

    events = member.pull_events()

    assert len(events) == 2

    assert isinstance(events[0], MemberValidated)

    assert isinstance(events[1], MemberActivated)

    assert events[1].member_id == member.id