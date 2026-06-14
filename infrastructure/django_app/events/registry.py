# infrastructure/django_app/events/registry.py

from domain.member.events import (
    MemberRegistered,
    MemberValidated,
    MemberActivated,
    MemberSuspended,
    MemberRejected,
    MemberExited,
)

EVENT_REGISTRY = {
    "MemberRegistered": MemberRegistered,
    "MemberValidated": MemberValidated,
    "MemberActivated": MemberActivated,
    "MemberSuspended": MemberSuspended,
    "MemberRejected": MemberRejected,
    "MemberExited": MemberExited,
}