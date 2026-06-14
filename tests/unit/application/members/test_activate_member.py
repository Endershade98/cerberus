# tests/unit/application/members/test_activate_member.py

from unittest.mock import Mock
from application.members.activate_member import ActivateMember


def test_activate_member_collects_events_into_uow():

    uow = Mock()
    repo = Mock()

    uow.member_repository = repo

    # FIX: collect deve essere mockato
    uow.collect = Mock()

    # fake context manager
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    member = Mock()
    member.activate = Mock()
    member.pull_events = Mock(return_value=["event1", "event2"])

    repo.get.return_value = member

    use_case = ActivateMember(uow)

    result = use_case.execute("123")

    member.activate.assert_called_once()
    repo.save.assert_called_once_with(member)

    # FIX: ora eventi finiscono nell'UoW
    uow.collect.assert_called_once_with(["event1", "event2"])
    print(uow.collect.call_args_list)

    assert result == member