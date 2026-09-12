# tests/unit/application/members/test_validate_member.py

from unittest.mock import Mock
import pytest
from src.domain.member.exceptions import MemberDomainError
from src.application.members.validate_member import ValidateMember


def test_validate_member_success():

    uow = Mock()
    repo = Mock()

    uow.member_repository = repo
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    member = Mock()
    member.validate = Mock()

    repo.get.return_value = member

    use_case = ValidateMember(uow)

    result = use_case.execute("123")

    member.validate.assert_called_once()
    repo.save.assert_called_once_with(member)
    assert result == member


def test_validate_member_not_found():

    uow = Mock()
    repo = Mock()

    uow.member_repository = repo
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    repo.get.return_value = None

    use_case = ValidateMember(uow)

    with pytest.raises(MemberDomainError):
        use_case.execute("missing")