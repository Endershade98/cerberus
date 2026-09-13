# src/domain/incentive/exceptions.py

from domain.shared.exceptions import DomainException


class IncentiveDomainError(DomainException):
    """Base exception for incentive domain errors."""