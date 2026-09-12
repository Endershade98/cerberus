# tests/unit/domain/energy/test_energy_asset.py

import pytest

from src.domain.energy.asset import EnergyAsset
from src.domain.shared.value_objects_extra import PodCode



def test_create_energy_asset():

    asset = EnergyAsset(
        pod_code=PodCode("IT001E12345"),
        plant_name="Plant A",
        owner_member_id="member-1",
    )

    assert asset.plant_name == "Plant A"
    assert asset.owner_member_id == "member-1"


def test_transfer_ownership():

    asset = EnergyAsset(
        pod_code=PodCode("IT001E12345"),
        plant_name="Plant A",
        owner_member_id="member-1",
    )

    asset.change_owner("member-2")

    assert asset.owner_member_id == "member-2"


def test_transfer_ownership_requires_new_owner():

    asset = EnergyAsset.create(
        pod=PodCode("IT001E12345"),
        name="Plant A",
        owner_member_id="member-1",
    )

    with pytest.raises(ValueError):
        asset.transfer_ownership("")