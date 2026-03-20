from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import schemas.schemas as schemas
import models.enums as enums
import db.crud as crud
from routes.users import get_current_user
from db.database import get_db

properties_router = APIRouter(
    prefix="/properties",
    tags=["Imóveis"],
)

@properties_router.post("", response_model=schemas.PropertyInDB, status_code=201)
def create_property(
    property_data: schemas.PropertyCreate,
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.user_type != enums.UserType.CONSTRUTORA:
        raise HTTPException(status_code=403, detail="Apenas Construtoras podem cadastrar imóveis")

    return crud.create_property(db, property_data, owner_id=current_user.id)


@properties_router.get("/me", response_model=List[schemas.PropertyInDB])
def get_my_properties(
    current_user: schemas.UserProfile = Depends(get_current_user),
    is_active: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    if current_user.user_type == enums.UserType.CORRETOR:
        raise HTTPException(status_code=403, detail="Corretores não possuem imóveis cadastrados.")

    return crud.get_properties_by_owner(db, owner_id=current_user.id, is_active=is_active)


@properties_router.get("/{property_id}", response_model=schemas.PropertyInDB)
def get_property(
    property_id: str,
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    property_data = crud.get_property_by_id(db, property_id)
    if not property_data:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")

    return property_data


@properties_router.get("", response_model=List[schemas.PropertyInDB])
def list_properties(
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db),
    city: Optional[str] = None,
    state: Optional[str] = None,
    neighborhood: Optional[str] = None,
    property_type: Optional[enums.PropertyType] = None,
    transaction_type: Optional[enums.TransactionType] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_bedrooms: Optional[int] = None,
    min_parking_spaces: Optional[int] = None,
    limit: int = 50
):
    return crud.list_properties(
        db,
        city=city,
        state=state,
        neighborhood=neighborhood,
        property_type=property_type,
        transaction_type=transaction_type,
        min_price=min_price,
        max_price=max_price,
        min_bedrooms=min_bedrooms,
        min_parking_spaces=min_parking_spaces,
        limit=limit
    )


@properties_router.put("/{property_id}", response_model=schemas.PropertyInDB)
def update_property(
    property_id: str,
    property_data: schemas.PropertyUpdate,
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.user_type != enums.UserType.CONSTRUTORA:
        raise HTTPException(status_code=403, detail="Apenas Construtoras podem editar imóveis")

    existing_property = crud.get_property_by_id(db, property_id)
    if not existing_property:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")

    if existing_property.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para editar este imóvel")

    update_data = property_data.model_dump(exclude_none=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="Nenhum campo para atualizar fornecido")

    return crud.update_property(db, property_id, update_data)


@properties_router.delete("/{property_id}", status_code=204)
def delete_property(
    property_id: str,
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.user_type != enums.UserType.CONSTRUTORA:
        raise HTTPException(status_code=403, detail="Apenas Construtoras podem deletar imóveis")

    existing_property = crud.get_property_by_id(db, property_id)
    if not existing_property:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")

    if existing_property.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para deletar este imóvel")

    crud.delete_property(db, property_id)
    return None