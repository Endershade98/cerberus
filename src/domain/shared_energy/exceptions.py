# src/domain/shared_energy/exceptions.py

from domain.shared.exceptions import DomainException


class SharedEnergyDomainError(DomainException):
    """Base exception for shared energy errors."""