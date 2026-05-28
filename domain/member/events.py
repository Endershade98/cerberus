# domain/member/events.py

from dataclasses import dataclass
from datetime import datetime

from domain.shared.events import DomainEvent
from domain.member.value_objects import MemberId


class DomainEvent:
    """Base class for all domain events."""
    def __init__(self):
        self.occurred_on = datetime.utcnow()


@dataclass(frozen=True)
class MemberActivated(DomainEvent):
    member_id: MemberId


@dataclass(frozen=True)
class MemberSuspended(DomainEvent):
    member_id: MemberId


@dataclass(frozen=True)
class MemberRejected(DomainEvent):
    member_id: MemberId


@dataclass(frozen=True)
class MemberExited(DomainEvent):
    member_id: MemberId


@dataclass(frozen=True)
class MemberRegistered(DomainEvent):
    member_id: MemberId


@dataclass(frozen=True)
class MemberValidated(DomainEvent):
    member_id: MemberId