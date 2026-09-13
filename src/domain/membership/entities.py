# src/domain/membership/entities.py

from dataclasses import dataclass

from domain.community.value_objects import CerId
from domain.membership.events import (
    MemberActivated,
    MemberExited,
    MemberRejected,
    MemberRegistered,
    MemberRoleChanged,
    MemberSuspended,
    MemberValidated,
)
from domain.membership.exceptions import InvalidMemberRoleChange
from domain.membership.status import MemberStateMachine, MemberStatus
from domain.membership.value_objects import (
    Address,
    EmailAddress,
    MemberId,
    MemberRole,
    TaxInformation,
)
from domain.shared.aggregate_root import AggregateRoot
from domain.shared.exceptions import BusinessRuleViolation


@dataclass
class Member(AggregateRoot):
    id: MemberId
    cer_id: CerId
    name: str
    email: EmailAddress
    role: MemberRole
    status: MemberStatus = MemberStatus.PENDING
    tax_info: TaxInformation | None = None
    address: Address | None = None

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not self.name.strip():
            raise BusinessRuleViolation("Member name is required.")

    @classmethod
    def create(
        cls,
        *,
        cer_id: CerId,
        name: str,
        email: EmailAddress | str,
        role: MemberRole,
        tax_info: TaxInformation | None = None,
        address: Address | None = None,
        member_id: MemberId | None = None,
    ) -> "Member":
        if isinstance(email, str):
            email = EmailAddress(email)

        member = cls(
            id=member_id or MemberId.generate(),
            cer_id=cer_id,
            name=name.strip(),
            email=email,
            role=role,
            status=MemberStatus.PENDING,
            tax_info=tax_info,
            address=address,
        )

        member.add_event(
            MemberRegistered(member_id=member.id)
        )

        return member

    def validate(self) -> None:
        self._transition_to(MemberStatus.VALIDATED)
        self.add_event(MemberValidated(member_id=self.id))

    def activate(self) -> None:
        if self.tax_info is None:
            raise BusinessRuleViolation(
                "Tax information is required before activation."
            )

        if self.address is None:
            raise BusinessRuleViolation(
                "Address is required before activation."
            )

        self._transition_to(MemberStatus.ACTIVE)
        self.add_event(MemberActivated(member_id=self.id))

    def suspend(self) -> None:
        self._transition_to(MemberStatus.SUSPENDED)
        self.add_event(MemberSuspended(member_id=self.id))

    def reject(self) -> None:
        self._transition_to(MemberStatus.REJECTED)
        self.add_event(MemberRejected(member_id=self.id))

    def exit(self) -> None:
        self._transition_to(MemberStatus.EXITED)
        self.add_event(MemberExited(member_id=self.id))

    def change_role(self, role: MemberRole) -> None:
        if self.status != MemberStatus.ACTIVE:
            raise InvalidMemberRoleChange(
                "Member role can only be changed while ACTIVE."
            )

        if self.role == role:
            return

        self.role = role

        self.add_event(
            MemberRoleChanged(member_id=self.id)
        )

    def _transition_to(self, target: MemberStatus) -> None:
        state_machine = MemberStateMachine(self.status)
        state_machine.transition(target)
        self.status = state_machine.current_status