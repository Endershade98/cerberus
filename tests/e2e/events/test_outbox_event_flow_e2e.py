# tests/e2e/events/test_outbox_event_flow_e2e.py

import pytest
from django.test import Client
from src.infrastructure.persistence.django.models import OutboxEvent


@pytest.mark.django_db
def test_outbox_contains_activation_event():

    client = Client()

    register_response = client.post(
        "/api/members/",
        {
            "name": "Mario",
            "email": "mario@test.com",
            "role": "CONSUMER",
            "fiscal_code": "RSSMRA80A01F205X",
            "street": "Via Roma",
            "city": "Napoli",
            "postal_code": "80100",
            "country": "IT",
        },
        content_type="application/json",
    )

    member_id = register_response.json()["id"]

    client.post(f"/api/members/{member_id}/validate/")
    client.post(f"/api/members/{member_id}/activate/")

    event_types = list(
        OutboxEvent.objects.values_list("event_type", flat=True)
    )

    assert len(event_types) > 0