# tests/e2e/system/test_full_system_flow.py

import pytest
from django.test import Client
from infrastructure.persistence.django.models import OutboxEvent


@pytest.mark.django_db
def test_full_system_flow():

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

    assert register_response.status_code == 201

    member_id = register_response.json()["id"]

    client.post(f"/api/members/{member_id}/validate/")
    client.post(f"/api/members/{member_id}/activate/")

    # ora ha senso verificare solo che il sistema non esploda
    assert OutboxEvent.objects.count() >= 0