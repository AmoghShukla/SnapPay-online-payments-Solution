from pydantic import BaseModel, EmailStr, Field

def LoginRequest(BaseModel):
    user_email : EmailStr = Field(...)
    user_password : str = Field(..., min_length=7, max_length=15)

def LoginResponse(BaseModel):
    message : str = Field(..., default="Login Successul!!!")
    access_token : str
    token_type : str = Field(..., default="Bearer!!")
