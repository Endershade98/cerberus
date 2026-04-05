# domain/member/value_objects.py
from enum import Enum

class MemberRole(str, Enum):
    """
    Enumeration representing the role of a Member in the system.

    Each role defines specific permissions and capabilities:
    - CONSUMER: Can only consume resources.
    - PRODUCER: Can only produce resources.
    - PROSUMER: Can both consume and produce resources.

    The role is assigned at registration and can be changed later
    if the member is active.
    """
    CONSUMER = "consumer"
    PRODUCER = "producer"
    PROSUMER = "prosumer"

    def can_produce(self) -> bool:
        return self in {MemberRole.PRODUCER, MemberRole.PROSUMER}
    
    def can_consume(self) -> bool:
        return self in {MemberRole.CONSUMER, MemberRole.PROSUMER}
