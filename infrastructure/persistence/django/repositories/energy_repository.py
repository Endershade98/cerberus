# infrastructure/persistence/django/repositories/energy_repository.py

from domain.energy.entities import EnergyRecord
from domain.energy.value_objects import EnergyQuantity
from infrastructure.persistence.django.models.energy import EnergyModel


class DjangoEnergyRepository:

    def save(self, record: EnergyRecord) -> None:
        self._persist(record)

    def add(self, record: EnergyRecord) -> None:
        self._persist(record)

    # -------------------------
    # SINGLE SOURCE OF TRUTH
    # -------------------------
    def _persist(self, record: EnergyRecord) -> None:

        member_id = record.member_id.value if hasattr(record.member_id, "value") else record.member_id

        quantity = record.quantity.value if hasattr(record.quantity, "value") else float(record.quantity)

        EnergyModel.objects.create(
            member_id=str(member_id),
            quantity=quantity,
        )

    def get_all(self) -> list[EnergyRecord]:
        return [
            EnergyRecord(
                id=row.id,
                member_id=row.member_id,
                quantity=EnergyQuantity(float(row.quantity)),
                recorded_at=row.recorded_at,
            )
            for row in EnergyModel.objects.all()
        ]