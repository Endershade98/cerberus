# domain/member/entities.py
from dataclasses import dataclass, field
from uuid import uuid4, UUID
from datetime import datetime

from .value_objects import MemberRole
from .status import MemberStatus, MemberStateMachine


@dataclass
class RegisterMemberInput:
    """ Input data for registering a new member. """
    role: MemberRole

@dataclass
class Member:
    id: UUID = field(default_factory=uuid4)
    role: MemberRole = MemberRole.CONSUMER
    status: MemberStatus = MemberStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

    def activate(self):
        sm = MemberStateMachine(self.status)
        sm.transition(MemberStatus.ACTIVE)
        self.status = sm.status

    def suspend(self):
        sm = MemberStateMachine(self.status)
        sm.transition(MemberStatus.SUSPENDED)
        self.status = sm.status

    def reject(self):
        sm = MemberStateMachine(self.status)
        sm.transition(MemberStatus.REJECTED)
        self.status = sm.status

    def exit(self):
        sm = MemberStateMachine(self.status)
        sm.transition(MemberStatus.EXITED)
        self.status = sm.status

    def change_role(self, new_role: MemberRole):
        if self.status != MemberStatus.ACTIVE:
            raise ValueError("Only active members can change role")

        self.role = new_role