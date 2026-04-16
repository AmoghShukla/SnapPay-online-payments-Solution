from datetime import datetime

from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, DateTime, ForeignKey, Integer

def UserCreate(BaseModel):
    user_name : str = Field(...)
    user_email : EmailStr = Field(...)
    user_password : str = Field(..., min_length=7, max_length=15)
    user_contact_no : int = Field(..., min_length=10, max_length=10)

def UserResponse(BaseModel):
    user_id: str
    upi_id : str
    user_name : str
    user_role : str
    user_email : EmailStr
    user_contact_no : int
    user_created_at : datetime
    user_wallet_id : int
