# domain/energy/status.py

from enum import Enum

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
    EnergyStatus.RECEIVED: [EnergyStatus.VALIDATING],
    EnergyStatus.VALIDATING: [
        EnergyStatus.VALIDATED,
        EnergyStatus.REJECTED
    ],
    EnergyStatus.VALIDATED: [EnergyStatus.AGGREGATING],
    EnergyStatus.AGGREGATING: [EnergyStatus.AGGREGATED],
    EnergyStatus.AGGREGATED: [EnergyStatus.CALCULATING],
    EnergyStatus.CALCULATING: [EnergyStatus.COMPLETED],
}

class EnergyStateMachine:

    def __init__(self, status: EnergyStatus):
        self.status = status

    def transition(self, new_status: EnergyStatus):
        allowed = ALLOWED_TRANSITIONS.get(self.status, [])

        if new_status not in allowed:
            raise Exception(
                f"Invalid transition {self.status} → {new_status}"
            )

        self.status = new_status