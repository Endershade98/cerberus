# tests/integration/api/members/test_members_api_errors.py

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_member_missing_fields():
    client = APIClient()

    response = client.post("/api/members/", {}, format="json")

    assert response.status_code in [400, 422]


@pytest.mark.django_db
def test_activate_member_not_found():
    client = APIClient()

    fake_id = "00000000-0000-0000-0000-000000000000"

    response = client.post(f"/api/members/{fake_id}/activate/")

    assert response.status_code in [404, 400]