# infrastructure/persistence/django/unit_of_work.py

from django.db import transaction


class DjangoUnitOfWork:

    def __init__(self, outbox_repo):
        self.outbox_repo = outbox_repo

    def commit(self, aggregate):

        with transaction.atomic():

            # persist domain events → outbox
            for event in aggregate.pull_events():
                self.outbox_repo.save(event)

    def rollback(self):
        transaction.rollback()