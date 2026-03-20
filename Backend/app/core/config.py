import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

def _required(key: str) -> str:
    value = os.getenv(key)
    if not value:
        raise RuntimeError(f"Variável de ambiente obrigatória não definida: {key}")
    return value

# Ambiente
ENV = os.getenv("ENV", "production")

# JWT
SECRET_KEY = _required("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
_expire_access = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
ACCESS_TOKEN_EXPIRE_MINUTES = int(_expire_access) if _expire_access else None

_expire_refresh = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")
REFRESH_TOKEN_EXPIRE_DAYS = int(_expire_refresh) if _expire_refresh else None

# PostgreSQL
DATABASE_URL = _required("DATABASE_URL")

# Frontend
FRONTEND_URL = os.getenv("FRONTEND_URL", "https://app.corretiza.com.br")