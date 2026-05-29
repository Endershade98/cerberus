# tests/unit/application/members/test_exit_member.py

from unittest.mock import Mock
from application.members.exit_member import ExitMember


def test_exit_member_success():

    repo = Mock()
    uow = Mock()

    member = Mock()
    member.exit = Mock()

    repo.get = Mock(return_value=member)

    use_case = ExitMember(repo, uow)

    result = use_case.execute("123")

    member.exit.assert_called_once()
    repo.save.assert_called_once_with(member)
    uow.commit.assert_called_once()
    assert result == member