# src/domain/shared/exceptions.py

class DomainException(Exception):
    """Base exception for domain errors."""


class BusinessRuleViolation(DomainException):
    """Raised when a domain business rule is violated."""


class InvalidStateTransition(DomainException):
    """Raised when an aggregate cannot perform a state transition."""