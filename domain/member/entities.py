# domain/member/entities.py

from dataclasses import dataclass, field
from datetime import datetime

from domain.shared.aggregate_root import AggregateRoot
from domain.shared.exceptions import (
    BusinessRuleViolation,
)

from domain.shared.time_provider import TimeProvider

from domain.member.status import (
    MemberStatus,
    MemberStateMachine,
)

from domain.member.value_objects import (
    Address,
    MemberId,
    MemberRole,
    TaxInformation,
)

from domain.member.events import (
    MemberRegistered,
    MemberValidated,
    MemberActivated,
    MemberSuspended,
    MemberRejected,
    MemberExited,
)

time_provider = TimeProvider()


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
        default_factory=lambda: time_provider.now()
    )

    # -----------------------
    # FACTORY
    # -----------------------

    @staticmethod
    def create(
        name,
        email,
        role,
        tax_info,
        address,
    ) -> "Member":

        member = Member(
            name=name,
            email=email,
            role=role,
            tax_info=tax_info,
            address=address,
            status=MemberStatus.PENDING,
        )

        member.add_event(
            MemberRegistered(
                member.id,
                email,
            )
        )

        return member

    # -----------------------
    # STATE MACHINE GATEWAY
    # -----------------------

    def _transition_to(
        self,
        target_status: MemberStatus,
    ) -> None:

        machine = MemberStateMachine(
            self.status
        )

        self.status = machine.transition(
            target_status
        )

    # -----------------------
    # LIFECYCLE
    # -----------------------

    def validate(self) -> None:

        self._transition_to(
            MemberStatus.VALIDATED
        )

        self.add_event(
            MemberValidated(self.id)
        )

    def activate(self) -> None:

        # Aggregate invariants

        if not self.tax_info:
            raise BusinessRuleViolation(
                "Missing tax info"
            )

        if not self.address:
            raise BusinessRuleViolation(
                "Missing address"
            )

        self._transition_to(
            MemberStatus.ACTIVE
        )

        self.add_event(
            MemberActivated(self.id)
        )

    def suspend(self) -> None:

        self._transition_to(
            MemberStatus.SUSPENDED
        )

        self.add_event(
            MemberSuspended(self.id)
        )

    def reject(self) -> None:

        self._transition_to(
            MemberStatus.REJECTED
        )

        self.add_event(
            MemberRejected(self.id)
        )

    def exit(self) -> None:

        self._transition_to(
            MemberStatus.EXITED
        )

        self.add_event(
            MemberExited(self.id)
        )

    # -----------------------
    # BUSINESS BEHAVIOR
    # -----------------------

    def change_role(
        self,
        role: MemberRole,
    ) -> None:

        if self.status != MemberStatus.ACTIVE:
            raise BusinessRuleViolation(
                "Only ACTIVE members can change role"
            )

        self.role = role