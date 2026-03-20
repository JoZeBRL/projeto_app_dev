from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas.schemas as schemas
import models.enums as enums
import db.crud as crud
from routes.users import get_current_user
from db.database import get_db

proposals_router = APIRouter(
    prefix="/proposals",
    tags=["Propostas"],
)


@proposals_router.post("", response_model=schemas.ProposalInDB, status_code=201)
def create_proposal(
    proposal_data: schemas.ProposalCreate,
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.user_type != enums.UserType.CORRETOR:
        raise HTTPException(status_code=403, detail="Apenas Corretores podem criar propostas")

    property_data = crud.get_property_by_id(db, proposal_data.property_id)
    if not property_data:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")

    return crud.create_proposal(db, proposal_data, corretor_id=current_user.id)


@proposals_router.get("/me", response_model=List[schemas.ProposalInDB])
def get_my_proposals(
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.user_type != enums.UserType.CORRETOR:
        raise HTTPException(status_code=403, detail="Apenas Corretores têm propostas próprias")

    return crud.get_proposals_by_corretor(db, current_user.id)


@proposals_router.get("/property/{property_id}", response_model=List[schemas.ProposalInDB])
def get_proposals_by_property(
    property_id: str,
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.user_type == enums.UserType.CORRETOR:
        raise HTTPException(status_code=403, detail="Corretores não podem ver propostas por imóvel")

    property_data = crud.get_property_by_id(db, property_id)
    if not property_data:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")

    if property_data.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para ver as propostas deste imóvel")

    return crud.get_proposals_by_property(db, property_id)


@proposals_router.get("/{proposal_id}", response_model=schemas.ProposalInDB)
def get_proposal(
    proposal_id: str,
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    proposal = crud.get_proposal_by_id(db, proposal_id)
    if not proposal:
        raise HTTPException(status_code=404, detail="Proposta não encontrada")

    if current_user.user_type == enums.UserType.CORRETOR and proposal.corretor_id != current_user.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para ver esta proposta")

    return proposal


@proposals_router.put("/{proposal_id}/negotiate", response_model=schemas.ProposalInDB)
def negotiate_proposal(
    proposal_id: str,
    negotiation_data: schemas.NegotiationCreate,
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    proposal = crud.get_proposal_by_id(db, proposal_id)
    if not proposal:
        raise HTTPException(status_code=404, detail="Proposta não encontrada")

    if proposal.status in [enums.ProposalStatus.ACEITA, enums.ProposalStatus.RECUSADA]:
        raise HTTPException(status_code=400, detail="Proposta já encerrada")

    if current_user.user_type == enums.UserType.CORRETOR and proposal.corretor_id != current_user.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para negociar esta proposta")

    if current_user.user_type == enums.UserType.CONSTRUTORA:
        property_data = crud.get_property_by_id(db, proposal.property_id)
        if property_data.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Você não tem permissão para negociar esta proposta")

    return crud.add_negotiation(db, proposal_id, current_user.id, negotiation_data)


@proposals_router.put("/{proposal_id}/status", response_model=schemas.ProposalInDB)
def update_proposal_status(
    proposal_id: str,
    status_data: schemas.ProposalStatusUpdate,
    current_user: schemas.UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.user_type == enums.UserType.CORRETOR:
        raise HTTPException(status_code=403, detail="Corretores não podem alterar o status da proposta")

    proposal = crud.get_proposal_by_id(db, proposal_id)
    if not proposal:
        raise HTTPException(status_code=404, detail="Proposta não encontrada")

    if proposal.status in [enums.ProposalStatus.ACEITA, enums.ProposalStatus.RECUSADA]:
        raise HTTPException(status_code=400, detail="Proposta já encerrada")

    property_data = crud.get_property_by_id(db, proposal.property_id)
    if property_data.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para alterar esta proposta")

    return crud.update_proposal_status(db, proposal_id, status_data.status)