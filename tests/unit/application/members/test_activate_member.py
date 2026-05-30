# tests/unit/application/members/test_activate_member.py

from unittest.mock import Mock
from application.members.activate_member import ActivateMember


def test_activate_member_success():

    uow = Mock()
    repo = Mock()
    uow.member_repository = repo

    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    publisher = Mock()

    member = Mock()
    member.activate = Mock()
    member.pull_events = Mock(return_value=[])

    repo.get = Mock(return_value=member)

    use_case = ActivateMember(uow, publisher)

    use_case.execute("123")

    member.activate.assert_called_once()
    uow.commit.assert_called_once()
    publisher.publish.assert_called_once()