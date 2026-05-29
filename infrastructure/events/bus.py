# infrastructure/events/bus.py

from collections import defaultdict
from typing import Callable, Type


class EventBus:
    """
    In-memory event bus (domain + integration events)
    """

    def __init__(self):
        self._handlers: dict[Type, list[Callable]] = defaultdict(list)

    def register(self, event_type: Type, handler: Callable):
        self._handlers[event_type].append(handler)

    def publish(self, event):
        for handler in self._handlers[type(event)]:
            handler(event)