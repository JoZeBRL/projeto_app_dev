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


@pytest.fixture
def imovel_id(client, construtora_token, property_data):
    response = client.post("/api/v1/properties",
        json=property_data,
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    return response.json()["id"]


@pytest.fixture
def proposal_data(imovel_id):
    return {
        "property_id": imovel_id,
        "client_full_name": "Cliente Teste",
        "client_email": "cliente@teste.com",
        "client_phone": "44999999999",
        "client_cpf": "123.456.789-09",
        "client_rg": "1234567",
        "client_birthdate": "1990-01-01",
        "client_marital_status": "Solteiro",
        "client_profession": "Engenheiro",
        "client_income": 10000.00,
        "client_zip_code": "87010-000",
        "client_address": "Rua das Flores, 123",
        "client_number": "123",
        "client_neighborhood": "Centro",
        "client_city": "Maringá",
        "client_state": "PR",
        "offered_value": 480000.00,
        "payment_type": "FINANCIAMENTO"
    }


def test_criar_proposta(client, corretor_token, proposal_data):
    response = client.post("/api/v1/proposals",
        json=proposal_data,
        headers={"Authorization": f"Bearer {corretor_token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "PENDENTE"
    assert data["offered_value"] == 480000.00


def test_construtora_nao_pode_criar_proposta(client, construtora_token, proposal_data):
    response = client.post("/api/v1/proposals",
        json=proposal_data,
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    assert response.status_code == 403


def test_minhas_propostas(client, corretor_token, proposal_data):
    client.post("/api/v1/proposals",
        json=proposal_data,
        headers={"Authorization": f"Bearer {corretor_token}"}
    )
    response = client.get("/api/v1/proposals/me",
        headers={"Authorization": f"Bearer {corretor_token}"}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_negociar_proposta(client, corretor_token, construtora_token, proposal_data):
    proposta = client.post("/api/v1/proposals",
        json=proposal_data,
        headers={"Authorization": f"Bearer {corretor_token}"}
    ).json()

    response = client.put(f"/api/v1/proposals/{proposta['id']}/negotiate",
        json={"offered_value": 490000.00, "payment_type": "FINANCIAMENTO"},
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "EM_NEGOCIACAO"
    assert response.json()["offered_value"] == 490000.00


def test_aceitar_proposta(client, corretor_token, construtora_token, proposal_data):
    proposta = client.post("/api/v1/proposals",
        json=proposal_data,
        headers={"Authorization": f"Bearer {corretor_token}"}
    ).json()

    response = client.put(f"/api/v1/proposals/{proposta['id']}/status",
        json={"status": "ACEITA"},
        headers={"Authorization": f"Bearer {construtora_token}"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ACEITA"


def test_corretor_nao_pode_alterar_status(client, corretor_token, proposal_data):
    proposta = client.post("/api/v1/proposals",
        json=proposal_data,
        headers={"Authorization": f"Bearer {corretor_token}"}
    ).json()

    response = client.put(f"/api/v1/proposals/{proposta['id']}/status",
        json={"status": "ACEITA"},
        headers={"Authorization": f"Bearer {corretor_token}"}
    )
    assert response.status_code == 403


def test_proposta_encerrada_nao_pode_negociar(client, corretor_token, construtora_token, proposal_data):
    proposta = client.post("/api/v1/proposals",
        json=proposal_data,
        headers={"Authorization": f"Bearer {corretor_token}"}
    ).json()

    client.put(f"/api/v1/proposals/{proposta['id']}/status",
        json={"status": "RECUSADA"},
        headers={"Authorization": f"Bearer {construtora_token}"}
    )

    response = client.put(f"/api/v1/proposals/{proposta['id']}/negotiate",
        json={"offered_value": 490000.00, "payment_type": "FINANCIAMENTO"},
        headers={"Authorization": f"Bearer {corretor_token}"}
    )
    assert response.status_code == 400