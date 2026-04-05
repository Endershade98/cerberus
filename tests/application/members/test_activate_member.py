# tests/application/members/test_activate_member.py
import pytest
from uuid import UUID

from application.members.activate_member import ActivateMember
from application.members.register_member import RegisterMember
from domain.member.entities import RegisterMemberInput
from domain.member.value_objects import MemberRole
from domain.member.status import MemberStatus

class FakeMemberRepository:
    def __init__(self):
        self.saved = []

    def save(self, member):
        self.saved.append(member)

    def list_all(self):
        return self.saved
    
def test_activate_member_changes_status_to_active():
    # Arrange
    repo = FakeMemberRepository()
    register_use_case = RegisterMember(repo)
    register_use_case.execute(RegisterMemberInput(role=MemberRole.CONSUMER))
    member = repo.saved[0]

    activate_use_case = ActivateMember(member)

    # Act
    activate_use_case.execute(RegisterMemberInput(role=MemberRole.CONSUMER))

    # Assert
    assert member.status == MemberStatus.ACTIVE