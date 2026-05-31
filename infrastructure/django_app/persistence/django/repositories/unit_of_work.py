# infrastructure/django_app/persistence/django/repositories/unit_of_work.py

from django.db import transaction

from infrastructure.django_app.persistence.django.repositories.member_repository import DjangoMemberRepository
from infrastructure.django_app.persistence.django.repositories.energy_repository import DjangoEnergyRepository
from infrastructure.django_app.outbox.repository import OutboxRepository


class DjangoUnitOfWork:

    def __init__(self, outbox_repo: OutboxRepository):
        self.outbox_repo = outbox_repo

        self.member_repository = DjangoMemberRepository()
        self.energy_repository = DjangoEnergyRepository()

        self._events = []
        self._transaction = None

    def __enter__(self):
        self._transaction = transaction.atomic()
        self._transaction.__enter__()
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            self.rollback()
            self._transaction.__exit__(exc_type, exc, tb)
            return False

        self.commit()
        self._transaction.__exit__(exc_type, exc, tb)
        return False

    def collect(self, events: list):
        self._events.extend(events)

    def commit(self):
        for event in self._events:
            self.outbox_repo.save(event)

        self._events.clear()

    def rollback(self):
        self._events.clear()