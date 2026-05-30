from unittest.mock import Mock
import pytest

from application.members.validate_member import ValidateMember
from domain.member.exceptions import MemberDomainError


def test_validate_member_success():

    uow = Mock()
    repo = Mock()
    uow.member_repository = repo

    # context manager mock
    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    member = Mock()
    member.validate = Mock()

    repo.get = Mock(return_value=member)

    use_case = ValidateMember(uow)

    result = use_case.execute("123")

    member.validate.assert_called_once()
    repo.save.assert_called_once_with(member)
    uow.commit.assert_called_once()
    assert result == member


def test_validate_member_not_found():

    uow = Mock()
    repo = Mock()
    uow.member_repository = repo

    uow.__enter__ = lambda self: uow
    uow.__exit__ = lambda *args: None

    repo.get = Mock(return_value=None)

    use_case = ValidateMember(uow)

    with pytest.raises(MemberDomainError) as exc:
        use_case.execute("missing")

    assert str(exc.value) == "Member not found"