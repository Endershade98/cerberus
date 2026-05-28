# domain/member/status.py

from enum import Enum
from domain.shared.exceptions import InvalidStateTransition


class MemberStatus(str, Enum):
    PENDING = "MEM-PENDING"
    ACTIVE = "MEM-ACTIVE"
    SUSPENDED = "MEM-SUSP"
    REJECTED = "MEM-REJ"
    EXITED = "MEM-EXIT"


ALLOWED_TRANSITIONS = {
    MemberStatus.PENDING: [MemberStatus.ACTIVE, MemberStatus.REJECTED],
    MemberStatus.ACTIVE: [MemberStatus.SUSPENDED, MemberStatus.EXITED],
    MemberStatus.SUSPENDED: [MemberStatus.ACTIVE, MemberStatus.EXITED],
}


class MemberStateMachine:
    def __init__(self, status: MemberStatus):
        self.status = status

    def transition(self, new_status: MemberStatus):

        allowed = ALLOWED_TRANSITIONS.get(self.status, [])

        if new_status not in allowed:
            raise InvalidStateTransition(
                f"{self.status} → {new_status} not allowed"
            )

        self.status = new_status