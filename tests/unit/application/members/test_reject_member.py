# tests/unit/application/members/test_reject_member.py

from unittest.mock import Mock
from application.members.reject_member import RejectMember


def test_reject_member_success():

    repo = Mock()
    uow = Mock()

    member = Mock()
    member.reject = Mock()

    repo.get = Mock(return_value=member)

    use_case = RejectMember(repo, uow)

    result = use_case.execute("123")

    member.reject.assert_called_once()
    repo.save.assert_called_once_with(member)
    uow.commit.assert_called_once()
    assert result == member