# infrastructure/events/handlers/member_handlers.py

class MemberActivatedHandler:
    """
    Integration event handler
    """

    def handle(self, event):
        print(f"[EVENT] Member activated: {event.member_id}")