# infrastructure/django_app/persistence/django/repositories/energy_repository.py

from domain.energy.entities import EnergyRecord
from domain.energy.value_objects import EnergyQuantity
from domain.energy.batch import EnergyBatch

from domain.energy.repositories import (
    EnergyRepository,
)

from src.infrastructure.persistence.django.models import (
    EnergyModel,
)


class DjangoEnergyRepository(
    EnergyRepository
):

    def save(
        self,
        record: EnergyRecord,
    ) -> None:

        EnergyModel.objects.create(
            id=record.id,
            member_id=record.member_id,
            recorded_at=record.recorded_at,
            quantity=record.quantity.value,
        )

    def get_all(
        self,
    ) -> list[EnergyRecord]:

        return [
            EnergyRecord(
                id=str(row.id),
                member_id=str(row.member_id),
                quantity=EnergyQuantity(
                    float(row.quantity)
                ),
                recorded_at=row.recorded_at,
            )
            for row
            in EnergyModel.objects.all()
        ]

    def get_batch(
        self,
        batch_id: str,
    ) -> EnergyBatch | None:

        raise NotImplementedError(
            "EnergyBatch persistence not implemented"
        )

    def save_batch(
        self,
        batch: EnergyBatch,
    ) -> None:

        raise NotImplementedError(
            "EnergyBatch persistence not implemented"
        )