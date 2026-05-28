# domain/member/entities.py

from dataclasses import dataclass, field
from datetime import datetime, UTC

from domain.shared.aggregate_root import AggregateRoot
from domain.shared.exceptions import BusinessRuleViolation

from domain.member.status import (
    MemberStatus,
    MemberStateMachine,
)

from domain.member.value_objects import (
    MemberRole,
    MemberId,
    TaxInformation,
    Address,
)

from domain.member.events import (
    MemberRegistered,
    MemberValidated,
    MemberActivated,
    MemberSuspended,
    MemberRejected,
    MemberExited,
)

from domain.member.policies import (
    ActivationPolicy,
    SuspensionPolicy,
)


@dataclass
class Member(AggregateRoot):

    id: MemberId = field(default_factory=MemberId.generate)

    name: str = ""
    email: str = ""

    role: MemberRole = MemberRole.CONSUMER

    status: MemberStatus = MemberStatus.REGISTERED

    tax_info: TaxInformation | None = None
    address: Address | None = None

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @staticmethod
    def register(
        name: str,
        email: str,
        tax_info: TaxInformation,
        address: Address,
    ):

        member = Member(
            name=name,
            email=email,
            tax_info=tax_info,
            address=address,
            status=MemberStatus.PENDING,
        )

        member.add_event(
            MemberRegistered(member_id=member.id)
        )

        return member

    def validate(self):

        self.status = (
            MemberStateMachine(self.status)
            .transition(MemberStatus.VALIDATED)
        )

        self.add_event(
            MemberValidated(member_id=self.id)
        )

    def activate(self):

        ActivationPolicy.validate(self)

        self.status = (
            MemberStateMachine(self.status)
            .transition(MemberStatus.ACTIVE)
        )

        self.add_event(
            MemberActivated(member_id=self.id)
        )

    def suspend(self):

        SuspensionPolicy.validate(self)

        self.status = (
            MemberStateMachine(self.status)
            .transition(MemberStatus.SUSPENDED)
        )

        self.add_event(
            MemberSuspended(member_id=self.id)
        )

    def reject(self):

        self.status = (
            MemberStateMachine(self.status)
            .transition(MemberStatus.REJECTED)
        )

        self.add_event(
            MemberRejected(member_id=self.id)
        )

    def exit(self):

        self.status = (
            MemberStateMachine(self.status)
            .transition(MemberStatus.EXITED)
        )

        self.add_event(
            MemberExited(member_id=self.id)
        )

    def reactivate(self):

        self.status = (
            MemberStateMachine(self.status)
            .transition(MemberStatus.ACTIVE)
        )

    def change_role(self, new_role: MemberRole):

        if self.status != MemberStatus.ACTIVE:
            raise BusinessRuleViolation(
                "Only ACTIVE members can change role"
            )

        self.role = new_role