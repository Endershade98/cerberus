# infrastructure/persistence/django/repositories/energy_repository.py

from domain.energy.entities import EnergyRecord
from domain.shared.value_objects import EnergyQuantity
from infrastructure.persistence.django.models.energy import EnergyModel


class DjangoEnergyRepository:

    def save(self, record):
        member_id = (
            record.member_id.value
            if hasattr(record.member_id, "value")
            else record.member_id
        )

        EnergyModel.objects.create(
            member_id=str(member_id),
            quantity=record.quantity.value,
        )

    def get_all(self) -> list[EnergyRecord]:
        return [
            EnergyRecord(
                member_id=record.member_id,
                timestamp=record.timestamp,
                quantity=EnergyQuantity(record.quantity),
            )
            for record in EnergyModel.objects.all()
        ]