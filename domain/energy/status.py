# domain/energy/status.py

from enum import Enum

from domain.shared.exceptions import (
    InvalidStateTransition,
)


class EnergyStatus(str, Enum):

    RECEIVED = "ENG-REC-RCV"
    VALIDATING = "ENG-VAL-START"
    VALIDATED = "ENG-VAL-OK"
    REJECTED = "ENG-VAL-ERR"

    AGGREGATING = "ENG-AGG-START"
    AGGREGATED = "ENG-AGG-DONE"

    CALCULATING = "ENG-CALC-START"
    COMPLETED = "ENG-CALC-DONE"

    FAILED = "ENG-FAIL"


ALLOWED_TRANSITIONS = {

    EnergyStatus.RECEIVED: {
        EnergyStatus.VALIDATING,
    },

    EnergyStatus.VALIDATING: {
        EnergyStatus.VALIDATED,
        EnergyStatus.REJECTED,
    },

    EnergyStatus.VALIDATED: {
        EnergyStatus.AGGREGATING,
    },

    EnergyStatus.AGGREGATING: {
        EnergyStatus.AGGREGATED,
    },

    EnergyStatus.AGGREGATED: {
        EnergyStatus.CALCULATING,
    },

    EnergyStatus.CALCULATING: {
        EnergyStatus.COMPLETED,
    },
}


class EnergyStateMachine:

    def __init__(self, status: EnergyStatus):
        self._status = status

    @property
    def current_status(self):
        return self._status

    def can_transition(
        self,
        target_status: EnergyStatus
    ) -> bool:

        return (
            target_status
            in ALLOWED_TRANSITIONS.get(
                self._status,
                set(),
            )
        )

    def transition(
        self,
        target_status: EnergyStatus
    ) -> EnergyStatus:

        if not self.can_transition(target_status):
            raise InvalidStateTransition(
                f"{self._status} → "
                f"{target_status} not allowed"
            )

        self._status = target_status

        return self._status