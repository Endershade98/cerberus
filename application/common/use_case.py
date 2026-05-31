# application/common/use_case.py

from typing import Optional, Generic, TypeVar

from domain.shared.unit_of_work import UnitOfWork
from domain.shared.event_publisher import EventPublisher


T = TypeVar("T")


class UseCase(Generic[T]):
    """
    Standard UseCase base:

    - UoW optional at construction time (for testability and simple API usage)
    - enforced at execution time
    - Publisher optional
    - transaction + event pipeline handled centrally
    """

    def __init__(
        self,
        uow: Optional[UnitOfWork] = None,
        publisher: Optional[EventPublisher] = None,
    ):
        self.uow = uow
        self.publisher = publisher

    def execute(self, *args, **kwargs) -> T:
        """
        Template Method:
        - ensures UoW exists
        - transaction scope
        - domain execution
        - event extraction
        - safe publishing outside tx
        """

        if self.uow is None:
            raise RuntimeError(
                f"{self.__class__.__name__} requires a UnitOfWork but none was provided"
            )

        with self.uow:
            result = self._execute(*args, **kwargs)
            events = self._collect_events(result)

        self._publish(events)
        return result

    # -------------------------
    # TO OVERRIDE
    # -------------------------
    def _execute(self, *args, **kwargs) -> T:
        raise NotImplementedError

    # -------------------------
    # EVENT HANDLING
    # -------------------------
    def _collect_events(self, result: T):
        """
        Default strategy:
        - if entity has pull_events()
        """
        if hasattr(result, "pull_events"):
            return result.pull_events()
        return []

    def _publish(self, events):
        if self.publisher and events:
            self.publisher.publish(events)