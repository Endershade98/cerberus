# tests/unit/domain/energy/test_energy_state_machine.py

import pytest

from domain.energy.status import (
    EnergyStateMachine,
    EnergyStatus
)


def test_should_allow_valid_transition():

    sm = EnergyStateMachine(EnergyStatus.RECEIVED)

    sm.transition(EnergyStatus.VALIDATING)

    assert sm.status == EnergyStatus.VALIDATING


def test_should_raise_for_invalid_transition():

    sm = EnergyStateMachine(EnergyStatus.RECEIVED)

    with pytest.raises(Exception):
        sm.transition(EnergyStatus.COMPLETED)