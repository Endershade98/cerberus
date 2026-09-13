# tests/unit/domain/energy/test_energy_asset.py

import pytest

from domain.community.value_objects import CerId
from domain.energy.asset import EnergyAsset
from domain.energy.value_objects import (
    EnergyAssetId,
    EnergyAssetStatus,
    EnergyAssetType,
    PodCode,
)
from domain.membership.value_objects import MemberId
from domain.shared.exceptions import BusinessRuleViolation


def make_asset():
    return EnergyAsset.create(
        cer_id=CerId.generate(),
        owner_member_id=MemberId.generate(),
        pod_code=PodCode("IT001E12345"),
        asset_type=EnergyAssetType.PROSUMER,
    )


def test_create_energy_asset():
    asset = make_asset()

    assert isinstance(asset.id, EnergyAssetId)
    assert asset.status == EnergyAssetStatus.ACTIVE
    assert asset.asset_type == EnergyAssetType.PROSUMER


def test_change_owner_of_active_asset():
    asset = make_asset()
    new_owner = MemberId.generate()

    asset.change_owner(new_owner)

    assert asset.owner_member_id == new_owner


def test_inactive_asset_cannot_change_owner():
    asset = make_asset()
    asset.deactivate()

    with pytest.raises(
        BusinessRuleViolation,
        match="Only active energy assets",
    ):
        asset.change_owner(MemberId.generate())


def test_deactivate_asset():
    asset = make_asset()

    asset.deactivate()

    assert asset.status == EnergyAssetStatus.INACTIVE


def test_activate_asset():
    asset = make_asset()
    asset.deactivate()

    asset.activate()

    assert asset.status == EnergyAssetStatus.ACTIVE