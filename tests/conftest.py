import pytest
from domain.member.entities import Member


@pytest.fixture
def member():
    return Member()