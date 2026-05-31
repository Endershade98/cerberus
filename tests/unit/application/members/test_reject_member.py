# tests/unit/application/members/test_reject_member.py

from unittest.mock import Mock
from application.members.reject_member import RejectMember


def test_reject_member_executes_and_persists():

    uow = Mock()
    repo = Mock()

    uow.member_repository = repo
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    member = Mock()
    member.reject = Mock()

    repo.get.return_value = member

    use_case = RejectMember(uow)

    result = use_case.execute("123")

    member.reject.assert_called_once()
    repo.save.assert_called_once_with(member)
    assert result == member