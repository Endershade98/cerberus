# tests/conftest.py

import pytest

from infrastructure.django_app.events.bus import EventBus
from infrastructure.django_app.outbox.repository import OutboxRepository
from infrastructure.django_app.persistence.django.repositories.unit_of_work import DjangoUnitOfWork

from datetime import datetime, UTC

from domain.shared.event_publisher import EventPublisher
from domain.shared.time_provider import FrozenTimeProvider
from domain.shared.id_provider import FixedIdProvider




@pytest.fixture(autouse=True)
def freeze_time(monkeypatch):

    fixed = datetime(2025, 1, 1, tzinfo=UTC)

    monkeypatch.setattr(
        "domain.shared.time_provider.TimeProvider",
        lambda: FrozenTimeProvider(fixed)
    )

    monkeypatch.setattr(
        "domain.shared.id_provider.IdProvider",
        lambda: FixedIdProvider()
    )

@pytest.fixture
def event_bus():
    return EventBus()


@pytest.fixture
def outbox_repo():
    return OutboxRepository()


@pytest.fixture
def uow(outbox_repo):
    return DjangoUnitOfWork(outbox_repo)


@pytest.fixture
def publisher(uow, event_bus):
    return EventPublisher(uow, dispatcher=event_bus)