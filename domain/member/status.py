# domain/member/status.py

from enum import Enum


class MemberStatus(str, Enum):
    """
    Enumeration representing the lifecycle status of a Member.

    Each status is aligned with business workflow definitions
    and documented in `tables.md`.
    """
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
    """
    State machine responsible for validating member status transitions.

    Ensures that:
    - only valid transitions are allowed
    - domain invariants are enforced

    Example:
        PENDING → ACTIVE  (valid)
        PENDING → EXITED  (invalid)
    """

    def __init__(self, status: MemberStatus):
        self.status = status

    def transition(self, new_status: MemberStatus):
        allowed = ALLOWED_TRANSITIONS.get(self.status, [])

        if new_status not in allowed:
            raise ValueError(
                f"Invalid transition {self.status} → {new_status}"
            )

        self.status = new_status