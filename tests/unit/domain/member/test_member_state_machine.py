# tests/unit/domain/member/test_member_state_machine.py

import pytest

from domain.member.status import (
    MemberStateMachine,
    MemberStatus
)

from domain.shared.exceptions import InvalidStateTransition


def test_should_allow_valid_transition():

    sm = MemberStateMachine(MemberStatus.PENDING)

    sm.transition(MemberStatus.ACTIVE)

    assert sm.status == MemberStatus.ACTIVE


def test_should_block_invalid_transition():

    sm = MemberStateMachine(MemberStatus.PENDING)

    with pytest.raises(InvalidStateTransition):
        sm.transition(MemberStatus.EXITED)