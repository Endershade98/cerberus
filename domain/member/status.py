# domain/member/status.py
from enum import Enum


class MemberStatus(str, Enum):
    PENDING = "MEM-PENDING"
    ACTIVE = "MEM-ACTIVE"
    SUSPENDED = "MEM-SUSP"
    REJECTED = "MEM-REJ"
    EXITED = "MEM-EXIT"

# RULES
ALLOWED_TRANSITIONS = {
    MemberStatus.PENDING: [
        MemberStatus.ACTIVE,
        MemberStatus.REJECTED
    ],
    MemberStatus.ACTIVE: [
        MemberStatus.SUSPENDED,
        MemberStatus.EXITED
    ],
    MemberStatus.SUSPENDED: [
        MemberStatus.ACTIVE,
        MemberStatus.EXITED
    ],
}

class MemberStateMachine:

    def __init__(self, status: MemberStatus):
        self.status = status

    def transition(self, new_status: MemberStatus):
        allowed = ALLOWED_TRANSITIONS.get(self.status, [])

        if new_status not in allowed:
            raise ValueError(
                f"Invalid transition {self.status} → {new_status}"
            )

        self.status = new_status