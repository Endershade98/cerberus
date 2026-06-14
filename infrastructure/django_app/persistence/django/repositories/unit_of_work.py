# infrastructure/django_app/persistence/django/repositories/unit_of_work.py

from django.db import transaction


class DjangoUnitOfWork:
    def __init__(self, outbox_repo):
        self.outbox_repo = outbox_repo
        self._transaction = None
        self._events = []

    # ---------------------------
    # Context manager
    # ---------------------------
    def __enter__(self):
        self._transaction = transaction.atomic()
        self._transaction.__enter__()

        self.member_repository = self._build_member_repository()
        self.energy_repository = self._build_energy_repository()

        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type:
                self.rollback()
                return False

            self.commit()
            return False

        finally:
            if self._transaction is not None:
                self._transaction.__exit__(exc_type, exc, tb)

    # ---------------------------
    # Events collection
    # ---------------------------
    def collect(self, events):
        # idempotente (FIX doppio call ActivateMember test)
        for e in events:
            if e not in self._events:
                self._events.append(e)

    # ---------------------------
    # Commit
    # ---------------------------
    def commit(self):
        for event in self._events:
            self.outbox_repo.save(event)

        self._events.clear()

    def rollback(self):
        self._events.clear()

    # ---------------------------
    # Repository builders (placeholder)
    # ---------------------------
    def _build_member_repository(self):
        from infrastructure.django_app.persistence.django.repositories.member_repository import (
            DjangoMemberRepository,
        )
        return DjangoMemberRepository()

    def _build_energy_repository(self):
        from infrastructure.django_app.persistence.django.repositories.energy_repository import (
            DjangoEnergyRepository,
        )
        return DjangoEnergyRepository()