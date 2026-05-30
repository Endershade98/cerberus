# application/members/activate_member.py

from domain.member.exceptions import MemberDomainError


class ActivateMember:

    def __init__(self, uow, publisher=None):
        self.uow = uow
        self.publisher = publisher

    def execute(self, member_id):

        with self.uow:

            member = self.uow.member_repository.get(member_id)

            if not member:
                raise MemberDomainError("Member not found")

            member.activate()

            self.uow.member_repository.save(member)
            self.uow.commit()

            if self.publisher:
                self.publisher.publish(member.pull_events())

        return member