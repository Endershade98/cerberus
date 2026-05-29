# application/members/activate_member.py

from domain.shared.event_publisher import EventPublisher


class ActivateMember:

    def __init__(self, repository, uow, publisher: EventPublisher):
        self.repository = repository
        self.uow = uow
        self.publisher = publisher

    def execute(self, member_id):

        member = self.repository.get(member_id)

        member.activate()

        self.repository.save(member)
        self.uow.commit()

        self.publisher.publish(member.pull_events())

        return member