# tests/unit/domain/energy/test_energy_device.py

import pytest

from domain.energy.device import EnergyDevice
from domain.energy.value_objects import (
    EnergyAssetId,
    EnergyDeviceId,
    EnergyDeviceStatus,
)
from domain.shared.exceptions import BusinessRuleViolation


def test_create_energy_device():
    asset_id = EnergyAssetId.generate()

    device = EnergyDevice.create(
        asset_id=asset_id,
        provider=" Provider ",
        external_id=" device-123 ",
    )

    assert isinstance(device.id, EnergyDeviceId)
    assert device.asset_id == asset_id
    assert device.provider == "Provider"
    assert device.external_id == "device-123"
    assert device.status == EnergyDeviceStatus.ACTIVE


def test_provider_is_required():
    with pytest.raises(
        BusinessRuleViolation,
        match="provider is required",
    ):
        EnergyDevice.create(
            asset_id=EnergyAssetId.generate(),
            provider="   ",
            external_id="device-123",
        )


def test_external_id_is_required():
    with pytest.raises(
        BusinessRuleViolation,
        match="External device identifier",
    ):
        EnergyDevice.create(
            asset_id=EnergyAssetId.generate(),
            provider="Provider",
            external_id="   ",
        )


def test_deactivate_device():
    device = EnergyDevice.create(
        asset_id=EnergyAssetId.generate(),
        provider="Provider",
        external_id="device-123",
    )

    device.deactivate()

    assert device.status == EnergyDeviceStatus.INACTIVE


def test_activate_device():
    device = EnergyDevice.create(
        asset_id=EnergyAssetId.generate(),
        provider="Provider",
        external_id="device-123",
    )
    device.deactivate()

    device.activate()

    assert device.status == EnergyDeviceStatus.ACTIVE