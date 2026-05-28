# domain/shared/unit_of_work.py

from abc import ABC, abstractmethod


class UnitOfWork(ABC):

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError