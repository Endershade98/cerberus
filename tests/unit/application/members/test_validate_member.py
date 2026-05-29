# tests/unit/application/members/test_validate_member.py

from unittest.mock import Mock
import pytest
from application.members.validate_member import ValidateMember


def test_validate_member_success():

    repo = Mock()
    uow = Mock()

    member = Mock()
    member.validate = Mock()

    repo.get = Mock(return_value=member)

    use_case = ValidateMember(repo, uow)

    result = use_case.execute("123")

    member.validate.assert_called_once()
    repo.save.assert_called_once_with(member)
    uow.commit.assert_called_once()
    assert result == member


def test_validate_member_not_found():

    repo = Mock()
    uow = Mock()

    repo.get = Mock(return_value=None)

    use_case = ValidateMember(repo, uow)

    with pytest.raises(ValueError):
        use_case.execute("missing")