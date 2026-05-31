# tests/unit/application/members/test_exit_member.py

from unittest.mock import Mock
from application.members.exit_member import ExitMember


def test_exit_member_executes_and_persists():

    uow = Mock()
    repo = Mock()

    uow.member_repository = repo
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    member = Mock()
    member.exit = Mock()

    repo.get.return_value = member

    use_case = ExitMember(uow)

    result = use_case.execute("123")

    member.exit.assert_called_once()
    repo.save.assert_called_once_with(member)
    assert result == member