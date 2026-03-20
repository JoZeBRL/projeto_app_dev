import logging
from fastapi import FastAPI
from middleware.cors_middleware import configure_cors
from db.database import engine
from contextlib import asynccontextmanager
from datetime import datetime, timezone
import routes.auth as auth
import routes.users as users
import routes.properties as properties
import routes.proposals as proposals
import core.config as config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

ENV = config.ENV
DEV_MODE = ENV == "development"

if DEV_MODE:
    logger.info("🛠️  MODO DESENVOLVIMENTO")
else:
    logger.info("🚀 MODO PRODUÇÃO")

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    engine.dispose()
    logger.info("✅ Engine encerrada.")

app = FastAPI(
    lifespan=lifespan,
    title="Corretiza Core API",
    description="API principal para o hub de corretores e construtoras.",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json"
)

configure_cors(app)

app.include_router(auth.auth_router, prefix="/api/v1")
app.include_router(users.users_router, prefix="/api/v1")
app.include_router(properties.properties_router, prefix="/api/v1")
app.include_router(proposals.proposals_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "app": "Corretiza API",
        "version": "1.0.0",
        "environment": ENV,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }