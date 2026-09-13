# src/domain/shared_energy/repositories.py

from abc import ABC, abstractmethod

from domain.shared_energy.shared_energy import SharedEnergy
from domain.shared_energy.value_objects import SharedEnergyId


class SharedEnergyRepository(ABC):

    @abstractmethod
    def save(self, shared_energy: SharedEnergy) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, shared_energy_id: SharedEnergyId) -> SharedEnergy | None:
        raise NotImplementedError

    @abstractmethod
    def find_for_member_period(
        self,
        member_id,
        calculation_period,
    ) -> SharedEnergy | None:
        raise NotImplementedError