# tests/unit/domain/energy/test_energy_service.py

from decimal import Decimal
from datetime import datetime

from domain.energy.entities import EnergyRecord
from domain.energy.services import EnergyDomainService


def test_should_calculate_total_energy():

    records = [
        EnergyRecord(
            member_id=1,
            timestamp=datetime.now(),
            value_kwh=Decimal("10")
        ),
        EnergyRecord(
            member_id=2,
            timestamp=datetime.now(),
            value_kwh=Decimal("15")
        ),
    ]

    total = EnergyDomainService.calculate_total(records)

    assert total.value == Decimal("25")