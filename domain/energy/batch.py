# domain/energy/batch.py

from dataclasses import dataclass, field

from domain.shared.aggregate_root import AggregateRoot
from domain.shared.id_provider import IdProvider

from domain.energy.status import (
    EnergyStatus,
    EnergyStateMachine,
)

id_provider = IdProvider()


@dataclass
class EnergyBatch(AggregateRoot):

    id: str = field(
        default_factory=id_provider.generate
    )

    status: EnergyStatus = (
        EnergyStatus.RECEIVED
    )

    def _transition(
        self,
        target: EnergyStatus,
    ):

        machine = EnergyStateMachine(
            self.status
        )

        self.status = machine.transition(
            target
        )

    def start_validation(self):

        self._transition(
            EnergyStatus.VALIDATING
        )

    def validate(self):

        self._transition(
            EnergyStatus.VALIDATED
        )

    def reject(self):

        self._transition(
            EnergyStatus.REJECTED
        )

    def start_aggregation(self):

        self._transition(
            EnergyStatus.AGGREGATING
        )

    def complete(self):

        self._transition(
            EnergyStatus.COMPLETED
        )

    def fail(self):

        self._transition(
            EnergyStatus.FAILED
        )

    def retry(self):

        self._transition(
            EnergyStatus.VALIDATING
        )