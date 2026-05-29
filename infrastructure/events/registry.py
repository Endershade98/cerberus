# infrastructure/events/registry.py

class EventRegistry:
    """
    Maps event types to handlers (integration layer routing)
    """

    def __init__(self):
        self._registry = {}

    def register(self, event_type, handler):
        self._registry.setdefault(event_type, []).append(handler)

    def get_handlers(self, event_type):
        return self._registry.get(event_type, [])