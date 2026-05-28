# domain/shared/unit_of_work.py

from abc import ABC, abstractmethod


class UnitOfWork(ABC):
    """
    Defines transaction boundary abstraction.
    """

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass