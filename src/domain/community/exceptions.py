# src/domain/community/exceptions.py

from domain.shared.exceptions import DomainException


class CerDomainError(DomainException):
    """Base exception for CER domain errors."""