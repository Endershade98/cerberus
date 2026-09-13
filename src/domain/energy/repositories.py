# src/domain/energy/repositories.py

from abc import ABC, abstractmethod

from domain.energy.asset import EnergyAsset
from domain.energy.batch import EnergyBatch
from domain.energy.device import EnergyDevice
from domain.energy.reading import EnergyReading
from domain.energy.value_objects import (
    EnergyAssetId,
    EnergyDeviceId,
    EnergyReadingId,
)
from domain.membership.value_objects import MemberId


class EnergyAssetRepository(ABC):

    @abstractmethod
    def save(self, asset: EnergyAsset) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, asset_id: EnergyAssetId) -> EnergyAsset | None:
        raise NotImplementedError

    @abstractmethod
    def find_by_owner(
        self,
        member_id: MemberId,
    ) -> list[EnergyAsset]:
        raise NotImplementedError


class EnergyDeviceRepository(ABC):

    @abstractmethod
    def save(self, device: EnergyDevice) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, device_id: EnergyDeviceId) -> EnergyDevice | None:
        raise NotImplementedError


class EnergyReadingRepository(ABC):

    @abstractmethod
    def save(self, reading: EnergyReading) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, reading_id: EnergyReadingId) -> EnergyReading | None:
        raise NotImplementedError

    @abstractmethod
    def find_by_device_and_interval(
        self,
        device_id: EnergyDeviceId,
        start,
        end,
    ) -> list[EnergyReading]:
        raise NotImplementedError


class EnergyBatchRepository(ABC):

    @abstractmethod
    def save(self, batch: EnergyBatch) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, batch_id) -> EnergyBatch | None:
        raise NotImplementedError