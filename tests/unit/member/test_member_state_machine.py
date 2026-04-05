# tests/unit/member/test_member_state_machine.py
import pytest
from domain.member.status import MemberStatus, MemberStateMachine


def test_valid_transition_pending_to_active():
    sm = MemberStateMachine(MemberStatus.PENDING)
    sm.transition(MemberStatus.ACTIVE)

    assert sm.status == MemberStatus.ACTIVE


def test_invalid_transition_pending_to_exited():
    sm = MemberStateMachine(MemberStatus.PENDING)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.EXITED)