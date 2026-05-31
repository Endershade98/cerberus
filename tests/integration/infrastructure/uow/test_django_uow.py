# tests/integration/infrastructure/uow/test_django_uow.py

import pytest

from infrastructure.django_app.persistence.django.repositories.unit_of_work import DjangoUnitOfWork



class FakeOutboxRepo:
    def __init__(self):
        self.saved = []

    def save(self, event):
        self.saved.append(event)


@pytest.mark.django_db
def test_uow_collect_and_commit():

    outbox = FakeOutboxRepo()
    uow = DjangoUnitOfWork(outbox)

    class FakeEvent:
        id = "1"
        occurred_on = None

    with uow:
        uow.collect([FakeEvent(), FakeEvent()])

    assert len(outbox.saved) == 2