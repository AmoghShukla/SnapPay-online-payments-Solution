import enum
from uuid import uuid4
from src.database.base import Base
from sqlalchemy import Date, Boolean, Column, DateTime, ForeignKey, Integer, String, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from datetime import datetime, UTC, date

class TransactionType(enum.Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

class TransactionStatus(enum.Enum):
    COMPLETED = "COMPLETED"
    IN_PROCESS = "IN_PROCESS"
    FAILED = "FAILED"


class Transaction_Class(Base):
    __tablename__="Transaction"

    transaction_id = Column(default =lambda : str(uuid4()), primary_key=True)
    transaction_type = Column(SQLAlchemyEnum(TransactionType), nullable=False)
    transaction_amount = Column(Integer, nullable=False)
    transaction_date = Column(Date, default= date.today)
    transaction_time = Column(DateTime, default= datetime.now(UTC))
    reciever_account_id = Column(String, nullable=False)
    sender_account_id = Column(String, nullable=False)
    transaction_status = Column(SQLAlchemyEnum(TransactionStatus), nullable=False)