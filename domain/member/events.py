# domain/member/events.py

from dataclasses import dataclass

from domain.shared.domain_event import DomainEvent
from domain.member.value_objects import MemberId


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