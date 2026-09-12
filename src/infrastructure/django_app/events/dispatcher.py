# infrastructure/django_app/events/dispatcher.py

class EventDispatcher:

    def __init__(self, bus):
        self.bus = bus

    def dispatch(self, event):
        self.bus.publish(event)