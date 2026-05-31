# interfaces/api/shared/uow_factory.py

from infrastructure.django_app.persistence.django.repositories.unit_of_work import DjangoUnitOfWork
from infrastructure.django_app.outbox.repository import OutboxRepository


def build_uow():
    return DjangoUnitOfWork(outbox_repo=OutboxRepository())