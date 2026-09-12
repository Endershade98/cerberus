# infrastructure/django_app/persistence/django/repositories/unit_of_work.py

from django.db import transaction

from domain.shared.unit_of_work import UnitOfWork


class DjangoUnitOfWork(UnitOfWork):

    def __init__(self, outbox_repo):

        super().__init__()

        self.outbox_repo = outbox_repo

        self._transaction = None

        self.member_repository = None
        self.energy_repository = None

    # ---------------------------
    # Context manager
    # ---------------------------

    def __enter__(self):

        self._transaction = transaction.atomic()
        self._transaction.__enter__()

        self.member_repository = (
            self._build_member_repository()
        )

        self.energy_repository = (
            self._build_energy_repository()
        )

        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ):

        try:

            if exc_type:
                self.rollback()
                return False

            self.commit()
            return False

        finally:

            if self._transaction:

                self._transaction.__exit__(
                    exc_type,
                    exc,
                    tb,
                )

    # ---------------------------
    # Transaction lifecycle
    # ---------------------------

    def commit(self):

        for event in self.pop_events():

            self.outbox_repo.save(event)

    def rollback(self):

        self.pop_events()

    # ---------------------------
    # Repositories
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