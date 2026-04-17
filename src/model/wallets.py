from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.database.base import Base
from uuid import uuid4


class Wallet_Class(Base):
    __tablename__="Wallet"

    
    wallet_id = Column(String, default= lambda : str(uuid4()), primary_key=True)
    wallet_balance = Column(Integer, default=0)

    user_id = Column(String, ForeignKey('User.user_id'), nullable=False)
    owner = relationship('User_Class', back_populates='wallet')