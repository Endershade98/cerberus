# tests/unit/application/members/test_suspend_member.py

from unittest.mock import Mock
from application.members.suspend_member import SuspendMember


def test_suspend_member_success():

    repo = Mock()
    uow = Mock()

    member = Mock()
    member.suspend = Mock()

    repo.get = Mock(return_value=member)

    use_case = SuspendMember(repo, uow)

    result = use_case.execute("123")

    member.suspend.assert_called_once()
    repo.save.assert_called_once_with(member)
    uow.commit.assert_called_once()
    assert result == member