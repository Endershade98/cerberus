# infrastructure/persistence/unit_of_work.py

from django.db import transaction

from domain.shared.unit_of_work import UnitOfWork


class DjangoUnitOfWork(UnitOfWork):

    def commit(self):
        transaction.commit()

    def rollback(self):
        transaction.rollback()