from fastapi import APIRouter, Depends
from requests import Session
from src.database.session import get_db
from src.schema.user import UserCreate, UserResponse

router = APIRouter('/auth', tags=['Auth'])

@router.post('/signup', response_model=UserResponse)
def Signup(payload : UserCreate, db :Session =  Depends(get_db)):
    pass