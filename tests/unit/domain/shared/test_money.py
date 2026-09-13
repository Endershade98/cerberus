# tests/unit/domain/shared/test_money.py

from decimal import Decimal

import pytest

from domain.shared.money import Currency, EUR, MoneyAmount


def test_currency_normalizes_code():
    currency = Currency(" eur ")

    assert currency.code == "EUR"


def test_currency_requires_three_characters():
    with pytest.raises(ValueError):
        Currency("EURO")


def test_money_amount_quantizes_to_two_decimals():
    money = MoneyAmount(Decimal("10.125"))

    assert money.value == Decimal("10.13")


def test_money_amount_rejects_negative_value():
    with pytest.raises(ValueError, match="cannot be negative"):
        MoneyAmount("-1")


def test_money_zero_uses_requested_currency():
    usd = Currency("USD")

    money = MoneyAmount.zero(usd)

    assert money.value == Decimal("0.00")
    assert money.currency.code == "USD"


def test_money_adds_same_currency():
    first = MoneyAmount("10.20")
    second = MoneyAmount("2.30")

    result = first.add(second)

    assert result.value == Decimal("12.50")
    assert result.currency.code == "EUR"


def test_money_rejects_different_currencies():
    eur = MoneyAmount("10", EUR)
    usd = MoneyAmount("10", Currency("USD"))

    with pytest.raises(
        ValueError,
        match="different currencies",
    ):
        eur.add(usd)