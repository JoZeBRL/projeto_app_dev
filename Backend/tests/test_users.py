def test_get_me(client, construtora_data):
    client.post("/api/v1/auth/register", json=construtora_data)
    login = client.post("/api/v1/auth/login", data={
        "username": construtora_data["email"],
        "password": construtora_data["password"]
    })
    token = login.json()["access_token"]

    response = client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == construtora_data["email"]
    assert data["user_type"] == "CONSTRUTORA"


def test_get_me_sem_token(client):
    response = client.get("/api/v1/users/me")
    assert response.status_code == 401


def test_update_me(client, construtora_data):
    client.post("/api/v1/auth/register", json=construtora_data)
    login = client.post("/api/v1/auth/login", data={
        "username": construtora_data["email"],
        "password": construtora_data["password"]
    })
    token = login.json()["access_token"]

    response = client.put("/api/v1/users/me",
        json={"full_name": "Nome Atualizado"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["full_name"] == "Nome Atualizado"


def test_update_me_sem_campos(client, construtora_data):
    client.post("/api/v1/auth/register", json=construtora_data)
    login = client.post("/api/v1/auth/login", data={
        "username": construtora_data["email"],
        "password": construtora_data["password"]
    })
    token = login.json()["access_token"]

    response = client.put("/api/v1/users/me",
        json={},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 400