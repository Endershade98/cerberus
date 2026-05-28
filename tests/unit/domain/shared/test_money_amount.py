# tests/unit/domain/shared/test_money_amount.py

from decimal import Decimal
import pytest

from domain.shared.value_objects import MoneyAmount


def test_should_create_money_amount():
    money = MoneyAmount(Decimal("10.50"))

    assert money.value == Decimal("10.50")


def test_should_not_allow_negative_money():
    with pytest.raises(ValueError):
        MoneyAmount(Decimal("-1"))