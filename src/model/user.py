from uuid import uuid4
from sqlalchemy import Column, DateTime, String, Integer
from datetime import datetime
from enum import Enum
from src.database.base import Base
from sqlalchemy.orm import relationship

class UserRole(Enum):
    USER = "USER"
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"

class User_Class(Base):
    __tablename__ = "User"

    def generate_upi(context):
        params = context.user_contact_no
        return f"{params}@upi"

    user_id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    upi_id = Column(default=generate_upi)
    user_name = Column(String, unique=True, nullable=False)
    user_password = Column(String, nullable=False)
    user_role = Column(String, nullable=False)
    user_email = Column(String, nullable=False)
    user_contact_no = Column(String, nullable=False)
    user_created_at = Column(DateTime, default=datetime.utcnow)

    account = relationship("Account", back_populate='owner')