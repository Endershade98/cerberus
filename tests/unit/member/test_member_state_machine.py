# tests/unit/member/test_member_state_machine.py
import pytest
from domain.member.status import MemberStatus, MemberStateMachine

# VALID TRANSITIONS TESTS

def test_valid_transition_pending_to_active():
    sm = MemberStateMachine(MemberStatus.PENDING)
    sm.transition(MemberStatus.ACTIVE)

    assert sm.status == MemberStatus.ACTIVE
    
def test_valid_transition_active_to_suspended():
    sm = MemberStateMachine(MemberStatus.ACTIVE)
    sm.transition(MemberStatus.SUSPENDED)

    assert sm.status == MemberStatus.SUSPENDED

def test_valid_transition_suspended_to_active():
    sm = MemberStateMachine(MemberStatus.SUSPENDED)
    sm.transition(MemberStatus.ACTIVE)

    assert sm.status == MemberStatus.ACTIVE

# INVALID TRANSITIONS TESTS

def test_invalid_transition_pending_to_exited():
    sm = MemberStateMachine(MemberStatus.PENDING)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.EXITED)

def test_invalid_transition_active_to_pending():
    sm = MemberStateMachine(MemberStatus.ACTIVE)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.PENDING)

def test_invalid_transition_suspended_to_pending():
    sm = MemberStateMachine(MemberStatus.SUSPENDED)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.PENDING)
    
def test_invalid_transition_rejected_to_active():
    sm = MemberStateMachine(MemberStatus.REJECTED)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.ACTIVE)

def test_invalid_transition_exited_to_active():
    sm = MemberStateMachine(MemberStatus.EXITED)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.ACTIVE)

def test_invalid_transition_exited_to_suspended():
    sm = MemberStateMachine(MemberStatus.EXITED)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.SUSPENDED)

def test_invalid_transition_exited_to_pending():
    sm = MemberStateMachine(MemberStatus.EXITED)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.PENDING)

def test_invalid_transition_exited_to_rejected():
    sm = MemberStateMachine(MemberStatus.EXITED)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.REJECTED)

def test_invalid_transition_rejected_to_pending():
    sm = MemberStateMachine(MemberStatus.REJECTED)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.PENDING)

def test_invalid_transition_rejected_to_suspended():
    sm = MemberStateMachine(MemberStatus.REJECTED)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.SUSPENDED)

def test_invalid_transition_rejected_to_exited():
    sm = MemberStateMachine(MemberStatus.REJECTED)

    with pytest.raises(ValueError):
        sm.transition(MemberStatus.EXITED)
