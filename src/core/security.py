from datetime import datetime, timedelta
import os
from passlib.context import CryptContext
from src.core.config import settings
import jwt

password_context = CryptContext(schemes=['bcrypt'], deprcated='auto')

class Security:

    @staticmethod
    def hash_password(plain_password : str):
        if len(plain_password.encode('utf-8')) > 72:
            raise ValueError("Password too long  (max 72 bytes)") 
        return password_context.hash(plain_password)
    
    @staticmethod
    def verify_password(plain_password : str, hashed_password : str):
        return password_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def create_access_token(data : dict):
        data_to_encode = data.copy()
        expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        data_to_encode.update({'exp' : expire})

        return jwt.encode(data_to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)