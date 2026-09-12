# tests/unit/domain/shared/test_extra_value_objects.py

import pytest
from decimal import Decimal

from src.domain.shared.value_objects_extra import (
    Percentage,
    PodCode,
    IncentiveAmount,
)


def test_percentage_valid():
    p = Percentage(Decimal("50"))
    assert p.value == 50


def test_percentage_invalid():
    with pytest.raises(ValueError):
        Percentage(Decimal("200"))


def test_pod_code_valid():
    PodCode("ABCDE")


def test_pod_code_invalid():
    with pytest.raises(ValueError):
        PodCode("A")


def test_incentive_valid():
    IncentiveAmount(Decimal("10"))


def test_incentive_invalid():
    with pytest.raises(ValueError):
        IncentiveAmount(Decimal("-1"))