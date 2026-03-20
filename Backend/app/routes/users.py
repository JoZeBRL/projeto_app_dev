from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import schemas.schemas as schemas
import db.crud as crud
import core.security as security
from db.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> schemas.UserProfile:
    try:
        payload = security.decode_access_token(token)
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Token inválido: {str(e)}")

    user_profile = crud.get_user_profile_by_id(db, user_id)
    if not user_profile:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user_profile

users_router = APIRouter(
    prefix="/users",
    tags=["Usuários"],
)

@users_router.get("/me", response_model=schemas.UserProfile)
def read_users_me(current_user: schemas.UserProfile = Depends(get_current_user)):
    return current_user

@users_router.put("/me", response_model=schemas.UserProfile)
def update_users_me(
    user_data: schemas.UserUpdate,
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    update_data = user_data.model_dump(exclude_none=True)

    if not update_data:
        raise HTTPException(status_code=400, detail="Nenhum campo para atualizar fornecido.")

    updated_user = crud.update_user_profile(db, current_user.id, update_data)

    if not updated_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

    return updated_user