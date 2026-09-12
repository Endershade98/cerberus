# domain/shared/unit_of_work.py

from abc import ABC, abstractmethod
from contextlib import AbstractContextManager


class UnitOfWork(
    AbstractContextManager,
    ABC,
):

    member_repository = None
    energy_repository = None

    def __init__(self):

        self._events = []

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):

        if exc_type:
            self.rollback()
        else:
            self.commit()

    def collect(self, events):

        if not events:
            return

        self._events.extend(events)

    def pop_events(self):

        events = list(self._events)

        self._events.clear()

        return events

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError