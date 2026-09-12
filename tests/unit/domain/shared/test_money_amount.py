# tests/unit/domain/shared/test_money_amount.py

import pytest
from decimal import Decimal

from src.domain.shared.value_objects import MoneyAmount


def test_should_create_money():
    m = MoneyAmount(Decimal("10.5"))
    assert m.value == Decimal("10.5")


def test_should_not_allow_negative():
    with pytest.raises(ValueError):
        MoneyAmount(Decimal("-1"))