# tests/unit/domain/energy/test_energy_service.py

from decimal import Decimal
from datetime import datetime

from domain.energy.entities import EnergyRecord
from domain.energy.services import EnergyDomainService
from domain.shared.value_objects import EnergyQuantity
from domain.member.value_objects import MemberId


def test_should_calculate_total_energy():
    # Arrange
    records = [
        EnergyRecord(
            member_id=MemberId.generate(),
            timestamp=datetime.now(),
            quantity=EnergyQuantity(Decimal("10")),
        ),
        EnergyRecord(
            member_id=MemberId.generate(),
            timestamp=datetime.now(),
            quantity=EnergyQuantity(Decimal("15")),
        ),
    ]

    # Act
    total = EnergyDomainService.calculate_total(records)

    # Assert
    assert total.value == Decimal("25")