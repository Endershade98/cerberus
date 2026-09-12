# domain/energy/asset.py

from src.domain.shared.aggregate_root import AggregateRoot


class EnergyAsset(AggregateRoot):


    def __init__(
        self,
        asset_id,
        pod_code
    ):

        self.id = asset_id
        self.pod_code = pod_code


    def change_pod(
        self,
        pod_code
    ):

        self.pod_code = pod_code