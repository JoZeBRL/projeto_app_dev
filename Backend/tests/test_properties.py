import pytest


@pytest.fixture
def construtora_token(client, construtora_data):
    client.post("/api/v1/auth/register", json=construtora_data)
    login = client.post("/api/v1/auth/login", data={
        "username": construtora_data["email"],
        "password": construtora_data["password"]
    })
    return login.json()["access_token"]


@pytest.fixture
def corretor_token(client, corretor_data):
    client.post("/api/v1/auth/register", json=corretor_data)
    login = client.post("/api/v1/auth/login", data={
        "username": corretor_data["email"],
        "password": corretor_data["password"]
    })
    return login.json()["access_token"]


@pytest.fixture
def property_data():
    return {
        "title": "Apartamento Centro",
        "property_type": "APARTAMENTO",
        "transaction_type": "VENDA",
        "price": 500000.00,
        "description": "Ótimo apartamento no centro",
        "address": "Rua das Flores, 123",
        "neighborhood": "Centro",
        "zip_code": "87010-000",
        "city": "Maringá",
        "state": "PR",
        "area_m2": 80.0,
        "bedrooms": 3,
        "bathrooms": 2,
        "parking_spaces": 1
    }


def test_criar_imovel(client, construtora_token, property_data):
    response = client.post("/api/v1/properties",
        json=property_data,
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == property_data["title"]
    assert data["city"] == "Maringá"


def test_corretor_nao_pode_criar_imovel(client, corretor_token, property_data):
    response = client.post("/api/v1/properties",
        json=property_data,
        headers={"Authorization": f"Bearer {corretor_token}"}
    )
    assert response.status_code == 403


def test_listar_imoveis(client, construtora_token, corretor_token, property_data):
    client.post("/api/v1/properties",
        json=property_data,
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    response = client.get("/api/v1/properties",
        headers={"Authorization": f"Bearer {corretor_token}"}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_buscar_imovel_por_id(client, construtora_token, property_data):
    created = client.post("/api/v1/properties",
        json=property_data,
        headers={"Authorization": f"Bearer {construtora_token}"}
    ).json()

    response = client.get(f"/api/v1/properties/{created['id']}",
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_buscar_imovel_inexistente(client, construtora_token):
    response = client.get("/api/v1/properties/00000000-0000-0000-0000-000000000000",
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    assert response.status_code == 404


def test_atualizar_imovel(client, construtora_token, property_data):
    created = client.post("/api/v1/properties",
        json=property_data,
        headers={"Authorization": f"Bearer {construtora_token}"}
    ).json()

    response = client.put(f"/api/v1/properties/{created['id']}",
        json={"title": "Apartamento Atualizado", "price": 550000.00},
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Apartamento Atualizado"


def test_deletar_imovel(client, construtora_token, property_data):
    created = client.post("/api/v1/properties",
        json=property_data,
        headers={"Authorization": f"Bearer {construtora_token}"}
    ).json()

    response = client.delete(f"/api/v1/properties/{created['id']}",
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    assert response.status_code == 204


def test_meus_imoveis(client, construtora_token, property_data):
    client.post("/api/v1/properties",
        json=property_data,
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    response = client.get("/api/v1/properties/me",
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1