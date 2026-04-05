# tests/application/members/test_register_member.py
import pytest
from uuid import UUID

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


def test_register_member_creates_member_with_pending_status():
    # Arrange
    repo = FakeMemberRepository()
    use_case = RegisterMemberUseCase(repo)

    # Act
    member_id = use_case.execute(RegisterMemberUseCaseInput(role=MemberRole.CONSUMER))

    # Assert
    assert isinstance(member_id, UUID)
    assert len(repo.saved) == 1

    saved_member = repo.saved[0]
    assert saved_member.status == MemberStatus.PENDING
    assert saved_member.role == MemberRole.CONSUMER

def test_register_member_with_invalid_role_raises_error():
    repo = FakeMemberRepository()
    use_case = RegisterMemberUseCase(repo)

    with pytest.raises(ValueError):
        use_case.execute(RegisterMemberUseCaseInput(role="invalid_role"))