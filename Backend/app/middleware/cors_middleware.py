from fastapi.middleware.cors import CORSMiddleware
import core.config as config


def configure_cors(app):
    """
    Configura CORS para desenvolvimento local.
    
    Em desenvolvimento: aceita qualquer porta em localhost (DINÂMICO)
    Em produção: apenas origens específicas configuradas em .env
    """
    # Verificar ambiente
    ENV = config.ENV
    DEV_MODE = ENV == "development"
    
    if DEV_MODE:
        # DESENVOLVIMENTO: Aceitar http://localhost:5174 (porta do Vite deste projeto)
        allow_origins = [
            "http://localhost:5174",      # Porta padrão do Vite para este projeto
            "http://127.0.0.1:5174",      # Localhost alternativo
        ]
        allow_credentials = True
        allow_methods = ["*"]
        allow_headers = ["*"]
    else:
        # PRODUÇÃO: Apenas origens específicas
        allow_origins = [
            config.FRONTEND_URL,
        ]
        allow_credentials = True
        allow_methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
        allow_headers = ["Content-Type", "Authorization"]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=allow_credentials,
        allow_methods=allow_methods,
        allow_headers=allow_headers,
    )
