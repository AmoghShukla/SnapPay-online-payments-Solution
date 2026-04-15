from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.database.base import Base
from uuid import uuid4


class Wallet_Class(Base):
    __tablename__="Wallet"

    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    wallet_id = Column(default= lambda : str(uuid4()), primary_key=True)
    wallet_balance = Column(Integer, default=0)

    owner = relationship('User_Class', back_populates='')