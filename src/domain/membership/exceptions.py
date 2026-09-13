# src/domain/member/exceptions.py

from domain.shared.exceptions import DomainException


class MemberDomainError(DomainException):
    """Base exception for membership domain errors."""


class InvalidMemberRoleChange(MemberDomainError):
    """Raised when a member cannot change role."""