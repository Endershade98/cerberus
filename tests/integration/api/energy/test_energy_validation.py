# tests/integration/api/energy/test_energy_validation.py

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_record_energy_missing_fields():
    client = APIClient()

    response = client.post("/api/energy/record/", {}, format="json")

    assert response.status_code == 400


@pytest.mark.django_db
def test_record_energy_invalid_kwh():
    client = APIClient()

    payload = {
        "member_id": "00000000-0000-0000-0000-000000000000",
        "kwh": "invalid"
    }

    response = client.post("/api/energy/record/", payload, format="json")

    assert response.status_code == 400