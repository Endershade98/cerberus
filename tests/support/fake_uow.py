# tests/support/fake_uow.py

from domain.shared.unit_of_work import UnitOfWork


class FakeMemberRepo:

    def __init__(self, store):
        self.store = store

    def save(self, member):
        self.store[member.id.value] = member

    def get(self, member_id):
        return self.store.get(member_id.value)

    def find_by_email(self, email):
        return next(
            (m for m in self.store.values() if m.email == email),
            None
        )

class FakeEnergyRepo:

    def __init__(self, store):
        self.store = store

    def save(self, record):
        self.store.append(record)

    def get_all(self):
        return list(self.store)
    

class FakeUnitOfWork(UnitOfWork):

    def __init__(self):
        self.members = {}
        self.energy = []
        self.events = []

        self.member_repository = FakeMemberRepo(self.members)
        self.energy_repository = FakeEnergyRepo(self.energy)

    def commit(self):
        pass

    def rollback(self):
        self.members.clear()
        self.energy.clear()
        self.events.clear()