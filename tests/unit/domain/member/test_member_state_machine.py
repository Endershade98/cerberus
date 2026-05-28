# tests/unit/domain/member/test_member_state_machine.py

import pytest

from domain.member.status import (
    MemberStateMachine,
    MemberStatus,
)

from domain.shared.exceptions import (
    InvalidStateTransition,
)


def test_should_allow_registered_to_pending_transition():

    sm = MemberStateMachine(
        MemberStatus.REGISTERED
    )

    sm.transition(MemberStatus.PENDING)

    assert sm.current_status == MemberStatus.PENDING


def test_should_allow_pending_to_validated_transition():

    sm = MemberStateMachine(
        MemberStatus.PENDING
    )

    sm.transition(MemberStatus.VALIDATED)

    assert sm.current_status == MemberStatus.VALIDATED


def test_should_allow_validated_to_active_transition():

    sm = MemberStateMachine(
        MemberStatus.VALIDATED
    )

    sm.transition(MemberStatus.ACTIVE)

    assert sm.current_status == MemberStatus.ACTIVE


def test_should_allow_active_to_suspended_transition():

    sm = MemberStateMachine(
        MemberStatus.ACTIVE
    )

    sm.transition(MemberStatus.SUSPENDED)

    assert sm.current_status == MemberStatus.SUSPENDED


def test_should_allow_suspended_to_active_transition():

    sm = MemberStateMachine(
        MemberStatus.SUSPENDED
    )

    sm.transition(MemberStatus.ACTIVE)

    assert sm.current_status == MemberStatus.ACTIVE


def test_should_block_invalid_transition():

    sm = MemberStateMachine(
        MemberStatus.PENDING
    )

    with pytest.raises(InvalidStateTransition):
        sm.transition(MemberStatus.EXITED)


def test_should_block_registered_to_active_transition():

    sm = MemberStateMachine(
        MemberStatus.REGISTERED
    )

    with pytest.raises(InvalidStateTransition):
        sm.transition(MemberStatus.ACTIVE)