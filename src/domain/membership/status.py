# domain/member/status.py

from enum import StrEnum

from domain.shared.exceptions import InvalidStateTransition


class MemberStatus(StrEnum):
    PENDING = "PENDING"
    VALIDATED = "VALIDATED"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    REJECTED = "REJECTED"
    EXITED = "EXITED"


_ALLOWED_TRANSITIONS: dict[MemberStatus, set[MemberStatus]] = {
    MemberStatus.PENDING: {
        MemberStatus.VALIDATED,
        MemberStatus.REJECTED,
    },
    MemberStatus.VALIDATED: {
        MemberStatus.ACTIVE,
        MemberStatus.REJECTED,
    },
    MemberStatus.ACTIVE: {
        MemberStatus.SUSPENDED,
        MemberStatus.EXITED,
    },
    MemberStatus.SUSPENDED: {
        MemberStatus.ACTIVE,
        MemberStatus.EXITED,
    },
    MemberStatus.REJECTED: set(),
    MemberStatus.EXITED: set(),
}


class MemberStateMachine:
    def __init__(self, status: MemberStatus) -> None:
        self.current_status = status

    def transition(self, target: MemberStatus) -> None:
        if target not in _ALLOWED_TRANSITIONS[self.current_status]:
            raise InvalidStateTransition(
                f"Cannot transition from "
                f"{self.current_status} to {target}."
            )

        self.current_status = target