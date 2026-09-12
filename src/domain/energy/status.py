# domain/energy/status.py

from enum import Enum

from src.domain.shared.exceptions import (
    InvalidStateTransition,
)


class EnergyStatus(str, Enum):

    RECEIVED = "ENG-REC-RCV"

    VALIDATING = "ENG-VAL-START"
    VALIDATED = "ENG-VAL-OK"

    REJECTED = "ENG-VAL-ERR"

    AGGREGATING = "ENG-AGG-START"

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
        EnergyStatus.COMPLETED,
        EnergyStatus.FAILED,
    },

    EnergyStatus.FAILED: {
        EnergyStatus.VALIDATING,
    },
}


class EnergyStateMachine:

    def __init__(
        self,
        current_status: EnergyStatus,
    ):
        self.current_status = current_status

    def transition(
        self,
        target_status: EnergyStatus,
    ) -> EnergyStatus:

        allowed = ALLOWED_TRANSITIONS.get(
            self.current_status,
            set(),
        )

        if target_status not in allowed:
            raise InvalidStateTransition(
                f"{self.current_status} -> {target_status}"
            )

        self.current_status = target_status

        return self.current_status