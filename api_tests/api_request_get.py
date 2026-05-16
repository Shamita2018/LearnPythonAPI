import requests
import json

base_url = "https://gorest.co.in"
auth_token = "Bearer cdebdd9c0b9a192e46660843d6353deb8f2470cc80894a02e33ae612f6d39bdb"


def test_get_users():
    """GET /users: fetches list of users and validates response structure."""
    url = base_url + "/public/v2/users"
    headers = {"Authorization": auth_token}

    response = requests.get(url, headers=headers)
    json_data = response.json()
    print("GET json response body:", json.dumps(json_data, indent=4))

    assert response.status_code == 200
    assert isinstance(json_data, list)
    assert len(json_data) > 0

    first_user = json_data[0]
    assert "id" in first_user
    assert "name" in first_user
    assert "email" in first_user
    assert "gender" in first_user
    assert "status" in first_user

    assert isinstance(first_user["id"], int)
    assert first_user["name"] is not None and first_user["name"].strip() != ""
    assert first_user["email"] is not None and "@" in first_user["email"]
    assert first_user["gender"] in ("male", "female")
    assert first_user["status"] in ("active", "inactive")
