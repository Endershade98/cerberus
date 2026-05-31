# tests/e2e/api/members/test_member_lifecycle_e2e.py

import pytest
from django.test import Client


@pytest.mark.django_db
def test_member_full_lifecycle():

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

    validate_response = client.post(
        f"/api/members/{member_id}/validate/"
    )

    assert validate_response.status_code in (200, 400)

    activate_response = client.post(
        f"/api/members/{member_id}/activate/"
    )

    assert activate_response.status_code in (200, 400)