# application/members/reject_member.py

class RejectMember:

    def __init__(self, repository, uow):
        self.repository = repository
        self.uow = uow

    def execute(self, member_id):

        member = self.repository.get(member_id)

        member.reject()

        self.repository.save(member)
        self.uow.commit()

        return member