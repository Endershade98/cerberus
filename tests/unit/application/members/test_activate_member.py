# tests/unit/application/members/test_activate_member.py

from unittest.mock import Mock
from application.members.activate_member import ActivateMember


def test_activate_member_publishes_events_outside_transaction():

    uow = Mock()
    repo = Mock()
    publisher = Mock()

    uow.member_repository = repo
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    member = Mock()
    member.activate = Mock()
    member.pull_events = Mock(return_value=["event1", "event2"])

    repo.get.return_value = member

    use_case = ActivateMember(uow, publisher)

    result = use_case.execute("123")

    member.activate.assert_called_once()
    repo.save.assert_called_once_with(member)

    publisher.publish.assert_called_once_with(["event1", "event2"])

    assert result == member