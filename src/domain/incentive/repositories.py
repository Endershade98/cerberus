# src/domain/incentive/repositories.py

from abc import ABC, abstractmethod

from domain.incentive.incentive import Incentive
from domain.incentive.value_objects import IncentiveId


class IncentiveRepository(ABC):

    @abstractmethod
    def save(self, incentive: Incentive) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, incentive_id: IncentiveId) -> Incentive | None:
        raise NotImplementedError

    @abstractmethod
    def find_for_member_period(
        self,
        member_id,
        reference_period,
    ) -> Incentive | None:
        raise NotImplementedError