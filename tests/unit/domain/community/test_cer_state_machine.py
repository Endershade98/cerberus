# tests/unit/domain/community/test_cer_state_machine.py

import pytest

from domain.community.status import CerStateMachine, CerStatus
from domain.shared.exceptions import InvalidStateTransition


@pytest.mark.parametrize(
    ("initial", "target"),
    [
        (CerStatus.DRAFT, CerStatus.ACTIVE),
        (CerStatus.ACTIVE, CerStatus.SUSPENDED),
        (CerStatus.ACTIVE, CerStatus.CLOSED),
        (CerStatus.SUSPENDED, CerStatus.ACTIVE),
        (CerStatus.SUSPENDED, CerStatus.CLOSED),
    ],
)
def test_valid_cer_state_transitions(initial, target):
    state_machine = CerStateMachine(initial)

    state_machine.transition(target)

    assert state_machine.current_status == target


@pytest.mark.parametrize(
    ("initial", "target"),
    [
        (CerStatus.DRAFT, CerStatus.SUSPENDED),
        (CerStatus.DRAFT, CerStatus.CLOSED),
        (CerStatus.ACTIVE, CerStatus.DRAFT),
        (CerStatus.SUSPENDED, CerStatus.DRAFT),
        (CerStatus.CLOSED, CerStatus.DRAFT),
        (CerStatus.CLOSED, CerStatus.ACTIVE),
        (CerStatus.CLOSED, CerStatus.SUSPENDED),
        (CerStatus.CLOSED, CerStatus.CLOSED),
    ],
)
def test_invalid_cer_state_transitions_raise(initial, target):
    state_machine = CerStateMachine(initial)

    with pytest.raises(InvalidStateTransition):
        state_machine.transition(target)