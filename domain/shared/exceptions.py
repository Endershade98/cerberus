# domain/shared/exceptions.py

class DomainException(Exception):
    """Base exception for domain layer."""


class BusinessRuleViolation(DomainException):
    """Raised when a business invariant is violated."""


class InvalidStateTransition(DomainException):
    """Raised when a state machine transition is invalid."""