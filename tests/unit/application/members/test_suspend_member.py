# tests/unit/application/members/test_suspend_member.py

from unittest.mock import Mock
from src.application.members.suspend_member import SuspendMember


def test_suspend_member_executes_and_persists():

    uow = Mock()
    repo = Mock()

    uow.member_repository = repo
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    member = Mock()
    member.suspend = Mock()

    repo.get.return_value = member

    use_case = SuspendMember(uow)

    result = use_case.execute("123")

    member.suspend.assert_called_once()
    repo.save.assert_called_once_with(member)
    assert result == member