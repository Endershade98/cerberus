# domain/shared/event_publisher.py

from abc import ABC, abstractmethod
from domain.shared.events import DomainEvent


class EventPublisher(ABC):

    @abstractmethod
    def publish(self, events: list[DomainEvent]) -> None:
        pass