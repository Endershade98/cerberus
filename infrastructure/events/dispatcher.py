# infrastructure/events/dispatcher.py

class EventDispatcher:
    """
    Thin abstraction over EventBus
    """

    def __init__(self, bus):
        self.bus = bus

    def dispatch(self, event):
        self.bus.publish(event)

    # backward compatibility FIX
    def publish(self, event):
        self.bus.publish(event)