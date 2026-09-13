# src/domain/community/repositories.py

from abc import ABC, abstractmethod

from domain.community.entities import Cer
from domain.community.value_objects import CerId


class CerRepository(ABC):

    @abstractmethod
    def save(self, cer: Cer) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, cer_id: CerId) -> Cer | None:
        raise NotImplementedError