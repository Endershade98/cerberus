# tests/unit/domain/member/test_member_state_machine.py

import pytest

from src.domain.member.status import MemberStateMachine, MemberStatus
from src.domain.shared.exceptions import InvalidStateTransition


def test_valid_transition():
    sm = MemberStateMachine(MemberStatus.REGISTERED)
    sm.transition(MemberStatus.PENDING)

    assert sm.current_status == MemberStatus.PENDING


def test_invalid_transition():
    sm = MemberStateMachine(MemberStatus.REGISTERED)

    with pytest.raises(InvalidStateTransition):
        sm.transition(MemberStatus.ACTIVE)