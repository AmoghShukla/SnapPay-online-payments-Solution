from typing import Annotated
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from requests import Session
from src.core.config import settings

from database.session import get_db

Oauth2Scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

def get_current_user(token : Annotated[str, Oauth2Scheme], db : Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        if payload is None:
            raise HTTPException('Invalid Token!!!')
        
        user_id = payload.get('sub')
        user_role = payload.get('user_role')

        if user_id is None or user_role is None:
            raise HTTPException('Invalid Token!!!')
        
        return {
            'user_id' : user_id,
            'user_role' : user_role
        }
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid Token!!!")

def require_role(allowed_roles : list):
    all_roles = [str(role).upper() for role in allowed_roles]
    def check_role(user = Depends(get_current_user)):
        if str(user['user_role']).upper() not in all_roles:
            raise HTTPException(status_code=403, detail="Forbidden : Unauthorised Access!!")
        return user
    return check_role
