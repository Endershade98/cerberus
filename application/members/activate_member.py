# application/members/activate_member.py

from uuid import UUID

from domain.member.repository import MemberRepository
from domain.shared.unit_of_work import UnitOfWork
from domain.shared.event_publisher import EventPublisher


class ActivateMember:

    def __init__(
        self,
        repository: MemberRepository,
        uow: UnitOfWork,
        publisher: EventPublisher,
    ):
        self.repository = repository
        self.uow = uow
        self.publisher = publisher

    def execute(self, member_id: UUID):

        member = self.repository.get_by_id(member_id)

        member.activate()

        self.uow.commit()

        self.publisher.publish(
            member.pull_events()
        )