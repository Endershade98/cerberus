# domain/member/entities.py

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime, UTC

from domain.member.value_objects import MemberRole
from domain.member.status import MemberStatus, MemberStateMachine
from domain.shared.aggregate_root import AggregateRoot
from domain.shared.exceptions import BusinessRuleViolation


@dataclass
class Member(AggregateRoot):

    name: str = ""
    email: str = ""
    role: MemberRole = MemberRole.CONSUMER
    status: MemberStatus = MemberStatus.PENDING
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

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
            raise BusinessRuleViolation("Only active members can change role")

        self.role = new_role