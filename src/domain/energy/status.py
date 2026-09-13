# src/domain/energy/status.py

from enum import StrEnum


class EnergyBatchStatus(StrEnum):
    RECEIVED = "RECEIVED"
    VALIDATED = "VALIDATED"
    REJECTED = "REJECTED"