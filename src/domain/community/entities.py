# src/domain/community/entities.py

from dataclasses import dataclass, field

from domain.community.events import (
    CerActivated,
    CerClosed,
    CerCreated,
    CerSuspended,
)
from domain.community.status import CerStateMachine, CerStatus
from domain.community.value_objects import CerId
from domain.shared.aggregate_root import AggregateRoot
from domain.shared.exceptions import BusinessRuleViolation


@dataclass
class Cer(AggregateRoot):
    id: CerId
    name: str
    status: CerStatus = CerStatus.DRAFT

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not self.name.strip():
            raise BusinessRuleViolation("CER name is required.")

    @classmethod
    def create(
        cls,
        name: str,
        cer_id: CerId | None = None,
    ) -> "Cer":
        cer = cls(
            id=cer_id or CerId.generate(),
            name=name.strip(),
            status=CerStatus.DRAFT,
        )

        cer.add_event(CerCreated(cer_id=cer.id))

        return cer

    def activate(self) -> None:
        self._transition_to(CerStatus.ACTIVE)
        self.add_event(CerActivated(cer_id=self.id))

    def suspend(self) -> None:
        self._transition_to(CerStatus.SUSPENDED)
        self.add_event(CerSuspended(cer_id=self.id))

    def close(self) -> None:
        self._transition_to(CerStatus.CLOSED)
        self.add_event(CerClosed(cer_id=self.id))

    def _transition_to(self, target: CerStatus) -> None:
        state_machine = CerStateMachine(self.status)
        state_machine.transition(target)
        self.status = state_machine.current_status