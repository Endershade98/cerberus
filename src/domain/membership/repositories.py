# src/domain/membership/repositories.py

from abc import ABC, abstractmethod

from domain.membership.entities import Member
from domain.membership.value_objects import EmailAddress, MemberId


class MemberRepository(ABC):

    @abstractmethod
    def save(self, member: Member) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, member_id: MemberId) -> Member | None:
        raise NotImplementedError

    @abstractmethod
    def find_by_email(
        self,
        email: EmailAddress,
    ) -> Member | None:
        raise NotImplementedError