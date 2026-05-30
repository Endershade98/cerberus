# tests/integration/api/energy/test_energy_api.py

import pytest


@pytest.mark.django_db
def test_record_energy_api_success(client, valid_energy_payload):
    response = client.post(
        "/api/energy/record/",
        valid_energy_payload,
        format="json"
    )

    assert response.status_code == 201
    assert "member_id" in response.data


@pytest.mark.django_db
def test_record_energy_invalid_input(client, invalid_energy_payload):
    response = client.post(
        "/api/energy/record/",
        invalid_energy_payload,
        format="json"
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_calculate_shared_energy(client, valid_energy_payload):
    client.post("/api/energy/record/", valid_energy_payload, format="json")

    response = client.get("/api/energy/calculate/")

    assert response.status_code == 200
    assert "total_kwh" in response.data