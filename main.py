from fastapi import FastAPI
from src.router.auth import Signup as SignUpRouter

app = FastAPI(title="SnapPay : Your Payments Solution Partner")

app.include_router(SignUpRouter)

@app.get('/')
def home():
    return {
        'message' : 'Your payments application is up and running!!'
    }