# src/domain/energy/device.py

from dataclasses import dataclass

from domain.energy.value_objects import (
    EnergyAssetId,
    EnergyDeviceId,
    EnergyDeviceStatus,
)
from domain.shared.exceptions import BusinessRuleViolation


@dataclass
class EnergyDevice:
    id: EnergyDeviceId
    asset_id: EnergyAssetId
    provider: str
    external_id: str
    status: EnergyDeviceStatus = EnergyDeviceStatus.ACTIVE

    def __post_init__(self) -> None:
        if not self.provider.strip():
            raise BusinessRuleViolation("Energy provider is required.")

        if not self.external_id.strip():
            raise BusinessRuleViolation(
                "External device identifier is required."
            )

    @classmethod
    def create(
        cls,
        *,
        asset_id: EnergyAssetId,
        provider: str,
        external_id: str,
        device_id: EnergyDeviceId | None = None,
    ) -> "EnergyDevice":
        return cls(
            id=device_id or EnergyDeviceId.generate(),
            asset_id=asset_id,
            provider=provider.strip(),
            external_id=external_id.strip(),
        )

    def deactivate(self) -> None:
        self.status = EnergyDeviceStatus.INACTIVE

    def activate(self) -> None:
        self.status = EnergyDeviceStatus.ACTIVE