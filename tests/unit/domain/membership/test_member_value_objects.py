# tests/unit/domain/membership/test_member_value_objects.py

from uuid import UUID

import pytest

from domain.membership.value_objects import (
    Address,
    EmailAddress,
    MemberId,
    MemberRole,
    TaxInformation,
)


def test_member_id_generates_identifier():
    member_id = MemberId.generate()

    assert isinstance(member_id.value, UUID)


def test_email_normalizes_value():
    email = EmailAddress("  USER@Example.COM ")

    assert email.value == "user@example.com"
    assert str(email) == "user@example.com"


@pytest.mark.parametrize(
    "value",
    [
        "",
        "invalid",
        "user@",
        "@example.com",
        "user@example",
    ],
)
def test_email_rejects_invalid_value(value):
    with pytest.raises(ValueError, match="Invalid email"):
        EmailAddress(value)


def test_tax_information_normalizes_fiscal_code():
    tax_info = TaxInformation(" abcdefghijklmnop ")

    assert tax_info.fiscal_code == "ABCDEFGHIJKLMNOP"


def test_tax_information_requires_sixteen_characters():
    with pytest.raises(
        ValueError,
        match="16 characters",
    ):
        TaxInformation("ABC")


def test_address_builds_full_address():
    address = Address(
        street="Via Roma 10",
        city="Matera",
        postal_code="75100",
        country="Italy",
    )

    assert address.full_address == (
        "Via Roma 10, 75100 Matera, Italy"
    )


def test_address_rejects_empty_fields():
    with pytest.raises(ValueError, match="cannot be empty"):
        Address(
            street="",
            city="Matera",
            postal_code="75100",
            country="Italy",
        )


def test_consumer_can_consume_but_not_produce():
    assert MemberRole.CONSUMER.can_consume() is True
    assert MemberRole.CONSUMER.can_produce() is False


def test_producer_can_produce_but_not_consume():
    assert MemberRole.PRODUCER.can_produce() is True
    assert MemberRole.PRODUCER.can_consume() is False


def test_prosumer_can_both_produce_and_consume():
    assert MemberRole.PROSUMER.can_produce() is True
    assert MemberRole.PROSUMER.can_consume() is True