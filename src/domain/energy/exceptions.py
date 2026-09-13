# src/domain/energy/exceptions.py

from domain.shared.exceptions import DomainException


class EnergyDomainError(DomainException):
    """Base exception for energy domain errors."""