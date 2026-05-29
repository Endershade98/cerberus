# tests/integration/api/energy/test_energy_api.py

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_record_energy_api_success():
    client = APIClient()

    payload = {
        "member_id": "00000000-0000-0000-0000-000000000000",
        "kwh": 12.5
    }

    response = client.post("/api/energy/record/", payload, format="json")

    assert response.status_code == 200
    assert "member_id" in response.data
    assert float(response.data["value_kwh"]) == 12.5


@pytest.mark.django_db
def test_calculate_shared_energy_api():
    client = APIClient()

    response = client.get("/api/energy/calculate/")

    assert response.status_code == 200
    assert "total_kwh" in response.data