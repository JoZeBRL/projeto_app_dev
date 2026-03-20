import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.database import Base, get_db
from main import app

# Banco de testes separado
TEST_DATABASE_URL = "postgresql://corretiza_user:senha123@localhost:5432/corretiza_test"

engine_test = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def construtora_data():
    return {
        "full_name": "Construtora Teste",
        "email": "construtora@teste.com",
        "password": "senha123",
        "user_type": "CONSTRUTORA"
    }


@pytest.fixture
def corretor_data():
    return {
        "full_name": "Corretor Teste",
        "email": "corretor@teste.com",
        "password": "senha123",
        "user_type": "CORRETOR",
        "creci_number": "12345"
    }