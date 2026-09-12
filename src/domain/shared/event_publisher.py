# domain/shared/event_publisher.py

from abc import ABC, abstractmethod

from src.domain.shared.domain_event import DomainEvent



class EventPublisher(ABC):

    @abstractmethod
    def publish(self, events: list[DomainEvent]) -> None:
        pass