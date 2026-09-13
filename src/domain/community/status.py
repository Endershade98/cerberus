# src/domain/community/status.py

from enum import StrEnum

from domain.shared.exceptions import InvalidStateTransition


class CerStatus(StrEnum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    CLOSED = "CLOSED"


_ALLOWED_TRANSITIONS: dict[CerStatus, set[CerStatus]] = {
    CerStatus.DRAFT: {
        CerStatus.ACTIVE,
    },
    CerStatus.ACTIVE: {
        CerStatus.SUSPENDED,
        CerStatus.CLOSED,
    },
    CerStatus.SUSPENDED: {
        CerStatus.ACTIVE,
        CerStatus.CLOSED,
    },
    CerStatus.CLOSED: set(),
}


class CerStateMachine:
    def __init__(self, status: CerStatus) -> None:
        self.current_status = status

    def transition(self, target: CerStatus) -> None:
        allowed = _ALLOWED_TRANSITIONS[self.current_status]

        if target not in allowed:
            raise InvalidStateTransition(
                f"Cannot transition from "
                f"{self.current_status} to {target}."
            )

        self.current_status = target