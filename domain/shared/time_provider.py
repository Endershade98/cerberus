# domain/shared/time_provider.py

from datetime import datetime, UTC


class TimeProvider:

    def now(self) -> datetime:
        return datetime.now(UTC)


class FrozenTimeProvider(TimeProvider):

    def __init__(self, fixed_time):
        self.fixed_time = fixed_time

    def now(self) -> datetime:
        return self.fixed_time