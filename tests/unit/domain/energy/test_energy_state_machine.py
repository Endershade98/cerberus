# tests/unit/domain/energy/test_energy_state_machine.py

import pytest

from src.domain.energy.status import EnergyStateMachine, EnergyStatus
from src.domain.shared.exceptions import InvalidStateTransition


def test_valid_transition():
    sm = EnergyStateMachine(EnergyStatus.RECEIVED)
    sm.transition(EnergyStatus.VALIDATING)

    assert sm.current_status == EnergyStatus.VALIDATING


def test_invalid_transition():
    sm = EnergyStateMachine(EnergyStatus.RECEIVED)

    with pytest.raises(InvalidStateTransition):
        sm.transition(EnergyStatus.COMPLETED)