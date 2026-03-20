import uuid
from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db.database import Base
import models.enums as enums
import sqlalchemy as sa


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(Text, nullable=False)
    creci_number = Column(String(50), nullable=True)
    user_type = Column(sa.Enum(enums.UserType), nullable=False, index=True)
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    properties = relationship("Property", back_populates="owner")
    proposals = relationship("Proposal", back_populates="corretor")
    enterprises = relationship("Enterprise", back_populates="owner")


class Property(Base):
    __tablename__ = "properties"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    property_type = Column(sa.Enum(enums.PropertyType), nullable=False, index=True)
    transaction_type = Column(sa.Enum(enums.TransactionType), nullable=False, index=True)
    price = Column(Numeric(12, 2), nullable=False, index=True)
    description = Column(Text, nullable=False)
    address = Column(String(255), nullable=False)
    neighborhood = Column(String(100), nullable=False)
    zip_code = Column(String(20), nullable=False)
    city = Column(String(100), nullable=False, index=True)
    state = Column(String(5), nullable=False, index=True)
    area_m2 = Column(Numeric(10, 2), nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    parking_spaces = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    owner = relationship("User", back_populates="properties")
    proposals = relationship("Proposal", back_populates="property")


class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    property_id = Column(UUID(as_uuid=True), ForeignKey("properties.id"), nullable=True, index=True)
    unit_id = Column(UUID(as_uuid=True), ForeignKey("units.id"), nullable=True, index=True)
    corretor_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    client_full_name = Column(String(255), nullable=False)
    client_email = Column(String(255), nullable=False)
    client_phone = Column(String(20), nullable=False)
    client_cpf = Column(String(14), nullable=False)
    client_rg = Column(String(20), nullable=False)
    client_birthdate = Column(String(10), nullable=False)
    client_marital_status = Column(String(50), nullable=False)
    client_profession = Column(String(100), nullable=False)
    client_income = Column(Numeric(12, 2), nullable=False)
    client_zip_code = Column(String(20), nullable=False)
    client_address = Column(String(255), nullable=False)
    client_number = Column(String(10), nullable=False)
    client_complement = Column(String(100), nullable=True)
    client_neighborhood = Column(String(100), nullable=False)
    client_city = Column(String(100), nullable=False)
    client_state = Column(String(5), nullable=False)
    offered_value = Column(Numeric(12, 2), nullable=False)
    payment_type = Column(sa.Enum(enums.PaymentType), nullable=False)
    observation = Column(Text, nullable=True)
    status = Column(sa.Enum(enums.ProposalStatus), nullable=False, default=enums.ProposalStatus.PENDENTE, index=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    property = relationship("Property", back_populates="proposals")
    corretor = relationship("User", back_populates="proposals")
    negotiations = relationship("Negotiation", back_populates="proposal")


class Negotiation(Base):
    __tablename__ = "proposal_negotiations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    proposal_id = Column(UUID(as_uuid=True), ForeignKey("proposals.id", ondelete="CASCADE"), nullable=False, index=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    offered_value = Column(Numeric(12, 2), nullable=False)
    payment_type = Column(sa.Enum(enums.PaymentType), nullable=False)
    observation = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    proposal = relationship("Proposal", back_populates="negotiations")


class Enterprise(Base):
    __tablename__ = "enterprises"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    total_floors = Column(Integer, nullable=False)
    delivery_forecast = Column(String(10), nullable=False)
    status = Column(sa.Enum(enums.EnterpriseStatus), nullable=False, index=True)
    address = Column(String(255), nullable=False)
    neighborhood = Column(String(100), nullable=False)
    zip_code = Column(String(20), nullable=False)
    city = Column(String(100), nullable=False, index=True)
    state = Column(String(5), nullable=False, index=True)
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    owner = relationship("User", back_populates="enterprises")
    floor_plans = relationship("FloorPlan", back_populates="enterprise")
    units = relationship("Unit", back_populates="enterprise")


class FloorPlan(Base):
    __tablename__ = "floor_plans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    enterprise_id = Column(UUID(as_uuid=True), ForeignKey("enterprises.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    area_m2 = Column(Numeric(10, 2), nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    parking_spaces = Column(Integer, nullable=False)
    base_price = Column(Numeric(12, 2), nullable=False)
    broker_commission = Column(Numeric(5, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    enterprise = relationship("Enterprise", back_populates="floor_plans")
    units = relationship("Unit", back_populates="floor_plan")


class Unit(Base):
    __tablename__ = "units"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    enterprise_id = Column(UUID(as_uuid=True), ForeignKey("enterprises.id"), nullable=False, index=True)
    floor_plan_id = Column(UUID(as_uuid=True), ForeignKey("floor_plans.id"), nullable=False, index=True)
    number = Column(String(10), nullable=False)
    floor = Column(Integer, nullable=False)
    price = Column(Numeric(12, 2), nullable=False)
    status = Column(sa.Enum(enums.UnitStatus), nullable=False, default=enums.UnitStatus.DISPONIVEL, index=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    enterprise = relationship("Enterprise", back_populates="units")
    floor_plan = relationship("FloorPlan", back_populates="units")