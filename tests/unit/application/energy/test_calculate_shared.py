# tests/unit/application/energy/test_calculate_shared.py

from decimal import Decimal
from datetime import datetime

from domain.energy.entities import EnergyRecord
from domain.energy.services import EnergyDomainService
from domain.shared.value_objects import EnergyQuantity
from domain.member.value_objects import MemberId


def test_calculate_shared_energy():
    # Arrange
    records = [
        EnergyRecord(
            member_id=MemberId.generate(),
            timestamp=datetime.now(),
            quantity=EnergyQuantity(Decimal("5")),
        ),
        EnergyRecord(
            member_id=MemberId.generate(),
            timestamp=datetime.now(),
            quantity=EnergyQuantity(Decimal("7")),
        ),
    ]

    # Act
    result = EnergyDomainService.calculate_total(records)

    # Assert
    assert result.value == Decimal("12")