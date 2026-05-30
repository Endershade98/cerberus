# tests/integration/api/energy/test_energy_validation.py

def test_missing_member_id(client):
    response = client.post("/api/energy/record/", {
        "kwh": 10
    }, format="json")

    assert response.status_code == 400