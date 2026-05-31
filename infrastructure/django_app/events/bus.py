# infrastructure/django_app/events/bus.py

from collections import defaultdict
from typing import Callable, Type, Any


class EventBus:

    def __init__(self):
        self._handlers: dict[Type, list[Callable]] = defaultdict(list)

    def register(self, event_type: Type, handler: Callable[[Any], None]):
        self._handlers[event_type].append(handler)

    def publish(self, event: Any):
        for handler in self._handlers.get(type(event), []):
            handler(event)