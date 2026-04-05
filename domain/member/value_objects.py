# domain/member/value_objects.py
from enum import Enum

class MemberRole(str, Enum):
    CONSUMER = "consumer"
    PRODUCER = "producer"
    PROSUMER = "prosumer"

    def can_produce(self) -> bool:
        return self in {MemberRole.PRODUCER, MemberRole.PROSUMER}
    
    def can_consume(self) -> bool:
        return self in {MemberRole.CONSUMER, MemberRole.PROSUMER}
