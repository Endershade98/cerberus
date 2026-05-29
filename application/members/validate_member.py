# application/members/validate_member.py

class ValidateMember:

    def __init__(self, repository, uow):
        self.repository = repository
        self.uow = uow

    def execute(self, member_id):

        member = self.repository.get(member_id)

        if not member:
            raise ValueError("Member not found")

        member.validate()

        self.repository.save(member)
        self.uow.commit()

        return member