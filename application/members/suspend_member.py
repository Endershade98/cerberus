# application/members/suspend_member.py

class SuspendMember:

    def __init__(self, uow):
        self.uow = uow

    def execute(self, member_id):

        with self.uow:
            member = self.uow.member_repository.get(member_id)

            member.suspend()

            self.uow.member_repository.save(member)
            self.uow.commit()

        return member