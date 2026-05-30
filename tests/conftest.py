# tests/conftest.py

import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def valid_member_payload():
    return {
        "name": "John Doe",
        "email": "john@example.com",
        "fiscal_code": "RSSMRA85T10A562S",  # 16 chars VALID
        "street": "Via Roma 1",
        "city": "Napoli",
        "postal_code": "80100",
        "country": "IT",
    }


@pytest.fixture
def invalid_energy_payload():
    return {
        "member_id": None,
        "kwh": "invalid"
    }


@pytest.fixture
def valid_energy_payload():
    return {
        "member_id": "00000000-0000-0000-0000-000000000001",
        "kwh": 10.5
    }