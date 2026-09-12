# tests/unit/domain/member/test_member_value_objects.py

import pytest

from src.domain.member.value_objects import (
    MemberId,
    TaxInformation,
    Address,
    MemberRole,
)


def test_tax_normalization():
    tax = TaxInformation("rssmra85t10a562s")
    assert tax.fiscal_code == "RSSMRA85T10A562S"


def test_tax_invalid_length():
    with pytest.raises(ValueError):
        TaxInformation("ABC")


def test_address_full():
    addr = Address("Via Roma", "Napoli", "80100", "IT")
    assert "Napoli" in addr.full_address()


def test_member_role_permissions():
    assert MemberRole.CONSUMER.can_consume()
    assert not MemberRole.CONSUMER.can_produce()

    assert MemberRole.PRODUCER.can_produce()
    assert MemberRole.PROSUMER.can_consume()