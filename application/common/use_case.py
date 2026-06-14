# application/common/use_case.py

from typing import Optional, Generic, TypeVar

from domain.shared.unit_of_work import UnitOfWork

T = TypeVar("T")


class UseCase(Generic[T]):
    """
    Clean event-driven UseCase:

    Flow:
    - execute domain logic
    - collect events from result OR aggregates
    - UoW.commit() persists + outbox
    """

    def __init__(self, uow: Optional[UnitOfWork] = None):
        self.uow = uow

    def execute(self, *args, **kwargs):
        if not self.uow:
            raise ValueError("UnitOfWork is required")

        with self.uow:
            result = self._execute(*args, **kwargs)

            events = self._collect_events(result)

            # SINGLE SOURCE OF TRUTH
            if events:
                self.uow.collect(events)

        return result

    def _execute(self, *args, **kwargs) -> T:
        raise NotImplementedError

    def _collect_events(self, result: T):
        """
        Default: pull events from aggregate root result
        """
        if hasattr(result, "pull_events"):
            return result.pull_events()
        return []