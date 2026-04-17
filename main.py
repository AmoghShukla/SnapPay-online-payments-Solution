from fastapi import FastAPI
from src.router.auth import router as AuthRouter
app = FastAPI(title="SnapPay : Your Payments Solution Partner")

app.include_router(AuthRouter)

@app.get('/')
def home():
    return {
        'message' : 'Your payments application is up and running!!'
    }