# tests/unit/domain/member/test_member_policies.py

import pytest
from domain.member.entities import Member
from domain.member.policies import ActivationPolicy
from domain.member.status import MemberStatus


def test_activation_policy_rejects_non_pending():
    member = Member(name="x", email="x@test.com")
    member.status = MemberStatus.ACTIVE

    with pytest.raises(Exception):
        ActivationPolicy.validate(member)