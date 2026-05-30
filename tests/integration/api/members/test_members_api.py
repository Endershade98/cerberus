# tests/integration/api/members/test_members_api.py

import pytest


@pytest.mark.django_db
def test_register_member_success(client, valid_member_payload):

    response = client.post("/api/members/", valid_member_payload, format="json")

    assert response.status_code == 201
    assert "id" in response.data
    assert response.data["status"]


@pytest.mark.django_db
def test_activate_member_success(client, valid_member_payload):

    res = client.post("/api/members/", valid_member_payload, format="json")
    member_id = res.data["id"]

    response = client.post(f"/api/members/{member_id}/activate/")

    assert response.status_code == 200
    assert response.data["status"]


@pytest.mark.django_db
def test_activate_member_not_found(client):

    fake_id = "00000000-0000-0000-0000-000000000000"

    response = client.post(f"/api/members/{fake_id}/activate/")

    assert response.status_code == 404


@pytest.mark.django_db
def test_validate_member(client, valid_member_payload):

    res = client.post("/api/members/", valid_member_payload, format="json")
    member_id = res.data["id"]

    response = client.post(f"/api/members/{member_id}/validate/")

    assert response.status_code == 200
    assert "status" in response.data