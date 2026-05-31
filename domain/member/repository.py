# domain/member/repository.py

from abc import ABC, abstractmethod
from domain.member.entities import Member
from domain.member.value_objects import MemberId


class MemberRepository(ABC):

    @abstractmethod
    def save(self, member: Member) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, member_id: MemberId) -> Member | None:
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> Member | None:
        raise NotImplementedError