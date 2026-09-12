# domain/energy/repository.py

from abc import ABC, abstractmethod


class EnergyRepository(ABC):


    @abstractmethod
    def save(self, record):
        pass


    @abstractmethod
    def get_all(self):
        pass


    @abstractmethod
    def get_window(
        self,
        start,
        end
    ):
        pass