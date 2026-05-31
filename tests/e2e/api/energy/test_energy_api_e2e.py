# tests/e2e/api/energy/test_energy_api_e2e.py

import pytest
from django.test import Client


@pytest.mark.django_db
def test_energy_record_and_calculation_flow():

    client = Client()

    response = client.post(
        "/api/energy/record/",
        {
            "member_id": "11111111-1111-1111-1111-111111111111",
            "kwh": 10.5,
        },
        content_type="application/json",
    )

    assert response.status_code == 201

    data = response.json()

    assert data["member_id"] == "11111111-1111-1111-1111-111111111111"
    assert data["kwh"] == 10.5

    response = client.get("/api/energy/calculate/")

    assert response.status_code == 200

    data = response.json()

    assert "total_kwh" in data