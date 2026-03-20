def test_health(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"


def test_register_construtora(client, construtora_data):
    response = client.post("/api/v1/auth/register", json=construtora_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == construtora_data["email"]
    assert data["user_type"] == "CONSTRUTORA"
    assert "id" in data


def test_register_email_duplicado(client, construtora_data):
    client.post("/api/v1/auth/register", json=construtora_data)
    response = client.post("/api/v1/auth/register", json=construtora_data)
    assert response.status_code == 400
    assert "Email já registrado" in response.json()["detail"]


def test_login_sucesso(client, construtora_data):
    client.post("/api/v1/auth/register", json=construtora_data)
    response = client.post("/api/v1/auth/login", data={
        "username": construtora_data["email"],
        "password": construtora_data["password"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"


def test_login_senha_errada(client, construtora_data):
    client.post("/api/v1/auth/register", json=construtora_data)
    response = client.post("/api/v1/auth/login", data={
        "username": construtora_data["email"],
        "password": "senha_errada"
    })
    assert response.status_code == 400


def test_login_email_inexistente(client):
    response = client.post("/api/v1/auth/login", data={
        "username": "naoexiste@teste.com",
        "password": "senha123"
    })
    assert response.status_code == 400