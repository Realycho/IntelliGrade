from sqlalchemy import Column, String, Boolean, UUID # Changed from Integer to UUID for id
from sqlalchemy.dialects.postgresql import UUID as PG_UUID # For PostgreSQL specific UUID type
from sqlalchemy.ext.declarative import declarative_base
import uuid # To generate default UUIDs

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) # Using PostgreSQL UUID type
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, index=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # If you want to add any relationships later, they would go here.
    # For example:
    # items = relationship("Item", back_populates="owner")
