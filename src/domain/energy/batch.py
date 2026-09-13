# src/domain/energy/batch.py

from dataclasses import dataclass
from datetime import datetime

from domain.energy.value_objects import EnergyBatchId
from domain.energy.status import EnergyBatchStatus
from domain.shared.aggregate_root import AggregateRoot
from domain.shared.exceptions import InvalidStateTransition


@dataclass
class EnergyBatch(AggregateRoot):
    id: EnergyBatchId
    source: str
    period_start: datetime
    period_end: datetime
    received_at: datetime
    status: EnergyBatchStatus = EnergyBatchStatus.RECEIVED

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if self.period_start >= self.period_end:
            raise ValueError("Batch period is invalid.")

        if not self.source.strip():
            raise ValueError("Batch source is required.")

    @classmethod
    def receive(
        cls,
        *,
        source: str,
        period_start: datetime,
        period_end: datetime,
        received_at: datetime,
        batch_id: EnergyBatchId | None = None,
    ) -> "EnergyBatch":
        return cls(
            id=batch_id or EnergyBatchId.generate(),
            source=source.strip(),
            period_start=period_start,
            period_end=period_end,
            received_at=received_at,
        )

    def validate(self) -> None:
        self._transition_to(EnergyBatchStatus.VALIDATED)

    def reject(self) -> None:
        self._transition_to(EnergyBatchStatus.REJECTED)

    def _transition_to(self, target: EnergyBatchStatus) -> None:
        allowed = {
            EnergyBatchStatus.RECEIVED: {
                EnergyBatchStatus.VALIDATED,
                EnergyBatchStatus.REJECTED,
            },
            EnergyBatchStatus.VALIDATED: set(),
            EnergyBatchStatus.REJECTED: set(),
        }

        if target not in allowed[self.status]:
            raise InvalidStateTransition(
                f"Cannot transition batch from "
                f"{self.status} to {target}."
            )

        self.status = target