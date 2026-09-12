# domain/energy/value_objects.py

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


@dataclass(frozen=True)
class EnergyQuantity:

    value: float


    def __post_init__(self):

        if self.value < 0:
            raise ValueError(
                "Energy cannot be negative"
            )


    def __add__(self, other):

        return EnergyQuantity(
            self.value + other.value
        )


    @staticmethod
    def zero():

        return EnergyQuantity(0)


class FlowDirection(str, Enum):

    PRODUCTION = "PRODUCTION"

    CONSUMPTION = "CONSUMPTION"



@dataclass(frozen=True)
class MeterReading:

    asset_id: str
    timestamp: datetime
    quantity: EnergyQuantity
    direction: FlowDirection



@dataclass(frozen=True)
class TimeWindow:

    start: datetime
    end: datetime


    def contains(self, value):

        return (
            self.start <= value <= self.end
        )