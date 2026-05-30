# application/members/exit_member.py

class ExitMember:

    def __init__(self, uow):
        self.uow = uow

    def execute(self, member_id):

        with self.uow:
            member = self.uow.member_repository.get(member_id)

            member.exit()

            self.uow.member_repository.save(member)
            self.uow.commit()

        return member