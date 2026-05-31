# domain/member/entities.py

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Optional

from domain.shared.aggregate_root import AggregateRoot
from domain.member.status import MemberStatus
from domain.member.value_objects import Address, MemberId, MemberRole, TaxInformation
from domain.member.events import (
    MemberRegistered,
    MemberValidated,
    MemberActivated,
    MemberSuspended,
    MemberRejected,
    MemberExited,
)
from domain.shared.exceptions import BusinessRuleViolation
from domain.shared.time_provider import TimeProvider

time_provider = TimeProvider()

@dataclass
class Member(AggregateRoot):

    id: MemberId = field(default_factory=MemberId.generate)

    name: str = ""
    email: str = ""

    role: MemberRole = MemberRole.CONSUMER
    status: MemberStatus = MemberStatus.REGISTERED

    tax_info: Optional[TaxInformation] = None
    address: Optional[Address] = None

    created_at: datetime = field(default_factory=lambda: time_provider.now())

    # -----------------------
    # FACTORY EXPLICITA (ONLY ENTRY POINT)
    # -----------------------
    @staticmethod
    def create(name, email, role, tax_info, address) -> "Member":
        member = Member(
            name=name,
            email=email,
            role=role,
            tax_info=tax_info,
            address=address,
            status=MemberStatus.PENDING,
        )

        member.add_event(MemberRegistered(member.id, email))

        return member

    # -----------------------
    # RULES
    # -----------------------
    def _ensure_status(self, allowed: set[MemberStatus]):
        if self.status not in allowed:
            raise BusinessRuleViolation(
                f"Invalid status: {self.status}"
            )

    # -----------------------
    # LIFECYCLE
    # -----------------------
    def validate(self):
        self.status = MemberStatus.VALIDATED
        self.add_event(MemberValidated(self.id))

    def activate(self):
        self._ensure_status({MemberStatus.VALIDATED})

        if not self.tax_info:
            raise BusinessRuleViolation("Missing tax info")

        if not self.address:
            raise BusinessRuleViolation("Missing address")

        self.status = MemberStatus.ACTIVE
        self.add_event(MemberActivated(self.id))

    def suspend(self):
        self._ensure_status({MemberStatus.ACTIVE})
        self.status = MemberStatus.SUSPENDED
        self.add_event(MemberSuspended(self.id))

    def reject(self):
        self.status = MemberStatus.REJECTED
        self.add_event(MemberRejected(self.id))

    def exit(self):
        self.status = MemberStatus.EXITED
        self.add_event(MemberExited(self.id))

    def change_role(self, role: MemberRole):
        from domain.member.rules import MemberRules

        MemberRules.assert_can_change_role(self.status)
        self.role = role