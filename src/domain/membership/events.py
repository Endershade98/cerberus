# domain/member/events.py

from dataclasses import dataclass

from domain.membership.value_objects import MemberId
from domain.shared.domain_event import DomainEvent


@dataclass(frozen=True, kw_only=True)
class MemberRegistered(DomainEvent):
    member_id: MemberId  # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class MemberValidated(DomainEvent):
    member_id: MemberId # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class MemberActivated(DomainEvent):
    member_id: MemberId # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class MemberSuspended(DomainEvent):
    member_id: MemberId  # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class MemberRejected(DomainEvent):
    member_id: MemberId # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class MemberExited(DomainEvent):
    member_id: MemberId # type: ignore[assignment]


@dataclass(frozen=True, kw_only=True)
class MemberRoleChanged(DomainEvent):
    member_id: MemberId # type: ignore[assignment]