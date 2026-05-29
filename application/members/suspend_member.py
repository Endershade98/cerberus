# application/members/suspend_member.py

class SuspendMember:

    def __init__(self, repository, uow):
        self.repository = repository
        self.uow = uow

    def execute(self, member_id):

        member = self.repository.get(member_id)

        member.suspend()

        self.repository.save(member)
        self.uow.commit()

        return member