# tests/e2e/test_member_registration.py

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_member_registration_e2e():

    client = APIClient()

    payload = {
        "name": "Mario Rossi",
        "email": "mario@test.com",
        "role": "CONSUMER",
        "fiscal_code": "RSSMRA80A01H501U",
        "street": "Via Roma",
        "city": "Napoli",
        "postal_code": "80100",
        "country": "IT",
    }

    response = client.post(
        "/api/members/",
        payload,
        format="json",
    )

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert "status" in data