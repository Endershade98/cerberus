# tests/application/members/test_activate_member.py
import pytest
from uuid import UUID

from application.members.activate_member import ActivateMemberUseCase
from application.members.register_member import RegisterMemberUseCase
from domain.member.entities import RegisterMemberUseCaseInput
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
    register_use_case = RegisterMemberUseCase(repo)
    register_use_case.execute(RegisterMemberUseCaseInput(role=MemberRole.CONSUMER))
    member = repo.saved[0]

    activate_use_case = ActivateMemberUseCase(member)

    # Act
    activate_use_case.execute(RegisterMemberUseCaseInput(role=MemberRole.CONSUMER))

    # Assert
    assert member.status == MemberStatus.ACTIVE