from sqlalchemy.orm import Session, joinedload
from typing import Optional
import uuid
import schemas.schemas as schemas
import models.models as models
import core.security as security
from models.enums import ProposalStatus


# ========= USUÁRIOS =========

def create_user(db: Session, user_data: schemas.UserRegister) -> schemas.UserProfile:
    password_hash = security.hash_password(user_data.password)
    user = models.User(
        full_name=user_data.full_name,
        email=user_data.email,
        password_hash=password_hash,
        creci_number=user_data.creci_number,
        user_type=user_data.user_type,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return _user_to_profile(user)


def get_user_by_email(db: Session, email: str) -> Optional[dict]:
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return None
    return {
        "id": str(user.id),
        "full_name": user.full_name,
        "email": user.email,
        "password_hash": user.password_hash,
        "creci_number": user.creci_number,
        "user_type": user.user_type,
        "is_active": user.is_active,
    }


def get_user_profile_by_id(db: Session, user_id: str) -> Optional[schemas.UserProfile]:
    user = db.query(models.User).filter(models.User.id == uuid.UUID(user_id)).first()
    if not user:
        return None
    return _user_to_profile(user)


def update_user_profile(db: Session, user_id: str, update_data: dict) -> Optional[schemas.UserProfile]:
    user = db.query(models.User).filter(models.User.id == uuid.UUID(user_id)).first()
    if not user:
        return None
    allowed_fields = {"full_name", "email", "creci_number"}
    for key, value in update_data.items():
        if key in allowed_fields:
            setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return _user_to_profile(user)


def _user_to_profile(user: models.User) -> schemas.UserProfile:
    return schemas.UserProfile(
        id=str(user.id),
        full_name=user.full_name,
        email=user.email,
        creci_number=user.creci_number,
        user_type=user.user_type,
        is_active=user.is_active,
    )


# ========= IMÓVEIS =========

def create_property(db: Session, property_data: schemas.PropertyCreate, owner_id: str) -> schemas.PropertyInDB:
    prop = models.Property(
        owner_id=uuid.UUID(owner_id),
        title=property_data.title,
        property_type=property_data.property_type,
        transaction_type=property_data.transaction_type,
        price=property_data.price,
        description=property_data.description,
        address=property_data.address,
        neighborhood=property_data.neighborhood,
        zip_code=property_data.zip_code,
        city=property_data.city,
        state=property_data.state,
        area_m2=property_data.area_m2,
        bedrooms=property_data.bedrooms,
        bathrooms=property_data.bathrooms,
        parking_spaces=property_data.parking_spaces,
    )
    db.add(prop)
    db.commit()
    db.refresh(prop)
    return _property_to_schema(prop)


def get_property_by_id(db: Session, property_id: str) -> Optional[schemas.PropertyInDB]:
    prop = db.query(models.Property).filter(models.Property.id == uuid.UUID(property_id)).first()
    if not prop:
        return None
    return _property_to_schema(prop)


def get_properties_by_owner(db: Session, owner_id: str, is_active: Optional[bool] = None) -> list:
    query = db.query(models.Property).filter(models.Property.owner_id == uuid.UUID(owner_id))
    if is_active is not None:
        query = query.filter(models.Property.is_active == is_active)
    return [_property_to_schema(p) for p in query.all()]


def list_properties(
    db: Session,
    city=None, state=None, neighborhood=None,
    property_type=None, transaction_type=None,
    min_price=None, max_price=None,
    min_bedrooms=None, min_parking_spaces=None,
    limit=50
) -> list:
    query = db.query(models.Property).filter(models.Property.is_active == True)
    if city:
        query = query.filter(models.Property.city == city)
    if state:
        query = query.filter(models.Property.state == state)
    if neighborhood:
        query = query.filter(models.Property.neighborhood == neighborhood)
    if property_type:
        query = query.filter(models.Property.property_type == property_type)
    if transaction_type:
        query = query.filter(models.Property.transaction_type == transaction_type)
    if min_price:
        query = query.filter(models.Property.price >= min_price)
    if max_price:
        query = query.filter(models.Property.price <= max_price)
    if min_bedrooms:
        query = query.filter(models.Property.bedrooms >= min_bedrooms)
    if min_parking_spaces:
        query = query.filter(models.Property.parking_spaces >= min_parking_spaces)
    return [_property_to_schema(p) for p in query.limit(limit).all()]


def update_property(db: Session, property_id: str, update_data: dict) -> Optional[schemas.PropertyInDB]:
    prop = db.query(models.Property).filter(models.Property.id == uuid.UUID(property_id)).first()
    if not prop:
        return None
    allowed_fields = {
        "title", "property_type", "transaction_type", "price", "description",
        "address", "neighborhood", "zip_code", "city", "state",
        "area_m2", "bedrooms", "bathrooms", "parking_spaces"
    }
    for key, value in update_data.items():
        if key in allowed_fields:
            setattr(prop, key, value)
    db.commit()
    db.refresh(prop)
    return _property_to_schema(prop)


def delete_property(db: Session, property_id: str) -> bool:
    prop = db.query(models.Property).filter(models.Property.id == uuid.UUID(property_id)).first()
    if not prop:
        return False
    prop.is_active = False
    db.commit()
    return True


def _property_to_schema(prop: models.Property) -> schemas.PropertyInDB:
    return schemas.PropertyInDB(
        id=str(prop.id),
        owner_id=str(prop.owner_id),
        title=prop.title,
        property_type=prop.property_type,
        transaction_type=prop.transaction_type,
        price=float(prop.price),
        description=prop.description,
        address=prop.address,
        neighborhood=prop.neighborhood,
        zip_code=prop.zip_code,
        city=prop.city,
        state=prop.state,
        area_m2=float(prop.area_m2),
        bedrooms=prop.bedrooms,
        bathrooms=prop.bathrooms,
        parking_spaces=prop.parking_spaces,
        is_active=prop.is_active,
        created_at=str(prop.created_at),
    )


# ========= PROPOSTAS =========

def create_proposal(db: Session, proposal_data: schemas.ProposalCreate, corretor_id: str) -> schemas.ProposalInDB:
    proposal = models.Proposal(
        property_id=uuid.UUID(proposal_data.property_id),
        corretor_id=uuid.UUID(corretor_id),
        client_full_name=proposal_data.client_full_name,
        client_email=proposal_data.client_email,
        client_phone=proposal_data.client_phone,
        client_cpf=proposal_data.client_cpf,
        client_rg=proposal_data.client_rg,
        client_birthdate=proposal_data.client_birthdate,
        client_marital_status=proposal_data.client_marital_status,
        client_profession=proposal_data.client_profession,
        client_income=proposal_data.client_income,
        client_zip_code=proposal_data.client_zip_code,
        client_address=proposal_data.client_address,
        client_number=proposal_data.client_number,
        client_complement=proposal_data.client_complement,
        client_neighborhood=proposal_data.client_neighborhood,
        client_city=proposal_data.client_city,
        client_state=proposal_data.client_state,
        offered_value=proposal_data.offered_value,
        payment_type=proposal_data.payment_type,
        observation=proposal_data.observation,
    )
    db.add(proposal)
    db.commit()
    db.refresh(proposal)
    return get_proposal_by_id(db, str(proposal.id))


def get_proposal_by_id(db: Session, proposal_id: str) -> Optional[schemas.ProposalInDB]:
    proposal = (
        db.query(models.Proposal)
        .options(joinedload(models.Proposal.negotiations))
        .filter(models.Proposal.id == uuid.UUID(proposal_id))
        .first()
    )
    if not proposal:
        return None
    return _proposal_to_schema(proposal)


def get_proposals_by_property(db: Session, property_id: str) -> list:
    proposals = (
        db.query(models.Proposal)
        .options(joinedload(models.Proposal.negotiations))
        .filter(models.Proposal.property_id == uuid.UUID(property_id))
        .order_by(models.Proposal.created_at.desc())
        .all()
    )
    return [_proposal_to_schema(p) for p in proposals]


def get_proposals_by_corretor(db: Session, corretor_id: str) -> list:
    proposals = (
        db.query(models.Proposal)
        .options(joinedload(models.Proposal.negotiations))
        .filter(models.Proposal.corretor_id == uuid.UUID(corretor_id))
        .order_by(models.Proposal.created_at.desc())
        .all()
    )
    return [_proposal_to_schema(p) for p in proposals]


def add_negotiation(db: Session, proposal_id: str, author_id: str, negotiation_data: schemas.NegotiationCreate) -> schemas.ProposalInDB:
    negotiation = models.Negotiation(
        proposal_id=uuid.UUID(proposal_id),
        author_id=uuid.UUID(author_id),
        offered_value=negotiation_data.offered_value,
        payment_type=negotiation_data.payment_type,
        observation=negotiation_data.observation,
    )
    db.add(negotiation)

    proposal = db.query(models.Proposal).filter(models.Proposal.id == uuid.UUID(proposal_id)).first()
    proposal.offered_value = negotiation_data.offered_value
    proposal.payment_type = negotiation_data.payment_type
    proposal.observation = negotiation_data.observation
    proposal.status = ProposalStatus.EM_NEGOCIACAO

    db.commit()
    return get_proposal_by_id(db, proposal_id)


def update_proposal_status(db: Session, proposal_id: str, status: ProposalStatus) -> schemas.ProposalInDB:
    proposal = db.query(models.Proposal).filter(models.Proposal.id == uuid.UUID(proposal_id)).first()
    proposal.status = status
    db.commit()
    return get_proposal_by_id(db, proposal_id)


def _proposal_to_schema(proposal: models.Proposal) -> schemas.ProposalInDB:
    return schemas.ProposalInDB(
        id=str(proposal.id),
        property_id=str(proposal.property_id),
        corretor_id=str(proposal.corretor_id),
        client_full_name=proposal.client_full_name,
        client_email=proposal.client_email,
        client_phone=proposal.client_phone,
        client_cpf=proposal.client_cpf,
        client_rg=proposal.client_rg,
        client_birthdate=str(proposal.client_birthdate),
        client_marital_status=proposal.client_marital_status,
        client_profession=proposal.client_profession,
        client_income=float(proposal.client_income),
        client_zip_code=proposal.client_zip_code,
        client_address=proposal.client_address,
        client_number=proposal.client_number,
        client_complement=proposal.client_complement,
        client_neighborhood=proposal.client_neighborhood,
        client_city=proposal.client_city,
        client_state=proposal.client_state,
        offered_value=float(proposal.offered_value),
        payment_type=proposal.payment_type,
        observation=proposal.observation,
        status=proposal.status,
        created_at=str(proposal.created_at),
        updated_at=str(proposal.updated_at),
        negotiations=[
            schemas.NegotiationInDB(
                id=str(n.id),
                proposal_id=str(n.proposal_id),
                author_id=str(n.author_id),
                offered_value=float(n.offered_value),
                payment_type=n.payment_type,
                observation=n.observation,
                created_at=str(n.created_at),
            )
            for n in proposal.negotiations
        ],
    )