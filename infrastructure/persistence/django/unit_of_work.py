# infrastructure/persistence/django/unit_of_work.py

from django.db import transaction

from infrastructure.persistence.django.repositories.member_repository import DjangoMemberRepository
from infrastructure.persistence.django.repositories.energy_repository import DjangoEnergyRepository


class DjangoUnitOfWork:
    """
    DDD Unit of Work:
    - single transaction boundary
    - explicit repositories
    - outbox support
    """

    def __init__(self, outbox_repo):
        self.outbox_repo = outbox_repo

        # repositories ALWAYS present
        self.member_repository = DjangoMemberRepository()
        self.energy_repository = DjangoEnergyRepository()

        self._events = []

        self._atomic = None

    # -------------------------
    # CONTEXT MANAGER (CLEAN)
    # -------------------------
    def __enter__(self):
        self._atomic = transaction.atomic()
        self._atomic.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                self.rollback()
                return False

            self.commit()
            return False

        finally:
            if self._atomic:
                self._atomic.__exit__(exc_type, exc_val, exc_tb)

    # -------------------------
    # REPOSITORY SAFE ACCESS
    # -------------------------
    def get_member_repo(self):
        return self.member_repository

    def get_energy_repo(self):
        return self.energy_repository

    # -------------------------
    # OUTBOX
    # -------------------------
    def collect(self, events):
        if events:
            self._events.extend(events)

    def commit(self):
        """
        Called ONLY by context manager exit
        """
        for event in self._events:
            self.outbox_repo.save(event)

        self._events.clear()

    def rollback(self):
        self._events.clear()