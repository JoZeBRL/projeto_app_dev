from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
import models.enums as enums


# ========= USUÁRIOS =========

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    creci_number: Optional[str] = None
    user_type: enums.UserType

    @field_validator("full_name")
    def full_name_min_length(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("Nome deve ter no mínimo 2 caracteres")
        return v

    @field_validator("password")
    def password_min_length(cls, v):
        if len(v) < 6:
            raise ValueError("Senha deve ter no mínimo 6 caracteres")
        return v

class TokenRefresh(BaseModel):
    refresh_token: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    creci_number: Optional[str] = None

    @field_validator("full_name")
    def full_name_min_length(cls, v):
        if v and len(v.strip()) < 2:
            raise ValueError("Nome deve ter no mínimo 2 caracteres")
        return v

class UserProfile(BaseModel):
    id: str
    full_name: str
    email: str
    creci_number: Optional[str] = None
    user_type: enums.UserType
    is_active: bool = True


# ========= IMÓVEIS =========

class PropertyCreate(BaseModel):
    title: str
    property_type: enums.PropertyType
    transaction_type: enums.TransactionType
    price: float
    description: str
    address: str
    neighborhood: str
    zip_code: str
    city: str
    state: str
    area_m2: float
    bedrooms: int
    bathrooms: int
    parking_spaces: int

    @field_validator("price", "area_m2")
    def must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Valor deve ser maior que zero")
        return v

    @field_validator("bedrooms", "bathrooms", "parking_spaces")
    def must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError("Valor deve ser maior ou igual a zero")
        return v

    @field_validator("state")
    def state_max_length(cls, v):
        if len(v.strip()) > 5:
            raise ValueError("State deve ter no máximo 5 caracteres")
        return v

class PropertyUpdate(BaseModel):
    title: Optional[str] = None
    property_type: Optional[enums.PropertyType] = None
    transaction_type: Optional[enums.TransactionType] = None
    price: Optional[float] = None
    description: Optional[str] = None
    address: Optional[str] = None
    neighborhood: Optional[str] = None
    zip_code: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    area_m2: Optional[float] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    parking_spaces: Optional[int] = None

    @field_validator("price", "area_m2")
    def must_be_positive(cls, v):
        if v and v <= 0:
            raise ValueError("Valor deve ser maior que zero")
        return v

    @field_validator("bedrooms", "bathrooms", "parking_spaces")
    def must_be_non_negative(cls, v):
        if v is not None and v < 0:
            raise ValueError("Valor deve ser maior ou igual a zero")
        return v

    @field_validator("state")
    def state_max_length(cls, v):
        if v and len(v.strip()) > 5:
            raise ValueError("State deve ter no máximo 5 caracteres")
        return v

class PropertyInDB(BaseModel):
    id: str
    owner_id: str
    title: str
    property_type: enums.PropertyType
    transaction_type: enums.TransactionType
    price: float
    description: str
    address: str
    neighborhood: str
    zip_code: str
    city: str
    state: str
    area_m2: float
    bedrooms: int
    bathrooms: int
    parking_spaces: int
    is_active: bool = True
    created_at: str


# ========= PROPOSTAS =========

class ProposalCreate(BaseModel):
    property_id: str
    client_full_name: str
    client_email: EmailStr
    client_phone: str
    client_cpf: str
    client_rg: str
    client_birthdate: str
    client_marital_status: str
    client_profession: str
    client_income: float
    client_zip_code: str
    client_address: str
    client_number: str
    client_complement: Optional[str] = None
    client_neighborhood: str
    client_city: str
    client_state: str
    offered_value: float
    payment_type: enums.PaymentType
    observation: Optional[str] = None

    @field_validator("offered_value", "client_income")
    def must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Valor deve ser maior que zero")
        return v

    @field_validator("client_cpf")
    def cpf_format(cls, v):
        if len(v.replace(".", "").replace("-", "")) != 11:
            raise ValueError("CPF inválido")
        return v

class NegotiationCreate(BaseModel):
    offered_value: float
    payment_type: enums.PaymentType
    observation: Optional[str] = None

    @field_validator("offered_value")
    def must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Valor deve ser maior que zero")
        return v

class ProposalStatusUpdate(BaseModel):
    status: enums.ProposalStatus

class NegotiationInDB(BaseModel):
    id: str
    proposal_id: str
    author_id: str
    offered_value: float
    payment_type: enums.PaymentType
    observation: Optional[str] = None
    created_at: str

class ProposalInDB(BaseModel):
    id: str
    property_id: str
    corretor_id: str
    client_full_name: str
    client_email: str
    client_phone: str
    client_cpf: str
    client_rg: str
    client_birthdate: str
    client_marital_status: str
    client_profession: str
    client_income: float
    client_zip_code: str
    client_address: str
    client_number: str
    client_complement: Optional[str] = None
    client_neighborhood: str
    client_city: str
    client_state: str
    offered_value: float
    payment_type: enums.PaymentType
    observation: Optional[str] = None
    status: enums.ProposalStatus
    created_at: str
    updated_at: str
    negotiations: Optional[list] = []