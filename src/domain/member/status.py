# domain/member/status.py

from enum import Enum

from src.domain.shared.exceptions import (
    InvalidStateTransition,
)


class MemberStatus(str, Enum):

    REGISTERED = "MEM-REG"
    PENDING = "MEM-PENDING"
    VALIDATED = "MEM-VALID"
    ACTIVE = "MEM-ACTIVE"
    SUSPENDED = "MEM-SUSP"
    REJECTED = "MEM-REJ"
    EXITED = "MEM-EXIT"


ALLOWED_TRANSITIONS = {

    MemberStatus.REGISTERED: {
        MemberStatus.PENDING,
    },

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
}


class MemberStateMachine:

    def __init__(
        self,
        current_status: MemberStatus,
    ):
        self.current_status = current_status

    def can_transition(
        self,
        target_status: MemberStatus,
    ) -> bool:

        return (
            target_status
            in ALLOWED_TRANSITIONS.get(
                self.current_status,
                set(),
            )
        )

    def transition(
        self,
        target_status: MemberStatus,
    ) -> MemberStatus:

        if not self.can_transition(
            target_status
        ):
            raise InvalidStateTransition(
                f"{self.current_status} -> "
                f"{target_status} not allowed"
            )

        self.current_status = target_status

        return self.current_status