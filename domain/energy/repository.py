# domain/energy/repository.py

from abc import ABC, abstractmethod
from domain.energy.entities import EnergyRecord

class EnergyRepository(ABC):

    @abstractmethod
    def save(self, record: EnergyRecord) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[EnergyRecord]:
        pass