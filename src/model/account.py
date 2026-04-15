import enum
from uuid import uuid4
from src.database.base import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum as SQLAlchemyEnum

class AccountType(enum.Enum):
    SAVINGS = "SAVINGS"
    CURRENT = "CURRENT"
    SALARY = "SALARY" 

class Banks(enum.Enum):
    SBI = "SBI"
    HDFC = "HDFC"
    KOTAK = "KOTAK"
    ICICI = "ICICI"


class Account_Class(Base):
    __tablename__="Account"

    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    Bank_name = Column(Enum)
    Account_number = Column(default=lambda: str(uuid4()),primary_key=True, index=True)
    Account_balance = Column(Integer, default=0)
    Account_type = Column(Enum, default=AccountType.SAVINGS)
    IFSC_Code = Column(..., Integer)
    Pan_Card = Column(..., String)
    Adhaar_Card = Column(..., Integer)
    is_primary = Column(..., Boolean, default=True)


