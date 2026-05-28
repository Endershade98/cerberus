# domain/member/repository.py

from abc import ABC, abstractmethod
from domain.member.entities import Member

class MemberRepository(ABC):

    @abstractmethod
    def add(self, member: Member) -> None:
        pass

    @abstractmethod
    def get_by_id(self, member_id: str) -> Member | None:
        pass