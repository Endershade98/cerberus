# tests/unit/domain/community/test_cer.py

import pytest

from domain.community.entities import Cer
from domain.community.events import (
    CerActivated,
    CerClosed,
    CerCreated,
    CerSuspended,
)
from domain.community.status import CerStatus
from domain.community.value_objects import CerId
from domain.shared.exceptions import BusinessRuleViolation, InvalidStateTransition


def test_create_creates_draft_cer():
    cer = Cer.create("  CER Basilicata  ")

    assert isinstance(cer.id, CerId)
    assert cer.name == "CER Basilicata"
    assert cer.status == CerStatus.DRAFT


def test_create_emits_cer_created_event():
    cer = Cer.create("CER Basilicata")

    events = cer.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], CerCreated)
    assert events[0].cer_id == cer.id


def test_create_rejects_blank_name():
    with pytest.raises(
        BusinessRuleViolation,
        match="CER name is required",
    ):
        Cer.create("   ")


def test_activate_changes_status():
    cer = Cer.create("CER Basilicata")

    cer.pull_events()
    cer.activate()

    assert cer.status == CerStatus.ACTIVE


def test_activate_emits_event():
    cer = Cer.create("CER Basilicata")
    cer.pull_events()

    cer.activate()

    events = cer.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], CerActivated)
    assert events[0].cer_id == cer.id


def test_suspend_changes_status():
    cer = Cer.create("CER Basilicata")
    cer.activate()

    cer.pull_events()
    cer.suspend()

    assert cer.status == CerStatus.SUSPENDED


def test_suspend_emits_event():
    cer = Cer.create("CER Basilicata")
    cer.activate()
    cer.pull_events()

    cer.suspend()

    events = cer.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], CerSuspended)
    assert events[0].cer_id == cer.id


def test_suspended_cer_can_be_activated_again():
    cer = Cer.create("CER Basilicata")
    cer.activate()
    cer.suspend()

    cer.activate()

    assert cer.status == CerStatus.ACTIVE


def test_close_active_cer():
    cer = Cer.create("CER Basilicata")
    cer.activate()

    cer.close()

    assert cer.status == CerStatus.CLOSED


def test_close_emits_event():
    cer = Cer.create("CER Basilicata")
    cer.activate()
    cer.pull_events()

    cer.close()

    events = cer.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], CerClosed)
    assert events[0].cer_id == cer.id


@pytest.mark.parametrize(
    "action",
    [
        "suspend",
        "close",
    ],
)
def test_draft_cer_cannot_skip_activation(action):
    cer = Cer.create("CER Basilicata")

    with pytest.raises(InvalidStateTransition):
        getattr(cer, action)()


def test_active_cer_cannot_be_activated_again():
    cer = Cer.create("CER Basilicata")
    cer.activate()

    with pytest.raises(InvalidStateTransition):
        cer.activate()


def test_closed_cer_cannot_be_reactivated():
    cer = Cer.create("CER Basilicata")
    cer.activate()
    cer.close()

    with pytest.raises(InvalidStateTransition):
        cer.activate()


def test_closed_cer_cannot_be_suspended():
    cer = Cer.create("CER Basilicata")
    cer.activate()
    cer.close()

    with pytest.raises(InvalidStateTransition):
        cer.suspend()


def test_closed_cer_cannot_be_closed_again():
    cer = Cer.create("CER Basilicata")
    cer.activate()
    cer.close()

    with pytest.raises(InvalidStateTransition):
        cer.close()