from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
from datetime import timedelta
import schemas.schemas as schemas
import db.crud as crud
import core.security as security
import core.config as config
from db.database import get_db

auth_router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"],
)


def _build_token_data(user_data: dict) -> dict:
    return {
        "user_id": user_data["user_id"] if "user_id" in user_data else user_data["id"],
        "email": user_data["email"],
        "user_type": user_data["user_type"]
    }


@auth_router.post("/login", response_model=schemas.Token)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user_data = crud.get_user_by_email(db, form_data.username)

    if not user_data:
        raise HTTPException(status_code=400, detail="Email ou senha incorretos")

    if not security.verify_password(form_data.password, user_data["password_hash"]):
        raise HTTPException(status_code=400, detail="Email ou senha incorretos")

    token_data = _build_token_data(user_data)

    access_token_expires = (
        timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        if config.ACCESS_TOKEN_EXPIRE_MINUTES else None
    )

    refresh_token_expires = (
        timedelta(days=config.REFRESH_TOKEN_EXPIRE_DAYS)
        if config.REFRESH_TOKEN_EXPIRE_DAYS else None
    )

    access_token = security.create_access_token(
        data=token_data,
        expires_delta=access_token_expires
    )

    refresh_token = security.create_access_token(
        data={**token_data, "type": "refresh"},
        expires_delta=refresh_token_expires
    )

    return schemas.Token(
        access_token=access_token,
        token_type="bearer",
        refresh_token=refresh_token
    )


@auth_router.post("/refresh", response_model=schemas.Token)
def refresh_access_token(token_data: schemas.TokenRefresh):
    try:
        payload = security.decode_access_token(token_data.refresh_token)

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Token inválido. Use um refresh_token.")

        user_id = payload.get("user_id")
        user_email = payload.get("email")
        user_type = payload.get("user_type")

        if not user_id or not user_email:
            raise HTTPException(status_code=401, detail="Token corrompido.")

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Refresh token inválido: {str(e)}")

    new_token_data = {
        "user_id": user_id,
        "email": user_email,
        "user_type": user_type
    }

    access_token_expires = (
        timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        if config.ACCESS_TOKEN_EXPIRE_MINUTES else None
    )

    new_access_token = security.create_access_token(
        data=new_token_data,
        expires_delta=access_token_expires
    )

    return schemas.Token(
        access_token=new_access_token,
        token_type="bearer",
        refresh_token=token_data.refresh_token
    )


@auth_router.post("/register", response_model=schemas.UserProfile)
def register_user(
    user_data: schemas.UserRegister,
    db: Session = Depends(get_db)
):
    if crud.get_user_by_email(db, user_data.email):
        raise HTTPException(status_code=400, detail="Email já registrado")

    return crud.create_user(db, user_data)