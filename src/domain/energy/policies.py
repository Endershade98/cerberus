# domain/energy/policies.py

from datetime import datetime
class EnergyValidationPolicy:


    def validate(self, record):

        if record.production < 0:
            raise ValueError()

        if record.consumption < 0:
            raise ValueError()


        return True



class DuplicateEnergyPolicy:


    def validate(
        self,
        existing,
        new
    ):

        if existing.timestamp == new.timestamp:
            raise ValueError(
                "Duplicate energy record"
            )

class DuplicateReadingPolicy:

    @staticmethod
    def is_duplicate(
        existing_records,
        asset_id,
        timestamp,
        direction,
    ):

        return any(
            r.asset_id == asset_id
            and r.timestamp == timestamp
            and r.direction == direction
            for r in existing_records
        )


class FutureReadingPolicy:

    @staticmethod
    def is_valid(
        timestamp: datetime,
        now: datetime,
    ) -> bool:

        return timestamp <= now


class TemporalAlignmentPolicy:

    VALID_MINUTES = {
        0,
        15,
        30,
        45,
    }

    @classmethod
    def is_valid(
        cls,
        timestamp: datetime,
    ):

        return (
            timestamp.minute
            in cls.VALID_MINUTES
        )