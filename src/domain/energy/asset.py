# src/domain/energy/asset.py

from dataclasses import dataclass

from domain.community.value_objects import CerId
from domain.energy.value_objects import (
    EnergyAssetId,
    EnergyAssetStatus,
    EnergyAssetType,
    PodCode,
)
from domain.membership.value_objects import MemberId
from domain.shared.aggregate_root import AggregateRoot
from domain.shared.exceptions import BusinessRuleViolation


@dataclass
class EnergyAsset(AggregateRoot):
    id: EnergyAssetId
    cer_id: CerId
    owner_member_id: MemberId
    pod_code: PodCode
    asset_type: EnergyAssetType
    status: EnergyAssetStatus = EnergyAssetStatus.ACTIVE

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

    @classmethod
    def create(
        cls,
        *,
        cer_id: CerId,
        owner_member_id: MemberId,
        pod_code: PodCode,
        asset_type: EnergyAssetType,
        asset_id: EnergyAssetId | None = None,
    ) -> "EnergyAsset":
        return cls(
            id=asset_id or EnergyAssetId.generate(),
            cer_id=cer_id,
            owner_member_id=owner_member_id,
            pod_code=pod_code,
            asset_type=asset_type,
        )

    def change_owner(self, member_id: MemberId) -> None:
        if self.status != EnergyAssetStatus.ACTIVE:
            raise BusinessRuleViolation(
                "Only active energy assets can change owner."
            )

        self.owner_member_id = member_id

    def deactivate(self) -> None:
        self.status = EnergyAssetStatus.INACTIVE

    def activate(self) -> None:
        self.status = EnergyAssetStatus.ACTIVE